<<<<<<< HEAD
<<<<<<< HEAD
139. Criando Objetos no Postgres
Depois de todos os preparativos, a gente vai começar a implementar o nosso projeto, então alguns pontos aqui para a gente esclarecer. Você pode ver que eu já estou com o Colab aberto. E a gente vai criar um notebook e a gente vai trabalhar nesse notebook.

Se você viu, já que o notebook é dividido em células e cada etapa do projeto a gente vai criar uma célula. E o objetivo é que cada célula seja autossuficiente.
O que eu quero dizer com isso? 
Eu poderia criar uma única conexão com o banco de dados na primeira célula e eu poderia reaproveitar essa conexão em todas as outras células.
Mas eu vou fazer diferente. O que eu vou colocar? Eu vou repetir essa conexão em todas as células, de forma que você tenha todo o código necessário para aquela atividade na célula.

O que a gente precisa fazer? O nosso objetivo é ler os nomes de imagens que estão em um banco de dados e inventariar essas imagens em um banco de dados, ler imagens que estão em um bucket.

Então a gente tem várias etapas para fazer. Primeiramente, a gente tem duas etapas que eu vou chamar assim, de pré configuração. Se a gente tivesse aqui uma ferramenta como a gente fez lá com o RedShift, onde tinha uma ferramenta de gerenciamento, a gente poderia criar o banco de dados e a tabela através dessa ferramenta.

Porém, aqui eu optei por uma abordagem diferente. A gente vai utilizar o próprio Python para criar o banco de dados na instância do Postgres e depois para criar tabela.
Então, o que a gente vai fazer para criar este banco de dados? O segundo código que a gente vai fazer. Nossa segunda célula é para criar a tabela.
Então, a biblioteca você já sabe que para interagir com qualquer serviço do AWS, e aí sim, a gente vai conectar. Utilizando o S3 no bucket dentro da pasta do banquete do S três e a gente vai ler a relação de imagens. Primeiramente, a gente vai testar a leitura, a conexão do banquete e a leitura dessas imagens, utilizando, por exemplo, um print para ver se a gente consegue ler o nome das imagens.

No segundo momento, a gente vai atualizar essa mesma célula para que, no momento em que a gente tenha o nome da imagem, a gente já faça a gravação dela no banco de dados.

Bom, e aí depois a gente vai criar mais uma célula para testar se as imagens estão, de fato, de fato gravadas lá no banco de dados, então é isso que a gente vai fazer, que passo a passo eu vou fazer aqui, etapa por etapa e vou explicar aqui detalhadamente o que a gente está, a gente está executando.

Então aqui, com o Google Colab aberto, eu vou criar um novo notebook. Eu vou dar aqui o nome para o notebook e os dados, depois encontra se esse notebook junto com o material do curso.
E então nossa primeira lição. Nossa primeira célula aqui é para criar o banco de dados lá no servidor de banco de dados no RDS. Postgres o link que nós configuramos em etapa anterior. Então a primeira coisa a gente precisa importar a biblioteca Psycopg2, que é uma biblioteca para você conectar e interagir com o banco de dados PostgresSQL. Não necessariamente que esteja lá no RDS do AWS. Qualquer banco de dados possuído em qualquer lugar, desde que, claro, você tenha acesso a esse banco de dados, e essa biblioteca Psycopg2 ela já vem instalada aqui no ambiente do Colab, então eu não preciso instalá-la diferente do Boto3 que a gente vai ter que instalar depois.

Então basta fazer o import aqui Psycopg2, eu vou só rodar aqui para testar, se a importação aqui é o imposto da biblioteca, aqui vai rodar sem problema. Então, enquanto ele fica rodando aqui, ok, a gente viu ali o check in verde.
Então eu vou fazer uma conexão com o banco de dados. Então vou criar uma variável que eu vou chamar de com o método aqui então do Psycopg2.
O método Conecte, e aqui eu preciso passar todos os parâmetros necessários para mim fazer essa conexão. Bom, o primeiro parâmetro que eu preciso é o host, que nada mais é do que o endereço onde está esse banco de dados, o host e nada mais do que aqui no RDS do meu endpoint e o endereço do banco de dados na internet, através de um servidor de DNS, então basta você copiar aqui este endereço.
Bom, a gente não criou um banco de dados, então a gente vai conectar no banco de dados padrão Database, que é o Postgres, esse é o banco de dados padrão, vou dar um enter aqui. Outra coisa que precisa é o uso usuário e user também usuário padrão. Post com esse mesmo nome do banco de dados e o password.

Então são essas as informações que a gente precisa para conectar com o nosso banco de dados. Então ele precisa saber onde o banco, o banco de dados está, qual é o nome do banco de dados, lado, servidor de banco de dados, qualquer usuário, qualquer senha, ok? Bom, aí aqui eu vou colocar um parâmetro para a conexão que é o auto commit = to.

E aqui eu passo a instrução que eu quero executar, a primeira instrução que eu quero executar e criar o banco de dados. Então eu posso simplesmente chamar assim o clientedatabaseinventário;

Eu queria um banco de dados e aí, claro, eu preciso fechar a minha conexão, senão ela fica aberta com ponto, close.
Bom, agora a gente pode executar eventualmente e pode ter algum tipo, algum erro de digitação. Vamos rodar aqui. Bom, como não tenho retorno nenhum aqui ficou com o check in em verde. Quer dizer que deu certo. Se você tem algum erro, você precisa verificar se o erro é de sintaxe e se foi alguma coisa que você digitou errado ou se foi um problema de conexão, você precisa revisar o host, o banco de dados, o usuário, a senha, geralmente a mensagem.
Ali ela vai lhe dizer qual é o problema.

Ok, então a gente executou aqui a primeira etapa.A segunda etapa é a gente criar a tabela deste banco de dados. Então, para isso a gente vai utilizar aqui essa outra célula. Porém, eu vou copiar aqui o código, já que o que a gente vai fazer é parecido. Agora, preste atenção no que a gente precisa mudar aqui.
A primeira coisa é que nós já temos um banco de dados criado inventário e o objetivo dessa segunda célula criar tabela. Eu não quero criar tabela dentro do banco de dados porque eu quero criar a dentro do banco de dados que eu criei. Então importante aqui em Database. Agora você vai substituir Postgres por inventário. Ok, o banco de dados já está criado, nós criamos ele, então a gente pode. Substituir sem problema a outra coisa que eu preciso alterar e que eu não quero mais criar um banco de dados eu já tenho.

Agora eu quero criar a tabela. Como a conexão vai ser feita diretamente do banco de dados, inventário quando ele rodar, que o corpo do execute, rodar.
Ele já vai criar tabela dentro do banco de dados, correto?
Então, pra mim criar tabela, eu vou digitar aqui create table arquivos que vai ter o campo ID arquivo que é do tipo inteiro int e nome do arquivo que é do tipo varchar, então aqui eu fecho um parênteses. Então são dois parênteses o ponto e vírgula para sinalizar que eu terminei o comando.

=======
139. Criando Objetos no Postgres
Depois de todos os preparativos, a gente vai começar a implementar o nosso projeto, então alguns pontos aqui para a gente esclarecer. Você pode ver que eu já estou com o Colab aberto. E a gente vai criar um notebook e a gente vai trabalhar nesse notebook.

Se você viu, já que o notebook é dividido em células e cada etapa do projeto a gente vai criar uma célula. E o objetivo é que cada célula seja autossuficiente.
O que eu quero dizer com isso? 
Eu poderia criar uma única conexão com o banco de dados na primeira célula e eu poderia reaproveitar essa conexão em todas as outras células.
Mas eu vou fazer diferente. O que eu vou colocar? Eu vou repetir essa conexão em todas as células, de forma que você tenha todo o código necessário para aquela atividade na célula.

O que a gente precisa fazer? O nosso objetivo é ler os nomes de imagens que estão em um banco de dados e inventariar essas imagens em um banco de dados, ler imagens que estão em um bucket.

Então a gente tem várias etapas para fazer. Primeiramente, a gente tem duas etapas que eu vou chamar assim, de pré configuração. Se a gente tivesse aqui uma ferramenta como a gente fez lá com o RedShift, onde tinha uma ferramenta de gerenciamento, a gente poderia criar o banco de dados e a tabela através dessa ferramenta.

Porém, aqui eu optei por uma abordagem diferente. A gente vai utilizar o próprio Python para criar o banco de dados na instância do Postgres e depois para criar tabela.
Então, o que a gente vai fazer para criar este banco de dados? O segundo código que a gente vai fazer. Nossa segunda célula é para criar a tabela.
Então, a biblioteca você já sabe que para interagir com qualquer serviço do AWS, e aí sim, a gente vai conectar. Utilizando o S3 no bucket dentro da pasta do banquete do S três e a gente vai ler a relação de imagens. Primeiramente, a gente vai testar a leitura, a conexão do banquete e a leitura dessas imagens, utilizando, por exemplo, um print para ver se a gente consegue ler o nome das imagens.

No segundo momento, a gente vai atualizar essa mesma célula para que, no momento em que a gente tenha o nome da imagem, a gente já faça a gravação dela no banco de dados.

Bom, e aí depois a gente vai criar mais uma célula para testar se as imagens estão, de fato, de fato gravadas lá no banco de dados, então é isso que a gente vai fazer, que passo a passo eu vou fazer aqui, etapa por etapa e vou explicar aqui detalhadamente o que a gente está, a gente está executando.

Então aqui, com o Google Colab aberto, eu vou criar um novo notebook. Eu vou dar aqui o nome para o notebook e os dados, depois encontra se esse notebook junto com o material do curso.
E então nossa primeira lição. Nossa primeira célula aqui é para criar o banco de dados lá no servidor de banco de dados no RDS. Postgres o link que nós configuramos em etapa anterior. Então a primeira coisa a gente precisa importar a biblioteca Psycopg2, que é uma biblioteca para você conectar e interagir com o banco de dados PostgresSQL. Não necessariamente que esteja lá no RDS do AWS. Qualquer banco de dados possuído em qualquer lugar, desde que, claro, você tenha acesso a esse banco de dados, e essa biblioteca Psycopg2 ela já vem instalada aqui no ambiente do Colab, então eu não preciso instalá-la diferente do Boto3 que a gente vai ter que instalar depois.

Então basta fazer o import aqui Psycopg2, eu vou só rodar aqui para testar, se a importação aqui é o imposto da biblioteca, aqui vai rodar sem problema. Então, enquanto ele fica rodando aqui, ok, a gente viu ali o check in verde.
Então eu vou fazer uma conexão com o banco de dados. Então vou criar uma variável que eu vou chamar de com o método aqui então do Psycopg2.
O método Conecte, e aqui eu preciso passar todos os parâmetros necessários para mim fazer essa conexão. Bom, o primeiro parâmetro que eu preciso é o host, que nada mais é do que o endereço onde está esse banco de dados, o host e nada mais do que aqui no RDS do meu endpoint e o endereço do banco de dados na internet, através de um servidor de DNS, então basta você copiar aqui este endereço.
Bom, a gente não criou um banco de dados, então a gente vai conectar no banco de dados padrão Database, que é o Postgres, esse é o banco de dados padrão, vou dar um enter aqui. Outra coisa que precisa é o uso usuário e user também usuário padrão. Post com esse mesmo nome do banco de dados e o password.

Então são essas as informações que a gente precisa para conectar com o nosso banco de dados. Então ele precisa saber onde o banco, o banco de dados está, qual é o nome do banco de dados, lado, servidor de banco de dados, qualquer usuário, qualquer senha, ok? Bom, aí aqui eu vou colocar um parâmetro para a conexão que é o auto commit = to.

E aqui eu passo a instrução que eu quero executar, a primeira instrução que eu quero executar e criar o banco de dados. Então eu posso simplesmente chamar assim o clientedatabaseinventário;

Eu queria um banco de dados e aí, claro, eu preciso fechar a minha conexão, senão ela fica aberta com ponto, close.
Bom, agora a gente pode executar eventualmente e pode ter algum tipo, algum erro de digitação. Vamos rodar aqui. Bom, como não tenho retorno nenhum aqui ficou com o check in em verde. Quer dizer que deu certo. Se você tem algum erro, você precisa verificar se o erro é de sintaxe e se foi alguma coisa que você digitou errado ou se foi um problema de conexão, você precisa revisar o host, o banco de dados, o usuário, a senha, geralmente a mensagem.
Ali ela vai lhe dizer qual é o problema.

Ok, então a gente executou aqui a primeira etapa.A segunda etapa é a gente criar a tabela deste banco de dados. Então, para isso a gente vai utilizar aqui essa outra célula. Porém, eu vou copiar aqui o código, já que o que a gente vai fazer é parecido. Agora, preste atenção no que a gente precisa mudar aqui.
A primeira coisa é que nós já temos um banco de dados criado inventário e o objetivo dessa segunda célula criar tabela. Eu não quero criar tabela dentro do banco de dados porque eu quero criar a dentro do banco de dados que eu criei. Então importante aqui em Database. Agora você vai substituir Postgres por inventário. Ok, o banco de dados já está criado, nós criamos ele, então a gente pode. Substituir sem problema a outra coisa que eu preciso alterar e que eu não quero mais criar um banco de dados eu já tenho.

Agora eu quero criar a tabela. Como a conexão vai ser feita diretamente do banco de dados, inventário quando ele rodar, que o corpo do execute, rodar.
Ele já vai criar tabela dentro do banco de dados, correto?
Então, pra mim criar tabela, eu vou digitar aqui create table arquivos que vai ter o campo ID arquivo que é do tipo inteiro int e nome do arquivo que é do tipo varchar, então aqui eu fecho um parênteses. Então são dois parênteses o ponto e vírgula para sinalizar que eu terminei o comando.

>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
=======
139. Criando Objetos no Postgres
Depois de todos os preparativos, a gente vai começar a implementar o nosso projeto, então alguns pontos aqui para a gente esclarecer. Você pode ver que eu já estou com o Colab aberto. E a gente vai criar um notebook e a gente vai trabalhar nesse notebook.

Se você viu, já que o notebook é dividido em células e cada etapa do projeto a gente vai criar uma célula. E o objetivo é que cada célula seja autossuficiente.
O que eu quero dizer com isso? 
Eu poderia criar uma única conexão com o banco de dados na primeira célula e eu poderia reaproveitar essa conexão em todas as outras células.
Mas eu vou fazer diferente. O que eu vou colocar? Eu vou repetir essa conexão em todas as células, de forma que você tenha todo o código necessário para aquela atividade na célula.

O que a gente precisa fazer? O nosso objetivo é ler os nomes de imagens que estão em um banco de dados e inventariar essas imagens em um banco de dados, ler imagens que estão em um bucket.

Então a gente tem várias etapas para fazer. Primeiramente, a gente tem duas etapas que eu vou chamar assim, de pré configuração. Se a gente tivesse aqui uma ferramenta como a gente fez lá com o RedShift, onde tinha uma ferramenta de gerenciamento, a gente poderia criar o banco de dados e a tabela através dessa ferramenta.

Porém, aqui eu optei por uma abordagem diferente. A gente vai utilizar o próprio Python para criar o banco de dados na instância do Postgres e depois para criar tabela.
Então, o que a gente vai fazer para criar este banco de dados? O segundo código que a gente vai fazer. Nossa segunda célula é para criar a tabela.
Então, a biblioteca você já sabe que para interagir com qualquer serviço do AWS, e aí sim, a gente vai conectar. Utilizando o S3 no bucket dentro da pasta do banquete do S três e a gente vai ler a relação de imagens. Primeiramente, a gente vai testar a leitura, a conexão do banquete e a leitura dessas imagens, utilizando, por exemplo, um print para ver se a gente consegue ler o nome das imagens.

No segundo momento, a gente vai atualizar essa mesma célula para que, no momento em que a gente tenha o nome da imagem, a gente já faça a gravação dela no banco de dados.

Bom, e aí depois a gente vai criar mais uma célula para testar se as imagens estão, de fato, de fato gravadas lá no banco de dados, então é isso que a gente vai fazer, que passo a passo eu vou fazer aqui, etapa por etapa e vou explicar aqui detalhadamente o que a gente está, a gente está executando.

Então aqui, com o Google Colab aberto, eu vou criar um novo notebook. Eu vou dar aqui o nome para o notebook e os dados, depois encontra se esse notebook junto com o material do curso.
E então nossa primeira lição. Nossa primeira célula aqui é para criar o banco de dados lá no servidor de banco de dados no RDS. Postgres o link que nós configuramos em etapa anterior. Então a primeira coisa a gente precisa importar a biblioteca Psycopg2, que é uma biblioteca para você conectar e interagir com o banco de dados PostgresSQL. Não necessariamente que esteja lá no RDS do AWS. Qualquer banco de dados possuído em qualquer lugar, desde que, claro, você tenha acesso a esse banco de dados, e essa biblioteca Psycopg2 ela já vem instalada aqui no ambiente do Colab, então eu não preciso instalá-la diferente do Boto3 que a gente vai ter que instalar depois.

Então basta fazer o import aqui Psycopg2, eu vou só rodar aqui para testar, se a importação aqui é o imposto da biblioteca, aqui vai rodar sem problema. Então, enquanto ele fica rodando aqui, ok, a gente viu ali o check in verde.
Então eu vou fazer uma conexão com o banco de dados. Então vou criar uma variável que eu vou chamar de com o método aqui então do Psycopg2.
O método Conecte, e aqui eu preciso passar todos os parâmetros necessários para mim fazer essa conexão. Bom, o primeiro parâmetro que eu preciso é o host, que nada mais é do que o endereço onde está esse banco de dados, o host e nada mais do que aqui no RDS do meu endpoint e o endereço do banco de dados na internet, através de um servidor de DNS, então basta você copiar aqui este endereço.
Bom, a gente não criou um banco de dados, então a gente vai conectar no banco de dados padrão Database, que é o Postgres, esse é o banco de dados padrão, vou dar um enter aqui. Outra coisa que precisa é o uso usuário e user também usuário padrão. Post com esse mesmo nome do banco de dados e o password.

Então são essas as informações que a gente precisa para conectar com o nosso banco de dados. Então ele precisa saber onde o banco, o banco de dados está, qual é o nome do banco de dados, lado, servidor de banco de dados, qualquer usuário, qualquer senha, ok? Bom, aí aqui eu vou colocar um parâmetro para a conexão que é o auto commit = to.

E aqui eu passo a instrução que eu quero executar, a primeira instrução que eu quero executar e criar o banco de dados. Então eu posso simplesmente chamar assim o clientedatabaseinventário;

Eu queria um banco de dados e aí, claro, eu preciso fechar a minha conexão, senão ela fica aberta com ponto, close.
Bom, agora a gente pode executar eventualmente e pode ter algum tipo, algum erro de digitação. Vamos rodar aqui. Bom, como não tenho retorno nenhum aqui ficou com o check in em verde. Quer dizer que deu certo. Se você tem algum erro, você precisa verificar se o erro é de sintaxe e se foi alguma coisa que você digitou errado ou se foi um problema de conexão, você precisa revisar o host, o banco de dados, o usuário, a senha, geralmente a mensagem.
Ali ela vai lhe dizer qual é o problema.

Ok, então a gente executou aqui a primeira etapa.A segunda etapa é a gente criar a tabela deste banco de dados. Então, para isso a gente vai utilizar aqui essa outra célula. Porém, eu vou copiar aqui o código, já que o que a gente vai fazer é parecido. Agora, preste atenção no que a gente precisa mudar aqui.
A primeira coisa é que nós já temos um banco de dados criado inventário e o objetivo dessa segunda célula criar tabela. Eu não quero criar tabela dentro do banco de dados porque eu quero criar a dentro do banco de dados que eu criei. Então importante aqui em Database. Agora você vai substituir Postgres por inventário. Ok, o banco de dados já está criado, nós criamos ele, então a gente pode. Substituir sem problema a outra coisa que eu preciso alterar e que eu não quero mais criar um banco de dados eu já tenho.

Agora eu quero criar a tabela. Como a conexão vai ser feita diretamente do banco de dados, inventário quando ele rodar, que o corpo do execute, rodar.
Ele já vai criar tabela dentro do banco de dados, correto?
Então, pra mim criar tabela, eu vou digitar aqui create table arquivos que vai ter o campo ID arquivo que é do tipo inteiro int e nome do arquivo que é do tipo varchar, então aqui eu fecho um parênteses. Então são dois parênteses o ponto e vírgula para sinalizar que eu terminei o comando.

>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
Então, a gente está criando então a tabela Arquivos, que vai ter o CD do arquivo, que é inteiro, e o nome do arquivo baixar. Então, lembrando lá no briefing, introdução que nós vamos armazenar no banco de dados, um dos nomes o arquivo, não o arquivo em si, apenas os nomes. Vamos executar aqui. E vê se então, mais uma vez que deu certo. Lembrando, então, que se você tiver algum erro, a primeira coisa é ler a mensagem. Pode ser um tipo aqui no script. Na conexão não vai ser esse. Se você já teve a conexão corretamente anteriormente, provavelmente pode ser algum problema aqui no cliente tb ok. Bom, então tudo certo.