.PHONY: run init-python3 prep

default: run

run:
	@. .venv/bin/activate; python -m sim.main

prep:
	. .venv/bin/activate; pip freeze > requirements.txt; pip install -r requirements.txt

init-python3:
	python3 -m venv .venv
	. .venv/bin/activate; pip install -r requirements.txt
