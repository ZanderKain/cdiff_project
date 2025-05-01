from Bio import SeqIO
import os
import re

# ==== Settings ====
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXTRACTED_DIR = os.path.join(PROJECT_DIR, "data", "toxins", "extracted")
COMBINED_DIR = os.path.join(PROJECT_DIR, "data", "toxins", "combined")
os.makedirs(COMBINED_DIR, exist_ok=True)

# ==== Prepare Strain Grouping ====
tcdA_sequences = {}
tcdB_sequences = {}

# Scan all extracted FASTA files
for fasta_file in os.listdir(EXTRACTED_DIR):
    if fasta_file.endswith(".fasta"):
        filepath = os.path.join(EXTRACTED_DIR, fasta_file)
        for record in SeqIO.parse(filepath, "fasta"):
            header = record.id
            # Try to capture the GCF or GCA from filename
            match = re.match(r"(GCF|GCA)_\d+\.\d+", fasta_file)
            if match:
                strain_id = match.group(0)
            else:
                strain_id = header.split("_")[0]  # fallback
            
            if "_TcdA" in fasta_file:
                # Keep longest TcdA per strain
                if strain_id not in tcdA_sequences or len(record.seq) > len(tcdA_sequences[strain_id].seq):
                    tcdA_sequences[strain_id] = record
            elif "_TcdB" in fasta_file:
                # Keep longest TcdB per strain
                if strain_id not in tcdB_sequences or len(record.seq) > len(tcdB_sequences[strain_id].seq):
                    tcdB_sequences[strain_id] = record

# ==== Save Clean Combined FASTA Files ====

SeqIO.write(tcdA_sequences.values(), os.path.join(COMBINED_DIR, "all_TcdA_sequences_clean.fasta"), "fasta")
SeqIO.write(tcdB_sequences.values(), os.path.join(COMBINED_DIR, "all_TcdB_sequences_clean.fasta"), "fasta")

print(f"Clean combined TcdA and TcdB FASTA files created in {COMBINED_DIR}")
