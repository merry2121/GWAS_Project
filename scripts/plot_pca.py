import matplotlib.pyplot as plt

# Read PCA results
with open("results/chr22_pca.eigenvec") as f:
    pca_data = [line.split() for line in f]

# Read ancestry information
population = {}

with open("data/integrated_call_samples_v3.20130502.ALL.panel") as f:
    next(f)

    for line in f:
        sample, pop, super_pop, gender = line.split()
        population[sample] = super_pop

# Store PC1, PC2, and ancestry
pc1 = []
pc2 = []
groups = []

for row in pca_data:
    sample = row[1]

    pc1.append(float(row[2]))
    pc2.append(float(row[3]))
    groups.append(population[sample])

# Colors for the five ancestry groups
colors = {
    "AFR": "red",
    "AMR": "blue",
    "EAS": "green",
    "EUR": "orange",
    "SAS": "purple"
}

# Create the PCA plot
plt.figure(figsize=(10, 8))

for group in colors:
    x = [pc1[i] for i in range(len(pc1)) if groups[i] == group]
    y = [pc2[i] for i in range(len(pc2)) if groups[i] == group]

    plt.scatter(
        x,
        y,
        label=group,
        color=colors[group],
        s=15,
        alpha=0.7
    )

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("1000 Genomes Chromosome 22 PCA")
plt.legend(title="Super Population")
plt.grid(alpha=0.3)

# Save the plot
plt.savefig("results/chr22_pca_PC1_PC2.png", dpi=300)

print("PCA plot saved successfully.")
