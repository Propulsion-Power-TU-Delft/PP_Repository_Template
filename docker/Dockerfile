# Docker setup file used to prepare the docker container which you can use to run automated regression tests with GitHub actions.
FROM ubuntu:latest
ENV LANG=C.UTF-8

# System command for downloading all required programs needed to run your program.
RUN apt-get update && apt-get install -y \
    python3 \
    git \
    build-essential \
    ccache && \ 
    apt-get update && \
    apt-get install -y python3-virtualenv

# Bash script used to run regression tests
COPY runCode.sh /runCode.sh
ENTRYPOINT ["/runCode.sh"]