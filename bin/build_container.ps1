param (
    $ContainerCategory,
    $ContainerName
)

$ResourcesScript = "$PSScriptRoot/../docker/$ContainerCategory/$ContainerName/resources.ps1"
if (Test-Path $ResourcesScript) {
    Invoke-Expression $ResourcesScript
}

docker build -t odyssey/$ContainerCategory/$ContainerName -f $PSScriptRoot\..\docker\$ContainerCategory\$ContainerName\Dockerfile $PSScriptRoot\..
