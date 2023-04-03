88. Criando Bancos de Dados e Tabelas
Bom, com o nosso servidor rodando, a gente pode então criar um banco de dados no nosso cluster.

Bom, o objetivo de um DataWarehouse como o Red Shift é fornecer processamento de dados, então você pode processar dados de uma forma geral e, claro, aplicações pode se conectar a redshift, isso pode ser feito por um driver ODBC, JDBC de várias formas.

O que a gente vai fazer aqui?A gente vai utilizar uma própria ferramenta interna que já vem aqui no AWS, então, se você clicar aqui no menu, você vai achar aqui editor de consultas, este aplicativo que ele vai utilizar para interagir com esse cluster que nós acabamos de criar, eu vou clicar nele, e aqui você pode ver o nosso editor de consultas ou query Editor, vejam que aqui você tem os clusters. 

Importante você precisa conectar o cluster, então ele está conectado.
Vejam que aqui existem dois bancos de dados.
Bom, aqui você tem um espaço que você pode criar consultas se você salvar.
Aqui você pode salvar a consulta, as consultas, elas vão ficar todas aqui. Aqui você pode gerenciar as consultas.
Existe também a opção aqui de notebooks, charts e aqui algumas configurações.

Bom, aqui eu vou então salvar essa consulta e vou dar um nome aqui DDR a ele que a gente vai utilizar para criar o nosso banco de dados.
Então aqui você vai digitar, create database ed;
Vamos chamar de ED o banco de dados.
Você pode ver aqui embaixo o resultado onde não teve erro. Vamos clicar aqui em Refresh para atualizar, vou expandir a lista aqui. Você pode ver que o banco de dados ed está aqui.

Agora a gente precisa criar toda a estrutura do banco de dados nas tabelas, conforme o schema que nós vimos no tutorial.

Você vai criar aqui uma nova guia, vou clicar aqui no editor, e se certifique de selecionar o banco de dados ED, senão você vai rodar o seu script no DEV, e não é o que a gente quer.

Então clica aqui no ED, e agora você vai abrir o script dessa sessão, você vai copiar e vai colar. Então, mais uma vez, junto ao material do curso, existe um script que você deve abrir com o editor de texto copiar e colar aqui, só isso aí.
Aí, depois que você colar aqui, vamos ver que você está definindo o formato da data.  Você está criando a tabela vendedores, a tabela de produtos, a tabela de clientes, a tabela de vendas, itens, venda. Você pode ver aqui que cada tabela tem sua chave primária. É um schema que nós já conhecíamos, de outras sessões em que também a gente viu no tutorial anterior.Então, agora você pode rodar esse script, porém, se certifique de não ter nada selecionado.
Você tem que estar só com o cursor clicado assim, sem nada selecionado, senão ele executa apenas o que foi selecionado.

Você vai executar mais uma vez, lembrando de estar conectado aqui no banco de dados que nós criamos, você pode ver aqui que ele abriu várias guias de resultado a cada uma e para uma consulta, ele considera consulta depois do ponto de vírgula.

Então, se você vir aqui, você vai ver que está tudo ok, então a gente está com nosso banco de dados criado.

Você vai ver que as cinco tabelas estão criadas aqui. Uma observação importante aqui, diferente lado do nosso estudo de caso, utilizando o banco de dados relacional e o modelo dimensional.
Lá nós utilizamos schemas aqui que está utilizando todo o esquema padrão, que é o sistema público, mas o RedShift tem suporte ao schema da mesma forma.
A gente apenas aqui não utilizou, ele usa por padrão o schema público, o que é perfeitamente normal e muito utilizado.