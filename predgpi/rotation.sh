#!/bin/bash
#mv ./volume/input_fasta/*.pssm ./volume/output
for file in  `ls ./volume/*.fasta`; do ./separator.py $file; ls ; done 
