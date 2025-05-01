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
git clone https://github.com/your-username/cdiff-toxin-polymorphism.git
cd cdiff-toxin-polymorphism
