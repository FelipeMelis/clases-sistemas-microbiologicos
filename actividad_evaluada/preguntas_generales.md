# Preguntas generales

## Regla de número de preguntas

Cada grupo debe determinar primero cuántos ASVs obtuvo en su pipeline 16S. Ese valor será `N`.

El informe debe responder al menos `N` preguntas de este documento. Las preguntas pueden elegirse libremente desde cualquier sección, siempre que las respuestas cubran ambos notebooks trabajados en la actividad.

La pregunta 10 es obligatoria porque define el valor de `N`.

## Notebook 16S: análisis de comunidades microbianas

### Configuración básica

1. ¿Qué dataset o grupo analizaste?
2. ¿Cuántas muestras hay en el archivo de metadata?
3. ¿Qué variable experimental usarás para comparar grupos? Por ejemplo: `Treatment`.
4. ¿Cuántas muestras hay en cada grupo?

### Procesamiento de lecturas

5. ¿Cuántas lecturas fueron importadas por muestra?
6. Después del trimming de primers, ¿todas las muestras conservaron lecturas?
7. Después de DADA2, ¿cuántas lecturas quedaron por muestra?
8. ¿Qué muestra tuvo el menor número de lecturas no quiméricas?
9. ¿Qué profundidad de muestreo (`SAMPLING_DEPTH`) elegiste para el análisis de diversidad y por qué?

### ASVs

10. ¿Cuántos ASVs se detectaron en tu dataset? Este número define cuántas preguntas debe responder tu grupo.
11. ¿Cuál es la diferencia entre un ASV y un OTU?
12. ¿Por qué DADA2 remueve quimeras?
13. ¿Alguna muestra tuvo una profundidad de lectura mucho menor que las otras?

### Diversidad alfa

14. ¿Qué mide la diversidad alfa?
15. Compara la diversidad de Shannon entre grupos. ¿Qué grupo parece más diverso?
16. ¿Las diferencias de diversidad alfa son estadísticamente significativas?
17. Si el test no es significativo, ¿qué significa eso?

### Diversidad beta

18. ¿Qué mide la diversidad beta?
19. En el gráfico PCoA, ¿las muestras se agrupan según tratamiento o grupo?
20. ¿Qué considera la distancia Bray-Curtis?
21. ¿El resultado de PERMANOVA fue significativo?
22. Si las muestras no se agrupan claramente, ¿cuáles podrían ser algunas explicaciones?

### Taxonomía

23. ¿Cuáles son los grupos bacterianos más abundantes en cada muestra?
24. ¿Los taxa dominantes difieren entre grupos?
25. ¿Hay taxa que parecen estar enriquecidos en una condición?
26. ¿Por qué los resultados taxonómicos de un dataset muy pequeño deben interpretarse con cuidado?

### Interpretación biológica

27. Según los resultados de diversidad y taxonomía, ¿las comunidades microbianas parecen diferir entre grupos?
28. ¿Qué resultado es más fuerte: diversidad alfa, diversidad beta o taxonomía? Explica.
29. ¿Qué datos adicionales o réplicas mejorarían la confianza en tu conclusión?
30. Escribe una interpretación biológica breve de tus resultados 16S en 5 a 8 frases.

### Calidad y limitaciones

31. ¿Cuál es una limitación de usar un dataset FASTQ muy pequeño?
32. ¿Por qué la rarefacción puede eliminar muestras?
33. ¿Por qué la clasificación taxonómica puede fallar en computadores con poca RAM?
34. ¿Qué pasos del pipeline 16S son computacionalmente más costosos?
35. ¿Qué mejora metodológica aumentaría la calidad de este análisis?

## Notebook DESeq: expresión diferencial

### Configuración y datos

36. ¿Qué dataset de conteos analizaste?
37. ¿Cuántos genes y cuántas muestras contiene la matriz de conteos?
38. ¿Cuántas muestras hay en cada condición experimental?
39. ¿Cuál fue el contraste usado en DESeq?
40. En este contraste, ¿qué significa un `log2FoldChange` positivo?
41. ¿Por qué la matriz de conteos debe contener valores enteros?
42. ¿Por qué es importante revisar la metadata antes de correr DESeq?

### Exploración inicial

43. ¿Las librerías tienen tamaños similares entre muestras?
44. ¿Qué muestra tuvo el mayor número total de conteos?
45. ¿Qué muestra tuvo el menor número total de conteos?
46. En el PCA, ¿las muestras se agrupan según condición?
47. ¿Qué podría indicar una muestra que se separa mucho del resto en el PCA?

### Resultados estadísticos

48. ¿Cuántos genes fueron significativos usando el umbral de FDR definido?
49. ¿Cuántos genes aumentaron en `treated`?
50. ¿Cuántos genes disminuyeron en `treated`?
51. ¿Cuál fue el gen con menor `padj`?
52. ¿Cuál fue el gen con mayor `log2FoldChange` positivo?
53. ¿Cuál fue el gen con `log2FoldChange` más negativo?
54. ¿Qué diferencia hay entre `pvalue` y `padj`?
55. ¿Por qué se usa corrección por múltiples pruebas en RNA-seq?
56. ¿Qué significa que un gen tenga `padj < 0.05`?
57. ¿Qué significa que un gen tenga un `log2FoldChange` grande pero no sea significativo?

### Visualización e interpretación

58. En el volcano plot, ¿qué representan los puntos rojos?
59. En el volcano plot, ¿qué representan los puntos azules?
60. ¿Qué genes aparecen etiquetados en el volcano plot?
61. En el heatmap, ¿los genes significativos separan las muestras por condición?
62. ¿Qué patrón general observas entre control y tratado en el heatmap?
63. ¿Qué funciones o pathways aparecen entre los genes significativos?
64. Usando `gene_metadata.csv`, interpreta tres genes significativos.
65. ¿Los genes significativos sugieren una respuesta biológica coherente al tratamiento?
66. ¿Qué limitaciones tiene interpretar resultados con solo seis muestras?
67. Escribe una conclusión breve integrando los resultados DESeq en 5 a 8 frases.
