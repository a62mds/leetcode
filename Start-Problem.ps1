<#
.Synopsis
   Set up skeleton directory for implementing solution to a problem.
.DESCRIPTION
   Use the Python tools in the `tools` directory to render the implementation file templates.
.EXAMPLE
   .\Start-Problem.ps1 PROBLEM_NUMBER
.INPUTS
   PROBLEM_NUMBER
     Valid non-paid only Leetcode problem number.
.OUTPUTS
   Solution implementation directory with skeleton files.
.NOTES
   Version 1.0

   Returns 0 if successful, 1 otherwise.
#>
Param(
    [Parameter(Mandatory=$true)][Int32]$PROBLEM_NUMBER
)

[Int32]$RETURN_CODE = 0

Try {
    Set-Location tools
    pipenv run python start_problem.py $PROBLEM_NUMBER
} Catch {
    Write-Error $Error[0]
    $RETURN_CODE = 1
} Finally {
    Set-Location $PSScriptRoot
}

Exit $RETURN_CODE
