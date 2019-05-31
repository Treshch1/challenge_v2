FROM selenium/standalone-chrome

ENV PYTHONUNBUFFERED 1

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip netcat \
 	&& apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /src && chown seluser:seluser /src && mkdir /src-docker && chown seluser:seluser /src-docker

ADD --chown=seluser:seluser requirements.txt /src-docker/requirements.txt

RUN pip3 install --no-cache-dir -U pip setuptools \
    && pip install --no-cache-dir -r /src-docker/requirements.txt

ADD --chown=seluser:seluser . /src

ENV PYTHONPATH /src

WORKDIR /src

CMD ["pytest"]