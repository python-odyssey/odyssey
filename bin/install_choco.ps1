[CmdletBinding(PositionalBinding=$False)]
param()

$Env:ChocolateyInstall = Join-Path "$Env:USERPROFILE" ".choco"
Write-Verbose "choco install directory: $Env:ChocolateyInstall"

Set-ExecutionPolicy Bypass -Scope Process

Write-Verbose "Installing choco"
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
