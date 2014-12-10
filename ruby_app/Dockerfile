# RUBY APP DOCKERFILE
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install build-essential ruby2.0 ruby2.0-dev libmysqlclient-dev libv8-dev bundler git vim

RUN mkdir /app
WORKDIR /app

EXPOSE 3000

