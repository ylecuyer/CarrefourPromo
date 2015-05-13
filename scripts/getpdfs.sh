#!/usr/bin/env bash

python getlinks.py > links.txt
aria2c -i links.txt
