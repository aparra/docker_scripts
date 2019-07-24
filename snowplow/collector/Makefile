.PHONY: build publish

build:
	docker build --rm -t scala-stream-collector-kinesis .

publish: build
	docker tag scala-stream-collector-kinesis aparra/scala-stream-collector-kinesis:0.15.0
	docker push aparra/scala-stream-collector-kinesis:0.15.0

