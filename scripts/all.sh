#!/usr/bin/env bash

rm -rf output
mkdir -p output/img/products
mkdir -p output/partials

cp nopicture.jpg output/img/products

./getpdfs.sh

./update.sh

rm input_*.pdf
rm links.txt
