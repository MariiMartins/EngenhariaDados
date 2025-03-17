52. Criando e Populando Banco de Dados
Agora a gente vai criar um diretório onde a gente vai baixar o material, os scripts do curso que a gente vai precisar para criar o nosso banco de dados.
 Então, primeiramente, que eu vou mudar para o usuário postgrees. Então o sudo su - postgres. Então, para isso a gente vai alternar aqui para o usuário postgres. Então, agora a gente está. Você pode ver aqui o que a gente está logado com o usuário postgres. Agora, se você executar aqui um PWD, o comando PWD dele mostra o diretório atual e se o diretório home do usuário possui eles, então é aqui que a gente vai baixar o nosso script.

Primeiro vamos criar uma pasta. Aqui para a gente baixar os arquivos. Então, mkdir relacional Para criar um diretório, vou criar um diretório chamado relacional.
Já a gente está estudando bancos de dados relacionais. Vamos entrar nesse diretório, então o CD relacional. Então vamos listar aqui. Você pode ver que o diretório está está vazio.

E agora a gente pode então baixar o arquivo.
Então a gente já falou do wget https://www.datascientist.com.br/engdados/relacional.zip
Ok, então você pode ver que ele baixou o arquivo.

Agora eu vou dar o LS aqui. A gente pode ver que o relacionado pontos IP está baixado. Agora a gente vai usar o programa, unzip que nós instalamos lá no início para descompactar esse arquivo. Então, unzip.

Relacional.zip
Então ele fez a descompactação. Então, aqui estão todos os scripts que nós falamos ou para criar tabela, inserir clientes, inserir produtos, inserir vendedores, vendas, itens, vendas e depois o interativo que aquilo que a gente vai executar passo a passo.
Se você quiser ver o conteúdo do arquivo, pode fazer o comando cat, por exemplo, que é de Create Table, e aqui você pode ver todo o conteúdo desse arquivo.

Então você está vendo o que ele define o estilo da data. Ele cria um esquema relacional. Ele cria uma sequência para ir de vendedor, cria tabela a vendedores, tabela produtos. Ele cria todo o banco de dados que nós já conhecemos, que nós já estudamos, ok. Bom, agora, então a gente pode logar no programa PSQL é um shell e é um programa de linha de comando do post do SQL. Então, no PSQL que ele pode fazer tudo, a gente pode consultar tabelas, a gente pode criar bancos de dados, inserir dados. A gente pode fazer qualquer coisa lá relacionado ao post do SQL.

Então vamos lá. Vamos executar PSQL. Eu vou limpar a tela aqui. Então você pode ver que o prompt que mudou para postgres. Então isso quer dizer que a gente está logado no PSQL, que ele é a primeira coisa que vamos aqui executar um barra list, ele lista os bancos de dados que existem aqui nesse servidor de banco de dados e a gente pode ver aqui que existe o banco de dados postgres, que é um banco de dados administrativo, template zero e Template um, que são modelos de banco de dados.
Então esses bancos de dados aqui eles são criados automaticamente na instalação do postgres.
A gente vai criar o nosso próprio banco de dados e o nosso nosso banco de dados.
Eu vou chamar aqui de Ed.

Então eu vou chamar aqui o comando Create Database ED;

Então, com este comando a gente vai criar um novo banco de dados. Então ele retorna ali, CREATE DATABASE.

Se a gente executar novamente o list, você pode ver que o ED agora apareceu aqui na nossa lista. Obviamente que este banco, por ter sido criado agora, é um banco de dados vazio. Ele não tem nada nele.

O que a gente precisa fazer agora? Agora a gente precisa posicionar a linha de comando aqui. Do nosso console neste bucket. Então a gente executa:
\c ed
E veja o que ele está dizendo que nós agora estamos conectados ao banco ed.
Você pode ver aqui que o prompt mudou. Antes estava conectado no banco de dados postgres, que é o banco de dados administrativo que já vem instalado no banco de dados padrão.

Agora a gente mudou a gestão no Banco ED.

Então, por que a gente precisa fazer isso? Porque no momento que a gente vai fazer alguma coisa, criar alguma tabela, inserir dados, enfim, isso vai acontecer no banco de dados onde o aplicativo que estiver posicionado. Então, se a gente não mudasse o banco de dados ED, ele ia criar tudo lá no banco de dados Postgres, isso não seria uma coisa boa.

Bom, então agora a gente vai executar os scripts de 1 até 6. Então, se você lembrar o script 1, ele cria toda a estrutura de tabelas e o script de 2 até 6 inserem dados.

Para a gente executar o script aqui eu uso o comando (\i) e eu tenho que passar o caminho deste script. Então, se você lembrar, a gente fez o download lá dos arquivos neste comando e neste caminho. Aqui, o relacional e aí o primeiro. Aqui eu vou digitar uma que eu digitei 1 ponto e tab. Ele já completou para mim porque só tenho um arquivo que começa com 1.

Então veja, eu estou dizendo pra ele que aí executar o script. Aqui está o caminho completo do script. Então agora eu posso dar entre aqui e você pode vir aqui que a gente não teve nenhum erro. Então você pode ver que ele criou um schema. O schema que a gente viu lá tem o relacional. Ele criou a sequência, tabela, sequência, tabela, sequência, tabela.

Então a sequência é o código alto incremento, que dá o identificador da tabela. Então aqui a gente criou todas as tabelas do nosso banco de dados.

Agora, essas tabelas todas estão vazias. A gente precisa, popular elas, então a gente vai executar os demais scripts.
Então eu vou começar aqui pelo script 2, que é os insert clientes.
Então um série de clientes vai inserir todos os nossos clientes, ou então você pode vir aqui que ele executou todas as inserções. Não tivemos erros.
Vamos agora para o script 3, então eu vou só digitar aqui três ponto. Ele vai inserir todos os produtos, então aqui são os tipos dos produtos, ele tem dez tipos de produtos.
Agora a gente pode usar o script 4 script quatro. Vai inserir os vendedores, então, insert vendedores estão também aqui. A gente tem dez vendedores que são inseridos.
Agora, o script, 5. Ele vai inserir as vendas. Então esse é o script um pouco maior, né? Ele vai inserir todas as vendas.
E o último script que vai deixar nosso banco de dados pronto para ser utilizado. A gente vai inserir os itens vendas, insert, itens, vendas, SQL. Então, esse foi o script mais longo, porque cada cada venda vai ter uma ou mais itens de venda.
Agora a gente pode executar aqui o Barra ed, que ele falou que não encontrou nenhuma relação.
Vamos fazer dt*.*
Então vejo aqui que ele está mostrando todas as tabelas, mas ele está mostrando também tabelas de outros Schema. Então a gente vai navegando aqui, lá no final, a gente vai achar o nosso schema relacional e as nossas tabelas, clientes, itens, venda, produtos, vendas e vendedores.
Então o nosso banco de dados está criado, a partir do próximo tutorial, a gente vai começar a interagir, a consultar, realizar consultas nesse banco de dados para a gente encerrar aqui e voltar para o pronto.

