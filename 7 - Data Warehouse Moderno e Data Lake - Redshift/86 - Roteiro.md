86. Roteiro
O nosso objetivo é criar uma tabela dentro de um DataWarehouse que seja uma tabela simples e desnormalizada para um usuário final criar um dashboard ad hoc, ou seja, que ele crie um dashboard sem planejamento conforme a necessidade dele. Só que para ele poder fazer isso, a gente precisa disponibilizar dados.

Então o que é que a gente vai fazer? Nós vamos criar no redshift um banco de dados e nós vamos popular esse banco de dados com dados de vendas.
De onde virão estes dados que vão popular esta essa tabela de vendas? Elas virão de arquivos CSV que vão estar no S3.
Então a gente vai construir o schema deste banco de dados no redshift e a gente vai utilizar um comando de importação do redshift que lê dados do S3.

Lembrando que o S3 é um sistema de arquivos e popula eles uma vez isso feito, a gente pode ir para o Google Data Studio e construir um dashboard.

Então a gente já falou do redshift, e a gente já falou do S3.
O que é o Google Data Studio, o Google Data Studio é uma ferramenta de produção de relatórios e dashboards.
E por que a gente escolheu o Google Data Studio e não, por exemplo, o Click Science, que é do próprio AWS, ou o Power BI ou Tableau? A gente escolheu o Google Data Studio porque é uma ferramenta totalmente gratuita, de fácil acesso e muito simples de ser utilizada. E também para que fique uma coisa que esteja fora do ferramental de um mesmo fornecedor. Então, esse vai ser o nosso objetivo.

Então, primeiro a gente vai acessar o AWS com a conta que a gente tem lá no AWS e a gente vai criar um cluster no redshift. A gente vai criar uma versão crítica, ou seja, que não vai ter custo deste cluster. Depois a gente vai criar bancos de dados e tabelas. Então, junto ao material do curso, existe um script para construir esse banco de dados, que são cinco tabelas que a gente já conhece clientes, vendas, vendedores, produtos, itens de venda.
Aí a gente vai criar um bucket no S3, Lá no S3 a gente vai fazer o upload de arquivos CSV, então esses arquivos CSV vão ser utilizados para carregar os dados para o redshift, e aí a gente vai criar credenciais.

O que são essas credenciais? Bom para o redshift conseguir acessar o bucket S3 mesmo sendo da mesma conta na mesma conta. Ele precisa de credenciais que a gente vai criar, essas credenciais que são compostas de uma ID, uma chave.
Bom, aí finalmente a gente vai pro redshift e vai criar um comando lá que se chama Copie. E esse comando, copie, ele vai ter a tabela que vai ser populada, o endereço do arquivo lá no S3, a zona do bucket, a região do bucket S3, as credenciais e alguns outros parâmetros.
Então, dessa forma a gente vai popular este DataWarehouse, esse pequeno Datawarehouse, depois a gente vai criar uma tabela desnormalizada, então a gente vai fazer lá um Select com vários n joins e a gente vai criar uma tabela desnormalizada.

Por que a gente vai criar uma tabela desnormalizada? Para facilitar o acesso do usuário. Então, em vez do usuário lá, quando for criar o Dashboard, ele, em vez de ter que fazer junções de várias tabelas ou ter que digitar consultas SQL, ele vai ter tudo de uma tabela só.

Então, por exemplo, a mesma tabela já vai ter o nome do vendedor, não vai ter o IDvendedor, vai ter o nome do produto, em vez de ter o ID produto. 

Bom, a gente vai voltar para redshift. A gente vai mudar uma configuração lá para que seja possível acesso público, que por padrão não é. Aí sim, a gente vai no Google Data Studio, a gente vai conectar no Redshift. E aí então a gente vai criar o nosso test board ad hoc. Então vai ser uma um passo a passo bem legal e bem interessante de um tutorial prático bem interessante. E tenho certeza que você vai adorar. 
Bom falando então do modelo de dados, então esse modelo de dados aqui que você já conhece, você vai ter um script para criar este modelo de dados que está no material do curso.
Então a gente tem as vendas, os clientes, os itens, vendas, produtos e vendedores, certo?
Então a gente vai criar esse banco de dados. Este é o script para criar este banco de dados lá no redshift. Também bem semelhante não é igual ao que a gente utilizou lá no postgres, utilizando o schema. Quando a gente não utiliza schema, a gente está criando isso no schema público. 
Então, a gente não tem ali, por exemplo, dimensional o ponto de vendedores ou simplesmente vendedores, produtos, clientes, vendas e itens, vendas aqui e ali, além de algumas outras pequenas alterações.

Esse é o exemplo de um arquivo CSV que nós vamos utilizar para carregar os dados. Então são cinco arquivos CSV. Cada um vai carregar uma tabela.
