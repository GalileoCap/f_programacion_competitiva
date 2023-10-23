#!/bin/bash

IFILES=($(ls sections/*.tex))

for ifile in "${IFILES[@]}"
do
  ofile=${ifile%.tex}_clean.tex
  echo "$ifile => $ofile"
  sed -e 's/\\pause//g' -e 's/\\item<[[:digit:]]\+-[[:digit:]]*>/\\item/g' $ifile > $ofile
done

sed -e 's/\.tex/_clean.tex/g' main.tex > main_clean.tex
