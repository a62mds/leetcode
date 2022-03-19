<#
.Synopsis
   Leetcode test runner script.
.DESCRIPTION
   Builds the test project and runs the executable produced.
.EXAMPLE
   .\Test-CPP-Solution.ps1
.INPUTS
   None
.OUTPUTS
   Results of the test run.
.NOTES
   Version 1.0
#>

[String]$TEST_DIRECTORY = ".test"
[Int32]$RETURN_CODE = 0

Try {
    If (!(Test-Path "$TEST_DIRECTORY")) {
        New-Item -Type directory "$TEST_DIRECTORY"
    }
    Set-Location "$TEST_DIRECTORY"
    cmake ..
    cmake --build .
    Set-Location Debug
    & ".\Test-Solution-0002.exe"
} Catch {
    Write-Error $Error[0]
    $RETURN_CODE = 1
} Finally {
    Set-Location $PSScriptRoot
}

Exit $RETURN_CODE
