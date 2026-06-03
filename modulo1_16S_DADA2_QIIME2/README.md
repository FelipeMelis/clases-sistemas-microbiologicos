# Módulo 1: 16S / DADA2 - QIIME2

## Objetivo

Entender y ejecutar un flujo estándar de análisis 16S rRNA, desde lecturas crudas hasta visualización de diversidad microbiana.

## Temas

1. Calidad de lecturas (FastQC / QIIME2 demux)
2. Denoising con DADA2
3. ASVs versus OTUs
4. Tabla ASV
5. Asignación taxonómica
6. Abundancia relativa
7. Diversidad alfa y beta
8. PCoA / PCA y gráficos taxonómicos

## Entorno

```bash
conda env create -f ../environment/environment_qiime2.yml
conda activate qiime2-amplicon-2024.10
```

## Contenido

| Archivo | Descripción |
|---|---|
| `notebook/16S_pipeline.ipynb` | Notebook paso a paso |
| `scripts/run_qiime2_pipeline.sh` | Versión CLI del pipeline |
| `data/raw_reads/` | Lecturas FASTQ de ejemplo |
| `data/metadata.tsv` | Metadata de las muestras |
| `data/taxonomy_db/` | Base de datos de taxonomía (ver instrucciones abajo) |

## Base de datos taxonómica

Descargar el clasificador Silva para QIIME2:

```bash
wget https://data.qiime2.org/2024.10/common/silva-138-99-seqs-515-806.qza \
     -O data/taxonomy_db/silva-138-99-515-806.qza
```
