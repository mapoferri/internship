#!/bin/bash

ls /home/predgpi_app/
#ls ./predgpi_app/input/

./rotation.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to split fasta file, so can't start the application Bacello: $status"
        exit $status
fi

mkdir ./volume/input/
for file in `ls /home/predgpi_app/*.fasta`; do mv $file ./volume/input/ ; ls ./volume/input/;  done

./elimination.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to eliminate multi-fasta file, so can't start the application Bacello: $status"
        exit $status
fi

./check_lenght.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to lining up the fasta files, so can't start the application Bacello: $status"
fi

./singleline.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to lining up the fasta files, so can't start the application Bacello: $status"

#Starting first the application (first process)
./application.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to start the application PredGPI: $status"
        exit $status
fi

#Starting the second process, only if the first has been working good, this one would find output files
mkdir ./volume/output/

./move.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to find any output file from the app PredGPI: $status"
        exit $status
fi

