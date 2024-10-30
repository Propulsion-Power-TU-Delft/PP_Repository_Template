# Base image
FROM ubuntu:latest
ENV LANG C.UTF-8
# Install all programs and modules necessary for your running your code.

RUN apt-get update && apt-get install -y \
    python3 \
    pkg-config \
    python3-pip \
    git \ 
    build-essential \ 
    ccache \ 
# Python modules
  && python3 -m pip install \
    numpy=1.26.4 \
    scikit-learn=1.2.2 \
    tensorflow=2.15.0 \ 
  && rm -rf /var/lib/apt/lista/* \
  && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
  && /usr/sbin/update-ccache-symlinks \
  && echo 'export PATH="/usr/lib/ccache:$PATH"' | tee -a ~/.bashrc

COPY docker/runCode.sh /runCode.sh

ENTRYPOINT /runCode.sh