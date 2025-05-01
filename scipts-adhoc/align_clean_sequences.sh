#!/bin/bash

# Project root
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."

COMBINED_DIR="$PROJECT_DIR/data/toxins/combined"

# Align TcdA
mafft --auto "$COMBINED_DIR/all_TcdA_sequences_clean.fasta" > "$COMBINED_DIR/all_TcdA_aligned.fasta"

# Align TcdB
mafft --auto "$COMBINED_DIR/all_TcdB_sequences_clean.fasta" > "$COMBINED_DIR/all_TcdB_aligned.fasta"

echo "Alignment completed: TcdA and TcdB aligned separately."
