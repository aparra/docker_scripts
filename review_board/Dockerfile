# REVIEW BOARD DOCKERFILE
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install wget git curl zip vim
RUN apt-get -y install subversion python-setuptools python-pip python-dev python-psycopg2 python-svn python-subversion

RUN easy_install -U reviewboard

RUN pip install -U uwsgi 

ADD start.sh /start.sh
ADD shell.sh /shell.sh

RUN chmod +x start.sh shell.sh

ADD wsgi/uwsgi.ini /uwsgi.ini

VOLUME ["/.ssh", "/media/"]

EXPOSE 8000

CMD ["/start.sh"]
