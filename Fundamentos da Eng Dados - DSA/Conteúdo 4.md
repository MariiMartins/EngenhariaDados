# 4. Armazenamento e Processamento Distribuido

## 1. Por que o Armazenamento de Dados é Importante?

## 2. Os Padrões de Acesso definem o Tipo de Armazenamento
    - quantos sistemas precisarão de acesso à camada de armazenamento de dados?
    - com que frequencia os sistemas acessarão o armazenamento de dados?
    - qual o volume de dados que esses sistemas estarão lendo?
    - quanta logica será aplicada por esses sistemas aos dados?
    - como o sistema acessa tecnicamente os dados?
    
<details> ## 3 e 4 Armazenamento SQL/NoSQL ou Armazenamento de Arquivos? P1
    -> Depende dos padrões de acesso;
    <details>SQL
        - O armazenamento SQL é o formato tradicional de armazenamento de dados no formato tabular;
        - É um dos formatos de armazenamento mais antigos e amplamente usados nos dias de hoje
        - Ideal para dados estruturados
        - Usamos SGBDs (Sistemas Gerenciadores de Bancos de Dados) como Oracle, PostgresSQL, SQL Server ou MySQL, entre outros.
    </details>    
    <details> NoSQL
        - O armazenamento NoSQL nasceu na era do BigData para permitir o armazenamento de dados em diferentes formatos, em especial, dados semi-estruturados como no formato JSON, XML ou colunar
        - São sistemas de armazenamento orientados à performance e facilidade de uso
        - Exemplos de SGBDs NoSQL: MongoDB, Redis, Apache Cassandra, Apache HBase e Amazon DynamoDB.
    </details>

    - BigData é definido por 4 Vs: Volume, Velocidade, Viariedade e Veracidade.
    - E o V de Variedxade é normalmente uma das partes mais complexas. Pode ser necessário trabalhar com dados no fromato de vídeo, áudio, imagens, texto, arquivos pdf ou mesmo ícones. Ou ainda dados em um formato que facilite a pesquisa e reduza o espaço necessário para armazenamento.
   - Bancos de dados SQL ou NoSQL podem nãoser ideais nesses casos, isso sem falar na performance de acesso.
   - Exatamente aí que precisaremos de alternativas para armazenamento de dados. Precisamos de diferentes formatos e diferentes sistemas.
   - Alternativas incluem: Parquet, Avro, JSON, CSV, ORC, HDF5 e vários outros formatos.
</details>
   
## 5. Armazenamento Colunar x Linha
    Armazenamento baseado em Linha
        | ID | Nome | Sobrenome | Salário |
        | -- | -- | --- | --- |
        |1001| Manuel | Bandeira | 12.000|
        |1002| Carlos | Drummond | 15.000|
        |1003| Cora | Coralina | 14.000|
    Armazenamento baseado em Coluna
        | ID | 1001:001, 1002:002, 1003:003|
        | Nome| Manuel: 001, Carlos:002, Cora:003 |
        | Sobrenome| Bandeira:001, Drummond: 002, Coralina: 003|
        | Salario|12.000:001, 15.000:002, 14.000:003|
    
## 6. Quando usar um Data Warehouse?
    - Um Data Warehouse é um tipo d e banco de dados projetado especificamente para consultas e análises eficientes de grandes quantidades de dados.
    - Ele é normalmente usado para armazenar e gerenciar dados de várias fontes, como bancos de dados transacionais ou arquivos de log.
    - Data Warehouse é um conceito, logo pode ser criado com SGBD SQL ou NoSQL, no formato colunar ou baseado em linha.
    - Existem varios motivos pelos quais voce pode optar por usar um DW:
        1- Grande volumes de dados: se a empresa possui um grande volume de dados que precisam ser armazenados e analisados, um DW pode ser uma solução eficiente.
        2- Necessidade de desempenho de consulta analítica: Os DW sãp projetados especificamente para desempenho de consultas, o que pode ser importante se voce precisar recuperar e analisar grandes quantidades de dados de maneira rápida.
        3 - Necessidade de integrar dados de várias fontes: Se voce tiver dados de varias fontes que precisa integrar e analisar em conjunto, um DW pode ser uma ferramenta útil.
        4 - necessidade de oferecer suporte à inteligencia de negócios (BI) e relatórios: Os DW costumam ser usados como base para inteligencia de negócios e sistemas de relatórios, pois permitem consultas e análises de dados rápidaws e eficientes.
        5 - Necessidade de dados históricos: Os DW são frequentemente usados para armazenar dados históricos, pois permitem consultas e análises de dados ao longo do tempo.
    Em geral, um DW é uma boa opção se voce tiver grande volume de dados que precisa armazenar e analisar com eficiencia ou se precisar oferecer suporte a sistemas de relatórios e inteligencia de negócios.    

## 7. Quando usar um Data Lake?
    - um DW requer que os mdados sejam limpos e organizadps antes do armazenamento.
    - o Data Lake permite o armazenamento dos dados no seu formato bruto para posterior processamento e organização

    DW -> Limpa e organiza, depois carrega
    DL -> Carrega, depois limpa e organiza

    - Um DL é um repositório centralizado que permite armazenar e processar grandes quantidades de dadso estruturados e não estruturados em escala.
    - Ele foi projetado para lidar com uma ampla variedade de tipos de dados e pode armazenar dados em sua forma bruta e não estruturada, permitindo que você armazene e processe dados de maniera mais flexível e escalável do que um banco de dados tradicional.

    - Assim como o DW, o DL é um conceito.
    - Mas por definição um banco de dados SQL não seria o ideal, uma vez que a ideia é carregar primeiro e limpar e organizar os dados depois.
    - Podemos usar bancos de dados NoSQL ou tecnologias de armazenamento distribuido para construir DL, localmente ou na nuvem!

    - Existem vários motivos pelos quais voce pode optar por usar um DL.
        1. Necessidade de armazenar e processar dados em sua forma bruta: Os DL permitem que você armazene e processe dados em sua forma bruta e não estruturada, o que pode ser útil se você precisar preservar os dados originais ou se quiser manter a flexibilidade na forma como processa e analisa os dados.
        
        2. Necessidade de armazenar e processar grandes volumes de dados: Se voce possui um grande volume de dados que precisam ser armazenados e processados, um Data Lake pode ser uma solução eficiente.

        3. Necessidade de armazenar e processar dados estruturados e não estruturados: Os DL são adequados para armazenar e processar dados estruturados e não estruturados, tornando-os uma boa escolha se voce tiver uma variedade diversificada de tipos de dados.

        4. Necessidade de escalabilidade: Os DL são projetados para serem escaláveis, permitindo que voce armazene e processe facilmente grandes quantidades de dados à medida que suas necessidades aumentam.

        5. Necessidade de um repositório de dados centralizado: Se voce tiver dados de várias fontes que precisa armazenar e processar em um local centralizado, um DL pode ser uma ferramenta útil.
    
    Em geral, um DL é uma boa opção se voce tiver grandes volumes de dados estruturados e não estruturados que precisa armazenar e processar em escala ou se precisar de um repositório centralizado para armazenar e processar dados de várias fontes.

## 8. Quando usar um Data Lakehouse?
    Um Data Lakehouse pode sere definido como uma plataforma de dados moderna construída a partir de uma combinação de um Data Lake e um Data Warehouse.
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

<!--
## 9. Quando usar um Data Store? P1
    Um Data Store é um repositório para armazenar e gerenciar dados.
    Tecnicamente podemos dividir os Data Stores em 7 categorias:
        1 - Bancos de Dados Relacionais (SQL - Normalmente usados em DWs)
        2 - Bancos de Dados Não Relacionais (NoSQL - podem ser usados em DWs ou Data Lakes)
        3- Sistemas de Arquivos (Distribuidos ou não, são usados em DLs e Data Lakehouses)
        4 - Armazenamento Key-Value
        5 - Full-Text Search Engine
        6 - Fila de Mensagens
        7 - In-Memory Data Store



## 10. Quando usar um Data Store? P2
    
## 11. Quando usar um Data Store? P3

## 12. Formatos de Arquivos frequentemente usados em Engenharia de Dados

## 13. Formato Parquet

## 14. Formato Avro

## 15. Formato ORC, CSV e JSON

## 16. O que é um sistema Distribuido?

## 17. Sistemas de Arquivos Distribuidos e Sistemas de Processamento Distribuido

## 18. Hierarquia de um Sistema Distribuido

## 19. 10 Exemplos de Sistemas de Arquivos Locais

## 20. 10 Exemplos de Sistemas de Arquivos Distribuidos

## 21. 20 Exemplos de Sistemas de Processamento Distribuidos

## 22. Vantagens de Distemas Distribuidos

## 23. Desvantagens de Sistemas Distribuidos

## 24. [PDF] Exemplos de Soluções Para Armazenamento e Processamento Distribuido

## 25. [PDF] Compressão de Arquivos para o ArmazenamentoDistribuido

## 26. [PDF] Demonstração Pratica 1 - O Funcionamento de um Sistema Distribuido

## 27. Demonstração Pratica 1 - Definindo o Ambiente

## 28. Demonstração Pratica 1 - Carga de Dados

## 29. Demonstração Pratica 1 - Comportamento do Sistema Distribuido quando um servidor fica indisponivel

## 30. Demonstração Pratica 1 - Acessando os Dados

--> 

## (31. Quiz)[]