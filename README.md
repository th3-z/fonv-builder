# fonv-builder

Source code for fonv-builder. Work in progress.


## Features 

* Fallout: New Vegas character planner

## Requirements

* Python3
* python3-flask
* python3-venv
* NodeJS

## Building

* `pip3 install -e .`
* `python setup.py bdist_wheel`
* `npm --prefix client/ run build`

## Install


* `python3 -m venv venv`
* `. venv/bin/activate`
* `pip3 install fonv_builder-VERSION-py3-none-any.whl`
* `mkdir -p venv/var/server-instance`
* `export FLASK_APP=server`
* `flask init-db`
* `waitress-serve --call 'server:create_app'`



2. `npm install client`
3. `npm install -g @vue/cli`
