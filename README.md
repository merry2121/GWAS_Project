# 1000 Genomes PCA Analysis

## Overview

This project uses chromosome 1 data from the 1000 Genomes Project to perform quality control, variant filtering, LD pruning, Principal Component Analysis (PCA), and population visualization.

## Dataset

The data comes from the 1000 Genomes Project Phase 3 dataset.

- 2504 individuals
- Chromosome 1 genotype data
- Population and super-population information
- Reference genome: GRCh37 / hg19
- Strict accessibility mask

## Analysis Steps

1. Downloaded chromosome 1 VCF data from the 1000 Genomes Project.
2. Normalized variants and removed duplicate variants using BCFtools.
3. Converted the processed data to PLINK binary format.
4. Applied the 1000 Genomes strict mask to keep variants in callable regions.
5. Applied MAF filtering.
6. Performed LD pruning to reduce highly correlated SNPs.
7. Used the remaining SNPs to perform PCA with PLINK.
8. Calculated the variance explained by the principal components.
9. Added population and super-population information to the PCA results.
10. Created a PC1 vs PC2 population plot using Python.

## Results

After applying the strict mask:

- 739,129 variants remained.
- 2,504 individuals were retained.

After LD pruning:

- Approximately 71,000 independent SNPs were used for PCA.

The first principal components explained:

- PC1: 53.49%
- PC2: 20.99%
- PC3: 9.04%
- PC4: 6.75%
- PC5: 3.06%

The PCA shows clear genetic structure among the major 1000 Genomes super-populations.

## Tools

- Linux / WSL
- BCFtools
- PLINK 1.9
- Python
- Matplotlib
- Git / GitHub

## Project Structure

GWAS_Project/
├── data/
├── reference/
├── results/
├── scripts/
│   └── plot_pca.py
├── .gitignore
└── README.md

Large genomic data files and intermediate files are excluded from Git using .gitignore.
