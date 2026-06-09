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
micromamba activate qiime2-amplicon-2025.4
```

## Opción de bajo uso de RAM

El notebook incluye una bandera al inicio:

```python
USE_SMALL_DATASET = True
```

Activarla usa `data/raw_reads_small/`, `data/metadata_small.tsv`, `results_small/`, un solo thread de QIIME2 y menos lecturas para aprender el modelo de error de DADA2. Esta opción está pensada para estudiantes con computadores de ~8 GB de RAM o para una demostración rápida en clase.

En modo pequeño, el notebook también usa métricas de diversidad no filogenéticas y omite por defecto la clasificación taxonómica con Silva, porque el clasificador `sklearn` es grande. Para forzar taxonomía en modo pequeño:

```python
RUN_TAXONOMY = True
```

## Contenido

| Archivo | Descripción |
|---|---|
| `notebook/16S_pipeline.ipynb` | Notebook paso a paso |
| `scripts/run_qiime2_pipeline.sh` | Versión CLI del pipeline |
| `data/raw_reads/` | Lecturas FASTQ de ejemplo |
| `data/raw_reads_small/` | Subconjunto pequeño para computadores con poca RAM |
| `data/metadata.tsv` | Metadata de las muestras |
| `data/metadata_small.tsv` | Metadata para el subconjunto pequeño |
| `data/taxonomy_db/` | Base de datos de taxonomía (ver instrucciones abajo) |

## Base de datos taxonómica

Descargar el clasificador Silva para QIIME2:

```bash
wget https://data.qiime2.org/2024.10/common/silva-138-99-seqs-515-806.qza \
     -O data/taxonomy_db/silva-138-99-515-806.qza
```
