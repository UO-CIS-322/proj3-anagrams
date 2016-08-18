#
# Project 3:  Vocabulary game with AJAX interaction
#
# Gnu make and bash are required. 
#
# To run from source: 
#    bash ./configure
#    make run 
# 
#  'make configure' may also work, but with error
#   messages.

Makefile.local: 
	bash ./configure

include Makefile.local  ## Where customizations go 

##
##  Virtual environment
##     
env:
	$(PYVENV)  env
	(.  env/bin/activate; pip install -r requirements.txt)


##
## Preserve virtual environment
##
dist:
	pip freeze >requirements.txt

# 'make run' runs Flask's built-in test server, 
#  with debugging turned on unless it is unset in CONFIG.py
# 
run:	env
	( . env/bin/activate; python3 flask_vocab.py ) || true

# 'make service' runs as a background job under the gunicorn 
#  WSGI server. FIXME:  A real production service would use 
#  NGINX in combination with gunicorn to prevent DOS attacks. 
#
#  For now we are running gunicorn on its default port of 8000. 
#  FIXME: Configuration builder could put the desired port number
#  into Makefile.local. 
# 
service:	env
	echo "Launching green unicorn in background"
	( . env/bin/activate; gunicorn --bind="0.0.0.0:8000" flask_vocab:app &) 


# 'clean' and 'veryclean' are typically used before checking 
# things into git.  'clean' should leave the project ready to 
# run, while 'veryclean' may leave project in a state that 
# requires re-running installation and configuration steps
# 
clean:
	rm -f *.pyc
	rm -rf __pycache__

veryclean:
	make clean
	rm -f CONFIG.py
	rm -rf env
	rm -f Makefile.local



