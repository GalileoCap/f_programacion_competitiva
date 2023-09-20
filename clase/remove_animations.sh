#!/bin/bash

IFILE=main.tex
OFILE=main_clean.tex

sed -e 's/\\pause//g' -e 's/\\item<[[:digit:]]\+-[[:digit:]]*>/\\item/g' $IFILE > $OFILE
