123. Introdução
Então, nesta sessão nós estamos começando a falar sobre processamento em Batch e sistema distribuídos.
Então a gente vai ver uma série de produtos de soluções mantidos pela Fundação Apache, todos esses produtos relacionados a dados, a aplicação orientadas a dados, a big data.

Então a gente não pode falar de todas. O ecossistema Hadoop, mantido pela Fundação Apache, é um ecossistema muito grande. São muitas soluções. A gente tem aqui algumas delas e a gente vai estudar algumas delas, as mais importantes durante o nosso curso.

Então, do ponto de vista de ingestão de dados, de colocar os dados, de importar os dados, em gerir, eles deixarão de disponível no ambiente analítico.
Nós temos aqui o Flume e o Scoop. O Flume é usado principalmente para informação não estruturada e o Scup para dados relacionais, dados que veem que têm como origem bancos de dados relacionais.

O fundamento do ecossistema do sistema Hadoop é o seu sistema de arquivos distribuído, o HDFS o sistema de arquivos distribuídos do Hadoop que a gente vai falar mais sobre ele, mas toda a parte de armazenamento de dados é composta por esse sistema de arquivos.

Depois nós estamos e temos Yarn e aí ele faz o gerenciamento de recursos. Então você imagina um ambiente reduzido. Você tem várias aplicações, vários processos que estão concorrendo com recursos. O Yarn é uma solução do Hadoop, que faz a gestão desses recursos.

Entre essas soluções, onde a gente tem o Hadoop propriamente dito, o reduto. Então a aplicação para processar grandes dados, grandes volumes de dados em um lote, em Batch, é um sistema de processamento de dados distribuídos.
Depois nós temos o Apaches Spark, que é uma aplicação de processamento de dados em tempo real, próximo ao tempo real em memória.

O Apache Pig é uma aplicação de script. A gente vai ver depois lá o Hadoop. Ele é uma linguagem de baixo nível. Você tem que fazer programação em Java.

Com o Apache Pig, você pode desenvolver scripts para criar aplicações map e Reduce.

Depois, nós temos um Mahout, que é uma biblioteca de machine learning para o ecossistema Hadoop.

O Hive que nós vamos estudar no nosso curso é uma solução de DataWarehouse para Big Data ou uma solução de dados estruturados que você pode gerenciar com linguagem muito semelhante ao SQL. Depois, a gente vai ver que a gente vai acabar colocando o DataWarehouse que nós criamos lá na seção de construção de DataWarehouse nós vamos colocar, nós vamos transformar, transportar esse DataWarehouse anterior legado para um DataWarehouse no Hive que vai se transformar num DataWarehouse de big data.

Depois, nós temos aplicações de streaming de processamento contínuo de dados e streaming. Então o Apache kafka e o Spark Streaming, que é uma parte do Spark que nós já falamos aqui.
Porém, ele trata de streaming.

Depois tem várias outras soluções aqui. Mesmo assim, a gente não tem todas. Mas, como eu falei, são todas aplicações cujo objetivo, cuja função era de alguma forma tratar. Elas tratam de dados de aplicações orientadas a dados.

Então, quando a gente fala de Hadoop, a gente está falando também de Map Reduce.
Então, Map Reduce o objetivo é dividir tarefas e processamento de dados em vários nós. Então, a gente está falando de nós, estamos falando de vários servidores, virtualizados ou não.

Então a gente, em vez de ter o processamento de dados em um grande servidor, um servidor robusto, vertical, a gente pega e distribui isso em vários servidores que vão trabalhar, que vão processar esses dados de forma colaborativa. É questão de dividir problemas para conquistar.

Então, você divide o trabalho, você chega a uma solução. Então você divide grandes trabalhos, grandes problemas de dados. Quando a gente fala de Hadoop de MapReduce, estamos falando de grandes volumes de dados, de forma que isso possa ser processado em conjunto em paralelo.

Então, além da questão de estar dividido em vários nos, existem vários desses nós que vão estar trabalhando simultaneamente a outros não. Outros vão esperar, por exemplo, o final da tarefa de mapeamento para iniciar a tarefa de redução, por exemplo.

Então, o fundamento que deu origem ao MapReduce e o Hadoop.
Ele veio. Através do documento, MapReduce que ele trata de processamento de dados simplificado em grandes clusters com muitos logs. Foi publicado em 2004 pelo Google. Aqui você tem o endereço deste documento que você pode consultar, caso você tenha curiosidade, tem interesse em conhecer um pouco mais.
HTTPS://ai.google/research/pubs/pub62

Então o Map Reduce ele é escalável e você pode aumentar ele de forma relativamente simples. Ele é altamente tolerante a falhas. Então, se um nó falhar, provavelmente você vai ter um outro nó lá que vai ter o mesmo conjunto de dados e ele vai seguir o processamento de onde ele parou. Por ele ser tolerante à falha de alta disponibilidade. Ele é confiável. Trabalha no conceito chave valor, um conceito simples de dados em que você tem uma chave e um valor por linha. Não cria gargalos na rede, pois dados não trafegam. O processamento é no nó. Então, isso é um conceito muito importante. Quando a gente está falando de processamento distribuído, o que acontece? Você tem um volume muito grande de dados.Vamos supor que seja um conjunto de dados muito grande, o que vai ser feito: Você vai dividir esses dados e você vai colocar esses dados divididos dentro dos nós. A partir daí, o processamento dos dados vai ser feito dentro de cada um desses nós. Nós não vamos ter mais um grande tráfico de dados entre nós, entre um nó master e um slide, por exemplo. Claro que vai existir um tráfico até você distribuir esses dados, mas o processamento é todo feito dentro do nó.

Então é importante a gente ter o conceito, a gente saber que quando a gente fala de MapReduce e Hadoop. A gente está falando de processamento, em Batch, você não está falando de uma, de um processamento interativo e que você vai rodar uma consulta e vai ter um resultado. Você não está falando de um processamento em tempo real. Você não está falando de streaming. Você está falando de processar grandes volumes em batch Então você tem um volume muito grande, você precisa processar para chegar ao resultado e você não precisa desse resultado e imediatamente pode levar algumas horas, alguns dias para você ter o resultado desse processamento.

Então, claro que isso só é válido se é aplicável quando a gente está falando de fato de grandes volumes de dados, porque não faz sentido você desenvolver um cluster MapReduce com um Hadoop, por exemplo, para processar um gigabyte de dados. Não faz sentido nenhum que ele é feito, Ele é projetado a arquitetura dele para grandes volumes de dados. Como eu já falei, ele é o core dele, fundamento dele de processamento de dados distribuídos. E ele é uma linguagem. Ele usa uma linguagem imperativa, que é Java. 

O que quer dizer isso? Quer dizer que é mais difícil. Você tem que desenvolver um programa, você tem que escrever um programa para rodar uma aplicação Hadoop, diferente, por exemplo, de uma linguagem declarativa como SQL, que você vai lá facilmente e coloca lá a consulta SQL E você declara consultas que ele é você ter já o resultado.
O Hadoop, embora ele tenha outras ferramentas que facilitem o core dele, A forma mais simples de ser utilizada é com uma linguagem imperativa Você desenvolvendo um programa em Java, a gente vai ver como que a gente faz A gente vai ver um pequeno exemplo lá de contagem de palavras.

Outro conceito importante é que os dados podem ser copiados para o sistema de arquivos distribuídos e, uma vez no sistema de arquivos distribuídos no HDFS Eles podem ser acessados por diversos sistemas pelo Hadoop, pelo Hive, pelo Spark. São sistemas diferentes, com propósitos diferentes. Porém, o sistema de arquivos, o banco de dados entre aspas onde eles estão é compartilhado e o mesmo sistema de arquivos distribuído.

E esse sistema de arquivos, como vamos falar mais adiante, Ele não é um sistema de arquivos comum. Ele não é o mesmo sistema de arquivos, por exemplo. Lá onde está rodando o Linux. Fisicamente, claro, ele pode ter uma parte dele lá. Mas, logicamente, ele é um outro sistema de arquivos que tem outra função. Então, ele é um sistema de arquivos feito especificamente para o processamento de grande volumes de dados.

Continuando ainda sobre o MapReduce, o mapeamento é executado em paralelo nos nós. Então vejo aqui que nós temos duas tarefas principais.Depois a gente vai ver que é um pouquinho mais. Mas as duas tarefas principais e a tarefa de mapeamento e de redução.
O que você vai ter no seu cluster?
Você vai ter nós responsáveis pelo mapeamento e nós responsáveis pela redução. Geralmente você terá menos nós para redução.
O que acontece?
O mapeamento pode ser executado, Ele é executado em paralelo pelos nós. Então, quando o mapeamento começa, todos nós aqui eles começam a trabalhar, a processar os dados, os nós de redução, eles vão estar parados. Eles só podem iniciar o processamento quando a etapa de mapeamento terminar. Isso porque isso tem um motivo, porque eles precisam do resultado do mapeamento. Você vai entender isso depois para que eles para que eles iniciem a tarefa de redução.

Existe ainda uma etapa intermediária. Então a gente tem aqui a redução, mas existe uma etapa intermediária, que é o shuffle, que a gente vai entender também depois, mas em detalhes. Existem alguns tipos de tarefa que requerem apenas uma etapa de mapeamento. 

Então, a gente teve aqui uma visão geral, um panorama geral do Hadoop e do ecossistema que compõe o Reduce, que são aplicações orientadas a dados, mantidas pela Fundação Apache.

