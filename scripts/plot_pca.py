import matplotlib.pyplot as plt

with open("../results/chr1_pca_with_pop.txt") as f:
    data = [line.split() for line in f]

colors = {
    "AFR": "red",
    "AMR": "blue",
    "EAS": "green",
    "EUR": "orange",
    "SAS": "purple"
}

plt.figure(figsize=(10, 8))

for pop, color in colors.items():
    x = []
    y = []

    for row in data:
        if row[13] == pop:
            x.append(float(row[2]))
            y.append(float(row[3]))

    plt.scatter(x, y, label=pop, color=color, s=15)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of 1000 Genomes Chromosome 1")
plt.legend()
plt.grid(True)

plt.savefig("../results/chr1_pca_PC1_PC2.png", dpi=300)
print("PCA plot saved successfully.")
