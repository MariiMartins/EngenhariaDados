- 76. ETL
ETL é o acrônimo para Extração, Transformação e Carga de Dados.
Então a gente viu que um armazém de dados não produz informação (a informação não é produzida no armazém de dados), a informação tem como origem outros sistemas, classicamente sistemas transacionais.

Então é preciso carregar esses dados para o modelo dimensional no armazém de dados. E esse processo não é um processo simples, como a gente vai ver, não é uma simples carga.

Então ETL são ferramentas de software cuja função é a extração de dados desses sistemas, diversos sistemas precisam ser transformados e consolidados.

A etapa de extração, transformação e carga é normalmente a etapa mais difícil, longa e cara na construção de um armazém de dados. Isso ainda é verdade para projetos de Big Data usando ferramentas não dimensionais.
Ferramentas que carregam dados, por exemplo, para um DataLake.

Estratégias de ETL.
Quais são as estratégias utilizadas na extração, transformação e carga de dados? Conectar em horários apropriados, então um sistema transacional, sistema onde a operação é conduzida normalmente tem uma alta demanda, uma alta carga de dados. Se uma ferramenta de ETL vai lá, por exemplo, em horários de alta produção e extrai esses dados, ele pode prejudicar a operação do sistema. Então, normalmente, essas conexões são feitas em horários de baixa utilização de que o sistema não é utilizado.

Extração dos dados necessários.
Então, uma ferramenta de ETL deve extrair apenas o que ela precisa. Se possível, fazer extrações diferenciais apenas de dados novos ou de dados que foram alterados, que foram atualizados.

Depois da extração.
Desconectar da fonte de dados é outra questão. Outra estratégia é que as conexões que uma ferramenta de ETL utiliza com a fonte de dados são conexões somente de leitura. São conexões mais seguras, porque? Porque uma ferramenta de ETL não precisa alterar dados na origem, ela apenas precisa extrair e capturar esses dados.

No uso clássico, uma ferramenta de ETL ela extrai dados de sistemas transacionais, transforma os dados do modelo relacional para o modelo dimensional e carrega esses dados para o armazém de dados.

Bom para se fazer extração e transformação e carga de dados. Se precisa de uma ferramenta, você tem que ter alguma ferramenta para fazer isso. Existe muitas ferramentas diferentes. Existe ferramentas manuais que você vai fazer, codificação de scripts e escrever rotinas SQL, que é o que a gente vai utilizar aqui, no nosso caso, prático.
Existem ferramentas de workflow, daí que você constrói etapas passo a passo. Aqui começa a falar de ferramentas especializadas em ETL, ou seja, você não está mais usando o sistema gerenciador de banco de dados.
Você está usando uma ferramenta que tem uma especialização em ETL e existe ferramentas mistas que misturam em workflow os processos manuais, codificação.

Alguns exemplos de ferramentas conhecidas de ferramentas especializadas em ETL é o Oracle Warehouse Builder, SAP Data Services, Power SAP Informática é uma das maiores e mais conhecidas. O SQL Server Integration Services da Microsoft, que faz parte do SQL Server. O IBM esforço FIR Warehouse Edition.

Bom, além de extrair dados, o processo de ter tem algumas tarefas e alguns problemas que ele precisa resolver. Então, por exemplo, ele tem que fazer tratamento da qualidade dos dados. Então os dados têm que estar correto, não ambíguo, consistente e completo.

Tem que fazer limpeza de dados, tirar dados duplicados, seguir regras de negócio.
Alteração de codificações, por exemplo, se você está extraindo dados de um mainframe, que é a codificação EDCDIC para ASCII, que é uma codificação de PC.
Transformar para o modelo dimensional. Se a informação vem lá de um banco de dados relacional, ela tem que ser transformada para o modelo dimensional.
Staging é uma etapa intermediária dos dados após a extração e antes de transformar e carregar. Então, o que acontece? Você tem lá bancos de dados transacionais e você tem lá o seu DataWarehouse. Você precisa carregar dados do transacional para o leitor DataWarehouse. Você tem que transformar esses dados nessa etapa em intermediária.

Você simplesmente extrai esses dados para um banco de dados intermediário, que é chamado de Staging, aqui do Staging, você inicia a etapa de transformação dos dados e começa a operar os dados, mudar o modelo, tratar a qualidade.
Por que você faz isso no Staging, numa etapa intermediária? Porque você assim isola o sistema transacional. Tudo o que você faz lá no sistema transacional é extrair a informação da maneira que ela está lá. Você extrai ela com o menor impacto possível, com o menor tempo possível e coloca nesta etapa intermediária.

A partir dessa etapa intermediária. Como é um ambiente propício para a transformação de dados, você não tem problema nenhum, nesse ambiente foi criado lá para transformação de dados. Então, no staging, ocorre a transformação e os dados são carregados no DataWarehouse no modelo dimensional.

Então, o statgin ele pode ser processado em memória ou em disco. Alguns projetos guardam dados de Stagin, outros apagam depois da carga. Então, existem projetos de construção de DataWarehouse que o Staging é carregado e ele é arquivado, carregado e é arquivado e ele fica arquivado lá durante algum tempo.

Existem outros projetos que não, o Stagin é criado, roda o processo de transformação lá para o armazém de dados e ele é imediatamente excluído.
Aí é uma estratégia que depende de vários fatores e depende duma decisão da equipe que está construindo o DataWarehouse.

Uma questão importante dados em Staging não devem ser acessados por usuários. Os dados são acessados no modelo de transação, onde a operação é no DataWarehouse. Nesse estágio intermediário, o usuário nenhum tem acesso, é o modelo de dados intermediário apenas para transformação, o usuário não tem acesso.

Dentre as funções do processo de ETL está consolidação de dados. Então, aqui alguns exemplos você vai consolidar, por exemplo, dados de compras e contas a pagar. São sistemas diferentes.
Como a gente falou, já é quase regra que um DataWarehouse vai consolidar dados de fontes diferentes, de sistemas diferentes, que são estruturas diferentes, que são mantidos por empresas diferentes em sistemas gerenciadores de banco de dados diferentes.

Então, por exemplo, no sistema de compras, você pode ter lá a sigla do Estado carregado como Rio Grande do Sul, carregado como RS. Lá no Contas a pagar, você tem por extenso, em vez da sigla no processo de consolidação de dados para o DataWarehouse, você tem que consolidar essa informação de uma única forma.

Outro problema de consolidação de dados: no compras você tem lá o cliente Maria com o ID 030 no Contas a pagar, a Maria é o mesmo cliente, mas ela tem uma chave diferente ela é 2345. Quando ela for para o DataWarehouse, a Maria, ela tem que ser única, o sistema do processo de carga tem que criar uma versão única da Maria. Não pode mais existir esta divergência. Ou seja, você não pode colocar no armazém de dados Duas Marias.

Então o processo de ETL é um processo importantíssimo. Como eu falei, é o mais longo, mais demorado e um dos mais importantes na construção de armazéns de dados.
