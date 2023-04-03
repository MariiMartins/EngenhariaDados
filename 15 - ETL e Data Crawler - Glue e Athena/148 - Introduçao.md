148. Introdução
Bem vindo a mais esta sessão e aqui o nosso assunto vai ser ETL também se aplica à ELT.

Basicamente no mundo de dados. Os dados não são produzidos num formato ideal para que eles sejam processados ou que eles sejam analisados. E, muitas vezes, diferentes tipos de análise requerem formatos diferentes.

Uma outra questão é que, além de formatos diferentes, os dados precisam estar em estruturas diferentes. E, além disso, há alguns tipos de processamento, alguns tipos de análise requerem que dados de diferentes fontes ou de diferentes formas de produção sejam consolidados.

Então, existe um requisito na área de engenharia de dados de você carregar dados de uma fonte para outra ou de várias fontes, para uma terceira fonte ou para uma quarta fonte. E este processo normalmente ele envolve ou ele tem um pré-requisito de que esses dados sofram transformação. Eles sejam transformados durante esse processo, seja não só do ponto de vista da estrutura desses dados, na forma como eles se apresentam, como também com relação ao tipo de dado.

Então, por exemplo, ele pode chegar num formato JSON e ele ser transformado, por exemplo, para um formato ORC, só para citar um exemplo.

Então, nessa seção aqui, o nosso objetivo é falar um pouco de transformação de dados de carga e transformação de dados. E para isso a gente vai utilizar uma ferramenta do AWS, que é o Glue.
Você vai ver que é uma ferramenta bastante poderosa, com vários recursos e por isso a gente vai utilizar que ela durante a nossa parte prática.
Então, o Glue é um serviço de gerenciamento de ETL e ele é baseado no Spark.

Por que ele é baseado no Spark? Porque o Spark é uma ferramenta que tem uma performance muito boa para esse processo de transformação de dados.
Quando a gente fala em Big Data, por exemplo, em construir ou manter um destaque, o que a gente precisa? A gente precisa do schema dos dados na origem e de destino.

A gente fala de schema que está falando de metadados. A gente tá falando da definição desses dados. Se você olhar, por exemplo, um banco de dados, uma tabela de um banco de dados, eu tenho um schema, quais são as colunas, quais são os tipos, quais são as restrições de integridade ou mesmo um formato mais simples, um formato como acessível, de onde eles têm, uma vez que eles têm uma, uma estrutura.

Então você precisa conhecer o schema dos dados na origem e no destino.

Você precisa conectar a origem e o destino, onde você vai precisar fazer provavelmente alguns tipos de transformação durante esse processo, em que os dados saem da origem e chegam até o destino.

Então, uma das ferramentas que o Glue oferece é um crawler. Então, o crawler é uma ferramenta que permite que você faça uma conexão com fontes de dados. Ele vai lá nessa fonte de dados com essa conexão que você definiu e ele vai descobrir o schema, a estrutura desses dados de forma automática.
Você provavelmente já ouviu falar de um crawler web, por exemplo, que ele vai numa página da web e descobre lá informações. Aqui estamos falando de um crawler de dados.Então, em vez de você, tem que ir lá, abrir os dados, conectar os dados para descobrir a sua estrutura, sua definição, seus metadados o crawler faz isso para você e depois que você executa o crawler, ele cria esses metadados no Glue, que é o chamado Data Catalog, ou um catálogo de dados.

E esse catálogo de dados ele pode ser compartilhado em várias ferramentas do AWS. Então você vai ter oportunidade de usar o crawler.

Uma outra ferramenta do Glue e o connector, o connector ele tem um repositório de informações necessárias para que sejam feitas conexões com fontes de dados, por exemplo, uma conexão com JDBC, ODBC, enfim.

Bom, e depois a gente tem o Glue Job, o Glue Job é um processo de ETL.
Então, se você já tem a origem dos dados, você já tem a definição desses dados que o Crawler descobriu, se você já tem o schema desses dados, você está pronto para transformar esses dados.

Então no Glue você constrói esse processo. Você pode fazer ele visualmente ou codificando, escrevendo o código na mão.
Então, no processo de ETL, você vai ter a origem de onde os dados vão surgir.
Você vai ter uma ou mais transformações e você vai ter os destinos para onde esses dados vão. E esse job ele pode ser executado sob demanda, ou seja, quando você precisar, você executa. Ele pode ser agendado para ser executado periodicamente, ou ele pode ter gatilhos que vão disparar automaticamente.

O processo é o Data Catalog ou catálogo de dados.
O que ele é? Ele é um repositório de metadados, então, o catálogo ele não vai ter os dados propriamente dito. Ele tem apenas a definição dos dados.
Um elemento principal do catálogo de dados é o data base. Ele tem aqui o nome de banco de dados, mas ele não é um banco de dados na definição que a gente conhece, de um banco de dados relacional, um database aqui no catálogo, ele é simplesmente um agrupamento lógico das tabelas.

Então, quando você executa o crawler e ele descobre que um determinado local lá, por exemplo, existem dez tabelas. Ele precisa agrupar logicamente essas tabelas, porque elas fazem parte de um mesmo problema de negócio.
Nessas tabelas estão relacionadas e a forma de agrupar isso é através de um database, então o também não cria, ele não carrega, não modifica os dados.
Ele é apenas uma referência, uma referência.

E os tables, como eu já expliquei ele representa os metadados ou tabulares que foram encontrados pelo crawler.

Mas é importante a gente entender aqui que o catálogo de dados ele não vai carregar os dados ou tirar os dados da sua fonte original. Os dados vão continuar lá da sua fonte original. Se você quiser mudar esses dados, ao transformar esses dados, a gente precisa criar um job, que é o que a gente vai fazer na parte que a gente falou ali no slide anterior. Então, o catálogo é apenas uma referência a esses dados.
