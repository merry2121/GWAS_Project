# Chromosome 1 GWAS Analysis

## Overview

This folder contains the results of GWAS preprocessing and Principal Component Analysis (PCA) performed using chromosome 1 data from the 1000 Genomes Project.

The analysis was performed using WSL Ubuntu, `bcftools`, and PLINK 1.9.

## Dataset

* Dataset: 1000 Genomes Project Phase 3
* Chromosome: 1
* Individuals: 2,504

## Analysis Pipeline

The chromosome 1 data was processed through several quality-control and population-structure analysis steps:

1. VCF quality checking
2. Variant normalization using `bcftools`
3. Conversion to PLINK binary format
4. Variant quality control
5. Missingness analysis
6. Minor Allele Frequency (MAF) filtering
7. Linkage Disequilibrium (LD) pruning
8. Principal Component Analysis (PCA)
9. PCA visualization

## PCA

PCA was performed using LD-pruned variants from the chromosome 1 dataset.

The PCA results are provided as:

* `chr1_pca.eigenval` — PCA eigenvalues
* `chr1_pca.eigenvec` — PCA coordinates for individuals
* `chr1_pca_PC1_PC2.png` — visualization of PC1 versus PC2
* `chr1_pca_with_pop.txt` — PCA coordinates combined with population information

## LD Pruning

The LD pruning results are:

* `chr1_ld.prune.in` — variants retained after LD pruning
* `chr1_ld.prune.out` — variants removed during LD pruning

## Missingness Analysis

The file:

* `chr1_missingness.imiss` — individual-level missing genotype information

Additional missingness and frequency files were generated during the analysis but are kept locally because some are large and are not stored in the GitHub repository.

## Tools

* WSL Ubuntu
* bcftools
* PLINK 1.9
* Python 3
* Matplotlib

## Purpose

The main purpose of this analysis was to perform genotype quality control and population-structure analysis using chromosome 1 data from the 1000 Genomes Project.

