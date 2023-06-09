# 2. Pipeline de Dados e o Processo de Engenharia de Dados

## 2.4 Pipeline de Dados x Pipeline ETL

    - Os sistemas de ETL são um tipo de pipeline de dados, pois movem dados de uma origem, transformam os dados e, em seguida, carregam os dados em um destino.
    Mas ETL geralmente é apenas um subprocesso de um pipeline de dados.
    - O termo ETL foi criado em uma época onde normalmente o único destino era um Data Warehouse e o processo era bem menos complexo. Hoje, o ETL faz parte de um processo maior de pipeline de dados.
    - Mas o processo é cada vez mais complexo e hoje podemos ter inúmeros tipos de processamento e inúmeros destinos. Por isso o termo pipeline de dados vem sendo cada vez mais usado.
    - Um pipeline de dados é mais amplo, pois é todo o processo envolvido no transporte de dados de um local para outro, incluindo limpeza, transformação, enriquecimento, segurança, orquestração, integração/ entrega contínua (CI/CD).
    - Um pipeline de dados pode ser composto de vários pipelines ETL, além de tarefas complementares como enriquecimento de dados, gestão de metadados, linhagem de dados entre outras tarefas. Um pipeline de dados pode ser criado para dados em batch (em lote), dados em streaming ou ambos.
    - Pense que o pipeline de dados é uma grande avenida por onde os dados passam indo do ponto A para o ponto B.
    - Um pipeline ETL seria uma parte desse trajeto.

## 2.5 Característica de Pipelines Modernos

Pipelines de dados robustos podem equipar uma empresa adequadamente para obter, coletar, gerenciar, analisar e usar dados com eficiência e então usar os dados para gerar novas oportunidades de mercado e fornecer processos de negócios mais eficientes e econômicos.Os pipelines de dados modernos tornam a extração de informações dos dados coletados rápida e eficiente.

As principais características ao considerar um pipeline de dados incluem:

- Processamento de dados contínuo e extensível.
- A elasticidade e agilidade da nuvem.
- Recursos isolados e independentes para processamento de dados.
- Acesso democratizado a dados e gerenciamento de autoatendimento.
- Alta disponibilidade e recuperação de desastres.

## 2.6 e 2.7 Principais Ferramentas para Construir Pipelines de Dados - Transformação de Dados

- [Apache Beam](https://beam.apache.org/)
- [Airbyte](https://airbyte.com/)
- [Stitch](https://www.stitchdata.com/)
- [Keboola](https://www.keboola.com/)
- [Dremio](https://www.dremio.com/)
- [Fivetran](https://www.fivetran.com/)
- [Dataform](https://dataform.co/)
- [Apache Airflow](https://airflow.apache.org/)
- [Apache Kafka](https://kafka.apache.org/)
- [Apache Spark](https://spark.apache.org/)
- [DBT](https://www.getdbt.com/)
- [AWS Glue](https://aws.amazon.com/pt/glue/)
- [Amazon Athena](https://aws.amazon.com/pt/athena/)

## 2.8 Principais Ferramentas para Construir Pipelines de Dados - Armazenamento e Cloud Computing

- [Databricks](https://www.databricks.com/)
- [Delta Lake](https://delta.io/)
- [Apache Hadoop](https://hadoop.apache.org/)
- [Apache Hive](https://hive.apache.org/)
- [Snowflake](https://www.snowflake.com/en/)
- [Google BigQuery](https://cloud.google.com/bigquery)
- [Amazon S3](https://aws.amazon.com/pt/s3/)
- [Amazon Redshift](https://aws.amazon.com/pt/redshift/)
- [Segment](https://segment.com/)
- [Azure Data Factory](https://azure.microsoft.com/pt-br/products/data-factory/)

## 2.9 Principais Ferramentas para Construir Pipelines de Dados - RealTime Analytics

- [Tableau](https://www.tableau.com/)
- [Amazon Kinesis](https://aws.amazon.com/pt/kinesis/)
- [Metabase](https://www.metabase.com/)
- [Looker Studio](https://lookerstudio.google.com/overview)
- [Apache Flink](https://flink.apache.org/)
- [Apache Druid](https://druid.apache.org/)
- [Apache Superset](https://superset.apache.org/)
- [Azure Synapse Analytics](https://azure.microsoft.com/pt-br/products/synapse-analytics/)
- [Redash](https://redash.io/)
- [Microstrategy](https://www.microstrategy.com/en)
- [Dataedo](https://dataedo.com/)
- [Power BI](https://powerbi.microsoft.com/pt-br/)
- [Presto](https://prestodb.io/)
- [Terraform](https://www.terraform.io/)

## 2.10 Ciclo de Vida da Engenharia de Dados - Diagrama

|ETAPA DSCIENTIST| FUNÇÃO DENGINEER|
| --- | --- |
|Data Preparation | Pair programming|
|Data Preparation| Use Data & SQL as common language |
| Evaluation|Testing |
| Evaluation |Monitoring features|
|Create packages: data preparation, modeling and prediction | Deployment|
| PRODUCT SPRINT|PRODUCT SPRINT |

A(Pair programming) -> B(Use Data & SQL as common language) ->C(Testing) -> D(Monitoring features) -> E(Deployment) -> F[PRODUCT SPRINT]

## 2.11 Ciclo de Vida da Engenharia de Dados - Fonte de Dados

Fontes de Dados (Batch e Streaming) -> | Ingestão de Dados | Transformação e Enriquecimento | Carga e Uso dos Dados | -> Analytics, Machine Learning e IA, Relatórios e Dashboards

Arquitetura de Dados, Gestão de Dados e Metadados, Orquestração, Segurança, CI/CD, DataOps

## 2.12 Ciclo de Vida da Engenharia de Dados - Ingestão de Dados

Uma vez que a empresa tem  definido as fontes de dados, ela então passa para o próximo componente que é a ingestão de dados. A ingestão de dados visa você tirar os dados da fonte (da origem) e fazer a ingestão na sua plataforma de dados.

Essa plataforma de dados pode ser no ambiente local com Apache Hadoop, eventualmente um data Lake, pode ser no ambiente em nuvem com Snowflake, com Amazon Redshift ou mesmo Amazon S3.  

Ou seja eu vou precisar de uma ferramenta que vai extrair os dados e fazer a ingestão no meu ambiente de dados da minha plataforma de dados, para que eu possa seguir em frente no meu processo criando os pipelines por exemplo para transformação, enriquecimento, uso de dados e assim por diante dependendo do tipo de fonte também fica fácil compreender que a ingestão de dados vai requerer os conectores, se eu tiver mais de uma fonte simultânea vou precisar extrair os dados de maneira simultânea, e depois realizar algum tipo de merge ou seja vou ter combinar os dados para então seguir adiante no processo.

Uma ferramenta como airbyte por exemplo vai buscar esses dados, faz a ingestão no sistema de armazenamento, já aplica a transformação e já leva adiante.

Então a ingestão de dados visa tirar os dados da fonte e levar esses dados para sua plataforma de dados, que é onde a "brincadeira" vai acontecer.

## 2.15 Ciclo de Vida da Engenharia de Dados - Armazenamento

Os dados são ativos digitais, eles têm que existir em algum lugar. Não pode existir no além ou no Limbo, então quando eu extrai os dados da fonte e eu fizer a ingestão na plataforma de dados para poder aplicar a transformação e enriquecimento; onde estarão os dados nesse momento? Em um sistema de armazenamento.

Ou seja, eu preciso de um armazenamento no mínimo intermediário para que eu possa colocar os dados ali, os dados vão residir naquele armazenamento para então aplicar transformação com linguagem SQL ou usar linguagem Python ou usar alguma outra ferramenta.

Uma vez que os dados tenham sido transformados, enriquecidos eu posso tirar os dados desse armazenamento e então levar para o destino. Esse armazenamento pode ser um Data Lake dentro da empresa, pode ser um data Store que é o sistema de
armazenamento, pode ser um data Warehouse. Depende de como a empresa vai construir a sua arquitetura.
Se a empresa decide extrair os dados do formato bruto e fazer a ingestão no formato bruto para depois poder limpar
transformar, o armazenamento provavelmente será um Data Lake.

Eventualmente a empresa pode extrair os dados, e já aplicar alguma transformação e carregar para DataWarehouse se os dados são mais simples e as transformações forem mais simples, isso também é uma arquitetura totalmente viável.

Se os dados são gerados em tempo real você pode extrair os dados no momento que eles são gerados, você já aplica a limpeza, transformação isso pode ficar até na memória do computador se o volume de dados não é tão grande você usa um cluster para um ambiente distribuído, isso fica na memória do ambiente distribuído no cluster, também é possível então você extraiu, jogou na memória do cluster, aplicou a transformação, já alimentou um dashboard lá com o sistema qualquer de analíticos, já entregou o resultado mas isso tem também outro lado é uma infraestrutura mais complexa para você manter, vai precisar de profissionais ainda mais capacitados, vai funcionar muito bem para um propósito, você não pode extrair todos os dados manter tudo no cluster de maneira simultânea o tempo inteiro dependendo do volume.

Talvez isso não seja algo factível, visto que temos sempre que canalizar cada cenário a necessidade da empresa como a empresa vai usar os dados no dia a dia.

## 2.21 [PDF] O que é CI/CD (Integração Contínua/ Entrega Contínua)

CI/CD (integração contínua e entrega contínua) é uma abordagem de desenvolvimento de  software  em  que  todos  os  desenvolvedores  trabalham  juntos  em  um  repositório compartilhado de códigos, à medida que as alterações são feitas, há um processo de build automatizado  para  detectar  problemas  de  código.  O  resultado  é  um  ciclo  de  vida  de desenvolvimento mais rápido e uma taxa de erro menor.

Um pipeline de CI/CD automatiza os dois processos a seguir para um processo de entrega de software de ponta a ponta:

- Integração contínua para criação e teste de código automatizado.
- Entrega contínua (ou implantação contínua) para lançamentos de código

Um pipeline de CI/CD combina criação, teste e implantação de código em um processo contínuo,  garantindo  que  todas  as  alterações  no  código  do repositório principal  possam  ser liberadas para produção. Um pipeline automatizado de CI/CD evita erros manuais e permite iterações rápidas de software. O conceito de CI/CD está cada vez mais sendo aplicado em Engenharia de Dados criando o que hoje chamamos de DataOps, com a operação contínua da plataforma de dados.

## 2.22 Ciclo de Vida da Engenharia de Dados - CI/CD

 Nasceu em Eng de Software -DevOps, para que tenham controle e segurança sobre mudanças.

## 2.23 Ciclo de Vida da Engenharia de Dados - DataOps

Conceito de DataOps vem ganhando conceito no mercado, a partir do momento em que empresas vêm investindo em Dados.

## [2.25 - Quiz](https://github.com/MariiMartins/EngenhariaDados/blob/e0586d7a13df852874632d8b74c1b79e9a748b39/Fundamentos%20da%20Eng%20Dados%20-%20DSA/QUIZ/2.25%20-%20Quiz.md)

<!--
[Diagramas com MD](https://support.typora.io/Draw-Diagrams-With-Markdown/)
-->
