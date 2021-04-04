[CmdletBinding()]
param(
    [String]
    $Python = (if(Test-Path "Env:PYTHON_EXECUTABLE") { "$Env:PYTHON_EXECUTABLE" } else { "python" })
)

poetry env use $Python
