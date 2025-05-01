import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==== Settings ====
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMBINED_DIR = os.path.join(PROJECT_DIR, "data", "toxins", "combined")
PLOTS_DIR = os.path.join(PROJECT_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

# ==== Load Data ====
tcdA_df = pd.read_csv(os.path.join(COMBINED_DIR, "TcdA_mutation_frequency.csv"))
tcdB_df = pd.read_csv(os.path.join(COMBINED_DIR, "TcdB_mutation_frequency.csv"))

# Trim to biological length
tcdA_df = tcdA_df[tcdA_df["Position"] <= 8200]
tcdB_df = tcdB_df[tcdB_df["Position"] <= 7200]

# ==== Determine common Y-axis range ====

# Temporary individual plots to find max density values
tcdA_density = sns.kdeplot(x=tcdA_df["Position"], weights=tcdA_df["Mutation_Frequency_%"], bw_adjust=0.5).get_lines()[0].get_data()
plt.close()
tcdB_density = sns.kdeplot(x=tcdB_df["Position"], weights=tcdB_df["Mutation_Frequency_%"], bw_adjust=0.5).get_lines()[0].get_data()
plt.close()

# Get the maximum density value across both
ymax = max(tcdA_density[1].max(), tcdB_density[1].max()) * 1.1  # Add 10% padding

# ==== Plot Dual Panel with Shared Y-Axis ====

fig, axes = plt.subplots(1, 2, figsize=(20, 6), sharey=True)

# TcdA
sns.kdeplot(
    x=tcdA_df["Position"],
    weights=tcdA_df["Mutation_Frequency_%"],
    bw_adjust=0.5,
    fill=True,
    color="purple",
    alpha=0.4,
    ax=axes[0]
)
axes[0].set_title("TcdA Mutation Density", fontsize=16)
axes[0].set_xlabel("Position in Aligned Gene", fontsize=14)
axes[0].set_ylabel("Mutation Density", fontsize=14)
axes[0].set_xlim(0, 8200)
axes[0].set_ylim(0, ymax)
axes[0].set_xticks([0, 2050, 4100, 6150, 8200])

# TcdB
sns.kdeplot(
    x=tcdB_df["Position"],
    weights=tcdB_df["Mutation_Frequency_%"],
    bw_adjust=0.5,
    fill=True,
    color="teal",
    alpha=0.4,
    ax=axes[1]
)
axes[1].set_title("TcdB Mutation Density", fontsize=16)
axes[1].set_xlabel("Position in Aligned Gene", fontsize=14)
axes[1].set_xlim(0, 7200)
axes[1].set_ylim(0, ymax)
axes[1].set_xticks([0, 1800, 3600, 5400, 7200])

plt.tight_layout()

output_file = os.path.join(PLOTS_DIR, "TcdA_TcdB_mutation_density_dualplot_sharedy.png")
plt.savefig(output_file, dpi=300)
plt.close()

print(f"✅ Shared Y-axis dual density plot saved: {output_file}")
