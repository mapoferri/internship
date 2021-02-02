echo `ls ./*.fasta`
#mkdir ./volume/output/
for file in `ls -1 ./volume/input_fasta/*_singleline.fasta` ; do psiblast -query $file -db ./database/*.fasta -evalue 0.01 -num_iterations 2 -out_ascii_pssm "${file%_singleline.fasta}.pssm" -num_alignments 50 -out "${file%.fasta}.alns.blast" ; done                
