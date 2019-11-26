# Rudeboy-API

Categorizes toxicity levels in a sentence

[![Python flask](https://img.shields.io/badge/Python-flask-blue.svg)](https://http://flask.pocoo.org/)

![Docker Automated Build](https://img.shields.io/docker/automated/deven96/rudeboyapi.svg?style=flat)
![Docker Pulls](https://img.shields.io/docker/pulls/deven96/rudeboyapi.svg?style=flat)

[![Build Status](https://travis-ci.com/bisoncorps/Rudeboy-PredictionEngine.svg?branch=master)](https://travis-ci.com/bisoncorps/Rudeboy-PredictionEngine)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- [Rudeboy-API](#rudeboy-api)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [Running Locally](#running-locally)


## Getting Started

Clone the repo

```bash
    # SSH
    git clone git@github.com:bisoncorps/Rudeboy-PredictionEngine.git   
    # HTTPS
    git clone https://github.com/bisoncorps/Rudeboy-PredictionEngine.git
```

Activate virtual environment. All project work should be done in virtualenvs and virtualenv names must be added to gitignore

### Installation

- Install the requirements

```bash
    # install pipenv
    sudo pip3 install pipenv

    # install requirements
    pipenv install
```

## Running Locally

- With flask dev server

```bash
    python flask_api/server.py
```

- With Gunicorn (port 8008)

```bash
    gunicorn -b :8008 flask_api:app
```

- With deployed Docker image from docker hub

```bash
    docker run deven96/rudeboyapi
```

Upon running image, docker container port is bound to [localhost](http://localhost:8008)

