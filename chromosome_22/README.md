# Chromosome 22 GWAS Analysis

## Overview

This folder contains the results of a GWAS preprocessing and Principal Component Analysis (PCA) performed using chromosome 22 data from the 1000 Genomes Project.

The analysis was performed using WSL Ubuntu, `bcftools`, and PLINK 1.9.

## Dataset

* Dataset: 1000 Genomes Project Phase 3
* Chromosome: 22
* Individuals: 2,504
* Initial variants: 1,104,364

## Analysis Pipeline

The chromosome 22 data was processed through the following steps:

1. VCF quality checking
2. Variant normalization using `bcftools`
3. Conversion from VCF/BCF format to PLINK binary format
4. Strict-region masking
5. SNP filtering
6. Minor Allele Frequency (MAF) filtering
7. Linkage Disequilibrium (LD) pruning
8. Principal Component Analysis (PCA)
9. PCA visualization

## Quality Control and Filtering

After normalization and conversion to PLINK format:

* 1,104,364 variants were available.
* Strict-mask filtering retained 749,426 variants.
* SNP filtering retained 726,054 variants.
* MAF ≥ 0.1 filtering retained 45,608 variants.
* LD pruning retained 3,444 variants for PCA.

## PCA Results

PCA was performed using the 3,444 LD-pruned variants from 2,504 individuals.

The first 10 principal components explained:

| Principal Component | Variance Explained |
| ------------------- | -----------------: |
| PC1                 |             53.62% |
| PC2                 |             24.43% |
| PC3                 |              7.64% |
| PC4                 |              6.59% |
| PC5                 |              1.48% |
| PC6                 |              1.34% |
| PC7                 |              1.27% |
| PC8                 |              1.24% |
| PC9                 |              1.21% |
| PC10                |              1.18% |

PC1 and PC2 together explain approximately **78.05%** of the variation captured by the first 10 PCs.

## Output Files

* `chr22_ld.prune.in` — variants retained after LD pruning
* `chr22_ld.prune.out` — variants removed during LD pruning
* `chr22_pca.eigenval` — eigenvalues from PCA
* `chr22_pca.eigenvec` — individual PCA coordinates
* `chr22_strict_mask_range.txt` — chromosome 22 strict-mask regions

## Tools

* WSL Ubuntu
* bcftools 1.19
* PLINK 1.9
* Python 3
* Matplotlib

## Purpose

The main purpose of this analysis was to perform quality control, population-structure analysis, and PCA on chromosome 22 genotype data from the 1000 Genomes Project.
