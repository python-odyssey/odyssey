[CmdletBinding()]
param(
    [String]
    $Version = "3.7.7"
)

pyenv update
pyenv install $Version
pyenv rehash
