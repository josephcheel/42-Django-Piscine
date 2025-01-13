#!/bin/sh

if [ ! -z $1 ]; then
	curl -sSI $1 | grep location | cut -d ":" -f 2-
else
	echo "usage: ./myawesomescript.sh [ex: https://www.42barcelona.com/]"
fi
