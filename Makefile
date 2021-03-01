.PHONY: run init-python3


run:
	@. .venv/bin/activate
	@python -m sim.main


init-python3:
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
