# Actividad Evaluada

## Objetivo

Cada grupo debe analizar un dataset asignado usando dos notebooks:

- `notebook_16S_evaluacion.ipynb`: análisis 16S con QIIME2/DADA2.
- `notebook_DESeq_evaluacion.ipynb`: análisis de expresión diferencial con PyDESeq2.

El resultado final es un informe breve basado en las preguntas de `preguntas_generales.md`.

## Regla de preguntas

1. Ejecutar el notebook 16S hasta obtener la tabla de ASVs.
2. Determinar cuántos ASVs se detectaron en el dataset del grupo.
3. Ese número será `N`.
4. El informe debe responder al menos `N` preguntas de `preguntas_generales.md`.
5. Las preguntas pueden elegirse libremente desde cualquier sección del documento.
6. Las respuestas deben incluir contenido de ambos notebooks: 16S y DESeq.
7. La pregunta 10 de `preguntas_generales.md` es obligatoria porque define el valor de `N`.

Ejemplo: si un grupo detecta 18 ASVs, debe responder al menos 18 preguntas. No tienen que ser las preguntas 1 a 18; pueden escoger preguntas de 16S y DESeq.

## Materiales

- `notebook_16S_evaluacion.ipynb` — notebook base para trimming, denoising, diversidad y taxonomía.
- `notebook_DESeq_evaluacion.ipynb` — notebook base para expresión diferencial, volcano plot y heatmap.
- `preguntas_generales.md` — banco de preguntas para el informe.
- `guia_apoyo.md` — explicación conceptual general sobre 16S y DESeq.
- `rubrica.md` — criterios de evaluación de la actividad.
- `dataset_grupo_A/` a `dataset_grupo_K/` — datasets asignados por grupo.

## Estructura de cada dataset

Cada carpeta `dataset_grupo_X/` contiene:

- `16S/raw_reads/` — lecturas paired-end FASTQ pequeñas.
- `16S/metadata.tsv` — metadata para el análisis 16S.
- `counts/counts_matrix.csv` — matriz de conteos para DESeq.
- `counts/metadata.csv` — metadata de las muestras RNA-seq.
- `counts/gene_metadata.csv` — anotaciones sintéticas para responder preguntas sobre genes.
- `counts/de_truth.csv` — respuesta simulada para uso docente.

## Datasets disponibles

- `dataset_grupo_A/`
- `dataset_grupo_B/`
- `dataset_grupo_C/`
- `dataset_grupo_D/`
- `dataset_grupo_E/`
- `dataset_grupo_F/`
- `dataset_grupo_G/`
- `dataset_grupo_H/`
- `dataset_grupo_I/`
- `dataset_grupo_J/`
- `dataset_grupo_K/`

## Entrega

Cada grupo debe entregar:

- Notebook 16S ejecutado con el dataset asignado.
- Notebook DESeq ejecutado con el dataset asignado.
- Informe con al menos `N` preguntas respondidas desde `preguntas_generales.md`.
- Figuras principales generadas por los notebooks, incluidas en el notebook o en el informe.

## Rúbrica

Los criterios de evaluación están descritos en `rubrica.md`.

## Consideraciones

Los datasets son deliberadamente pequeños para que puedan correr en computadores con poca RAM.

La clasificación taxonómica con Silva puede seguir siendo pesada. Si falla por memoria, registrar la limitación y evaluar el pipeline 16S hasta diversidad.
