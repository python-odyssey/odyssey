FROM mcr.microsoft.com/powershell:lts-windowsservercore-2004

WORKDIR C:/temp

COPY bin/install_choco.ps1 \
     bin/install_pyenv.ps1 \
     bin/refresh_path.ps1 \
     bin/install_python.ps1 \
     bin/activate_python.ps1 \
     bin/install_poetry.ps1 \
     bin/install_git.ps1 \
     ./

SHELL ["pwsh", "-c"]

USER ContainerUser

RUN .\install_choco.ps1 && \
    .\install_pyenv.ps1 && \
    .\install_python.ps1 3.7.7 && \
    .\activate_python.ps1 3.7.7 && \
    .\install_poetry.ps1 && \
    .\install_git.ps1

WORKDIR C:/odyssey

CMD pwsh
