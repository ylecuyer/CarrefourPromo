#!/usr/bin/env bash

rm -rf output
mkdir output
mkdir output/img
cp nopicture.jpg output/img/

./getpdfs.sh

./update.sh

rm input_*.pdf
rm links.txt
