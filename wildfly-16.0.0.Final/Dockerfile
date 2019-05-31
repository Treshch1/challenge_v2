FROM openjdk:11.0.3-jdk-stretch

RUN mkdir /src

ADD . /src

EXPOSE 8080

CMD ["/bin/bash", "/src/bin/standalone.sh"]