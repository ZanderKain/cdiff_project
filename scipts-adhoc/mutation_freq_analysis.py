from Bio import AlignIO
import pandas as pd
import os

def analyze_mutations(alignment_file, output_file, toxin_name):
    alignment = AlignIO.read(alignment_file, "fasta")
    strains = [record.id for record in alignment]

    # Explicitly select NZ_CP076401.1 as reference
    reference_id = "NZ_CP076401.1"
    ref_seq = None

    for record in alignment:
        if reference_id in record.id:
            ref_seq = record
            break

    if ref_seq is None:
        raise Exception(f"Reference {reference_id} not found in alignment!")

    print(f"Using {reference_id} as reference for {toxin_name}.")

    results = []

    for pos in range(len(ref_seq.seq)):
        ref_base = ref_seq.seq[pos]

        # Skip positions where reference base is a gap
        if ref_base == "-":
            continue

        mutations = []
        mutation_types = []

        for record in alignment[1:]:  # Skip reference
            strain_base = record.seq[pos]
            if strain_base != ref_base and strain_base != "-":
                mutations.append(strain_base)

        if mutations:
            mutation_freq = len(mutations) / (len(alignment) - 1) * 100  # percentage excluding reference
            mutation_types_unique = ";".join(sorted(set(mutations)))
        else:
            mutation_freq = 0.0
            mutation_types_unique = "-"

        results.append({
            "Position": pos + 1,
            "Reference_Base": ref_base,
            "Mutation_Frequency_%": round(mutation_freq, 2),
            "Mutations_Observed": mutation_types_unique
        })

    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

    print(f"Mutation frequency analysis complete for {toxin_name}: {output_file}")

# ==== Settings ====
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMBINED_DIR = os.path.join(PROJECT_DIR, "data", "toxins", "combined")

# Run for TcdA
analyze_mutations(
    alignment_file=os.path.join(COMBINED_DIR, "all_TcdA_aligned.fasta"),
    output_file=os.path.join(COMBINED_DIR, "TcdA_mutation_frequency.csv"),
    toxin_name="TcdA"
)

# Run for TcdB
analyze_mutations(
    alignment_file=os.path.join(COMBINED_DIR, "all_TcdB_aligned.fasta"),
    output_file=os.path.join(COMBINED_DIR, "TcdB_mutation_frequency.csv"),
    toxin_name="TcdB"
)
