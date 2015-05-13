#!/usr/bin/env bash

pdftotext input_express.pdf output.txt
gawk '{ match($0, /([0-9]{13})/, arr); if(arr[1] != "") { getline; getline; print arr[1] ";" $0 } }' output.txt > formated.txt
python productinfos.py "crf_express"

pdftotext input_contact output.txt
gawk '{ match($0, /([0-9]{13})/, arr); if(arr[1] != "") { getline; getline; print arr[1] ";" $0 } }' output.txt > formated.txt
python productinfos.py "crf_contact"

pdftotext input_city output.txt
gawk '{ match($0, /([0-9]{13})/, arr); if(arr[1] != "") { getline; getline; print arr[1] ";" $0 } }' output.txt > formated.txt
python productinfos.py "crf_city"

pdftotext input_montagne output.txt
gawk '{ match($0, /([0-9]{13})/, arr); if(arr[1] != "") { getline; getline; print arr[1] ";" $0 } }' output.txt > formated.txt
python productinfos.py "crf_montagne"
