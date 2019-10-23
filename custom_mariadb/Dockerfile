FROM mariadb

MAINTAINER Anderson Parra <ander.pp@gmail.com>

# Add the content of the sql-scripts/ directory to image
# All scripts in docker-entrypoint-initdb.d/ are automatically executed during container startup
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

