# Visualizaciones QIIME2 para revisar en clase

Estos archivos `.qzv` vienen del pipeline 16S completo del Módulo 1. Están ordenados para mostrarlos en una sesión de repaso usando QIIME2 View.

Abrir cada archivo en:

https://view.qiime2.org

## Archivos seleccionados

| Orden | Archivo | Qué muestra | Uso en clase |
|---|---|---|---|
| 1 | `01_sequences_summary.qzv` | Calidad de las lecturas antes del trimming. | Revisar perfiles de calidad por posición y justificar parámetros de trimming. |
| 2 | `02_sequences_trimmed_summary.qzv` | Calidad después de remover primers/adaptadores. | Comparar contra las lecturas crudas y confirmar que el preprocesamiento funcionó. |
| 3 | `03_denoising_stats.qzv` | Lecturas filtradas, denoised, merged y no quiméricas por muestra. | Identificar pérdida de lecturas y explicar el efecto de DADA2. |
| 4 | `04_asv_table_summary.qzv` | Número de secuencias por muestra y ASVs detectados. | Elegir profundidad de rarefacción y discutir cobertura. |
| 5 | `05_rep_seqs.qzv` | Secuencias representativas de los ASVs. | Mostrar qué es un ASV y cómo se representa como secuencia. |
| 6 | `06_alpha_rarefaction.qzv` | Curvas de rarefacción alfa. | Evaluar si la profundidad de muestreo captura la diversidad observada. |
| 7 | `07_shannon_significance.qzv` | Diversidad Shannon comparada entre grupos. | Discutir diversidad alfa y significancia estadística. |
| 8 | `08_bray_curtis_emperor.qzv` | PCoA con distancia Bray-Curtis. | Visualizar diferencias de composición usando abundancias. |
| 9 | `09_bray_curtis_significance.qzv` | Test PERMANOVA para Bray-Curtis. | Conectar el gráfico PCoA con una prueba estadística. |
| 10 | `10_weighted_unifrac_emperor.qzv` | PCoA con Weighted UniFrac. | Explicar distancia filogenética ponderada por abundancia. |
| 11 | `11_unweighted_unifrac_emperor.qzv` | PCoA con Unweighted UniFrac. | Comparar presencia/ausencia filogenética contra Weighted UniFrac. |
| 12 | `12_taxonomy.qzv` | Asignación taxonómica de ASVs. | Revisar confianza y niveles taxonómicos asignados. |
| 13 | `13_taxa_barplot.qzv` | Composición taxonómica por muestra. | Interpretar cambios de abundancia relativa entre grupos. |

## Secuencia sugerida de explicación

1. Calidad de datos: archivos 1 y 2.
2. Denoising y tabla ASV: archivos 3, 4 y 5.
3. Diversidad alfa: archivos 6 y 7.
4. Diversidad beta: archivos 8, 9, 10 y 11.
5. Taxonomía: archivos 12 y 13.