# SVN SERVER DOCKERFILE
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install wget git curl zip vim
RUN apt-get -y install subversion apache2 libapache2-svn apache2-utils libsvn-perl 
RUN apt-get -y install python-setuptools python-svn python-subversion

RUN easy_install -U simplejson 

# Install bug-fixed RBTolls
RUN git clone https://github.com/aparra/rbtools.git /home/rbtools
RUN python /home/rbtools/setup.py install

RUN mkdir -p /home/svn
RUN svnadmin create /home/svn/son_om

# Set svn hooks
ADD svn/hooks/post-commit /home/svn/son_om/hooks/post-commit
ADD svn/hooks/create-ticket-reviewboard.py /home/svn/son_om/hooks/create-ticket-reviewboard.py
 
# Set permissions
RUN addgroup subversion
#RUN usermod -a -G subversion www-data
#RUN chown -R www-data:subversion /home/svn
RUN chmod -R g+rws /home/svn
RUN chmod o+x /home/svn/son_om/hooks/post-commit
RUN chmod o+x /home/svn/son_om/hooks/create-ticket-reviewboard.py
 
# Configure Apache to serve up Subversion
#RUN rm /etc/apache2/mods-available/dav_svn.conf
ADD apache/dav_svn.conf /etc/apache2/mods-available/dav_svn.conf
 
#ENV APACHE_RUN_USER    www-data
#ENV APACHE_RUN_GROUP   www-data
#ENV APACHE_PID_FILE    /var/run/apache2.pid
#ENV APACHE_RUN_DIR     /var/run/apache2
#ENV APACHE_LOCK_DIR    /var/lock/apache2
#ENV APACHE_LOG_DIR     /var/log/apache2

EXPOSE 80

CMD ["/usr/sbin/apache2ctl"]
