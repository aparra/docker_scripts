# SVN SERVER DOCKERFILE
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install wget git curl zip vim
RUN apt-get -y install subversion apache2 libapache2-svn apache2-utils libsvn-perl 
RUN apt-get -y install python-setuptools python-svn python-subversion

RUN mkdir -p /home/svn
RUN svnadmin create /home/svn/son_om

# Configure 'permisions'
RUN chmod -R 777 /home/svn

# Configure Apache to serve up Subversion
ADD apache/dav_svn.conf /etc/apache2/mods-available/dav_svn.conf
 
EXPOSE 80

CMD ["/usr/sbin/apache2ctl"]
