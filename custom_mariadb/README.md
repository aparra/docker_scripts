## Testing

    docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true aparra/custom_mariadb
    mysql -u root -h 0.0.0.0
    use custom_db;
    select * from some_table;

