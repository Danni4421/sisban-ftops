#!/bin/bash

sleep 10
flask db migrate
flask db upgrade 
flask run

tail -f /dev/null