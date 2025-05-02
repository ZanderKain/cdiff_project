#!/bin/bash

#Set the directory where the 212 genomes are located
GENOME_DIR="../data/genomes/cdiff_complete/ncbi_dataset/data"
TOXIN_DIR="../data/toxins/extracted"

#Relative path to reference toxin FASTA files
TcdA_REF="../data/toxins/tcdA_fastaseq_ref.txt"
TcdB_REF="../data/toxins/tcdB_fastaseq_ref.txt"

#Loop over all .fna files inside all subfolders
find "$GENOME_DIR" -type f -name "*.fna" | while read genome; do
	strain=$(basename "$genome" .fna)
	
	echo "Processing $strain"

	#Create BLAST database
	makeblastdb -in "$genome" -dbtype nucl

	#BLAST TcdA
	blastn -query "$TcdA_REF" -db "$genome" -outfmt 6 -max_target_seqs 1 -out tmp_TcdA.txt
	if [[ -s tmp_TcdA.txt ]]; then
		awk '{print $2"\t"$9"\t"$10}' tmp_TcdA.txt | \
		awk '{if($2<$3) print $1"\t"$2-1"\t"$3; else print $1"\t"$3-1"\t"$2}' > tmp_TcdA.bed

		bedtools getfasta -fi "$genome" -bed tmp_TcdA.bed -fo "$TOXIN_DIR/${strain}_TcdA.fasta"
	fi

	#BLAST TcdB
	blastn -query "$TcdB_REF" -db "$genome" -outfmt 6 -max_target_seqs 1 -out tmp_TcdB.txt
	if [[ -s tmp_TcdB.txt ]]; then
		awk '{print $2"\t"$9"\t"$10}' tmp_TcdB.txt | \
		awk '{if($2<$3) print $1"\t"$2-1"\t"$3; else print $1"\t"$3-1"\t"$2}' > tmp_TcdB.bed

		bedtools getfasta -fi "$genome" -bed tmp_TcdB.bed -fo "$TOXIN_DIR/${strain}_TcdB.fasta"
	fi

#Clean up
	rm -f tmp_TcdA.txt tmp_TcdB.txt tmp_TcdA.bed tmp_TcdB.bed
done

echo "Extraction complete. All TcdA and TcdB sequences saved to $TOXIN_DIR"
