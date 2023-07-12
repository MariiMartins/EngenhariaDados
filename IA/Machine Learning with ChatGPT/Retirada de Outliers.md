Existem várias técnicas que podem ser utilizadas para remover outliers de um DataFrame. Vou apresentar algumas das técnicas mais comuns:

Método Z-score: Calcula o desvio padrão dos dados e identifica os pontos de dados que estão além de um limite especificado. Os pontos de dados além desse limite são considerados outliers.

Intervalo interquartil (IQR): Calcula o intervalo entre o primeiro quartil (25%) e o terceiro quartil (75%) dos dados. Qualquer ponto de dados que esteja abaixo de Q1 - 1,5 *IQR ou acima de Q3 + 1,5* IQR é considerado um outlier.

Gráficos de dispersão: Plotar gráficos de dispersão para visualizar a distribuição dos dados. Pontos de dados que estão longe da tendência geral dos dados podem ser identificados como outliers.

Análise de desvio: Calcular a média e o desvio padrão dos dados e remover os pontos de dados que estão além de um número especificado de desvios padrão da média.

Algoritmos de detecção de outliers: Alguns algoritmos específicos, como o Isolation Forest, Local Outlier Factor (LOF) e o método DBSCAN (Density-Based Spatial Clustering of Applications with Noise), são projetados para detectar e remover outliers.

Regras de domínio: Com base no conhecimento do domínio ou em regras específicas do problema, pode-se estabelecer critérios para identificar e remover outliers. Por exemplo, definir um limite máximo ou mínimo para uma determinada variável. (...)
