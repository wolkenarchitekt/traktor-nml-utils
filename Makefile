CONTAINER  = traktor-nml-utils
HOST_UID = $(shell id -u)
HOST_GID = $(shell id -g)
DOCKER_CMD = docker run --user $(UID):$(GID) -v $(PWD):/app -it --rm $(CONTAINER)

build:
	docker build -t $(CONTAINER) .

clean:
	-docker stop $(CONTAINER)
	-docker rm $(CONTAINER)

shell:
	docker run -it --rm $(CONTAINER) bash

test:
	docker run -it --rm $(CONTAINER) pytest

lint:
	docker run -it --rm $(CONTAINER) flake8

mypy:
	docker run -it --rm $(CONTAINER) pytest --mypy

publish:
	$(DOCKER_CMD) pandoc --from=markdown --to=rst --output=README README.md
	$(DOCKER_CMD) python setup.py sdist
	$(DOCKER_CMD) twine upload dist/*
