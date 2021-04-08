param (
    $ContainerName
)

$ResourcesScript = "$PSScriptRoot/../docker/$ContainerName/resources.ps1"
if (Test-Path $ResourcesScript) {
    Invoke-Expression $ResourcesScript
}

docker build -t odyssey/$ContainerName -f $PSScriptRoot\..\docker\$ContainerName\Dockerfile $PSScriptRoot\..
