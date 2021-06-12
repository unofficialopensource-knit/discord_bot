#!/bin/bash


gunicorn --config "python:config.wsgi"
