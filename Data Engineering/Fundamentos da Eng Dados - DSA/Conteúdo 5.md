# 5. Data Warehouse, Data Lake e Data Lakehouse

## 1 e 2. Como Implementar um Data Warehouse

Existem várias etapas para implementar um DW. Aqui estão elas:

- Identificação de Requisitos: Reunir os requisitos de negócio e de dados para determinar o que será incluído no DW.
- Projeto e Arquitetura: Definir a arquitetura do DW, incluindo a forma como os dados serão armazenados e gerenciados.
- Integração: Integrar os dados de várias fontes diferentes em um único local, geralmente usando ferramentas de ETL.
- Construir um DW: Utilizar a arquitetura projetada para construir o DW usando ferramentas de banco de dados ou plataformas de DW em nuvem.
- Cargas de Dados: Carregar os dados integrados, limpos e processados no DW.
- Agendar Atualizações: Configurar as atualizações automáticas para que os dados sejam atualizados regularmente (carga diária, semanal, mensal, etc..)
-Acesso e Segurança: Fornecer acesso autorizado aos dados do DW através de relatórios, visualizações e consultas para que os usuários possam obter insights.
- Monitoramento: Monitorar a performance do DW e realizar manutenção regular para garantir que ele esteja funcionando corretamente e atendendo às necessidades dos usuários.
- Usar Data Marts: Os Data Marts são DWs departamentais, em geral com volume de dados menor. O uso de Data Marts pode evitar problemas de performance e segurança de acesso aos dados.
- Manutenção do Modelo de Dados: Revisar periodicamente o modelo e fazer alterações conforme mudanças no cenário de negócios.

## 3 e 4. Como Implementar um Data Lake

Existem várias etapas para implementar um Data Lake. Aqui estão elas:

1. Identificar os Requisitos: Reunir os requisitos de negócios e dados para determinar o que será incluído no DL.
2. Escolher uma Plataforma: Podemos usar o HDFS para uma implementação local ou uma plataforma em nuvem, como o Amazon S3, Microsoft Azure Data Lake Storage ou Google Cloud Storage.
3. Integração: Ao invés de usar o ETL (Extração, Transformação, Carga) como no caso do DW, com Data Lakes usamos ELT (Extração, Carga,Transformação).
4. Armazenamento: A próxima etapa é armazenar os dados  integrados no Data Lake, geralmente em formato bruto ou semi-estruturado.
5. Agendamentos: Configurar as atualizações automáticas para que os dados sejam carregados regularmente.
6. Acesso: Fornecer acesso aos dados do DL através de ferramentas de análise, como o Apache Hive ou o Apache Spark.
7. Governança de Dados: Garantir a qualidade e a confiabilidade dos dados armazenados no DL, usando ferramentas de governança de dados.
8. Monitoramento: Monitorar a performance do DL e realizar manutenção regular para garantir que ele esteja funcionando corretamente e atendendo às necessidades dos usuários.

## 5. Como Implementar um Data Lakehouse

Um Data Lakehouse é uma combinação de um Data Lake e um Data Warehouse, que combina a flexibilidade e escalabilidade de um Data Lake com a governança e performance de um Data Warehouse.

A implementação de um Data Lakehouse envolve algumas etapas semelhantes às de um Data Lake e um Data Warehouse. As etapas gerais incluem:

1. Identificar os Requisitos: Reunir os requisitos de negócios e dados para determinar o que será incluído no Data Lakehouse.
2. Escolher uma Plataforma: O Data Lakehouse já nasceu no ambiente em nuvem e plataformas como o Azure Synapse Analytics, Google BigQuery, Dremio, Databricks ou Snowflake são opções.
3. Integrações: Integrar os dados de várias fontes diferentes usando ferramentas de ETL ou de integração de dados, para atender a diferentes formatos e estruturas.
4. Armazenamento: Armazenar os dados integrados no Data Lakehouse, geralmente em formato bruto, semi-estruturado ou estruturado e com a capacidade de lidar com grande volume de dados.
5. Governança de Dados, Atualizações e Monitoramento: Assim como o DW e Data Lake.

## 6. Vantagens e Desvantagens

Data Warehouse - Vantagens:

- Dados estruturados e limpos, o que facilita a análise e geração de relatórios.
- Performance de consultas e relatórios é geralmente melhor devido a otimização dos dados.
- Governança de dados mais robusta, garantindo a qualidade e confiabilidade dos dados.
- Maior capacidade de suportar demandas de negócios e análise avançada.

Data Warehouse - Desvantagens:

- Pode ser caro e complexo de implementar e manter.
- Exige um processo de limpeza e modelagem de dados rigoroso antes da carga de dados.
- Restringe a capacidade de armazenar grandes volumes de dados não estruturados.
- Pode ser limitado em lidar com dados em tempo real ou com fontes dinâmicas e não estruturadas.

Data Lake - Vantagens:

- Capaz de armazenar grandes volumes de dados não estruturados e semiestruturados.
- Flexível para lidar com diferentes formatos de dados e fontes.
- Escalável para lidar com grandes volumes de dados.
- Permite análise avançada e aplicações de Big Data, Machine Learning e IA.

Data Lake - Desvantagens:

- Governança de dados menos robusta comparando a um DW, o que pode levar a problemas de qualidade e confiabilidade dos dados.
- Performance de consultas e relatórios pode ser menor devido à falta de otimização dos dados.
- Pode ser caro e complexo de implementar e manter.
- Depende de ferramentas adicionais para limpeza e modelagem de dados antes da análise.

Data Lakehouse - Vantagens:

- Combina as vantagens de Data Warehouse e Data Lakes, fornecendo a capacidade de armazenar grandes volumes de dados não estruturados e semi-estruturados, além de garantir uma boa governança e performance em consultas e relatórios.
- Flexibilidade para lidar com diferentes formatos de dados e fontes.
- Escalável para lidar com grandes volumes de dados.
- Permite análise avançada e aplicações de BigData, Machine Learning e IA.

Data Lakehouse - Desvantagens:

- Pode ser caro e complexo de implementar e manter, devido à necessidade de conhecimento especializado e uma equipe multidisciplinar.
- Depende de ferramentas adicionais para limpeza e modelagem de dados antes da análise.
- Ainda é um conceito recente no mercado e necessita de evolução e maturidade.

## 7. Enterprise Data Hub

## 8. Arquitetura Data Mesh

Data Mesh é uma abordagem para construir uma arquitetura de dados descentralizada, através de um design de autoatendimento orientado a domínio (área de negócio).

A proposta principal é dimensionar os dados por descentralização orientada por domínio.

Com Data Mesh a responsabilidade pelos dados usados nas análises é transferida da equipe de dados central para as equipes de domínio, apoiada por uma equipe de plataforma de dados que fornece uma plataforma independente de domínio.

## 9. [PDF] Demonstração Prática 2 - Implementando um Data Lakehouse

## 10. Demonstração Prática 2 - Por que usamos o Data Lakehouse?

## 11. Demonstração Prática 2 - Arquitetura da solução de um Data Lakehouse

## 12. Demonstração Prática 2 - Definindo o ambiente na Nuvem para o Data Lakehouse

## 13. Demonstração Prática 2 - Trabalhando com o Data Lakehouse

## [14. Quiz](https://github.com/MariiMartins/EngenhariaDados/blob/e0586d7a13df852874632d8b74c1b79e9a748b39/Fundamentos%20da%20Eng%20Dados%20-%20DSA/QUIZ/5.14%20-%20Quiz.md)
