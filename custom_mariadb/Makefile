.PHONY: build

build:
	docker build --rm -t custom_mariadb .

publish: build
	docker tag custom_mariadb aparra/custom_mariadb
	docker push aparra/custom_mariadb

