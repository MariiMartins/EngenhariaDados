<!--
# 3. Sistemas de Armazenamento de Dados

## 3.1 Introdução

## 3.2 O "V" de Volume em Big Data

- Como vamos armazenar grandes conjuntos de dados?
- Como vamos acessar grandes conjuntos de dados armazenados?
- Vamos realmente armazenar tudo?

## 3.3 Como Armazenamos Big Data?

Em linhas gerais o armazenamento pode ser feito com base na seguinte regra:
- Os dados são estruturados ou podem ser estruturados antes do armazenamneto? *usamos um Data Warehouse*
- Os dados não estruturados ou não podem ser estruturados antes do armazenamento? *usamos um Data Lake ou um Data Store"

## 3.4 Bancos de Dados Relacionais x Bancos de Dados NoSQL - Parte 1/2

- Bancos de Dados Relacionais são bancos de dados estruturados e com schema (organização dos dados) bem definido.
O schema é definido e criado antes do armazenamneto dos dados.

Um Data Warehouse, por exemplo, é criado com alguma tecnologia de banco relacional como SGBD (Sistema Gerenciador de Banco de Dados) Oracle, IBM DB2, Microsoft SQL Server, MySQL, PostgreSQL e muitos outros.
Em um banco de dados relacional os dados são organizados em tabela.

## 3.5 Bancos de Dados Relacionais x Bancos de Dados NoSQL - Parte 2/2

-Bancos de dados não relacionais (NoSQL) partem do principio que os dados podem ser semi ou não estruturados e que outros tipos de relacionamentos podem existir entre os dados.

Podemos usar Bancos de Dados Não Relacionais (NoSQL) para construir Data Lakes e Data Stores (Data Lakes e Data Stores são conceitos, como veremos mais adiante).
Normalmente não precisamos definir o schema antes do armazenamneto ou o schema é definido no momento do armazenamneto dos dados.
Existem diversos tipos de Banco de Dados NoSQL

## 3.6 Definindo Data Warehouses - Parte 1/2

Um Data Warehouse (DW) é um sistema de armazenamneto que conecta e harmoniza grandes quantidades de dados de muitas fontes diferentes.

Seu objetivo é alimentar a inteligencia de negócios (Business Intelligence), relatórios e análises e oferecer suporte aos requisitos de negócio, para que as empresas possam transformar seus dados em insights e tomar decisões inteligentes baseadas em dados.

Os DWs armazenam dados atualis e históricos em um único lugar e atuam como a única fonte de informações confiáveis para uma organização.

Os dados fluem para um DW a partir de sistemas transacionais (como ERP e CRM), bancos de dados e fontes externas, como sistemas de parceiros, dispositivos de internet das coisas (IoT), aplicativos de mídia social - geralmente em uma cadência regular.

O surgimento da computação em nuvem causou uma mudança no cenário.
Nos últimos anos, os locais de armazenamento de dados mudaram da infraestrutura local tradicional para vários locais, incluindo nuvem privada e nuvem públixa.

O schema deve ser definido antes do processo de armazenamento dos dados.

## 3.7 Definindo Data Warehouses - Parte 2/2

Os DWs modernos são projetados para lidar com dados estruturados e não estruturados, como vídeos, aqruivos de imagem e dados de sensor (embora Data Lakes ainda sejam opçoes melhores para dados não estruturados).

Alguns aproveitam a análise integrada e a tecnologia de banco de dados in-memory (que mantém o conjunto de dados na memória do computador em vez de no armazenamneto em disco) para fornecer acesso em tempo real a dados confiáveis e impulsionar a tomada de decisão.

Sem DW é muito dificil combinar dados de fontes heterogêneas, garantir que estejam no formato certo para análise e obter uma visão atual e de longo alcance dos dados ao longo do tempo.

## 3.8 Benefícios do DW

- *Melhor Análise de Negócios:* com o DW, os tomadores de decisão têm acesso a dados de várias fontes e não precisam mais tomar decisões com base em informações incompletas.

- *Consultas mais Rápidas:* os DWs são construídos especificamente para recuperação e análise rápida de dados. Com um DW, você pode consultar rapidamente grandes quantidades de dados consolidados com pouco ou nenhum suporte de TI.

- *Melhoria na Qualidade dos Dados:* antes de serem carregados no DW, os dados passam por um processo de limpeza garantindo quue os dados sejam transformados em um formato consistente para apoiar análises - e decisões - com base em dados precisos e de alta qualidade.

- *Visão Histórica:* ao armazenar dados históricos ricos, um data warehouse permite que os tomadores de decisão aprendam com tendências e desafios passados, façam previsões e conduzam a melhoria contínua dos negócios.

## 3.9 Definindo Data Lakes - Parte 1/2

Um Data Lake é um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala. Podemos armazenar os dados como estão na fonte, sem ter que primeiro estrutura-los e executar diferentes tipos de análises - de paineis e visualizacoes a processamento de Big Data, análise em tempo real e aprendizado de máquina para orientar melhores decisões.

Dependendo dos requisitos, uma empresa típica exigirá um Data Warehouse e um Data Lake, pois eles atendem a diferentes necessidades e casos de uso.

A estrutura dos dados ou schema (esquema) não é definida quando os dados sçao capturados. Isso significa que voce pode armazenar todos os dados em formato bruto sem a necessidade de saber quais perguntas de negócios deverão ser respondidas no futuro.

## 3.10 Definindo Data Lakes - Parte 2/2

Diferentes tipos de análises, como consultas SQL, análises de Big Data, pesquisa de texto, análises em tempo real e aprendizado de máquina, podem ser usados para descobrir insights.

Os Data Lakes permitem que as empresas gerem diferentes tipos de percepções sobre os dados, desde relatorios sobre dados históricos até modelos pre ditivos criados com Machine Learning.

O principal desafio de uma arquitetura de Data Lake é que os dados brutos são armazenados sem supervisão do conteúdo. Para que um Data Lake torne os dados utilizáveis, ele precisa ter mecanismos definidos para catalogar e proteger os dados. Sem esses elementos, os dados não podem ser encontrados ou confiáveis, resultando em "Pantano de Dados" (Data Swamp). Atender às necessidades de públicos mais amplos exige que os Data Lakes tenham governança, gestão de metadados, consistencia semântica e controles de acesso.

Data Lake é um conceito e pode ser construído com diferentes tecnologias como Apache Hadooop ou Banco de Dados NoSQL.

Podemos importar dados do DW para o Data Lake e vice-versa dependendo das necessidades de negócio da empresa.

Para o DW normalmente usamos *ETL* (Extração, Transformação e Carga)

Para o Data Lake normalmente usamos *ELT* (Extração, Carga e Transformação)

Data Lakes e DWs podem fazer parte de uma grande estrutura central de armazenamneto chamada DataHub.

## 3.11 Benefícios do Data Lake

- *Armazenamento em Formato Bruto:* não precisamos limpar e transformar os dados antes do armazenamento.
- *Importação de Qualquer Quantidade de Dados em Tempo Real:* os dados sao coletados de várias fontes e movidos para o Data Lake em seu formato original. Este processo permite dimensionar dados de qualquer tamanho, enquanto economiza tempo de definição de estrutura de dados, esquema e transformações.
- *Repositório Central para Todos os Dados da Empresa:* os Data Lakes permitem que várias funções como Cientistas de Dados, Engenheiros de Machine Learning, Analista de Dados e Analistas de Negócios, acessem dados com sua ferramenta analítica específica.
- *Sem Necessidade de Movimentação dos Dados:* análises podem ser executadas sem necessidade de mover os dados para um sistema de análise separado

## 3.12 Definindo Data Stores

Um Data Store é um repositório para armazenar e gerenciar de forma persistente coleções de dados que incluem não apenas dados estruturados, mas também tipos de armazenamento variado, como documentos, dados no formato de chave-valor, filas de mensagens e outros formatos de arquivo.

Tipos mais comuns de Data Stores:

- Armazenamento de chave-valor (Redis, Memcached)
- Motor de pesquisa de texto completo (Elastic Search)
- Fila de mensagens (Apache Kafka)
- Sistema de arquivos distribuidos (Hadoop HDFS, AWS S3)

## 3.13 Benefícios do Data Store

- *Armazenamento de Variados Tipos de Dados:* dados que não se encaixam em outros repositórios de armazenamento.
- *Flexibilidade :* armazenamento de dados aderente às necessidades da aplicação final.
- *Suporte a Dados Semi-Estruturados :* dados que possuem alguma organização prévia, mas que devem ser usados em seu formato original.
- *Custo Total Menor:* por se tratar de um tipo simplificado de armazenamento o custo total tende a ser menor que outra solução de armazenamento.

## 3.14 Sistemas Híbridos de Armazenamento
