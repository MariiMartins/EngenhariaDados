# 2. Pipeline de Dados e o Processo de Engenharia de Dados

<!--
## <details> <summary> 2.4 Pipeline de Dados x Pipeline ETL </summary>
    - Os sistemas de ETL são um tipo de pipeline de dados, pois movem dados de uma origem, transformam os dados e, em seguida carregam os dados em um destino. 
    Mas ETL geralmente é apenas um subprocesso de um pipeline de dados.
    - O termo ETL foi criado em uma época onde normalmente o único destino era um Data Warehouse e o processo era bem menos complexo. Hoje ETL faz parte de um processo maior de pipeline de dados.
    - Mas o processo é cada vez mais complexo e hoje podemos ter ínumeros tipos de processamento e inúmeros destinos. Por isso o termo pipeline de dados vem sendo cada vez mais usado.
    - Um pipeline de dados é mais amplo, pois é todo o processo envolvido no transporte de dados de um local para outro, incluindo limpeza, transformação, enriquecimento, segurança, orquestração integração/ entrega contínua (CI/CD).
    - Um pipeline de dados pode ser composto de vários pipelines ETL, além de tarefas complementares como enriquecimento de dados, gestão de metadados, linhagem de dados entre outras tarefas. Um pipeline de dados pode ser criado para dados em batch (em lote), dados em streaming ou ambos.
    - Pense que o pipeline de dados é uma grande avenida por onde os dados passam indo do ponto A para o ponto B.
    - Um pipeline ETL seria uma parte desse trajeto.
</details>        

## <details> <summary> 2.5 Característica de Pipelines Modernos </summary>

    Pipelines de dados robustos podem equipar uma empresa adequadamente para obter, coletar, gerenciar, analisar e usar dados com eficiência e então usar os dados para gerar novas oportunidades de mercado e fornecer processos de negócios mais eficientes e econômicos.Os pipelines de dados modernos tornam a extração de informações dos dados coletados rápida e eficiente.
    As principais características ao considerar um pipeline de dados incluem:
        - Processamento de dados contínuo e extensível.
        - A elasticidade e agilidade da nuvem.
        - Recursos isolados e independentes para processamento de dados.
        - Acesso democratizado a dados e gerenciamento de autoatendimento.
        - Alta disponibilidade e recuperação de desastres.
</details>

## <details><summary> 2.6 e 2.7 Principais Ferramentas para Construir Pipelines de Dados - Transformação de Dados </summary>

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
</details>

## <details> <summary> 2.8 Principais Ferramentas para Construir Pipelines de Dados - Armazenamento e Cloud Computing
</summary>

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

</details>

## <details> <summary> 2.9 Principais Ferramentas para Construir Pipelines de Dados - RealTime Analytics </summary>

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

</details>

## <details><summary> 2.10 Ciclo de Vida da Engenharia de Dados - Diagrama </summary>

|ETAPA DSCIENTIST| FUNÇÃO DENGINEER|
| --- | --- |
|Data Preparation | Pair programming|
|Data Preparation| Use Data & SQL as common language |
| Evaluation|Testing |
| Evaluation |Monitoring features|
|Create packages: data preparation, modeling and prediction | Deployment|
| PRODUCT SPRINT|PRODUCT SPRINT |

A(Pair programming) -> B(Use Data & SQL as common language) ->C(Testing) -> D(Monitoring features) -> E(Deployment) -> F[PRODUCT SPRINT]

</details>

## <details><summary> 2.11 Ciclo de Vida da Engenharia de Dados - Fonte de Dados </summary>

Fontes de Dados (Batch e Streaming) -> | Ingestão de Dados | Transformação e Enriquecimento | Carga e Uso dos Dados | -> Analytics, Machine Learning e IA, Relatórios e Dashboards

Arquitetura de Dados, Gestão de Dados e Metadados, Orquestração, Segurança, CI/CD, DataOps
</details>

## <details><summary> 2.12 Ciclo de Vida da Engenharia de Dados - Ingestão de Dados </summary>
    Uma vez que a empresa tem  definido as fontes de dados, ela então passa para o próximo componente que a ingestão de dados. A ingestão de dados Visa você tirar os dados da fonte (da origem) e fazer a ingestão na sua plataforma de dados. 
    Essa plataforma de dados pode ser no ambiente local com Apache Hadoop, eventualmente um data Lake, pode ser no ambiente em nuvem com Snow Flake, com Amazon Redshift ou mesmo Amazon S3.  
    Ou seja eu vou precisar de uma ferramenta que vai extrair os dados e fazer a ingestão no meu ambiente de dados da minha plataforma de dados, para que eu possa seguir em frente no meu processo criando os pipelines por exemplo para transformação, enriquecimento, uso de dados e assim por diante dependendo do tipo de fonte também fica fácil compreender que a ingestão de dados vai requerer os conectores, se eu tiver mais de uma fonte simultânea vou precisar extrair os dados de maneira simultânea, e depois realizar algum tipo de merge ou seja vou ter combinar os dados para então seguir adiante no processo.
    Uma ferramenta como airbyte por exemplo vai buscar esses dados faz a ingestão no sistema de armazenamento, já aplica a transformação e já leva adiante.
    Então a ingestão de dados Visa tirar os dados da fonte e levar esses dados para sua plataforma de dados que é onde a "brincadeira" vai acontecer.
</details>
-->

## Tópico
<!-- 
2.13) Ciclo de Vida da Engenharia de Dados - Transformação e Enriquecimento
2.14) Ciclo de Vida da Engenharia de Dados - Carga e Uso dos Dados
2.15) Ciclo de Vida da Engenharia de Dados - Armazenamento
2.16) Ciclo de Vida da Engenharia de Dados - Analytics, Machine Learning, IA, Relatórios e Dashboards
2.17) Ciclo de Vida da Engenharia de Dados - Arquitetura de Dados
2.18) Ciclo de Vida da Engenharia de Dados - Gestão de Dados e Metadados
2.19) Ciclo de Vida da Engenharia de Dados - Orquestração
2.20) Ciclo de Vida da Engenharia de Dados - Segurança
2.21) [PDF] O que é CI/CD (Integração Contínua/ Entrega Contínua)
2.22) Ciclo de Vida da Engenharia de Dados - CI/CD 
2.23) Ciclo de Vida da Engenharia de Dados - DataOps
2.24) Ciclo de Vida da Engenharia de Dados - Conclusão
2.25) Quiz
-->

<!--
[Diagramas com MD](https://support.typora.io/Draw-Diagrams-With-Markdown/)
-->