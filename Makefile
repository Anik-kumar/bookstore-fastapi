CONTAINER_NAME:=fast-api-project
TAG:=latest
VERSION:=0.1.1

.PHONY: build
build:
	docker build \
		--build-arg VERSION=$(VERSION) \
		--tag $(CONTAINER_NAME):$(TAG) \
		.

.PHONY: lint
lint:
	poetry run black --check .
	poetry run pylint_runner --rcfile ./.pylintrc

.PHONY: reformat
reformat:
	poetry run black .
	poetry run pylint_runner --rcfile ./.pylintrc

.PHONY: run
run:
	docker-compose stop
	docker-compose up
