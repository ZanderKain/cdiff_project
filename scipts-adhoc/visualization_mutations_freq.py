import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==== Settings ====
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMBINED_DIR = os.path.join(PROJECT_DIR, "data", "toxins", "combined")
PLOTS_DIR = os.path.join(PROJECT_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

# ==== Plotting Function with Trimming and Quarter Ticks ====

def plot_mutation_frequency_trimmed(frequency_csv, output_prefix, toxin_name, trim_length):
    df = pd.read_csv(frequency_csv)

    # Sort positions
    df = df.sort_values(by="Position")

    # Trim to biologically relevant length
    df = df[df["Position"] <= trim_length]

    plt.figure(figsize=(18, 6))
    sns.barplot(x="Position", y="Mutation_Frequency_%", data=df, palette="viridis")

    plt.title(f"Mutation Frequency Across {toxin_name} (Trimmed)", fontsize=18)
    plt.xlabel("Position in Aligned Gene", fontsize=14)
    plt.ylabel("Mutation Frequency (%)", fontsize=14)

    # Add ticks at 0%, 25%, 50%, 75%, 100%
    ticks = [0, trim_length * 0.25, trim_length * 0.5, trim_length * 0.75, trim_length]
    plt.xticks(ticks, [f"{int(x)}" for x in ticks], fontsize=12)

    plt.grid(True, axis="y", linestyle="--", alpha=0.6)

    output_file = os.path.join(PLOTS_DIR, f"{output_prefix}_mutation_frequency_barplot_trimmed.png")
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()

    print(f"Trimmed plot saved: {output_file}")

# ==== Run for TcdA and TcdB ====

# TcdA (~8,200 bp)
plot_mutation_frequency_trimmed(
    frequency_csv=os.path.join(COMBINED_DIR, "TcdA_mutation_frequency.csv"),
    output_prefix="TcdA",
    toxin_name="TcdA",
    trim_length=8200
)

# TcdB (~7,200 bp)
plot_mutation_frequency_trimmed(
    frequency_csv=os.path.join(COMBINED_DIR, "TcdB_mutation_frequency.csv"),
    output_prefix="TcdB",
    toxin_name="TcdB",
    trim_length=7200
)
