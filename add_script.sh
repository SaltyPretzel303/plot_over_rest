#!/bin/bash

x="10"
y="20"

if [ "$#" -eq "2" ]
then
	echo "Arguments provided: x->$1 y->$2"

	x="$1"
	y="$2"
fi

curl --request POST \
 --data '{"x":'"$x"', "y":'"$y"'}' \
 --header 'Content-Type: application/json' \
 localhost:8000/add