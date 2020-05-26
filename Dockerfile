FROM ubuntu:17.10

RUN apt update && apt install -y python3 \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y python3-pip

RUN groupadd -r analysis && useradd -m --no-log-init --gid analysis analysis

RUN pip3 install lizard

USER analysis
COPY src /analyzer

WORKDIR /
CMD ["/analyzer/analyze.sh"]

