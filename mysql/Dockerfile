# MYSQL DOCKERFILE
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install mysql-client mysql-server

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
RUN /usr/sbin/mysqld & \
    sleep 10s &&\
    echo "GRANT ALL ON *.* TO myuser@'%' IDENTIFIED BY 'mypassword' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql

EXPOSE 3306
CMD ["/usr/bin/mysqld_safe"]

