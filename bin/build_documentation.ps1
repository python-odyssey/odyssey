Push-Location (Resolve-Path (Join-Path $PSScriptRoot '..' 'docs'))
try {
    poetry run .\make.bat html
} finally {
    Pop-Location
}
