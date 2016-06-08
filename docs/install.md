# Installation instructions for Beer Tracker.

## Requirements

- [Python 3.5.0](https://www.python.org/)
- [Pyenv](https://github.com/yyuu/pyenv)
- [Pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
- [Pip](https://pip.pypa.io/en/latest/installing.html)
- Optional [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## For local development, set dev environment variable

Set this environment variable in your .bashrc or .zshrc
~~~ sh
export ENVIRONMENT="dev"
~~~

## Installation
~~~ sh
# Clone repo and cd to repo
git clone git@github.com:ChadevPython/beer-tracker.git

# Set config file
copy/rename config/example-dev.py to config/dev.py
this is where we store local config variables hidden from git

# Set current directory python version
pyenv local 3.5.0

# Create virtual environment
pyenv virtualenv beer-tracker

# Set current directory to beer-tracker virtual environment
# pyenv-virtualenv will automatically activate this environment
pyenv local beer-tracker

# Install project dependencies
pip install -r pip.txt

# Run project
./run.py

# Open web browser to localhost:5000
open http://localhost:5000
~~~ 

## Optional
~~~ sh
# Create virtual environment
virtualenv env

# Activate virtual environment
. env/bin/activate
~~~
