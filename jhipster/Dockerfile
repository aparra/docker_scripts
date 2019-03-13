FROM jhipster/jhipster:v3.8.0

MAINTAINER Anderson Parra <ander.pp@gmail.com>

USER root

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install software-properties-common

# install jdk-11
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get -y install openjdk-11-jdk

# install mysql-client
RUN apt-get -y install mysql-client

# default user from jhipster container
USER jhipster

