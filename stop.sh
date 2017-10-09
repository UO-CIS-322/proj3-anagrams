#! /bin/bash
#
# Stop the service started by start.sh
# It's process ID should be in ./SERVICE_PID
#
# See design notes in start.sh
# 
this=${BASH_SOURCE[0]}
here=`dirname ${this}`
pushd ${here}
pid=`cat SERVICE_PID`
numpat='^[0-9]+$'
if [[ ${pid} =~  ${numpat} ]]; then
    # That looks like a process ID ...
    echo "PS: "
    ps -x ${pid}
    echo "Killing process ${pid}"
    kill -9 ${pid}
    sleep 1 
    ps -x ${pid}
else
    echo "Didn't find expected value in ${here}/SERVICE_PID"
    echo "Found /${pid}/"
    echo "Didn't match /${numpat}/"
fi;
popd

