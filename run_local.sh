#!/bin/bash

export FLASK_APP=server/app.py
export FLASK_ENV=development
export FLASK_DEBUG=false

if [ $# -eq 0 ]
    then
        echo "Root dir argument is required"
        exit 1
fi

export ROOT_DIR=$1

flask run