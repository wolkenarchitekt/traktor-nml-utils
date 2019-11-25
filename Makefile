CONTAINER  = traktor-nml-utils
HOST_UID = $(shell id -u)
HOST_GID = $(shell id -g)

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
	docker run --user $(UID):$(GID) -v $(PWD)/dist:/app/dist -it --rm $(CONTAINER) python setup.py sdist
	docker run --user $(UID):$(GID) -v $(PWD)/dist:/app/dist -it --rm $(CONTAINER) twine upload dist/*

