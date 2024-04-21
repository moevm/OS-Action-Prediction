#!/bin/bash
#enable debug
#set -x
# stop tracing: sudo pkill -f strace

log_path="./log"
log="$log_path/strace.txt"

childPID=`sudo ps -eo pid=`

echo "+++Start+++" > $log
echo $childPID >> $log
echo "+++End+++" >> $log

for pid in $childPID
do
    command=`sudo ps -p $pid -o command= | awk '{print $1}' | sed -e 's/\[\|\]\|\//_/g'`

    echo "$pid $command" >> $log
    echo "---" >> $log
    if [[ -n "$command" ]]
    then
        strace -ff -p $pid -o "$log_path/trace_log/$command" &
    fi
done