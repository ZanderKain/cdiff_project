import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==== Settings ====
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMBINED_DIR = os.path.join(PROJECT_DIR, "data", "toxins", "combined")
PLOTS_DIR = os.path.join(PROJECT_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

# ==== Function to Plot Density Curve ====

def plot_mutation_density(frequency_csv, output_prefix, toxin_name, trim_length):
    df = pd.read_csv(frequency_csv)

    # Sort and trim
    df = df.sort_values(by="Position")
    df = df[df["Position"] <= trim_length]

    plt.figure(figsize=(18, 6))
    sns.kdeplot(
        x=df["Position"],
        weights=df["Mutation_Frequency_%"],
        bw_adjust=0.5,  # Bandwidth adjustment; lower = sharper curve
        fill=True,
        color="purple",
        alpha=0.4
    )

    plt.title(f"Mutation Density Across {toxin_name} Toxin Gene", fontsize=18)
    plt.xlabel("Position in Aligned Gene", fontsize=14)
    plt.ylabel("Mutation Density (smoothed)", fontsize=14)

    # Add 0%, 25%, 50%, 75%, 100% ticks
    ticks = [0, trim_length * 0.25, trim_length * 0.5, trim_length * 0.75, trim_length]
    plt.xticks(ticks, [f"{int(x)}" for x in ticks])

    plt.grid(True, linestyle="--", alpha=0.6)

    output_file = os.path.join(PLOTS_DIR, f"{output_prefix}_mutation_density_curve.png")
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()

    print(f"Density plot saved: {output_file}")

# ==== Run for TcdA and TcdB ====

# TcdA
plot_mutation_density(
    frequency_csv=os.path.join(COMBINED_DIR, "TcdA_mutation_frequency.csv"),
    output_prefix="TcdA",
    toxin_name="TcdA",
    trim_length=8200
)

# TcdB
plot_mutation_density(
    frequency_csv=os.path.join(COMBINED_DIR, "TcdB_mutation_frequency.csv"),
    output_prefix="TcdB",
    toxin_name="TcdB",
    trim_length=7200
)
