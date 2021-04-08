[CmdletBinding(PositionalBinding=$False)]
param()

$Env:ChocolateyInstall = Join-Path "$Env:USERPROFILE" ".choco"
Write-Verbose "choco install directory: $Env:ChocolateyInstall"

"Yes" | choco install pyenv-win --yes

$PyEnvHome = Join-Path -Path "$env:USERPROFILE" -ChildPath ".pyenv/pyenv-win"

[System.Environment]::SetEnvironmentVariable("PYENV", $PyEnvHome, "User")
[System.Environment]::SetEnvironmentVariable("PYENV_HOME", $PyEnvHome, "User")

$Env:PYENV = "$PyEnvHome"
$Env:PYENV_HOME = "$PyEnvHome"

Push-Location $PSScriptRoot
try {
    .\refresh_path.ps1
}
finally {
    Pop-Location
}
