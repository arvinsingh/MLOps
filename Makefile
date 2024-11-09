.PHONY: run-builder run-inference install check clean runner-builder runner-inference
.DEFAULT_GOAL := runner-inference

run-builder: install
	cd src; poetry run python runner_builder.py;

run-inference: install
	cd src; poetry run python runner_inference.py;

install:
	poetry install

check:
	poetry run flake8 src

clean:
	rm -rf `find . -type d -name __pycache__`

runner-builder: check run-builder clean

runner-inference: check run-inference clean