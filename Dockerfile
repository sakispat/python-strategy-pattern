FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-minimal python3-setuptools python3-pip && \
    pip3 install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY init.sh /usr/src/app/init.sh

RUN chmod +x /usr/src/app/init.sh

CMD [ "tail", "-f", "/dev/null" ]