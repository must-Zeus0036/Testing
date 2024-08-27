# Makefile for Pig Dice Game

# Variables
PYTHON = python
VENV_DIR = venv
SOURCE = pig_game.py
REQUIREMENTS = requirements.txt

# Targets
.PHONY: all run venv clean

all: run

run:
	$(PYTHON) $(SOURCE)

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/Scripts/activate && pip install -r $(REQUIREMENTS)

clean:
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
venv:
    python -m venv venv
    venv/Scripts/activate && pip install -r requirements.txt
