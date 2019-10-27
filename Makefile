.DEFAULT_GOAL := help
VIRTUALENV_DIR = .venv
CONTAINER  = traktor-nml-utils

build:  ## Build Docker container
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
