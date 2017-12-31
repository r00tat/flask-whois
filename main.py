#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import subprocess

from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<string:domain>")
def whois(domain):
    whois_result = subprocess.run(["whois", domain], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return Response(whois_result.stdout, mimetype="text/plain; charset=utf-8")

if __name__ == '__main__':
    # Setup logging
    log_format = '%(asctime)s %(levelname)5s %(message)s'
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    logging.info("starting app")
    # Run app flask server
    app.run(
        host=os.environ.get('HOST', '0.0.0.0'),
        port=int(os.environ.get('PORT', 8080)),
        debug=True)
