FROM ubuntu:focal-20210401

WORKDIR /mnt/temp

COPY bin/install_apt_packages.sh \
     bin/install_pyenv.sh \
     bin/install_python.sh \
     bin/activate_python.sh \
     bin/install_poetry.sh \
     ./

SHELL ["/bin/bash", "-c"]

RUN ./install_apt_packages.sh
RUN ./install_pyenv.sh
RUN . ~/.bashrc && ./install_python.sh 3.7.7
RUN . ~/.bashrc && ./activate_python.sh 3.7.7
RUN . ~/.bashrc && ./install_poetry.sh

WORKDIR /mnt/odyssey

CMD /bin/bash
