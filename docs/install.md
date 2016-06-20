# Installation instructions for Beer Tracker.

## Requirements

- [Python 3.5.0](https://www.python.org/)
- [Pyenv](https://github.com/yyuu/pyenv)
- [Pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
- [Pip](https://pip.pypa.io/en/latest/installing.html)
- [Postgresql](https://www.postgresql.org/download/)
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
pip install -r pip-linux.txt

# Run project
./run.py

# Open web browser to localhost:5000
open http://localhost:5000
~~~ 

## Windows
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
pip install -r pip-win.txt

# Run project
./run.py

# Open web browser to localhost:5000
open http://localhost:5000
~~~ 

If you get errors, you probably didn't have the correct build tools 
(included if you have Visual Studio 2010). 
In that case, follow the directions below and then retry.

# PyCrypto (Windows)

You'll need to install PyCrypto which requires compilation (and relevant 
interpreter) OR downloading a wheel / binary installer.

**Compile from source**

Python 3.5 needs this compiler: Microsoft Visual C++ 14.0:

http://landinghub.visualstudio.com/visual-cpp-build-tools

Python 3.3 or 3.4 needs this compiler: Microsoft Visual C++ 10.0:

http://download.microsoft.com/download/1/D/9/1D9A6C0E-FC89-43EE-9658-B9F0E3A76983/vc_web.exe

**Or use a pre-compiled binary**

https://github.com/sfbahr/PyCrypto-Wheels
32 or 64 bit Python 3.5 (run command below)
...for 64-bit: pip install --use-wheel --no-index --find-links=https://github.com/sfbahr/PyCrypto-Wheels/raw/master/pycrypto-2.6.1-cp35-none-win_amd64.whl pycrypto
...for 32-bit: pip install --use-wheel --no-index --find-links=https://github.com/sfbahr/PyCrypto-Wheels/raw/master/pycrypto-2.6.1-cp35-none-win32.whl pycrypto

https://github.com/axper/python3-pycrypto-windows-installer
32 or 64 bit Python 3.4 (self installing binary)

## Optional
~~~ sh
# Create virtual environment
virtualenv env

# Activate virtual environment
. env/bin/activate
~~~
