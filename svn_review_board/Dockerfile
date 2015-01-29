#SVN SERVER + REVIEW BOARD DOCKERFILE
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install wget git curl zip vim

# Install svn

RUN apt-get -y install subversion apache2 libapache2-svn apache2-utils libsvn-perl 
RUN apt-get -y install python-setuptools python-svn python-subversion

RUN easy_install -U simplejson 

# Install bug-fixed RBTolls
RUN git clone https://github.com/aparra/rbtools.git /home/rbtools
RUN /usr/bin/python /home/rbtools/setup.py install

RUN mkdir -p /home/svn
RUN svnadmin create /home/svn/son_om

# Set svn hooks
ADD svn/hooks/post-commit /home/svn/son_om/hooks/post-commit
ADD svn/hooks/create-ticket-reviewboard.py /home/svn/son_om/hooks/create-ticket-reviewboard.py
 
# Set "permissions"
RUN chmod -R 777 /home/svn
RUN chmod -R 777 /var/www
 
# Configure Apache to serve up Subversion
ADD apache/dav_svn.conf /etc/apache2/mods-available/dav_svn.conf

# Define locale
RUN localedef -i en_US -f UTF-8 en_US.UTF-8
 
EXPOSE 80

# Install review board

RUN apt-get -y install python-pip python-dev python-psycopg2

RUN easy_install -U reviewboard

RUN pip install -U uwsgi

ADD rb/start.sh /start_rb.sh
ADD rb/shell.sh /shell.sh

RUN chmod +x start_rb.sh shell.sh

ADD wsgi/uwsgi.ini /uwsgi.ini

VOLUME ["/.ssh", "/media/"]

EXPOSE 8000

ADD start.sh /start.sh
RUN chmod +x start.sh

CMD ["/start.sh"]
