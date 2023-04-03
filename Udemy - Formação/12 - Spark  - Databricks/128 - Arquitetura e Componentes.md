<<<<<<< HEAD
<<<<<<< HEAD
128. Arquitetura e Componentes
Bom, então vamos entender um pouquinho melhor os componentes e a arquitetura do Spark.
Então, o Spark é formado por quatro principais componentes e tem as bibliotecas de machine learning ou seja, você pode criar modelos de machine learning com bibliotecas nativas do Spark,  muito embora você possa utilizar outras bibliotecas utilizando o Spark como site Lane, você também tem a opção de utilizar bibliotecas nativas do Spark, que é o ML Lib.
Existe também outro componente que é o SQL, que é o Spark SQL e o Spark SQL permite que você importe dados que você persista dados em formatos de Big Data, como Parquet ou RC. Você pode consultar esses dados utilizando uma sintaxe de SQL, uma sintaxe semelhante à que você utiliza em outros bancos de dados.

Existe um componente de processamento em streaming que é processamento em streaming. E de uma forma bem simplificada, o processamento, estilo e são aquelas aplicações que os dados precisam ser processados à medida que são produzidos em tempo real, próximo ao tempo real.
Então, imagine, por exemplo, um sistema de cercamento eletrônico com câmeras de vídeo que ele verifica veículos entrando e saindo de uma cidade.
Se você vai gravar os vídeos durante o dia e processar a noite para ver se passou o veículo roubado? A aplicação não faz muito sentido. Esse é um caso em que os dados precisam ser processados em tempo real, próximo ao tempo real. Então, é um exemplo de processamento de aplicação em streaming, o Spark tem essa característica e depois o processamento de gráficos que a gente estudou aqui no curso.

Então, o Spark também tem uma biblioteca para isso, o Sparks, que ele permite ler dados tabulares de diversos formatos. Então, aqui, formato que a gente já conhece, CSV, JSON, Parquet, ORC , um formato para Big Data e você pode utilizar a sintaxe SQL. Então, o Spark Extreme, como falei para um streaming de dados estruturados ou a biblioteca de grafos, você pode processar dados acíclicos dirigidos e gráficos acíclicos. Só que eles, grafos que não têm ciclos. Então, o spark também tem essa biblioteca e os elementos aqui do Sparks Park Section. Então, quando a gente cria uma aplicação para iniciar essa sessão, a gente vai ver depois isso no código. E o application é o programa.

Bom, o elemento principal de dados do Spark existem vários. É um data frame, o data frame semelhante ao data frame que a gente estudou no R e ao Data Frame do Panda São dados tabulares em que cada coluna pode ter um tipo de dado diferente.
O Spark também Ele tem um outro tipo de dado, que é o RDD. Mas ele é um formato, eu diria assim ele é mais antigo e Ele não tem as características de um data frame, então existe uma migração, inclusive das bibliotecas do Spark para o uso de data frame, então é apenas dele que ele vai falar. 

Mas é importante você saber que existe também o a estrutura de dados conhecido como RDD.

Então, um data frame ele é imutável, ou seja, você não consegue alterar o data frame. Você tem que criar outro. Se você vai alterar, por exemplo, uma coluna, se você vai ter um valor de uma coluna, você precisa criar outro frame.
E quando você faz uma transformação, você na verdade está produzindo outro. E o Spark também tem o conceito de Lazy Evaluation, quer dizer que os dados só ocorrem se os dados são transformados de fato quando ocorre uma ação.

Então, isso pode parecer um pouquinho estranho, um pouquinho complicado.
Então, o que é um lazy evaluation? Quer dizer que a transformação dos dados, de fato, só acontece quando há uma ação. Então, existem duas, duas categorias de transformações de dados ou funções para transformar dados no Spark 
As chamadas transformações e as chamadas ações.

Sempre que você fizer uma transformação, você digita lá um comando para fazer uma transformação. O Spark não vai de fato executar aquilo. Ele vai apenas registrar aquilo. Ele vai colocar aquilo numa fila de processo.

Então, por exemplo, você tem lá um conjunto de dados que você importou. Você aplica um filtro, você quer apenas o mês de janeiro. Isso é uma transformação. Ele registra essa transformação, mas não executa.

Depois, você faz uma union, um comando de um único outro conjunto de dados. Você tem outra transformação. Depois, você pega esse conjunto de dados e gera uma amostra.

Se usa o sample também, você tem uma transformação para que não executa nada. Aí, finalmente, você usa o comando, por exemplo, dataframe.show aqui você tem uma ação. Quando tem uma ação, ele vai mostrar os dados.
Aqui, o comando vai mostrar os dados. Ele vai executar toda e todo o sistema que toda essa pilha de transformações Esse é essa forma que o Spark funciona. É uma característica para otimizar o processo, que é assim que ele consegue otimizar o processo. 

Aqui a gente tem uma lista de transformações e uma lista de ações. A gente vai ver algumas delas, mas obviamente que a gente não vai estudar todas.
| Transformações | Ações |
| --- | --- |
| map | reduce |
| filter | collect |
| flatMap | count |
| mapPartitionsWhithIndex | first |
| mapPartitions | take |
| sample | takeSample |
| union | takeOrder |
| intersection | saveAsTextFile |
| distinct | saveAsSequenceFile |
| groupByKey | saveAsObjectFile |
| reduceByKey | countByKey |
| aggregateByKey | foreach |
| sortByKey | -- |
| join | -- |
| cogroup | -- |
| cartesian | -- |
| pipe | -- |
| coalesce | -- |
| repartition | -- |
| repartitionAndSortWithinPartitions | -- |

O importante aqui que você precisa saber que quando você tem pelo processo de Lazy e evaluation, quando você tem uma transformação, o um processo de fato não é executado. Ele vai ser executado só quando você faz uma ação.
=======
128. Arquitetura e Componentes
Bom, então vamos entender um pouquinho melhor os componentes e a arquitetura do Spark.
Então, o Spark é formado por quatro principais componentes e tem as bibliotecas de machine learning ou seja, você pode criar modelos de machine learning com bibliotecas nativas do Spark,  muito embora você possa utilizar outras bibliotecas utilizando o Spark como site Lane, você também tem a opção de utilizar bibliotecas nativas do Spark, que é o ML Lib.
Existe também outro componente que é o SQL, que é o Spark SQL e o Spark SQL permite que você importe dados que você persista dados em formatos de Big Data, como Parquet ou RC. Você pode consultar esses dados utilizando uma sintaxe de SQL, uma sintaxe semelhante à que você utiliza em outros bancos de dados.

Existe um componente de processamento em streaming que é processamento em streaming. E de uma forma bem simplificada, o processamento, estilo e são aquelas aplicações que os dados precisam ser processados à medida que são produzidos em tempo real, próximo ao tempo real.
Então, imagine, por exemplo, um sistema de cercamento eletrônico com câmeras de vídeo que ele verifica veículos entrando e saindo de uma cidade.
Se você vai gravar os vídeos durante o dia e processar a noite para ver se passou o veículo roubado? A aplicação não faz muito sentido. Esse é um caso em que os dados precisam ser processados em tempo real, próximo ao tempo real. Então, é um exemplo de processamento de aplicação em streaming, o Spark tem essa característica e depois o processamento de gráficos que a gente estudou aqui no curso.

Então, o Spark também tem uma biblioteca para isso, o Sparks, que ele permite ler dados tabulares de diversos formatos. Então, aqui, formato que a gente já conhece, CSV, JSON, Parquet, ORC , um formato para Big Data e você pode utilizar a sintaxe SQL. Então, o Spark Extreme, como falei para um streaming de dados estruturados ou a biblioteca de grafos, você pode processar dados acíclicos dirigidos e gráficos acíclicos. Só que eles, grafos que não têm ciclos. Então, o spark também tem essa biblioteca e os elementos aqui do Sparks Park Section. Então, quando a gente cria uma aplicação para iniciar essa sessão, a gente vai ver depois isso no código. E o application é o programa.

Bom, o elemento principal de dados do Spark existem vários. É um data frame, o data frame semelhante ao data frame que a gente estudou no R e ao Data Frame do Panda São dados tabulares em que cada coluna pode ter um tipo de dado diferente.
O Spark também Ele tem um outro tipo de dado, que é o RDD. Mas ele é um formato, eu diria assim ele é mais antigo e Ele não tem as características de um data frame, então existe uma migração, inclusive das bibliotecas do Spark para o uso de data frame, então é apenas dele que ele vai falar. 

Mas é importante você saber que existe também o a estrutura de dados conhecido como RDD.

Então, um data frame ele é imutável, ou seja, você não consegue alterar o data frame. Você tem que criar outro. Se você vai alterar, por exemplo, uma coluna, se você vai ter um valor de uma coluna, você precisa criar outro frame.
E quando você faz uma transformação, você na verdade está produzindo outro. E o Spark também tem o conceito de Lazy Evaluation, quer dizer que os dados só ocorrem se os dados são transformados de fato quando ocorre uma ação.

Então, isso pode parecer um pouquinho estranho, um pouquinho complicado.
Então, o que é um lazy evaluation? Quer dizer que a transformação dos dados, de fato, só acontece quando há uma ação. Então, existem duas, duas categorias de transformações de dados ou funções para transformar dados no Spark 
As chamadas transformações e as chamadas ações.

Sempre que você fizer uma transformação, você digita lá um comando para fazer uma transformação. O Spark não vai de fato executar aquilo. Ele vai apenas registrar aquilo. Ele vai colocar aquilo numa fila de processo.

Então, por exemplo, você tem lá um conjunto de dados que você importou. Você aplica um filtro, você quer apenas o mês de janeiro. Isso é uma transformação. Ele registra essa transformação, mas não executa.

Depois, você faz uma union, um comando de um único outro conjunto de dados. Você tem outra transformação. Depois, você pega esse conjunto de dados e gera uma amostra.

Se usa o sample também, você tem uma transformação para que não executa nada. Aí, finalmente, você usa o comando, por exemplo, dataframe.show aqui você tem uma ação. Quando tem uma ação, ele vai mostrar os dados.
Aqui, o comando vai mostrar os dados. Ele vai executar toda e todo o sistema que toda essa pilha de transformações Esse é essa forma que o Spark funciona. É uma característica para otimizar o processo, que é assim que ele consegue otimizar o processo. 

Aqui a gente tem uma lista de transformações e uma lista de ações. A gente vai ver algumas delas, mas obviamente que a gente não vai estudar todas.
| Transformações | Ações |
| --- | --- |
| map | reduce |
| filter | collect |
| flatMap | count |
| mapPartitionsWhithIndex | first |
| mapPartitions | take |
| sample | takeSample |
| union | takeOrder |
| intersection | saveAsTextFile |
| distinct | saveAsSequenceFile |
| groupByKey | saveAsObjectFile |
| reduceByKey | countByKey |
| aggregateByKey | foreach |
| sortByKey | -- |
| join | -- |
| cogroup | -- |
| cartesian | -- |
| pipe | -- |
| coalesce | -- |
| repartition | -- |
| repartitionAndSortWithinPartitions | -- |

O importante aqui que você precisa saber que quando você tem pelo processo de Lazy e evaluation, quando você tem uma transformação, o um processo de fato não é executado. Ele vai ser executado só quando você faz uma ação.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
=======
128. Arquitetura e Componentes
Bom, então vamos entender um pouquinho melhor os componentes e a arquitetura do Spark.
Então, o Spark é formado por quatro principais componentes e tem as bibliotecas de machine learning ou seja, você pode criar modelos de machine learning com bibliotecas nativas do Spark,  muito embora você possa utilizar outras bibliotecas utilizando o Spark como site Lane, você também tem a opção de utilizar bibliotecas nativas do Spark, que é o ML Lib.
Existe também outro componente que é o SQL, que é o Spark SQL e o Spark SQL permite que você importe dados que você persista dados em formatos de Big Data, como Parquet ou RC. Você pode consultar esses dados utilizando uma sintaxe de SQL, uma sintaxe semelhante à que você utiliza em outros bancos de dados.

Existe um componente de processamento em streaming que é processamento em streaming. E de uma forma bem simplificada, o processamento, estilo e são aquelas aplicações que os dados precisam ser processados à medida que são produzidos em tempo real, próximo ao tempo real.
Então, imagine, por exemplo, um sistema de cercamento eletrônico com câmeras de vídeo que ele verifica veículos entrando e saindo de uma cidade.
Se você vai gravar os vídeos durante o dia e processar a noite para ver se passou o veículo roubado? A aplicação não faz muito sentido. Esse é um caso em que os dados precisam ser processados em tempo real, próximo ao tempo real. Então, é um exemplo de processamento de aplicação em streaming, o Spark tem essa característica e depois o processamento de gráficos que a gente estudou aqui no curso.

Então, o Spark também tem uma biblioteca para isso, o Sparks, que ele permite ler dados tabulares de diversos formatos. Então, aqui, formato que a gente já conhece, CSV, JSON, Parquet, ORC , um formato para Big Data e você pode utilizar a sintaxe SQL. Então, o Spark Extreme, como falei para um streaming de dados estruturados ou a biblioteca de grafos, você pode processar dados acíclicos dirigidos e gráficos acíclicos. Só que eles, grafos que não têm ciclos. Então, o spark também tem essa biblioteca e os elementos aqui do Sparks Park Section. Então, quando a gente cria uma aplicação para iniciar essa sessão, a gente vai ver depois isso no código. E o application é o programa.

Bom, o elemento principal de dados do Spark existem vários. É um data frame, o data frame semelhante ao data frame que a gente estudou no R e ao Data Frame do Panda São dados tabulares em que cada coluna pode ter um tipo de dado diferente.
O Spark também Ele tem um outro tipo de dado, que é o RDD. Mas ele é um formato, eu diria assim ele é mais antigo e Ele não tem as características de um data frame, então existe uma migração, inclusive das bibliotecas do Spark para o uso de data frame, então é apenas dele que ele vai falar. 

Mas é importante você saber que existe também o a estrutura de dados conhecido como RDD.

Então, um data frame ele é imutável, ou seja, você não consegue alterar o data frame. Você tem que criar outro. Se você vai alterar, por exemplo, uma coluna, se você vai ter um valor de uma coluna, você precisa criar outro frame.
E quando você faz uma transformação, você na verdade está produzindo outro. E o Spark também tem o conceito de Lazy Evaluation, quer dizer que os dados só ocorrem se os dados são transformados de fato quando ocorre uma ação.

Então, isso pode parecer um pouquinho estranho, um pouquinho complicado.
Então, o que é um lazy evaluation? Quer dizer que a transformação dos dados, de fato, só acontece quando há uma ação. Então, existem duas, duas categorias de transformações de dados ou funções para transformar dados no Spark 
As chamadas transformações e as chamadas ações.

Sempre que você fizer uma transformação, você digita lá um comando para fazer uma transformação. O Spark não vai de fato executar aquilo. Ele vai apenas registrar aquilo. Ele vai colocar aquilo numa fila de processo.

Então, por exemplo, você tem lá um conjunto de dados que você importou. Você aplica um filtro, você quer apenas o mês de janeiro. Isso é uma transformação. Ele registra essa transformação, mas não executa.

Depois, você faz uma union, um comando de um único outro conjunto de dados. Você tem outra transformação. Depois, você pega esse conjunto de dados e gera uma amostra.

Se usa o sample também, você tem uma transformação para que não executa nada. Aí, finalmente, você usa o comando, por exemplo, dataframe.show aqui você tem uma ação. Quando tem uma ação, ele vai mostrar os dados.
Aqui, o comando vai mostrar os dados. Ele vai executar toda e todo o sistema que toda essa pilha de transformações Esse é essa forma que o Spark funciona. É uma característica para otimizar o processo, que é assim que ele consegue otimizar o processo. 

Aqui a gente tem uma lista de transformações e uma lista de ações. A gente vai ver algumas delas, mas obviamente que a gente não vai estudar todas.
| Transformações | Ações |
| --- | --- |
| map | reduce |
| filter | collect |
| flatMap | count |
| mapPartitionsWhithIndex | first |
| mapPartitions | take |
| sample | takeSample |
| union | takeOrder |
| intersection | saveAsTextFile |
| distinct | saveAsSequenceFile |
| groupByKey | saveAsObjectFile |
| reduceByKey | countByKey |
| aggregateByKey | foreach |
| sortByKey | -- |
| join | -- |
| cogroup | -- |
| cartesian | -- |
| pipe | -- |
| coalesce | -- |
| repartition | -- |
| repartitionAndSortWithinPartitions | -- |

O importante aqui que você precisa saber que quando você tem pelo processo de Lazy e evaluation, quando você tem uma transformação, o um processo de fato não é executado. Ele vai ser executado só quando você faz uma ação.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
