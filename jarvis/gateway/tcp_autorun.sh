#!/bin/bash

echo "check Process [tcp.py]"

PL=`ps -ef | grep TCP.py` 


if [[ "$PL" == *"python"* ]];then
	echo "already tcp process activated"
else
	echo "tcp process activate"
	echo `python /usr/local/mysql/bin/TCP.py`
fi
