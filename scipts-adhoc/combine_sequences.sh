#!/bin/bash

#Paths
EXTRACTED_DIR="../data/toxins/extracted"
COMBINED_DIR="../data/toxins/combined"
mkdir -p "$COMBINED_DIR"

#Combine TcdA sequences
cat "$EXTRACTED_DIR"/*_TcdA.fasta > "$COMBINED_DIR/all_TcdA_sequences.fasta"

#Combine TcdB sequenes
cat "$EXTRACTED_DIR"/*_TcdB.fasta > "$COMBINED_DIR/all_TcdB_sequences.fasta"

echo "Combined all TcdA & TcdB sequences into $COMBINED_DIR." 
