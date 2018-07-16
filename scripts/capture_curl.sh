#!/bin/bash

inputfile=$1

for uri in `cat $inputfile`; do
    echo "STARTING CURL FOR ${uri}"
    curl -v "${uri}"
done
