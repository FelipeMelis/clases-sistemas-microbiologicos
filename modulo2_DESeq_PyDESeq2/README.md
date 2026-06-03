# Módulo 2: DESeq / PyDESeq2

## Objetivo

Analizar datos de conteo e identificar genes (o features) diferencialmente expresados usando PyDESeq2.

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
pip install -r ../environment/requirements_pydeseq2.txt
```

## Contenido

| Archivo | Descripción |
|---|---|
| `notebook/deseq2_pipeline.ipynb` | Notebook paso a paso |
| `scripts/run_pydeseq2.py` | Versión script del pipeline |
| `data/counts_matrix.csv` | Matriz de conteos (genes × muestras) |
| `data/metadata.csv` | Metadata (condición, réplica, etc.) |
