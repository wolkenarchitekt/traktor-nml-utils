CONTAINER  = traktor-nml-utils
VIRTUALENV_DIR = .venv

clean:
	rm -rf dist
	rm -rf $(VIRTUALENV_DIR)

docker-build:
	docker build -t $(CONTAINER) .

docker-clean:
	-docker stop $(CONTAINER)
	-docker rm $(CONTAINER)

docker-shell:
	docker run -it --rm $(CONTAINER) bash

docker-test:
	docker run -it --rm $(CONTAINER) pytest

docker-lint:
	docker run -it --rm $(CONTAINER) flake8 traktor_nml_utils
	docker run -it --rm $(CONTAINER) mypy traktor_nml_utils
	docker run -it --rm $(CONTAINER) black --check --exclude traktor_nml_utils/models/ traktor_nml_utils tests/

virtualenv-create:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip install --upgrade setuptools pip && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt && \
		pip install -e .

virtualenv-test:
	. $(VIRTUALENV_DIR)/bin/activate && \
		pytest tests

pypi-upload:
	rm -rf dist
	. $(VIRTUALENV_DIR)/bin/activate && \
		python setup.py sdist && \
		twine upload dist/*

xml-to-xsd:
	# Generate XSD from XML using xmlbeans
	docker build \
		--build-arg inputfile=collection.nml \
		-t xml2xsd \
		-f ./xml_to_xsd/Dockerfile \
		./xml_to_xsd
	docker run xml2xsd > xml_to_xsd/collection.xsd

	docker build \
		--build-arg inputfile=history.nml \
		-t xml2xsd \
		-f ./xml_to_xsd/Dockerfile \
		./xml_to_xsd
	docker run xml2xsd > xml_to_xsd/history.xsd

xsd-to-python:
	. $(VIRTUALENV_DIR)/bin/activate && \
	    xsdata xml_to_xsd/collection.xsd --package traktor_nml_utils.models && \
	    xsdata xml_to_xsd/history.xsd --package traktor_nml_utils.models \
	        > traktor_nml_utils/models/__init__.py

xml-to-python: xml-to-xsd xsd-to-python
