# Leetcode Solutions

Solutions to problems from [leetcode](https://leetcode.com/).

## Prerequisites

- Powershell (eventually will have bash available as well)
- xelatex
- Python 3.9+
- pipenv
- cmake 3.10+
- C++14 compatible compiler

Project has been developed and tested on Windows 10 using the following:

- Powershell 5.1.19041.1320
- MiKTeX-XeTeX 4.4 (MiKTeX 21.6)
- Python 3.9.4
- pipenv, version 2020.11.15
- cmake version 3.10.0
- MSVC 19.16.27045.0

## Usage

To pull the problem statement and set up a skeleton directory for problem number `PROBLEM_NUMBER`, run the following
command from the root directory of the project:

```shell
.\Start-Problem.ps1 PROBLEM_NUMBER
```

At this time, only non-paid only problems are available.

Once the skeleton directory is set up, the user can navigate to the newly created `problems/problem-PROBLEM_NUMBER`
directory and begin documenting and implementing solutions to the problem.

### Documentation

Documentation is LaTeX-based. The user fills in the appropriate `.tex` files in the documentation directory, namely
`problems/problem-PROBLEM_NUMBER/documentation/tex`, and builds a PDF using the `Build-Document.ps1` script located in
the `problems/problem-PROBLEM_NUMBER/documentation` directory by running the following command from that directory:

```shell
.\Build-Document.ps1
```

The result, provided the build is successful, is a `Problem-PROBLEM_NUMBER.pdf` file located in the
`problems/problem-PROBLEM_NUMBER/documentation` directory. Some additional, non-tracked build artifacts are also
produced in a `problems/problem-PROBLEM_NUMBER/documentation/.build` directory.

### Implementation

Currently, skeleton files for the following languages are produced when the `Start-Problem.ps1` script is called:

- C++
- Python

For a given language `LANGUAGE`, the skeleton files are produced in a
`problems/problem-PROBLEM_NUMBER/solutions/LANGUAGE` directory. The general structure of this directory, although the
file names and types vary between languages, is as follows:

```plaintext
problems
|
+ problem-PROBLEM_NUMBER
.   |
.   + solutions
.   .   |
    .   + LANGUAGE
    .       |
            + Environment-Rules.environment-rules-ext
            + Solution-PROBLEM_NUMBER.solution-ext
            + Solution-PROBLEM_NUMBER-Test.solution-test-ext
            + Test-LANGUAGE-Solution.ps1
```

The user should not have to touch the `Environment-Rules.environment-rules-ext` or `Test-LANGUAGE-Solution.ps1` files.
These are pre-generated from templates and _should_ just work.

Ideally, a TDD-based approach is followed and the user adds unit tests in the
`Solution-PROBLEM_NUMBER-Test.solution-test-ext` file to ensure the solution to be implemented actually does what it is
supposed to. These unit tests are executed by running the following command from the
`problems/problem-PROBLEM_NUMBER/solutions/LANGUAGE` directory:

```shell
.\Test-LANGUAGE-Solution.ps1
```

The user implements a solution to the problem in the `Solution-PROBLEM_NUMBER.solution-ext` file.

### C++ Solutions

The skeleton directory for a C++ implementation of the solution to problem `PROBLEM_NUMBER` lives in the
`problems/problem-PROBLEM_NUMBER/solutions/cpp` directory, which is structured as follows:

```plaintext
problems
|
+ problem-PROBLEM_NUMBER
.   |
.   + solutions
.   .   |
    .   + cpp
    .   .   |
        .   + CMakeLists.txt
        .   + Solution-PROBLEM_NUMBER.h
            + Solution-PROBLEM_NUMBER.test.cpp
            + Test-CPP-Solution.ps1
```

The unit test framework used is [`Doctest`](https://github.com/doctest/doctest), which is included in the project as a
`git` submodule and lives in the `libs\cpp\external\doctest` directory. The user implements unit tests in the
`Solution-PROBLEM_NUMBER.test.cpp` file.

The solution is implemented in a header file `Solution-PROBLEM_NUMBER.h` which contains at least a `Solution` class
that implements an algorithm that solves the problem. This header file is `#include`d in the
`Solution-PROBLEM_NUMBER.test.cpp` file.

CMake is used to configure the build system and build the unit test executable from the
`Solution-PROBLEM_NUMBER.test.cpp` file. Both of these steps are taken care of by running the following command from 
the `problems/problem-PROBLEM_NUMBER/solutions/cpp` directory:

```shell
.\Test-CPP-Solution.ps1
```

### Python Solutions

The skeleton directory for a Python implementation of the solution to problem `PROBLEM_NUMBER` lives in the
`problems/problem-PROBLEM_NUMBER/solutions/python` directory, which is structured as follows:

```plaintext
problems
|
+ problem-PROBLEM_NUMBER
.   |
.   + solutions
.   .   |
    .   + python
    .   .   |
        .   + Pipfile
        .   + solution_PROBLEM_NUMBER.py
            + test_solution_ROBLEM_NUMBER.py
            + Test-Python-Solution.ps1
```

The unit test framework used is [unittest](https://docs.python.org/3.9/library/unittest.html) from the Python standard
library. The user implements unit tests in the `test_solution_ROBLEM_NUMBER.py` file.

The solution is implemented in the file `solution_PROBLEM_NUMBER.py` which contains at least a `Solution` class
that implements an algorithm that solves the problem. This file is `import`ed in the `test_solution_ROBLEM_NUMBER.py`
file.

Pipenv is used to create and maintain the virtual environment for the solution. The unit tests are executed by running
the following command from the `problems/problem-PROBLEM_NUMBER/solutions/python` directory:

```shell
.\Test-Python-Solution.ps1
```
