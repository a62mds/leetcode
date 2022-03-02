<#
.Synopsis
   Builds a PDF document from the LaTeX files.
.DESCRIPTION
   Convenience script that ensures dependencies are installed and runs the appropriate command to build a PDF from the
   LaTeX files.
.EXAMPLE
   .\Build-Documentation-0001.ps1
.INPUTS
   None.
.OUTPUTS
   PDF document along with some further LaTeX artifacts.
.NOTES
   Version 1.0.0
#>
[String]$PROBLEM_NAME = "Problem-0001"
[String]$MAIN_TEX_FILENAME = "main.tex"
[String]$BUILD_DIRNAME = ".build"

[Int32]$RETURN_CODE = 0


Try {
    # Ensure XeLaTeX is installed (will throw System.Management.Automation.CommandNotFoundException otherwise)
    xelatex --version | Out-Null

    # Build the document twice to get references right
    For ($i = 0; $i -lt 2; $i++) {
        xelatex -output-directory "${PSScriptRoot}/${BUILD_DIRNAME}" -jobname "${PROBLEM_NAME}" "${MAIN_TEX_FILENAME}"
        if ($LastExitCode -ne 0) {
            Write-Host "Error: Failed to build '${MAIN_TEX_FILENAME}'" -ForegroundColor Red
            Exit 1
        }
    }

    Move-Item -Path "${PSScriptRoot}/${BUILD_DIRNAME}/${PROBLEM_NAME}.pdf" -Destination "${PSScriptRoot}"
}
Catch {
    Write-Error $Error[0]
    $RETURN_CODE = 1
}
Finally {
    Set-Location $PSScriptRoot
}

Exit $RETURN_CODE
