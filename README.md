# C. difficile Toxin Gene Polymorphism Analysis

This project analyzes mutation patterns in the TcdA and TcdB toxin genes of *Clostridioides difficile* using publicly available whole genome sequences. The goal is to identify polymorphism hotspots, understand conservation patterns, and compare evolutionary pressures acting on the two toxin genes.

## Project Structure

cdiff_project/ ├── data/ │ ├── TcdA_mutation_frequency.csv │ ├── TcdB_mutation_frequency.csv │ └── aligned_sequences/ ├── plots/ │ ├── TcdA_mutation_frequency_barplot.png │ ├── TcdB_mutation_density_curve.png │ └── TcdA_TcdB_mutation_density_dualplot.png ├── scripts/ │ ├── extract_genes.sh │ ├── align_clean_sequences.sh │ ├── mutation_freq_analysis.py │ └── mutation_density_curve.py └── README.md


## Key Findings

- **TcdA** shows a broad mid-gene polymorphism peak.
- **TcdB** displays multiple sharp polymorphism clusters across its gene.
- **Conserved N-terminal regions** suggest essential functional domains.
- **Top mutations** show high prevalence (>66%) across strains.

## Tools & Dependencies

This project used the following tools:

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12.3 | Scripting and data analysis |
| Biopython | 1.83 | FASTA parsing and alignment reading |
| Pandas | 2.1.4 | Mutation matrix and dataframes |
| MAFFT | v7.505 | Multiple sequence alignment |
| Seaborn / Matplotlib | 0.13 / 3.6.3 | Plotting visualizations |
| Datasets | v18.0.2 | Genome downloading and organization |
| Bash | — | Automation and file handling |

## How to Run the Analysis

1. Clone this repository:

```bash
git clone https://github.com/ZanderKain/cdiff_project.git
cd cdiff_project
```

2. Activate your environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Extract TcdA and TcdB gene from the 212 GCF fasta files given the reference genome's coords for both toxin genes
```bash
bash scipts-adhoc/extract_tcdA_tcdB.sh
```

4. Combines all fasta sequences generated from the previous step to be in one master fasta file for each toxin (A & B):
```bash
bash scipts-adhoc/combine_sequences.sh
```

5. Run python script to then clean the extracted fasta sequences to remove duplicates and leaving only the longest/most likely toxin sequence for each asseccion ID:
```bash
python scipts-adhoc/clean_extracted_toxins.py
```

6. Run alignment (if starting from raw sequences):
```bash
bash scipts-adhoc/align_clean_sequences.sh
```

7. Run detect polymorphism script:
```bash
bash scipts-adhoc/detect_polymorphisms.py
```

8. Run mutation frequency analysis: *CHECK ON THIS LATER*
```bash
bash scipts-adhoc/mutation_freq_analysis.py
```

9. Can run visualization scripts:
```bash
python scipts-adhoc/mutation_density_curve.py
python scipts-adhoc/visualization_mutations_freq.py
python scipts-adhoc/dual_mutation_dense_plot.py