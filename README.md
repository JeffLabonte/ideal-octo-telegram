[![CI](https://github.com/JeffLabonte/ideal-octo-telegram/actions/workflows/ci.yml/badge.svg)](https://github.com/JeffLabonte/ideal-octo-telegram/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JeffLabonte/ideal-octo-telegram/branch/main/graph/badge.svg?token=Utdpt898bV)](https://codecov.io/gh/JeffLabonte/ideal-octo-telegram)

# ideal-octo-telegram

API to control your devices on your network and make all your automation scripts available at one place

## Requirements:

- Docker
- Docker-Compose
  - [Version >= 1.28](https://github.com/docker/compose)
    - `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose`
- Ansible:
  - To Deploy on your own servers
- Python 3.9
- Postgresql
- [Poetry](https://python-poetry.org/docs/#installation)

## Getting Started:

- Install some postgresql dependencies to compile the code:
  - On Linux:
    - Ubuntu/Debian: `sudo apt install libpq-devel python3-dev`
    - Fedora 34: `sudo dnf install libpq-devel python-devel`
  - On macOS:
    - `brew install postgresql`
- Before running `make install`

## Stuff to Know:

- You can register a user on `/api/auth/registration`
- Prod build run on port`80`
- You can build images by running `docker-compose build`

## How to run API Docs locally:

This project uses [django-spectacular](https://github.com/tfranzel/drf-spectacular) to generate its doc.

You can generate the API docs by running the following command:

```bash
make generate_docs
```

then you need to run a server to host this doc, I am using the container proposed in the [django-spectacular](https://github.com/tfranzel/drf-spectacular) documentation.

You can run the local server by running this command:

```bash
make run_docs
```

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

**_Note: You can use `ansible-vault` to encrypt your `hosts.yml`_**
Run the playbook:

```bash
# If deploy/hosts.yml is encrypted with ansible-vault
ansible-playbook -i deploy/hosts.yml deploy/deploy_code.yml --ask-vault-pass

# If deploy/hosts.yml is not encrypted with ansible-vault
ansible-playbook -i deploy/hosts.yml deploy/deploy_code.yml -e "DATABASE_USER=a_database_username" -e "DATABASE_PASSWORD=a_long_password" -e
"DATABASE_NAME=ideal-octo-telegram"
```
