.PHONY: build test run clean

# Docker image name
IMAGE_NAME = factorial-api

build:
	docker build -t $(IMAGE_NAME) .

test:
	docker run --rm $(IMAGE_NAME) pytest -v

run:
	docker run --name testing -p 9000:9000 $(IMAGE_NAME)

stop:
	docker stop testing || true

clean: stop
	docker rmi $(IMAGE_NAME) || true