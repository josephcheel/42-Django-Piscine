#!/bin/bash
PYTHON_EXE=python3
LOCAL_LIB=local_lib
URL_LIB=https://github.com/jaraco/path.git
MY_PROGRAM=my_program.py
LOG_FILE=install.log

echo "---------Pip Version---------"
$PYTHON_EXE -m pip -V
if [ -d $LOCAL_LIB ]; then
	rm -rf $LOCAL_LIB
fi
echo "---------Downloading $URL_LIB in $LOCAL_LIB---------"
git clone $URL_LIB $LOCAL_LIB
echo "---------Installing $URL_LIB in $LOCAL_LIB---------"
$PYTHON_EXE -m pip install -e $LOCAL_LIB --log $LOG_FILE 
if $PYTHON_EXE -m pip show path ; then
	echo "path is installed"
	echo "---------Running $MY_PROGRAM---------"
	$PYTHON_EXE $MY_PROGRAM
else
	echo "path is not installed"
fi