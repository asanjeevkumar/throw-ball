# Clear PYTHONPATH to ensure we don't accidentally import files from elsewhere
export PYTHONPATH=
PYTHON := python3.6

check-coding-standards: check-pycodestyle check-pylint

.python-files:
	find . -path ./venv -prune -o -type f -name '*.py' -print > $@

.INTERMEDIATE: .python-files

with_python_files := xargs --arg-file .python-files

check-pycodestyle: venv | .python-files
	$(with_python_files) $</bin/python -m pycodestyle --config=.pycodestyle

check-pylint: venv | .python-files
	$(with_python_files) $</bin/python -m pylint

requirements.txt: | requirements.in
	$(PYTHON) -m piptools compile --output-file $@ $<

deps: venv

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv --python=$(PYTHON)
	venv/bin/python -m pip install pip==18.0
	venv/bin/python -m pip install -r $< --progress-bar off
	touch $@

clean:
	find . -name '*.pyc' -type f -delete
	find . -name '__pycache__' -type d -delete
	rm -rf venv

.PHONY: check-coding-standards check-pylint clean deps