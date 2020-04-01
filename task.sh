#!/bin/bash
unset TMOUT
cd `dirname $0`;
python logCollecter.py -m time -v 00:30:00 --auto;
if [ $? -ne 0 ]; then
    echo "Error! exit task"
    exit 1
fi
python logCutter.py
if [ $? -ne 0 ]; then
    echo "Error! exit task"
    exit 1
fi
exit 0;