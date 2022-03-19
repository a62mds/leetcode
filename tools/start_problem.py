"""
Set up a skeleton directory for solutions to the specified non-paid only Leetcode problem.

Documentation LaTeX files are generated.

Languages in use:

- C++
- Python

"""
import argparse
import json
from pathlib import Path
import requests
import sys
import traceback
from typing import Any, Dict, List, Tuple

import bs4
from jinja2 import Environment, FileSystemLoader, Template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


TOOLS_DIR = Path(__file__).resolve().parent
ROOT_DIR = TOOLS_DIR.parent
PROBLEMS_DIR = ROOT_DIR / "problems"
TEMPLATE_DIR = TOOLS_DIR / "templates"

PROBLEM_NUMBER_PLACEHOLDER: str = "xxxx"

LEETCODE_API_URL: str = "https://leetcode.com/api/problems/all/"
LEETCODE_PROBLEMS_URL: str = "https://leetcode.com/problems"

CHROMEDRIVER_PATH = r"./driver/chromedriver.exe"


def main(args: argparse.Namespace) -> int:
    """
    Set up a skeleton directory for solutions to the specified non-paid only Leetcode problem.

    Scrapes the problem statement from leetcode using a strategy heavily influenced by
    https://github.com/Bishalsarang/Leetcode-Questions-Scraper.git, converts it to LaTeX format, and renders the result
    using the appropriate template.

    Renders LaTeX templates for documenting the algorithms used to solve the problem, along with a build script that
    compiles the LaTeX files into a PDF.

    Renders C++ templates for a C++ implementation of the problem solution.

    Renders Python templates for a Python implementation of the problem solution.
    """
    return_code: int = 0

    try:
        problem_number: int = args.problem_number
        padded_problem_number: str = f"{problem_number:04d}"

        problem_info: Dict[str, Any] = get_problem_info(LEETCODE_API_URL, problem_number)

        problem_title: str = problem_info["question__title"]
        problem_slug: str = problem_info["question__title_slug"]
        problem_url: str = f"{LEETCODE_PROBLEMS_URL}/{problem_slug}"

        problem_name: str = f"Problem-{padded_problem_number}"

        problem_dir: Path = PROBLEMS_DIR / problem_name.lower()
        print(f"Creating directory {problem_dir}...")
        problem_dir.mkdir(parents=True, exist_ok=True)

        question_content: "bs4.element.Tag" = get_question_content(problem_url)

        problem_statement: str = html_to_latex(question_content)

        image_urls: List[str] = get_image_urls(question_content)
        if image_urls:
            image_dir: Path = problem_dir / "documentation" / "img"
            print(f"Creating directory {image_dir}...")
            image_dir.mkdir(parents=True, exist_ok=True)
            download_images(image_urls, image_dir)

        for template_path in filter(lambda p: p.is_file(), TEMPLATE_DIR.glob("**/*")):
            relative_template_path: Path = template_path.relative_to(TEMPLATE_DIR)
            relative_render_path = Path(
                *(p.replace(PROBLEM_NUMBER_PLACEHOLDER, padded_problem_number) for p in relative_template_path.parts)
            )
            render_path: Path = (problem_dir / relative_render_path).with_suffix("")      # Strip the .j2

            if render_path.is_file():
                print(f"Not overwriting existing file {render_path}")
                continue

            # The trim_blocks and lstrip_blocks args remove extraneous whitespace when creating successive lines from a for
            # loop. See https://jinja2docs.readthedocs.io/en/stable/templates.html?highlight=trim_blocks#whitespace-control
            # for details
            template_env = Environment(
                loader=FileSystemLoader(template_path.parent),
                trim_blocks=True,
                lstrip_blocks=True
            )

            template: Template = template_env.get_template(template_path.name)
            rendered_template: str = template.render(
                problem_title=problem_title,
                problem_name=problem_name,
                problem_number=problem_number,
                padded_problem_number=padded_problem_number,
                problem_statement=problem_statement,
                problem_url=problem_url
            )

            print(f"Writing rendered template to {render_path}")
            render_path.parent.mkdir(parents=True, exist_ok=True)
            with render_path.open(mode="w") as render_file:
                render_file.write(rendered_template)

    except Exception:
        print(traceback.format_exc())
        return_code = 1

    return return_code


def get_problem_info(api_url: str, problem_number: int) -> Dict[str, Any]:
    """
    Retrieve the problem info as a JSON object and return as a dict, assuming the supplied problem number is valid. If
    there is no free problem with the supplied problem number, return None.
    """
    response: "requests.models.Response" = requests.get(api_url)

    response.raise_for_status()

    all_problems: Dict = json.loads(response.text)["stat_status_pairs"]
    for problem in all_problems:
        problem_info = problem["stat"]
        if problem_info["question_id"] == problem_number:
            if problem["paid_only"]:
                raise ValueError(f"Problem number {problem_number} is a paid-only problem")
            return problem_info

    raise ValueError(f"Could not find problem number {problem_number}")


def get_question_content(problem_url: str) -> "bs4.element.Tag":
    """
    Get the div that contains the question content (i.e. problem statement).
    """
    # Setup Selenium Webdriver
    options = Options()
    options.headless = True                     # Don't show browser window
    options.add_argument("--log-level=3")       # Log only fatal errors

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(problem_url)

    # Wait 20 secs or until div with id initial-loading disappears
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.ID, "initial-loading"))
    )

    soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

    return soup.find("div", {"class": "content__u3I1 question-content__JfgR"})


def html_to_latex(question_content: "bs4.element.Tag") -> str:
    """
    Convert the HTML question content to LaTeX.
    """
    node_converters = {
        "p": p_to_latex,
        "img": img_to_latex,
        "pre": pre_to_latex,
        "ul": ul_to_latex
    }

    tag_converters = [
        lambda x: x.replace("<strong>", "\\textbf{").replace("</strong>", "}"),
        lambda x: x.replace("<code>", "\\code{").replace("</code>", "}"),
        lambda x: x.replace("<sup>", "\\textasciicircum").replace("</sup>", "")
    ]

    entity_converters = [
        lambda x: x.replace("&lt;", "<")
    ]

    latex = ""

    div = question_content.find_all("div")[-1]                              # Get innermost nested <div>
    for child in div.find_all(recursive=False):
        inner_latex = node_converters.get(child.name, lambda x: "")(child)
        inner_latex = inner_latex.encode("ascii", errors="ignore").decode() # Remove non-ascii chars
        if inner_latex:
            latex += inner_latex + "\n\n"

    for tag_converter in tag_converters:
        latex = tag_converter(latex)

    for entity_converter in entity_converters:
        latex = entity_converter(latex)

    latex = latex.rstrip()                                                  # Remove trailing newlines

    return latex


def p_to_latex(p_node: "bs4.element.Tag") -> str:
    """
    Convert a paragraph node to LaTeX.
    """
    subsection_indicators = [
        "Example",
        "Constraints",
        "Follow-up"
    ]

    latex = str(p_node).replace("<p>", "").replace("</p>", "")

    if any(latex.startswith(f"<strong>{x}") for x in subsection_indicators):
        latex = latex.replace("<strong>", "\n\\subsection*{").replace("</strong>", "}")

    return latex


def img_to_latex(img_node: "bs4.element.Tag") -> str:
    """
    Convert an image (assumes the image file has already been downloaded to the `img` directory) node to LaTeX.
    """
    latex = f"\\begin{{figure}}[h!]\n"
    latex += f"  \\includegraphics[width=0.6\\textwidth]{{img/{img_node['src'].split('/')[-1]}}}\n"
    latex += f"  \\centering\n"
    latex += f"\\end{{figure}}"

    return latex


def pre_to_latex(pre_node: "bs4.element.Tag") -> str:
    """
    Convert preformatted text node to LaTeX.
    """
    latex = str(pre_node).replace("<pre>", "\\begin{lstlisting}\n").replace("</pre>", "\\end{lstlisting}")
    latex = latex.replace("<strong>", "").replace("</strong>", "")

    return latex


def ul_to_latex(ul_node: "bs4.element.Tag") -> str:
    """
    Convert an unordered list node to LaTeX.
    """
    latex = str(ul_node).replace("<ul>", "\\begin{itemize}").replace("</ul>", "\\end{itemize}")
    latex = latex.replace("<li>", "  \item{").replace("</li>", "}")

    return latex


def get_image_urls(question_content: "bs4.element.Tag") -> List[str]:
    """
    Return a list of URLs for the images in the question content.
    """
    image_urls: List[str] = list()
    for image_data in question_content.find_all("img"):
        image_url = image_data["src"]
        image_urls.append(image_url)

    return image_urls


def download_images(image_urls: List[str], target_dir: Path) -> None:
    """
    Download each image from the URL in the list and save in the target directory.
    """

    for image_url in image_urls:
        image_name: str = image_url.split("/")[-1]
        print(f"Downloading image from URL {image_url}...")
        request = requests.get(image_url)

        request.raise_for_status()

        image_path: Path = target_dir / image_name
        print(f"Saving image to file {image_path}...")
        with image_path.open(mode="wb") as image_file:
            image_file.write(request.content)


if __name__ == "__main__":

    PARSER = argparse.ArgumentParser(description="Set up a skeleton directory for creating a problem solution")
    PARSER.add_argument(
        "problem_number",
        type=int,
        help="Problem number"
    )

    ARGS: argparse.Namespace = PARSER.parse_args()

    RETURN_CODE: int = main(ARGS)

    sys.exit(RETURN_CODE)
