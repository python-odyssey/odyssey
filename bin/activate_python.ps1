[CmdletBinding()]
param(
    [String]
    $Version = "3.7.7"
)

pyenv global $Version
pyenv rehash
