# Docker setup file used to prepare the docker container which you can use to run automated regression tests with GitHub actions.
FROM ubuntu:latest
ENV LANG=C.UTF-8

# System command for downloading all required programs needed to run your program.
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    build-essential \
    ccache \ 
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
    && /usr/sbin/update-ccache-symlinks \
    && echo 'export PATH="/usr/lib/ccache:$PATH"' | tee -a ~/.bashrc \
    && apt-get update \
    && apt-get install -y python3-virtualenv \
    && apt-get install -y python3-venv 

# Bash script used to run regression tests
COPY runCode.sh /runCode.sh
ENTRYPOINT ["/runCode.sh"]