"""
Simple Flask web site 
"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import session
from flask import jsonify # For AJAX transactions

import json
import logging
import argparse  # For the vocabulary list
import sys

# Our own modules
from letterbag import LetterBag
from vocab import Vocab
from jumble import jumbled

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.COOKIE_KEY  # Should allow using session variables

#
# One shared 'Vocab' object, read-only after initialization,
# shared by all threads and instances.  Otherwise we would have to
# store it in the browser and transmit it on each request/response cycle, 
# or else read it from the file on each request/responce cycle,
# neither of which would be suitable for responding keystroke by keystroke.
#

def get_command_line():
  """
  Returns a namespace of command-line argument values
  """
  parser = argparse.ArgumentParser(
    description="Vocabulary anagram through a web server")
  parser.add_argument("vocab", type=argparse.FileType('r'),
                      default="data/vocab.txt",
                      help="A file containing vocabulary words, one per line")
  args = parser.parse_args()
  return args

CMDLN = get_command_line()
WORDS = Vocab( CMDLN.vocab )

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
  flask.g.vocab = WORDS.as_list();
  flask.session["target_count"] = min( len(flask.g.vocab), CONFIG.SUCCESS_COUNT )
  flask.session["jumble"] = jumbled(flask.g.vocab, flask.session["target_count"])
  flask.session["matches"] = [ ]
  app.logger.debug("Session variables have been set")
  assert flask.session["matches"] == [ ]
  assert flask.session["target_count"] > 0
  app.logger.debug("At least one seems to be set correctly")
  return flask.render_template('vocab.html')

@app.route("/keep_going")
def keep_going():
  """
  After initial use of index, we keep the same scrambled
  word and try to get more matches
  """
  flask.g.vocab = WORDS.as_list();
  return flask.render_template('vocab.html')
  

@app.route("/success")
def success():
  return flask.render_template('success.html')

#######################
# Form handler.  
# CIS 322 (399se) note:
#   You'll need to change this to a
#   a JSON request handler
#######################

@app.route("/_check", methods = ["POST"])
def check():
  app.logger.debug("Entering check")
  assert flask.session["target_count"] > 0
  app.logger.debug("Fetched target_count")
  text = request.form["attempt"]
  jumble = flask.session["jumble"]
  app.logger.debug("Checking '{}' from '{}'".format(text, jumble))
  in_jumble = LetterBag(jumble).contains(text)
  matched = WORDS.has(text)
  app.logger.debug("Matched? {}".format(matched))
  matches = flask.session.get("matches", []) # Default to empty list
  if matched and in_jumble and not (text in matches):
    app.logger.debug("***Matched {}***".format(text))
    matches.append(text)
    flask.session["matches"] = matches
  elif text in matches:
    flask.flash("You already found {}".format(text))
  elif not matched:
    flask.flash("{} isn't in the list of words".format(text))
  elif not in_jumble:
    flask.flash('"{}" can\'t be made from the letters {}'.format(text,jumble))
  else:
    app.logger.debug("This case shouldn't happen!")
    assert False  # Raises AssertionError

  if len(matches) >= flask.session["target_count"]:
    app.logger.debug("Success")
    return flask.redirect(url_for("success"))
  else:
    app.logger.debug("Redirecting to 'keep going'")
    return flask.redirect(url_for("keep_going"))

###############
# AJAX request handlers 
#   These return JSON, rather than rendering pages. 
###############

@app.route("/_example")
def example():
  """
  Example ajax request handler
  """
  app.logger.debug("Got a JSON request");
  rslt = { "key": "value" }
  return jsonify(result=rslt)


#################
# Functions used within the templates
#################

@app.template_filter( 'filt' )
def format_filt( something ):
    """
    Example of a filter that can be used within
    the Jinja2 code
    """
    return "Not what you asked for"
  
###################
#   Error handlers
###################
@app.errorhandler(404)
def error_404(e):
  app.logger.warning("++ 404 error: {}".format(e))
  return render_template('404.html'), 404

@app.errorhandler(500)
def error_500(e):
   app.logger.warning("++ 500 error: {}".format(e))
   assert app.debug == False # Why did
   return render_template('500.html'), 500

@app.errorhandler(403)
def error_403(e):
  app.logger.warning("++ 403 error: {}".format(e))
  return render_template('403.html'), 403



#############

# Set up to run from cgi-bin script, from
# gunicorn, or stand-alone.
#

if __name__ == "__main__":
    # Standalone, with a dynamically generated
    # secret key.  Debugger is using PIN code now;
    # should be safe even when globally accessible from ix.
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service. 
    app.debug=False

