from Bio import AlignIO
import pandas as pd
import os

#Settings
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ALIGNMENT_DIR = os.path.join(PROJECT_DIR, 'data', 'toxins')

#Choose the alignment file
alignment_file = os.path.join(ALIGNMENT_DIR, 'all_TcdA_aligned.fasta')
output_file = os.path.join(ALIGNMENT_DIR, 'TcdA_polymorphisms.csv')

#Load the alignment
alignment = AlignIO.read(alignment_file, 'fasta')
reference = alignment[0] #Using first sequence as reference

#detect polymorphisms
polymorphisms = []

for i in range(alignment.get_alignment_length()):
    bases = [record.seq[i] for record in alignment]
    ref_base = bases[0]
    unique_bases = set(bases)
    
    if len(unique_bases) > 1: #variantion detected
        var_info = {
            'position': i + 1,
            'reference_base': ref_base,
            'Variants': ';'.join(sorted(unique_bases)),
            'Strain_carrying_variant': []
        }
        
        strain_variants = []
        for record in alignment:
            if record.seq[i] != ref_base:
                strain_variants.append(f"{record.id}:{record.seq[i]}")
                
        var_info['Strain_carrying_variant'] = ';'.join(strain_variants)
        
        polymorphisms.append(var_info)
        
#Create a DataFrame and save to CSV
polymorphisms_df = pd.DataFrame(polymorphisms)
polymorphisms_df.to_csv(output_file, index=False)
print(f"Polymorphisms detected and saved to {output_file}") 