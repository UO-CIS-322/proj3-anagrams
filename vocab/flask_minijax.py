"""
Tiny demo of Ajax interaction
"""

import flask
from flask import request  # Data from a submitted form
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging
import argparse  # For the vocabulary list
import sys

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.secret_key  # Should allow using session variables


###
# Pages
###

@app.route("/")
def index():
  return flask.render_template('minijax.html')

###############
# AJAX request handlers 
#   These return JSON to the JavaScript function on
#   an existing page, rather than rendering a new page. 
###############

@app.route("/_countem")
def countem():
  text = request.args.get("text", type=str)
  length = len(text)
  rslt = { "long_enough": length >= 5 }
  return jsonify(result=rslt)

#############

# Run locally
if __name__ == "__main__":
    # Standalone. 
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

# If we run 'python3 flask_minijax.py, we get the above 'main'.
# If we run 'gunicorn flask_minijax:app', we instead get a
# 'main' inside gunicorn, which loads this file as a module
# and accesses the Flask 'app' object.
# 
