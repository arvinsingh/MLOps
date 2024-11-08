.PHONY: run install check clean runner
.DEFAULT_GOAL := runner

run: install
	cd src; poetry run python runner.py;

install:
	poetry install

check:
	poetry run flake8 src

clean:
	rm -rf `find . -type d -name __pycache__`

runner: check run clean
