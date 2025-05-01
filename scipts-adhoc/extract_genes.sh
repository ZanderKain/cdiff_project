#!/bin/bash

TcdA_ref="ref_TcdA.fasta"
TcdB_ref="ref_TcdB.fasta"

for genome in data/genomes/**/*.fna; do
	basename=$(basename "$genome".fna)

	makeblastdb -in "$genome" -dbtype nucl

	blastn -query $TcdA_ref -db "$genome" -outfmt 6 -max_target_seqs 1 -out tmp_tcdA.txt
	blastn -query $TcdB_ref -db "$genome" -outfmt 6 -max_target_seqs 1 -out tmp_tcdB.txt

	#Extract sequences using BLAST coordinates
	awk 'BEGIN{FS="\t"} { print $2, $9, $10}' tmp_tcdA.txt > tcdA_coords.txt
	awk 'BEGIN{FS="\t"} { print $2, $9, $10}' tmp_tcdB.txt > tcdB_coords.txt

done

