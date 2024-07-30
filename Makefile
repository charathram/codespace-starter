# Variables
VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
TEST_DIR := src/tests
REQUIREMENTS := requirements-dev.txt

# Default target
all: test

# Create virtual environment
$(VENV_DIR):
	python3 -m venv $(VENV_DIR)

# Install dependencies
install: $(VENV_DIR)
	$(PIP) install -r $(REQUIREMENTS)

# Run tests
test: install
	$(PYTHON) -m pytest $(TEST_DIR)

# Clean virtual environment and cache files
clean:
	rm -rf $(VENV_DIR) __pycache__ $(TEST_DIR)/__pycache__ .pytest_cache

# Linting
lint:
	$(PYTHON) -m flake8 .

# Format code
format:
	$(PYTHON) -m black .

# Help
help:
	@echo "Makefile commands:"
	@echo "  make all       - Install dependencies and run tests (default)"
	@echo "  make install   - Create virtual environment and install dependencies"
	@echo "  make test      - Run tests"
	@echo "  make clean     - Remove virtual environment and cache files"
	@echo "  make lint      - Run flake8 for linting"
	@echo "  make format    - Run black to format code"
	@echo "  make help      - Show this help message"