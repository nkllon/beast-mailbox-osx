.PHONY: help clean build install test lint format wheel

help:
	@echo "beast-mailbox-osx - macOS native extensions"
	@echo ""
	@echo "Available targets:"
	@echo "  clean    - Remove build artifacts"
	@echo "  build    - Build extension in-place"
	@echo "  install  - Install in development mode"
	@echo "  test     - Run tests"
	@echo "  lint     - Run linters"
	@echo "  format   - Format code"
	@echo "  wheel    - Build universal2 wheel"

clean:
	rm -rf build/ dist/ wheelhouse/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.so" -delete

build: clean
	python setup.py build_ext --inplace

install:
	pip install -e ".[dev]"

test: build
	pytest tests/ -v

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/

wheel: clean
	python -m cibuildwheel --output-dir dist

.DEFAULT_GOAL := help

