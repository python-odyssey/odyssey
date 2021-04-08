[CmdletBinding(PositionalBinding=$False)]
param()

choco install git --yes

Push-Location $PSScriptRoot
try {
    .\refresh_path.ps1
}
finally {
    Pop-Location
}
