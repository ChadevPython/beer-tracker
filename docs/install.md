# Installation instructions for Beer Tracker.

## Requirements

- [Python 2.7](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Pip](https://pip.pypa.io/en/latest/installing.html)

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

# Create virtual environment
virtualenv env

# Activate virtual environment
. env/bin/activate

# Install project dependencies
pip install -r pip.txt

# Run project
./run.py

# Open web browser to localhost:5000
open http://localhost:5000

~~~
