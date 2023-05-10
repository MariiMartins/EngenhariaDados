# 4. Armazenamento e Processamento Distribuído

## 1. Por que o Armazenamento de Dados é Importante?

## 2. Os Padrões de Acesso definem o Tipo de Armazenamento

    - quantos sistemas precisarão de acesso à camada de armazenamento de dados?
    - com que frequência os sistemas acessarão o armazenamento de dados?
    - qual o volume de dados que esses sistemas estarão lendo?
    - quanta lógica será aplicada por esses sistemas aos dados?
    - como o sistema acessa tecnicamente os dados?

<details><summary>  3 e 4 Armazenamento SQL/NoSQL ou Armazenamento de Arquivos? </summary>

    - Depende dos padrões de acesso;
    
    SQL
        - O armazenamento SQL é o formato tradicional de armazenamento de dados no formato tabular;
        - É um dos formatos de armazenamento mais antigos e amplamente usados nos dias de hoje
        - Ideal para dados estruturados
        - Usamos SGBDs (Sistemas Gerenciadores de Bancos de Dados) como Oracle, PostgresSQL, SQL Server ou MySQL, entre outros.
   
    NoSQL
        - O armazenamento NoSQL nasceu na era do BigData para permitir o armazenamento de dados em diferentes formatos, em especial, dados semi-estruturados como no formato JSON, XML ou colunar
        - São sistemas de armazenamento orientados à performance e facilidade de uso
        - Exemplos de SGBDs NoSQL: MongoDB, Redis, Apache Cassandra, Apache HBase e Amazon DynamoDB.
    
    - BigData é definido por 4 Vs: Volume, Velocidade, Viariedade e Veracidade.
    - E o V de Variedade é normalmente uma das partes mais complexas. Pode ser necessário trabalhar com dados no formato de vídeo, áudio, imagens, texto, arquivos pdf ou mesmo ícones. Ou ainda dados em um formato que facilite a pesquisa e reduza o espaço necessário para armazenamento.
    - Bancos de dados SQL ou NoSQL podem não ser ideais nesses casos, isso sem falar na performance de acesso.
    - Exatamente aí que precisaremos de alternativas para armazenamento de dados. Precisamos de diferentes formatos e diferentes sistemas.
    - Alternativas incluem: Parquet, Avro, JSON, CSV, ORC, HDF5 e vários outros formatos.

</details>

## 5. Armazenamento Colunar x Linha

Armazenamento baseado em Linha

| ID | Nome | Sobrenome | Salário |
| ---- | ---- | ---- | ---- |
|1001 | Manuel | Bandeira | 12.000 |
|1002 | Carlos | Drummond | 15.000 |
|1003 | Cora | Coralina | 14.000 |

Armazenamento baseado em Coluna

| Campo | Valor |
| --- | --- |
| ID | 1001:001, 1002:002, 1003:003|
| Nome| Manuel: 001, Carlos:002, Cora:003 |
| Sobrenome| Bandeira:001, Drummond: 002, Coralina: 003|
 Salario |12.000:001, 15.000:002, 14.000:003|

## 6. Quando usar um Data Warehouse?

    - Um Data Warehouse é um tipo de banco de dados projetado especificamente para consultas e análises eficientes de grandes quantidades de dados.
    - Ele é normalmente usado para armazenar e gerenciar dados de várias fontes, como bancos de dados transacionais ou arquivos de log.
    - DW é um conceito, logo pode ser criado com SGBD SQL ou NoSQL, no formato colunar ou baseado em linha.
    - Existem varios motivos pelos quais você pode optar por usar um DW:
        1- Grande volumes de dados: se a empresa possui um grande volume de dados que precisam ser armazenados e analisados, um DW pode ser uma solução eficiente.
        2- Necessidade de desempenho de consulta analítica: Os DW sãp projetados especificamente para desempenho de consultas, o que pode ser importante se você precisar recuperar e analisar grandes quantidades de dados de maneira rápida.
        3 - Necessidade de integrar dados de várias fontes: Se você tiver dados de varias fontes que precisa integrar e analisar em conjunto, um DW pode ser uma ferramenta útil.
        4 - necessidade de oferecer suporte à inteligencia de negócios (BI) e relatórios: Os DW costumam ser usados como base para inteligencia de negócios e sistemas de relatórios, pois permitem consultas e análises de dados rápidas e eficientes.
        5 - Necessidade de dados históricos: Os DW são frequentemente usados para armazenar dados históricos, pois permitem consultas e análises de dados ao longo do tempo.
    Em geral, um DW é uma boa opção se você tiver grande volume de dados que precisa armazenar e analisar com eficiencia ou se precisar oferecer suporte a sistemas de relatórios e inteligencia de negócios.    

## 7. Quando usar um Data Lake?

    - um DW requer que os dados sejam limpos e organizados antes do armazenamento.
    - o Data Lake permite o armazenamento dos dados no seu formato bruto para posterior processamento e organização

    DW -> Limpa e organiza, depois carrega
    DL -> Carrega, depois limpa e organiza

    - Um DL é um repositório centralizado que permite armazenar e processar grandes quantidades de dadso estruturados e não estruturados em escala.
    - Ele foi projetado para lidar com uma ampla variedade de tipos de dados e pode armazenar dados em sua forma bruta e não estruturada, permitindo que você armazene e processe dados de maniera mais flexível e escalável do que um banco de dados tradicional.

    - Assim como o DW, o DL é um conceito.
    - Mas por definição um banco de dados SQL não seria o ideal, uma vez que a ideia é carregar primeiro e limpar e organizar os dados depois.
    - Podemos usar bancos de dados NoSQL ou tecnologias de armazenamento distribuido para construir DL, localmente ou na nuvem!

    - Existem vários motivos pelos quais você pode optar por usar um DL.
        1. Necessidade de armazenar e processar dados em sua forma bruta: Os DL permitem que você armazene e processe dados em sua forma bruta e não estruturada, o que pode ser útil se você precisar preservar os dados originais ou se quiser manter a flexibilidade na forma como processa e analisa os dados.
        
        2. Necessidade de armazenar e processar grandes volumes de dados: Se você possui um grande volume de dados que precisam ser armazenados e processados, um Data Lake pode ser uma solução eficiente.

        3. Necessidade de armazenar e processar dados estruturados e não estruturados: Os DL são adequados para armazenar e processar dados estruturados e não estruturados, tornando-os uma boa escolha se você tiver uma variedade diversificada de tipos de dados.

        4. Necessidade de escalabilidade: Os DL são projetados para serem escaláveis, permitindo que você armazene e processe facilmente grandes quantidades de dados à medida que suas necessidades aumentam.

        5. Necessidade de um repositório de dados centralizado: Se você tiver dados de várias fontes que precisa armazenar e processar em um local centralizado, um DL pode ser uma ferramenta útil.
    
    Em geral, um DL é uma boa opção se você tiver grandes volumes de dados estruturados e não estruturados que precisa armazenar e processar em escala ou se precisar de um repositório centralizado para armazenar e processar dados de várias fontes.

## 8. Quando usar um Data Lakehouse?

    Um Data Lakehouse pode ser definido como uma plataforma de dados moderna construída a partir de uma combinação de um Data Lake e um Data Warehouse.
    Mais especificamente, um Data Lakehouse une o armazenamento flexível de dados não estruturados de um Data Lake e os recursos e ferramnetas de gerenciamento de data Warehouses e os implementa estrategicamnete como um sistema maior.
    Essa integração de duas ferramnetas exclusivas traz o melhor dos dois mundos para os usuários.
    Data Lakehouses implementam estruturas de dados e recursos de gerenciamneto de dados semelhantes aos de um DW diretamente sobre o armazenamento em nuvem de baixo custo em formatos abertos e, normalmente, distribuidos.

    O Data Lakehouse traz o princípio:
        From BI to AI
        - A questão é que nem todas as empresas estão usando AI (Artificial Intelligence)!
        - Ou ainda, tudo que a empresa precisa é de um relatório de BI ou apenas de um sistema de armazenamento de dados no formato bruto!
    
    Vantagens ao usar um Data Lakehouse:
        1 - Escalabilidade
        2 - Flexibilidade
        3 - Desempenho de Consulta
        4 - Repositório Centralizado

    Desvantagens ao usar um Data Lakehouse:
        1 - Complexidade
        2 - Uso Intensivo de Recursos
        3 - Desafios Adicionais de Governança de Dados
        4 - Desafios Adicionais de Integração de Dados

## 9, 10 e 11. Quando usar um Data Store?

    Um Data Store é um repositório para armazenar e gerenciar dados.
    Tecnicamente podemos dividir os Data Stores em 7 categorias:
        1 - Bancos de Dados Relacionais (SQL - Normalmente usados em DWs)
        2 - Bancos de Dados Não Relacionais (NoSQL - podem ser usados em DWs ou Data Lakes)
        3- Sistemas de Arquivos (Distribuidos ou não, são usados em DLs e Data Lakehouses)
        4 - Armazenamento Key-Value
        5 - Full-Text Search Engine
        6 - Fila de Mensagens
        7 - In-Memory Data Store

    - Sistemas de Arquivos
        - Podem ser lcoal ou em rede (NTFS, FAT, NAS, SAN)
        - Podem ser distribuidos (HDFS - Hadoop Distribuited File System, Object Storage)
        - POdem ser na nuvem (Amazon S3, Azure Blob Storage, Google Storage, Delta Lake)
        - O objetivo é armazenar dados em qualquer formato de arquivo (CSV, JSON, PARQUET, AVRO, ORC)
        - Em geral tem baixo custo
    
    - Armazenamento Key-Value
        - Outra maniera de armazenar dados não relacionais é em um armazenamento de cahve-valor (key-value)
        - Um armazenamento de chave-valor é basicamente um hashmap em escala de produção: um mapa de chaves para valores. Não há esquemas sofisticados ou relacionamentos entre os dados. Nenhuma tabela ou ouyro grupo lógico de dados do mesmo tipo. Apenas chaves e valores, é isso.
        - Exemplos de armazenamntos de chave-valor: Redis e Memcached

    - Full-Text Search Engine (Mecanismo de Pesquisa de Texto)
        - Os mecanismos de pesquisa são um tipo especial de armazenamento de dados projetados para um caso de uso muito específico: pesquisar documentos de texto.
        - Você envia documentos semiestruturados para o mecanismo de pesquisa, mas em vez de armazená-los como estão e usar analisadores XML ou JSON para extrair informações, o mecanismo de pesquisa divide o conteúdo do documento em um novo formato otimizado para pesquisa com base em substrings de campos de texto.
        - Elasticsearch é o principal representante desta categoria.

    Fila de Mensagens
        - Um data Store bastante útil é o tipo fila de mensagem, agindo como um middleware.
        - Você pode se surpreender ao ver as filas de mensagens nesta lista porque elas são consideradas mais uma ferramenta de transferência de dados do que uma ferramenta de armazenamento de dados, mas as filas de mensagens armazenam seus dados com tanta confiabilidade e ainda mais persistência do que algumas das outras ferramentas que listamos anteriormente.
        - O Apache Kafka é o principal representante desta categoria.
    
    In-Memory Data Store
        - In-Memory Data Store são sistemas que armazenam, leem, gravam e acessam dados na memória de acesso aleatório (RAM) em vez de na memória somente leitura (ROM).
        - Os In-Memory Data Stores usam RAM para recuperar dados rapidamente, fazendo réplicas constantes atualizadas de registros de dados e são definidos pelo local em que mantêm os dados, não necessariamente pelo tipo de estrutura de dados.
        - Redis, VoltDB e SAP Hana são os principais representantes desta categoria.

## 12. Formatos de Arquivos frequentemente usados em Engenharia de Dados

    Uma vez definidos os objetivos, casos de uso e os padrões de acesso, teremos que fazer escolhas quanto ao armazenamento de dados.
        - Armazenamento estruturado, semi ou não estruturados? Todos são possíveis?
        - Sistemas de armazenamento como DW, DL, Data Lakehouse ou DS? Todos são possíveis? Integrações?
        - Armazenamento local ou na nuvem? Ambos?
        - Qual formato de arquivo usar para o armazenamento temporário durante o pipeline de dados ou armazenamento do resultado?

## 13. Formato Parquet

    - Parquet é um formato de armazenamento colunar para armazenar grandes quantidades de dados de forma eficiente.
    - É uma escolha popular para armazenar dados no ecossistema Hadoop (em ambiente distríbuido) porque permite consultas e análises eficientes usando ferramnetas como Apache Spark, Apache Hive e Impala.
    - Vale a pena notar que o Parquet não é a única opção para armazenar dados de forma eficiente. Outras opções incluem Avro, ORC e Delta Lake.

    -Alguns casos de uso específicos para arquivos no formato Parquet:
        - Armazenamneto de grandes quantidades de dados estruturados ou semiestruturados.
        - Consulta de dados usando ferramentas semelhantes a SQL.
        - Compartilhamento de dados entre sistemas.
        - Data warehousing.
    
    - Principais características de arquivos no formato Parquet:
        - Ótima compressão dos dados (excelente para armazenamento)
        - Leitura seletiva (leitura somente do que realmente precisa dentro do arquivo)
        - Suporote em diversas plataformas (Spark, Pandas, etc..)
        - Fácil de particionar (excelente para leitura dos dados)

## 14. Formato Avro

    - Avro é um formato de serialização para armazenar dados.
    - Esse formato é frequentemente usado no ecossitema Hadoop porque oferece suporte a estruturas de dados complexas e é eficiente para armazenar grandes quantidades de dados em um ambiente distribuido.

    -Alguns casos de uso específicos para arquivos no formato Avro:
        - Armazenamento de grandes quantidades de dados
        - armazenamento de dados com estruturas complexas
        - compartilhamento de dados entre sistemas
        - Processamento de dados com hadoop

    - Principais características de arquivos no formato Parquet:
        - Permite mudanças de schema
        - Orientado a linha
        - suporte a schema irregular (como JSON)

## 15. Formato ORC, CSV e JSON

    ORC
        - ORC (Optimized Row Columnar) é um formato de armazenamento colunar para armazenar grandes quantidades de dados de forma eficiente.
        - Arquivos ORC são compostos de grupos de linhas.
        - Arquivos ORC suportam tipos de dados como datetime, decimal e tipos complexos (lists, maps, structs)

    CSV
        - Arquivos CSV (Comma Separated Values) são simples, fáceis e amplamente usados para armazenar dados.
        - Nada especial. Sem compressão. Sem cabeçalhos built-in (como parquet ou avro)
        - são muito fáceis de usar, desde que o volume de dados não seja muito grande.
        - O delimitador é importante

    JSON
        - um dos formatos de arquivos mais úteis para armazenar dados semi-estruturados.
        - JSON (JavaScript Object Notation) é um formato de intercâmbio de dados leve que é facil para os humanos lerem e escreverem e fácil para as máquinas analisarem e gerarem. É frequentemente usado para armazenar e trocar dados pela internet. Muito usado em aplicações web.
        - Alternativas são o formato XML e YAML.

## 16. O que é um sistema Distribuído?

    - Considere um único sevidor (computador), essa máquina tem uma quantidade limitada de espaço em disco (1TB, por exemplo) e tem limitação física de capacidade computacional (por exemplo 1 processador Intel Core i& e 16GB de RAM), essas são limitações fisicas do computador e do que ele pode armazenar e processar.
    - E se pudermos usar a capacidade de armazenamento e processamento de diversos computadores simultaneamente? Sim, podemos fazer isso, e assim nasceram os sistemas distribuidos.
    - Um sistema distribuido é uma rede de computadores que trabalham juntos como um único sistema, e que pode ser usado para armazenamento, processamento ou ambos.
    - Esses sistemas são projetados para compartilhar recursos e cargas de trabalho entre vários computadores, permitindo que eles dimensionem e lidem com cargas de trabalho maiores do que um único computador poderia fazer sozinho.
    - Os sistemas distribuidos são frequentemente usados para fornecer serviços como armazenamento de arquivos, gerenciamento de banco de dados ou computação distribuida e podem ser encontrados em uma variedade de contextos, incluindo aplicações web, computação em nuvem, simulações científicas e, claro, Engenharia de dados.
    - Existem muitas abordagens diferentes para projetar e implementar sistemas distribuidos, e a arquitetura e o design específicos de um determinado sistema dependerão das necessidades e objetivos do sistema.
    - Mas se sistemas distribuidos trouxeram uma solução eficiente para armazenamento e processamneto, também trouxeram um novo problema:
        - Como vamos gerenciar as tarefas computacionais em diversos computadores simultaneamente?

## 17. Sistemas de Arquivos Distribuidos e Sistemas de Processamento Distribuído

    Mas se sistemas distribuidos trouxeram uma solução eficiente para armazenamento e processamento, também trouxeram um novo problema:
        Como vamos gerenciar as tarefas computacionais em diversos computadores simultaneamente?
    Para um computador funcionar, além do hardware, ele precisa (pelo menos) dos seguintes softwares:
        Sistema Operacional (Windows, Linux ou MacOS, por exemplo)
        Sistema de Arquivos Local (NTFS, ext4, APFS, por exemplo)
    Mas um sistema de arquivos local não foi desenvolvido para ambiente distribuido. Ele existe para gerenciar o armazenamento e processamento localmente. Logo, precisamos de uma outra camada de software para um sistema distribuído!
    - Um sistema distribuido existe sobre a camada local de um computador.
    
    - Considere um sistema distribuido de 3 máquinas:
        - Cada máquina terá seu próprio sistema operacional;
        - Cada máquina terá seu próprio sistema de arquivos local;
        - Podemos ter cada máquina do sistema distribuido com SO Linux e cada máquina com sistema de arquivos ext4, por exemplo.
    Considerando um sistema distribuido de 3 máquinas, para que as 3 máquinas realmente funcionem com um sistema distribuído, precisamos de mais duas camadas de software:
        - Um sistema de arquivos distribuido, capaz de gerenciar o armazenamento de forma distribuida pelo sistema. 
        - Um sistema de processamento distribuido, capaz de ler e gravar dados do sistema de armazenamento distribuido e realizar o processamento usando a capacidade computacional oferecida pelas 3 máquinas.

## 18. Hierarquia de um Sistema Distribuído

## 19. 10 Exemplos de Sistemas de Arquivos Locais

Sistemas de Arquivos Locais:
    FAT(FAT16, FAT32)
    NTFS
    HFS e HPFS
    PFS
    UFS
    ext2, ext3, ext4
    XFS
    Veritas File System
    VMS
    ZFS
    ReiserFS

## 20. 10 Exemplos de Sistemas de Arquivos Distribuidos

Sistema de Arquivos Distribuidos:
    Hadoop Distribuited File System (HDFS)
    Windows Distribuited File System
    Network File System (NFS)
    Server Message Block (SMB)
    Google File System (GFS)
    Lustre
    GlusterFS
    Amazon S#, Google Cloud Storage, Microsoft Block Storage.

## 21. 20 Exemplos de Sistemas de Processamento Distribuidos

O Processamento Distribuído pode ser usado sempre que for necessário algum tipo de computação (cálculos, resumos, simulações, organização de dados, etc..) e que o processamneto local não seja suficiente.
Usamos processamento Distribuído quando é necessário alta capacidade computacional e/ou trabalhar com alto volume de dados.
Para realizar o processamento distribuido precisamos de software capaz de funcionar em ambiente distribuido.

Exemplos de Sistemas de Processamento distribuido:
    Apache Spark
    Apache Storm
    Apache Flink
    Apache Flume
    Apache Kafka
    Apache Hadoop MapReduce
    Apache Beam
    Elasticsearch
    Dremio
    Presto
    Snowflake
    Fivetran
    Apache Airflow
    Airbyte
    DBT
    Google BigQuery
    AWS Glue
    AWs Athena
    Amazon EMR (Elastic MapReduce)
    Microsoft Azure Synapse

## 22. Vantagens de Sistemas Distribuidos

Existem várias vantagens em usar um sistema distribuido:
    - Escalabilidade: Um sistema distribuido pode ser dimensionado facilmente para lidar com cargas de trabalho crescente adicionando mais computadores ao sistema.
    - Confiabilidade: Se um computador falhar, os outros computadores do sistema podem continuar funcionando.
    - Desempenho: Os sistemas distribuidos geralmente terão um desempenho melhor do que um único computador porque as tarefas podem ser divididas entre vários computadores, permitindo que sejam concluídas em paralelo.
    - Flexibilidade: os sistemas distribuidos podem ser projetados para serem felxíveis e adaptáveis, permitindo que sejam usados em uma variedade de contextos diferentes e para uma ampla gama de aplicações.

## 23. Desvantagens de Sistemas Distribuidos

Existem também algumas desvantagens em usar sistema distribuido:
    - complexidade: Os sistemas distribuidos podem ser complexos de projetar e manter, exigindo conhecimento especializado.
    - Sobrecarga de Comunicação: Em um sistema distribuido, os computadores precisam se comunicar uns com os outros para coordenar suas ações e compartilhar informações. Isso pode introduzir sobrecarga e latência adicionais.
    - Riscos de Segurança: Os sistemas distribuidos podem ser mais vulneraveis a ameaças de segurança, como ataques a computadores individuais ou à propria rede.
    - Custo: Configurar e manter um sistema distribuido pode ser mais caro do que usar um único computador, seja localmente ou em nuvem

## 24. [PDF] Exemplos de Soluções Para Armazenamento e Processamento Distribuído

Existem muitos exemplos de soluções de armazenamento e processamento distribuído, incluindo:
    • Armazenamento em nuvem: sistemas de armazenamento em nuvem, como Amazon S3  ou  Google  Cloud  Storage,  permitem  que  os  usuários  armazenem  e  recuperem dados de uma rede de servidores em vez de um único computador. Isso permite um armazenamento escalável e altamente disponível que pode ser acessado de qualquer lugar com uma conexão à Internet.
    • Sistemas de arquivos distribuídos: sistemas de arquivos distribuídos, como o Cloud Storage  do  Google  e  o  HDFS  do  Apache  Hadoop,  permitem   que  os   usuários armazenem e acessem arquivos em vários computadores em um sistema distribuído.
    • Bancos  de  dados  distribuídos:  bancos  de  dados  distribuídos,  como  MongoDB  e Cassandra,  permitem  que  os  usuários  armazenem  e  acessem  dados  em  vários computadores em um sistema distribuído.
    • Plataformas  de  computação:distribuída:  plataformas  de  computação  distribuída, como Apache Sparke Apache Airflow, permitem que os usuários processem grandes quantidades de dados em paralelo em um sistema distribuído. Essas plataformas são frequentemente usadas para tarefas de análise de dados e aprendizado de máquina.
    • Redes de entrega de conteúdo (CDNs): CDNs, como Akamai e Cloudflare, usam uma rede  distribuída  de  servidores  para  entregar  conteúdo  (como  sites  e  vídeos)  para usuários com alta disponibilidade e baixa latência. 
    • Redes descentralizadas: redes  como  a Blockchain Ethereum,  permitem  que  os usuários   compartilhem   recursos   e   informações   diretamente   entre   si   sem   a necessidade de um servidor central.

## 25. [PDF] Compressão de Arquivos para o Armazenamento Distribuído

A compressão é uma técnica comum usada em sistemas de armazenamento distribuído para  reduzir  a  quantidade  de  espaço  de  armazenamento  necessária  para  um  determinado conjunto de dados. Isso pode ser especialmente útil em sistemas distribuídos de grande escala, onde o volume de dados armazenados pode ser muito grande.Existem  várias  maneiras  de  usar  a  compactação  em  sistemas  de  armazenamento distribuído:
    - No  nível  do  arquivo:  Arquivos  individuais  podem  ser  compactados  antes  de  serem armazenados  no  sistema  de  armazenamento  distribuído.  Isso  pode  ser  feito  usando vários algoritmos  de  compactação,  como  gzip  ou  bzip2,  que  podem  reduzir  significativamente  o tamanho do arquivo.
    - No  nível  do  bloco:  Em  alguns  sistemas  de  armazenamento  distribuído,  os  dados  são armazenados em blocos, que normalmente são de tamanho fixo (por exemplo, 128MB). Esses blocos  podem  ser  compactados  antes  de  serem  armazenados,  usando  um  algoritmo  de compactação sem perdas ou com perdas.
    - Compactação em trânsito: Os dados também podem ser compactados à medida que são transferidos  entre  computadores  no  sistema  distribuído.  Isso  pode  ser  feito  usando  uma variedade de técnicas, como compactação HTTP ou dimensionamento de janela TCP.
É importante observar que a eficácia da compactação dependerá das características dos dados que estão sendo compactados. Alguns tipos de dados, como texto ou código, podem ser altamente compactáveis, enquanto outros tipos de dados, como imagens ou vídeos, podem ser menos compactáveis.Sendo assim, os dados podem ser armazenados em bancos de dados SQL, em bancos de dados  NoSQL,  em  Data  Lakes  com  diferentes  formatos  de  arquivos  e  ainda  é  possível  aplicar compressão.  A  decisão  da  arquitetura  de  armazenamento  depende  do  volume  de  dados,  do padrão de acesso, tipo de processamento e casos de uso.

## 26. [PDF] Demonstração Pratica 1 - O Funcionamento de um Sistema Distribuído

## 27. Demonstração Pratica 1 - Definindo o Ambiente

## 28. Demonstração Pratica 1 - Carga de Dados

## 29. Demonstração Pratica 1 - Comportamento do Sistema Distribuído quando um servidor fica indisponivel

## 30. Demonstração Pratica 1 - Acessando os Dados

## [31. Quiz](link)
