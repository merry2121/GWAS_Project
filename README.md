# GWAS Analysis Project

**Author:** Meron Kidane  
**GitHub:** merry2121

## Overview

This project performs genotype quality control and population-structure analysis using genotype data from the **1000 Genomes Project Phase 3**.

The analysis focuses on **chromosome 22** and was performed using **WSL Ubuntu, bcftools, PLINK 1.9, Python, and Matplotlib**.

## Analysis Pipeline

The chromosome 22 data was processed through the following steps:

1. Obtain chromosome 22 VCF genotype data
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
├── chromosome_22/
│   ├── README.md
│   └── results/
│
├── scripts/
├── data/
├── reference/
├── results/
└── README.md
