# Guía de apoyo conceptual

Este documento entrega contexto general para la actividad evaluada. No reemplaza los notebooks ni responde las preguntas del informe. Su objetivo es ayudar a recordar qué mide cada análisis y cómo leer los resultados principales.

## Análisis 16S

El análisis 16S se usa para estudiar comunidades microbianas a partir de una región del gen 16S rRNA. Este gen está presente en bacterias y arqueas, y contiene regiones conservadas y regiones variables. Las regiones conservadas permiten amplificar el gen con primers generales; las regiones variables ayudan a distinguir distintos grupos microbianos.

En esta actividad se trabaja con lecturas paired-end. El pipeline transforma lecturas crudas en una tabla de ASVs y visualizaciones para comparar muestras.

## Qué es un ASV

Un ASV es una variante de secuencia amplicónica. Representa una secuencia biológica inferida a partir de las lecturas, después de corregir errores de secuenciación. A diferencia de los OTUs tradicionales, los ASVs no se agrupan usando un umbral fijo de similitud como 97%; intentan resolver diferencias de secuencia más finas.

El número de ASVs depende del dataset, la calidad de las lecturas, los parámetros de procesamiento y la diversidad real de las muestras.

## Pasos principales del notebook 16S

1. Importación de lecturas: convierte los FASTQ en artefactos QIIME2.
2. Revisión de calidad: permite observar la calidad por posición antes de elegir parámetros.
3. Trimming: remueve primers y secuencias no biológicas.
4. Denoising con DADA2: filtra lecturas, corrige errores, une pares y remueve quimeras.
5. Tabla ASV: resume cuántas lecturas de cada ASV aparecen en cada muestra.
6. Diversidad alfa: resume diversidad dentro de cada muestra.
7. Diversidad beta: compara composición entre muestras.
8. Taxonomía: asigna posibles grupos taxonómicos a las secuencias representativas.

## Diversidad alfa y beta

La diversidad alfa describe propiedades dentro de una muestra. Puede considerar riqueza, abundancia relativa o uniformidad, dependiendo de la métrica usada.

La diversidad beta compara diferencias entre muestras. En QIIME2, estas comparaciones suelen visualizarse con PCoA y evaluarse con pruebas estadísticas como PERMANOVA.

Las métricas no son equivalentes. Algunas consideran abundancias, otras presencia/ausencia, y otras incorporan información filogenética.

## Taxonomía en 16S

La clasificación taxonómica intenta asignar cada ASV a un grupo biológico usando una base de datos de referencia. La calidad de esta asignación depende de la región amplificada, la base de datos, el clasificador usado y la calidad de las secuencias.

Los resultados taxonómicos deben leerse como una aproximación, especialmente cuando el dataset es pequeño.

## Análisis DESeq

DESeq2 es un método usado para analizar expresión diferencial a partir de matrices de conteos. En este curso se usa PyDESeq2, una implementación en Python compatible con la lógica de DESeq2.

El objetivo es comparar condiciones experimentales y detectar genes cuyo nivel de conteo cambia de forma consistente entre grupos.

## Qué datos usa DESeq

DESeq trabaja con:

- Una matriz de conteos: genes en filas y muestras en columnas.
- Una tabla de metadata: describe a qué condición pertenece cada muestra.
- Un diseño experimental: define qué variable se quiere comparar.

Los conteos deben ser enteros porque representan lecturas asignadas a genes.

## Contraste y log2FoldChange

El contraste define qué comparación se está haciendo. Por ejemplo, comparar `treated` contra `control` significa que el cambio se estima en relación con la condición control.

El `log2FoldChange` resume el tamaño y dirección del cambio entre condiciones. Su interpretación depende del orden del contraste configurado en el notebook.

## Significancia y FDR

En RNA-seq se evalúan muchos genes al mismo tiempo. Por eso no basta con mirar un valor p sin corregir. El FDR ajusta los resultados para controlar el efecto de múltiples pruebas.

Un gen significativo combina evidencia estadística y un criterio de tamaño de efecto definido en el análisis.

## Visualizaciones en DESeq

El PCA muestra si las muestras se agrupan según patrones globales de conteos.

El volcano plot combina tamaño de efecto y significancia estadística. Es útil para ubicar genes con cambios grandes y evidencia estadística fuerte.

El heatmap muestra patrones de expresión relativa para un subconjunto de genes, normalmente genes significativos o genes con mayor evidencia de cambio.

## Uso de gene_metadata

`gene_metadata.csv` contiene anotaciones sintéticas para apoyar la lectura de resultados. Estas anotaciones no se usan para ajustar el modelo estadístico. Se agregan después para ayudar a describir genes, productos, categorías funcionales y pathways.

## Recomendaciones para responder el informe

- Usar resultados generados por el propio dataset del grupo.
- Revisar las figuras antes de escribir respuestas.
- Reportar nombres de archivos o tablas cuando una respuesta dependa de un resultado específico.
- Diferenciar observaciones descriptivas de resultados estadísticos.
- Mencionar limitaciones técnicas cuando un paso no pueda ejecutarse por memoria o por falta de recursos.

## Palabras clave para estudiar más

### 16S y microbioma

- 16S rRNA gene
- amplicon sequencing
- microbial community profiling
- paired-end reads
- FASTQ quality scores
- primer trimming
- QIIME2
- DADA2
- denoising
- chimera removal
- ASV, amplicon sequence variant
- OTU, operational taxonomic unit
- feature table
- representative sequences
- rarefaction
- alpha diversity
- beta diversity
- Shannon diversity
- observed features
- Bray-Curtis distance
- Jaccard distance
- UniFrac distance
- PCoA, principal coordinates analysis
- PERMANOVA
- taxonomic classification
- Silva database
- Naive Bayes classifier
- relative abundance

### DESeq y expresión diferencial

- RNA-seq counts
- count matrix
- sample metadata
- differential expression analysis
- DESeq2
- PyDESeq2
- experimental design
- design formula
- contrast
- control condition
- treated condition
- size factor normalization
- library size
- dispersion estimation
- negative binomial model
- Wald test
- p-value
- adjusted p-value
- FDR, false discovery rate
- multiple testing correction
- log2FoldChange
- up-regulated genes
- down-regulated genes
- PCA
- volcano plot
- heatmap
- gene annotation
- pathway annotation
