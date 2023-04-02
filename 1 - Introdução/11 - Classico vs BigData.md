11. Classico VS. BigData

Nós falamos rapidamente da diferenciação entre o Data Warehouse clássico e o Data Warehouse Big Data que são os Data Lakes e aqui a gente vai trazer isso. A gente vai estudar isso um pouco mais aprofundado. A gente vai entender isso um pouco melhor. Algumas observações aqui que o Data Warehouse tradicional ele não é substituído pelo  Data Lake.

Então o Data Lake atual, o Data Lake Big Data sobre HDFS não é uma substituição do Data Warehouse clássico.
Da mesma forma que os bancos de dados não substituem os modelos relacionais, a gente está falando aqui de tecnologias diferentes para problemas de dados diferentes problemas de dados que não existiam anteriormente foram criados devido a esse fenômeno que nós chamamos, que nós conhecemos como Big Data, e por isso foram criadas soluções diferentes. Porém, os problemas antigos continuam e você ainda precisa manter transações. A empresa ainda precisa manter, se manter funcionando, ela ainda precisa emitir notas, enfim. Então, para isso ainda existe o armazém de dados, Ainda existe o modelo relacional. Ainda você precisa produzir informação limpa para a produção de cubos, dashboards, Enfim, então ainda se usa o Data Warehouse tradicional, então são tecnologias diferentes para problemas diferentes.

Então, aqui este infográfico você também encontra ele inteiro para baixar no ambiente do curso. Então aqui se faz a comparação entre o armazém de dados clássico e o armazém de dados Big Data.
Então, primeiro, com relação a velocidade no modelo clássico, geralmente você tinha em questão de velocidade D+1. Isso quer dizer o quê? Que os sistemas transacionais produziam dados durante o dia, a geralmente à noite, esses dados eram extraídos, tratados e carregados no armazém de dados gerencial, ou seja, a velocidade era D+1. Você tinha a informação disponível para os executivos, os gerentes da empresa no outro dia, depois de mais um dia.

Em Big Data, o que a gente tem? Nós temos streaming de dados, ou seja, aplicações analisando dados em tempo real enquanto elas são produzidas. E nós temos Batch, aplicações em Batch que processam grandes volumes de dados, volumes de dados normalmente muito superiores ao que eram produzir, que eram tratados no armazém clássico.

Com relação ao volume. Então, um grande armazém de dados clássico tratava de terabytes de dados. Um projeto de big data, vai tratar de petabytes de dados, variedade.

O armazém de dados clássico, ele processava, armazenava apenas dados estruturados, com uma estrutura rígida definida entre linhas e colunas. Em Big Data, nós temos dados não estruturados, semi-estruturados e temos também dados estruturados.

Com relação a arquitetura. No modelo clássico, onde tinha uma arquitetura centralizada vertical, ou seja, você tinha um grande servidor, um servidor especializado, um appliance.Que fazia todo o processamento dos dados em Big Data a gente viu lá que a gente tem os clusters.Nós temos uma aplicação distribuída em vários nós.

Do ponto de vista de crescimento, de escalabilidade. Se você precisar crescer a aplicação aqui, você, o que você fazia? Você colocava mais memória, se aumentava a CPU, você aumentava o disco.Aqui no modelo Big Data, o que você faz? Você adiciona mais um nó ou você levanta mais uma máquina virtual no  seu hack, por exemplo. Claro que aqui também (clássico) você pode aumentar a sua arquitetura, adicionando mais memória, mais CPU, mais processamento. Mas, de uma maneira geral, você aumenta a sua capacidade, adicionando nós.

O tráfego de dados. No modelo clássico, ele era entre a aplicação cliente e o servidor, então você tinha lá o grande servidor com os clientes. O maior tráfego de dados ocorria aqui. Em Big Data, o maior tráfego de dados ocorre entre os servidores, não entre os servidores, supondo que a lista de clientes não entre os servidores e o cliente.
O modelo clássico. Ele carregava dados limpos e que se sabia que já tinha valor. Então, tinha um processo extenso de transformação de dados. No modelo Big Data.Todo dado é coletado e carregado para dentro do Data Lake, depois se avalia se aquilo tem valor, depois se faz tratamento.

O processo de carga a gente já falou rapidamente aqui ele era de extração, transformação e carga (ETL – Classico)
Aqui ele era de extração, carga e transformação. (ELT – BigData) a transformação é feita depois que os dados já estão no armazém de dados e já estão dentro do Data Lake.

O hardware aqui especializado é um appliance (Classico) e aqui (BigData) é  chamado commodity hardware que a gente já estudou.

O que a gente já entendeu? O conceito, que é um hardware comum, o equipamento comum.
Então os Data Lakes são armazéns de dados corporativos. Eles podem ser estruturados sobre HDFS, então HDFS é o sistema de arquivos distribuído, que faz parte do ecossistema Hadoop da fundação Apache que a gente vai estudar, bastante. Dados no DataLake que são carregados no formato nativo, não são transformados da maneira que eles foram produzidos eles são carregados. Eles podem ter uma área de descarga no formato ativo, uma área de consumo onde os dados já estão tratados, eles podem ter cópias temporárias, então vamos entender o que quer dizer isso.

Então, vejo aqui. 
Eles têm as várias fontes de produção de dados, a captura, que pode ser por streaming, enquanto os dados são produzidos ou pode ser em Batch aí o processo de ingestão todo dado é colocado da maneira bruta, da maneira que é criado dentro do Data Lake e depois o que pode acontecer? Pode ocorrer uma área onde são feitas cópias temporais, se manter instantâneos, snapshots dos dados para você manter isso de forma histórica. Então isso pode ser copiado. Para uma outra área do Data Lake e pode ter áreas específicas onde o dado é transformado para, por exemplo, fornecer relatórios de BI para criar modelos para machine learning, para fornecer informação e dados para o cientista de dados, por exemplo, para fornecer dados de integração para outras aplicações. Então, essa estrutura básica que você encontra em um DataLake BigData normalmente implementado sobre a cadeia FS.