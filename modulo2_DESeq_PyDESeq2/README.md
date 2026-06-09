# Módulo 2: DESeq / PyDESeq2

## Objetivo

Analizar datos de conteo e identificar genes (o features) diferencialmente expresados usando PyDESeq2.

El dataset de ejemplo simula un experimento RNA-seq microbiológico: cultivos bacterianos en medio rico con glucosa (`control`) versus cultivos en medio limitado en nitrógeno (`treated`) después de 24 h. La matriz contiene 500 genes y 10 muestras: 5 réplicas biológicas por condición.

## Temas

1. Matriz de conteos y metadata
2. Normalización
3. Réplicas biológicas
4. PCA exploratorio
5. Log2 fold change
6. Valor p y FDR
7. Genes diferencialmente expresados
8. Volcano plot
9. Heatmap
10. Interpretación de resultados

## Entorno

```bash
micromamba run -n qiime2-amplicon-2025.4 python3 scripts/run_pydeseq2.py \
  --counts data/counts_matrix.csv \
  --metadata data/metadata.csv \
  --gene-metadata data/gene_metadata.csv \
  --condition condition \
  --contrast treated control \
  --outdir results
```

## Contenido

| Archivo | Descripción |
|---|---|
| `notebook/deseq2_pipeline.ipynb` | Notebook paso a paso |
| `scripts/run_pydeseq2.py` | Versión script del pipeline |
| `data/counts_matrix.csv` | Matriz de conteos crudos (500 genes × 10 muestras) |
| `data/metadata.csv` | Metadata (condición, réplica, medio de cultivo, incubación y batch) |
| `data/gene_metadata.csv` | Anotaciones sintéticas por gen para interpretar resultados |
| `data/de_truth.csv` | Verdadero estado simulado de cada gen para fines docentes |
