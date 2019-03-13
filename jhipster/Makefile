.PHONY: build

build:
	docker build --rm -t jhipster380-java11 .

publish: build
	docker tag jhipster380-java11 aparra/jhipster:3.8.0-jdk11
	docker push aparra/jhipster:3.8.0-jdk11

