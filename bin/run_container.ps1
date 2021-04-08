param (
    [String]
    $ContainerName,
    [Switch]
    $Test = $False
)

$HostPath = Resolve-Path (Join-Path $PSScriptRoot ..)
if ($ContainerName -match "windows") {
    $ContainerPath = "C:\odyssey"
    $ContainerCommand = @("pwsh", "-c", ".\bin\install_dependencies.ps1 && .\bin\run_pytest.ps1")
}
else {
    $ContainerPath = "/mnt/odyssey"
    $ContainerCommand = @("sh", "-c", ". ~/.profile && ./bin/install_dependencies.sh && ./bin/run_pytest.sh")
}

if ($Test) {
    docker run --interactive --tty --volume "$HostPath`:$ContainerPath" odyssey/$ContainerName @ContainerCommand
}
else {
    docker run --interactive --tty --volume "$HostPath`:$ContainerPath" odyssey/$ContainerName
}
