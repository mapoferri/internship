#!/bin/bash
for file in `ls ./volume/input/*_singleline.fasta` ;
do python ./predgpi-master/gp.py "$file" > "${file%.fasta}_stdout";
done
