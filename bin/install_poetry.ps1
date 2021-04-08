Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing -OutFile get-poetry.py;
& python get-poetry.py --yes --version 1.0.9;
Remove-Item get-poetry.py;

$PoetryHome = Join-Path -Path "$env:USERPROFILE" -ChildPath ".poetry/bin"
$Path = [System.Environment]::GetEnvironmentVariable("PATH", "User") + ";" + $PoetryHome

[System.Environment]::SetEnvironmentVariable("PATH", $Path, "User")

Push-Location $PSScriptRoot
try {
    .\refresh_path.ps1
}
finally {
    Pop-Location
}
