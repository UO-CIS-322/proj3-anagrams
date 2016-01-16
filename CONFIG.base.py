"""
Configuration of flask application.
Everything that could be different between running
on your development platform or on ix.cs.uoregon.edu
(or on a different deployment target) shoudl be here.
"""
DEBUG = True
PORT = 5000 # Replace with a randomly chosen port 
SUCCESS_COUNT = 2  # How many matches do we require? 
#   Obtain a cookie key with 
#   import uuid
#   str(uuid.uuid4())
# We do it just once so that multiple processes
# will share the same key.
# Should look like COOKIE_KEY = 'xxxxxxxxxx-xxxx-xxxx'
COOKIE_KEY = '0166c5c7-c4fc-4b20-9bcb-219733271fde' # Replace with a new key

