CONTAINER  = traktor-nml-utils
HOST_UID = $(shell id -u)
HOST_GID = $(shell id -g)
NML_DIR = /home/ifischer/traktor3/History
DOCKER_CMD = docker run --user $(UID):$(GID) -v $(PWD):/app -v $(NML_DIR):/traktor:ro -it --rm $(CONTAINER)
VIRTUALENV_DIR = .venv

build:
	docker build -t $(CONTAINER) .

clean:
	find . \! -user $(USER) -exec sudo chown $(USER) {} \;
	rm -rf *.egg-info .tox .pytest_cache .venv
	-docker stop $(CONTAINER)
	-docker rm $(CONTAINER)

shell:
	$(DOCKER_CMD) bash

test:
	$(DOCKER_CMD) pytest

lint:
	$(DOCKER_CMD) flake8

mypy:
	$(DOCKER_CMD) pytest --mypy

test-import:
	$(DOCKER_CMD) traktor_nml_utils traktor-import-dir --nml-dir /traktor

publish:
	$(DOCKER_CMD) pandoc --from=markdown --to=rst --output=README README.md
	$(DOCKER_CMD) python setup.py sdist
	$(DOCKER_CMD) twine upload dist/*

.PHONY: virtualenv
virtualenv:
	virtualenv --python=/usr/bin/python3.7 $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip install -r requirements.txt && \
        pip install -r requirements-dev.txt && \
        pip install .
