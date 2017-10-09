#! /bin/bash
#
# Usage:  ./start.sh [port]
#  
# Start the service as a background process, saving
# the process number (of the lead process) in SERVICE_PID.
#
#

PORTNUM=$1
if [[ "${PORTNUM}" == "" ]]; then
    PORTNUM="8000"
fi;

echo "***Will listen on port ${PORTNUM}***"

this=${BASH_SOURCE[0]}
here=`dirname ${this}`
activate="${here}/env/bin/activate"
echo "Activating ${activate}"
source ${activate}
echo "Activated"

pushd vocab
python3 flask_vocab.py -P ${PORTNUM} &
pid=$! 
popd
echo "${pid}" >SERVICE_PID
echo "***"
echo "Flask server started"
echo "PID ${pid} listening on port ${PORTNUM}"
echo "SERVICE_PID: " `cat SERVICE_PID`
echo "***"

#
#
# Design notes:
# This is a shell script outside the Makefile so that we
# can make sure it is run by bash, with one shell process
# running the whole script.  Make uses a separate shell
# process for each line of a recipe, making it difficult to
# capture the process ID.  Also Make can use a different
# shell, and may act differently between Windows and Unix.
#
# see also: stop.sh

