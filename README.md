# ideal-octo-telegram

API to control your devices on your network and make all your automation scripts available at one place


## Requirements:

* Docker
* Docker-Compose
* Ansible:
    * To Deploy on your own servers
* Python 3.9
* Postgresql
* [Poetry](https://python-poetry.org/docs/#installation)


## Getting Started:

* Install some postgresql dependencies to compile the code:
    * On Linux:
        * Ubuntu/Debian: `sudo apt install libpq-devel python3-dev`
        * Fedora 34: `sudo dnf install libpq-devel python-devel`
    * On macOS:
        * `brew install postgresql`
* Before running `make install`

## Stuff to Know:

* You can register a user on `/api/auth/registration`
* Prod build run on port`80`
* You can build images by running `docker-compose build`


