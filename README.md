[![CI](https://github.com/JeffLabonte/ideal-octo-telegram/actions/workflows/ci.yml/badge.svg)](https://github.com/JeffLabonte/ideal-octo-telegram/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JeffLabonte/ideal-octo-telegram/branch/main/graph/badge.svg?token=Utdpt898bV)](https://codecov.io/gh/JeffLabonte/ideal-octo-telegram)

# ideal-octo-telegram

API to control your devices on your network and make all your automation scripts available at one place


## Requirements:

* Docker
* Docker-Compose
    * (Version >= 1.28)[https://github.com/docker/compose]
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

## Deployment with Ansible:

If you are here, I consider that you have `docker` and `docker-compose` installed on your server

You need to copy the hosts.yml.example. You can do that my running
the following command:

```bash
make copy_new_config
```

The hosts.yml can take that form:

```yml
webservers:
    hosts:
        server_a:
            ansible_connection: ssh
            ansible_host: "<the IP address or hostname>"
            ansible_user: "<User to use>"
            ansible_password: "<User's password>"
            ansible_become_password: "<sudo password>"
```

***Note: You can use `ansible-vault` to encrypt your `hosts.yml`***
Run the playbook:

```bash
# If deploy/hosts.yml is encrypted with ansible-vault
ansible-playbook -i deploy/hosts.yml deploy/deploy_code.yml --ask-pass

# If deploy/hosts.yml is not encrypted with ansible-vault
ansible-playbook -i deploy/hosts.yml deploy/deploy_code.yml -e "DATABASE_USERNAME=a_database_username" -e "DATABASE_PASSWORD=a_long_password" -e
"DATABASE_NAME=ideal-octo-telegram"
```

