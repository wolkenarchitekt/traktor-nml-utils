CONTAINER  = traktor-nml-utils
VIRTUALENV_DIR = .venv

docker-build:
	docker build -t $(CONTAINER) .

docker-clean:
	-docker stop $(CONTAINER)
	-docker rm $(CONTAINER)

docker-shell:
	docker run -it --rm $(CONTAINER) bash

docker-test:
	docker run -it --rm $(CONTAINER) pytest -s -v tests/test_parser.py::test_get_cuepoints

docker-lint:
	docker run -it --rm $(CONTAINER) flake8

docker-mypy:
	docker run -it --rm $(CONTAINER) pytest --mypy

virtualenv-build:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt && \
		pip install -e .

virtualenv-test:
	. $(VIRTUALENV_DIR)/bin/activate && \
		pytest -s -v tests/test_parser.py::test_get_cuepoints

package:
	# Convert readme for pypi
	pandoc --from=markdown --to=rst --output=README README.md

xml_schema_build:
	docker build \
		--build-arg inputfile=collection.nml \
		-t trang \
		-f ./xml_schema_gen/Dockerfile \
		./xml_schema_gen
	docker run --rm -v $(PWD):/opt/workspace trang
xml_schema_run:
generate-models:
#	docker build \
#		--build-arg inputfile=collection.nml \
#		--build-arg package="traktor_nml_utils.schema.collection" \
#		-t trang \
#		-f ./xml_schema_gen/Dockerfile \
#		./xml_schema_gen
#	docker run --rm -v $(PWD):/opt/workspace trang

#	docker build \
#		--build-arg inputfile=history.nml \
#		--build-arg package="traktor_nml_utils.models.history" \
#		-t trang \
#		-f ./xml_schema_gen/Dockerfile \
#		./xml_schema_gen
	docker run --rm -v $(PWD):/opt/workspace trang
