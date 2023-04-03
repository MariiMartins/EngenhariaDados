152. Executando o Crawler
Então agora a gente pode partir para o Glue.
E aqui está a página inicial, então a gente pode ver que tem bastante opções aqui, então a gente pode criar Delta, mas o Delta também como eu expliquei, não é propriamente um banco de dados. Ele só agrupa, logicamente, tabelas ou fontes de dados. Aqui a gente tem tabelas que na verdade também são elas apenas são schemas que apontam para dados que estão em algum outro local.

Aqui a gente tem chemas, conectores, crawlers, que também vamos utilizar classe first como uma forma de você construir metadados.
Configurações do catálogo, o catálogo e esse conjunto de schemas aqui que existe. Depois, aqui a gente tem a parte de ETL, o Glue Studio, que a gente cria os Jobs, que são os pipelines, os workflow, os de processamento de dados. Aqui há notebooks que a gente pode codificar um processo de ETL.

Depois, algumas ferramentas de classificação, a detecção de dados sensíveis, por exemplo, informação médica ou informação que não que precisa ser apagada e aqui várias outras funcionalidades.

Bom, a primeira coisa que a gente precisa começar fazendo aqui é criar um banco de dados, um database. 
Então o processo de criar também é bem simples, a única informação obrigatória que se precisa é o nome. Então, como os nossos dados são de vendas, eu vou chamar o nosso banco de dados de vendas.
Então, mais uma vez, ele também é só uma forma de você agrupar, logicamente, tabelas, e as tabelas alas nada mais são do que referências para dados que estão fisicamente em outros locais.

Então, aqui eu criei, eu dei o nome de venda aqui. São valores opcionais, eu não vou utilizar e eu vou criar aqui o database. Tem que pegar o hábito de fazer tudo com letra minúscula. Então criei aqui o nosso data base e você pode até criar as tabelas manualmente. 

Mas outra opção que a gente tem é utilizar um crawler que ele já vai criar essas tabelas associadas ao Database que a gente criou.

Então, vou mostrar como ele faz, vamos aqui em Crawlers Classifiers. Você pode ver aqui que não tem nenhum crawler aqui. Vamos clicar aqui em create Crawler e a gente vai configurar a primeira coisa que um nome para o crawler eu vou chamar de cloud crawler vendas, uma descrição que é opcional não vou colocar nada. 

Então, lembrando o objetivo do crawler, ele vai como se fosse uma aplicação de cloud, por exemplo, de crawler que você cria ela para ir a internet capturar dados aqui.

Esse tipo de cloud crawler de dados. Você vai dizer pra ele onde estão os dados, e ele vai fazer uma descoberta do schemas desses dados. A gente vai ver que essa descoberta às vezes não é 100%, principalmente com dados em que você não tem uma definição de schema ele tem que fazer uma descoberta, como é o caso do CSV. Mas é bem interessante.

Então, aqui a fonte do Data Source, ele pode pesquisar vários locais, inclusive através de um drive JDBC, que daí é um leque muito grande de opções.
Mas, no nosso caso, aqui a gente quer S3, que é onde está lá o nosso usuário, que você se vê aqui, uma conexão de rede opcional a gente não precisa.
Ele pergunta o local do UTC 3 é na nossa conta local. Se for uma conta diferente, obviamente que ela teria que ter permissões para isso.

Eu vou deixar o S3 aberto porque a gente vai precisar depois de pegar o caminho de outras pastas dentro do nosso bucket. Então o bucket que a gente criou é o Data Lake 5007 e os nossos dados onde o crawler vai atuar e que o Source data. Então você sei que a pasta que está, os arquivos que a gente importou e eu posso vir aqui copiar a URI do S3 e colar aqui o primeiro, ele fica vermelho ali, mas depois que você sai, ele já fica ok.

Ou a outra coisa que você pode fazer é navegar aqui tem a opção de como serão as próximas execuções do Crowler. Então, ele pode fazer em todas as subpastas, apenas em novas subpastas ou apenas em novos eventos, quando acontecer alguma coisa nova.