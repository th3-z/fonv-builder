# fonv-builder

Source code for fonv-builder. Work in progress.

## Features 

* Fallout: New Vegas character planner


## Building

### Build requirements

* Python3
* python3-flask
* python3-venv
* NodeJS

### Instructions

* `pip3 install -e .`
* `python setup.py bdist_wheel`
* `npm install client`
* `npm install -g @vue/cli`
* `npm --prefix client/ run build`

## Installation

### Requirements

* Python3
* python3-flask
* python3-venv

### Instructions

Copy the distribution to your web server path, install the `.whl` and serve the backend with waitress. A Nginx example is provided in `example.nginx.conf`.

* `python3 -m venv venv`
* `. venv/bin/activate`
* `pip3 install fonv_builder-VERSION-py3-none-any.whl`
* `mkdir -p venv/var/server-instance`
* `export FLASK_APP=server`
* `flask init-db`
* `waitress-serve --call 'server:create_app'`
