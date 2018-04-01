TEMPFILE := $(shell mktemp -u)

.PHONY: install clean uninstall venv check doc docs html api coala pylint pydocstyle pytest

install:
	sh ./bump-version.sh
	pip3 install -r requirements.txt
	python3 setup.py install

uninstall:
	python3 setup.py install --record ${TEMPFILE} && \
		cat ${TEMPFILE} | xargs rm -rf && \
		rm -f ${TEMPFILE}

devenv:
	@echo "Installing latest development requirements"
	pip3 install -U -r dev_requirements.txt

venv:
	virtualenv -p python3 venv && source venv/bin/activate && pip3 install -r requirements.txt
	@echo "Run 'source venv/bin/activate' to enter virtual environment and 'deactivate' to return from it"

clean:
	find . -name '*.pyc' -or -name '__pycache__' -print0 | xargs -0 rm -rf
	rm -rf venv venv-coala coverage.xml
	rm -rf dist json2sql.egg-info build

pytest:
	@echo ">>> Executing testsuite"
	python3 -m pytest -s --cov=./json2sql -vvl --timeout=2 test/*.py

pylint:
	@echo ">>> Running pylint"
	pylint json2sql

coala:
	@# We need to run coala in a virtual env due to dependency issues
	@echo ">>> Preparing virtual environment for coala" &&\
	  # setuptools is pinned due to dependency conflict &&\
	  [ -d venv-coala ] || virtualenv -p python3 venv-coala &&\
	   . venv-coala/bin/activate &&\
	   pip3 install coala-bears "setuptools>=17.0" &&\
	  echo ">>> Running coala" &&\
	  venv-coala/bin/python3 venv-coala/bin/coala --non-interactive

pydocstyle:
	@echo ">>> Running pydocstyle"
	pydocstyle json2sql test

check: pytest pylint pydocstyle coala

docs: doc
html: doc
test: check
