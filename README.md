# GWAS Analysis Project

**Author:** Meron Kidane
**GitHub:** merry2121

## Overview

This project performs genotype quality control and population-structure analysis using genotype data from the **1000 Genomes Project Phase 3**.

The analysis was performed using **WSL Ubuntu, bcftools, PLINK 1.9, Python, and Matplotlib**.

Two chromosomes were analyzed:

* **Chromosome 1** — initial analysis and PCA
* **Chromosome 22** — dedicated analysis requested for the project

## Analysis Pipeline

The general workflow was:

1. Obtain chromosome-specific VCF genotype data
2. Validate and normalize variants using `bcftools`
3. Convert genotype data to PLINK binary format
4. Apply strict-region masking
5. Keep SNP variants
6. Calculate allele frequencies
7. Apply Minor Allele Frequency (MAF) filtering
8. Perform Linkage Disequilibrium (LD) pruning
9. Perform Principal Component Analysis (PCA)
10. Visualize the PCA results

## Project Structure

```text
GWAS_Project/
│
├── chromosome_1/
│   ├── README.md
│   └── results/
│
├── chromosome_22/
│   ├── README.md
│   └── results/
│
├── scripts/
├── data/
├── reference/
└── README.md
```

## Chromosome 1

The chromosome 1 analysis includes genotype quality control, missingness analysis, LD pruning, and PCA.

See the complete chromosome 1 results here:

**[Chromosome 1 Analysis](chromosome_1/)**

## Chromosome 22

The chromosome 22 analysis follows the same general GWAS preprocessing workflow and was performed using chromosome 22 genotype data.

Key results:

* 2,504 individuals
* 1,104,364 initial variants
* 749,426 variants after strict-mask filtering
* 726,054 SNP variants
* 45,608 variants after MAF ≥ 0.1 filtering
* 3,444 variants retained after LD pruning
* PCA performed using the 3,444 LD-pruned variants

The first two principal components explained approximately **78.05%** of the variation captured by the first 10 principal components.

See the complete chromosome 22 analysis here:

**[Chromosome 22 Analysis](chromosome_22/)**

## Software and Tools

* **bcftools 1.19** — VCF/BCF processing and variant normalization
* **PLINK 1.9** — genotype quality control, filtering, LD pruning, and PCA
* **Python 3** — data processing and visualization
* **Matplotlib** — PCA visualization
* **WSL Ubuntu** — Linux environment on Windows

## Data

The genotype data used in this project comes from the **1000 Genomes Project Phase 3**.

Large raw genotype files and reference genome files are kept locally and are not uploaded to this repository because of their large file sizes.

## Purpose

The purpose of this project is to demonstrate a practical GWAS preprocessing workflow, including genotype quality control, allele-frequency filtering, LD pruning, and population-structure analysis using PCA.

