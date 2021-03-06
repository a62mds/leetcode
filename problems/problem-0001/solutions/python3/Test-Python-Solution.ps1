<#
.Synopsis
   Leetcode test runner script for Python solutions.
.DESCRIPTION
   Runs the unit tests.
.EXAMPLE
   .\Test-Python-Solution.ps1
.INPUTS
   None
.OUTPUTS
   Results of the test run.
.NOTES
   Version 1.0
#>

[Int32]$RETURN_CODE = 0

Try {
    pipenv run python -m unittest discover
} Catch {
    Write-Error $Error[0]
    $RETURN_CODE = 1
} Finally {
    Set-Location $PSScriptRoot
}

Exit $RETURN_CODE
