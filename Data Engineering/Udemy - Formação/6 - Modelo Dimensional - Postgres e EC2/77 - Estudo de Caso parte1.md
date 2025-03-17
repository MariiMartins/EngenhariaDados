- 77. Estudo de Caso Parte I
Então a gente vai voltar com o nosso caso prático.
E o objetivo agora é construir um armazém de dados para que o administrador da loja JJbike possa compreender o seu negócio.

Então, na sessão passada, nós construímos um sistema de transação para o negócio da JJBike operar onde tinha lá, por exemplo, o cadastro dos produtos, as vendas. Agora, ele precisa construir um armazém de dados para que os administradores da empresa possam fazer a gestão do negócio.

Uma arquitetura tradicional do armazém de dados obviamente, aqui, de forma simplificada, você vai ter uma estrutura de operação onde vai estar o sistema transacional.
Você vai ter uma estrutura de estocagem, onde vão estar os dados extraídos no formato intermediário e você vai ter o seu DataWarehouse, o seu armazém de dados com as informações gerenciais.
No nosso caso prático, obviamente que ele vai ser simplificado. Nós vamos separar o relacional e o dimensional pelo schema. Eles vão estar dentro de um mesmo banco de dados, num grande sistema para uma grande empresa, com um grande volume de dados. Obviamente que não é essa arquitetura que você vai encontrar, mas para fins didáticos, práticos, vai funcionar da mesma forma.

A ferramenta que nós vamos usar é o postgres que você já tem instalado e que você colocou. Já o sistema transacional a gente já construiu e carregou dados do sistema transacional, então a gente não tem que fazer nenhum tipo de instalação e configuração.

Nesta seção a gente vai apenas implementar o nosso modelo dimensional e aqui está o nosso modelo dimensional. Então, assim como modelo relacional, é importante que você conheça que você tenha familiaridade com este modelo para você saber o que você está fazendo lá.

Na parte prática, quando você rodar os scripts, quando você rodar as consultas, para consultar o modelo, então eu sugiro que você faça um print que você imprima, enfim, que você tenha familiaridade com este modelo.

Então, o modelo é o fator vendas. A gente está modelando as vendas da loja de bicicletas. Nós temos, além da fato, nós temos uma dimensão produto, uma dimensão cliente, uma dimensão tempo e uma dimensão vendedor.

Então, eu vejo que a dimensão cliente aqui ela tenha a chave substituta, que é chave cliente e tem o id cliente, que é a chave do sistema relacional. Da mesma forma que as outras dimensões, a chave produto que é a chave substituta e de produto a dimensão. O vendedor chave vendedor que é a chave substituta de vendedor é a chave do modelo relacional.

A dimensão tempo que nós falamos deixamos claro que é obrigatória, ela tem apenas uma chave substituta. Obviamente que não tem que manter integridade com o banco relacional, então ela tem apenas uma chave de ligação com a fato vendas.

E o que a gente tem aqui é data, onde vai ficar a data por extenso. Aqui, a data preciso dizer a data no formato dia, mês e ano. Depois nós temos separado aqui o dia, o mês, o ano, o dia da semana e o trimestre.
Uma dimensão tempo pode ter mais ou menos atributos, depende do tipo de modelagem. Então você pode colocar um indicadores se o dia é feriado, se é alta temporada, se é baixa temporada, se é inverno e verão, enfim, você pode colocar vários outros atributos aqui. A nossa dimensão tempo tem essas características.

A nossa fato vendas. Ela tem uma chave primária e as chaves estrangeiras para as quatro dimensões. Nós temos as quatro: medidas, quantidade do produto vendido, valor unitário, valor total e desconto.
Então, a gente pode perceber aqui que é um modelo dimensional com grau bem detalhado. A gente tem bastante detalhes, a gente tem a venda a nível de produto. Então a gente tem a ligação com o produto, com o vendedor, com o cliente e, com o tempo, o dia que a venda foi realizada. Ok, então é um modelo dimensional de vendas clássico, com algumas características específicas.

Vamos voltar aqui, por exemplo, para o cliente.
Nós temos o nome do cliente, o estado, sexo, status dele, que é aquela questão da fidelidade, e vejam aqui nós colocamos um indicador de validade no cliente, na dimensão produto e na dimensão o vendedor.

Então, por exemplo, se a gente precisar recarregar este modelo, nós temos: 
A data de validade é que se nós precisar refazer o modelo. E também se a gente quiser saber o início e a validade de cada item que foi incluído, na dimensão produto, então a gente tem a descrição do produto e produto e na dimensão, o vendedor tem o nome do vendedor em nome.
Então esse é o nosso modelo dimensional.


No próximo vídeo, a gente vai estudar este modelo dimensional com um pouco mais de detalhe. A gente vai entender como que a gente chegou a ter esse modelo.
O que você vai precisar baixar do ambiente? Você vai precisar baixar a dimensional, pontos IP, arquivo dimensional, pontos IP e você vai salvar ele no local padrão da sua máquina virtual.

Home Cloud vira download, assim como você fez lá no modelo relacional, os scripts que nós vamos utilizar.
Então nós temos cinco scripts.
A numeração aqui continua. Caso você baixe junto esses scripts com os scripts do modelo relacional, você não vai ter confusão.
Com relação à numeração, elas continuam no modelo relacional, parou no sete e a gente continua do oito.
Então a gente tem um script create table, que vai criar a estrutura das tabelas para a gente construir o nosso armazém de dados.
A gente tem um script, insert, dimensão, tempo Esse script é um código que vai criar, é popular, que vai popular a dimensão, tempo que ela vai estar criada, que vai popular a dimensão, tempo. Existe várias formas de você carregar a dimensão, tempo. Lembro que a gente falou que a dimensão tempo é previamente carregada. Ela fica pronta antes mesmo de você começar a carregar os fatos e as dimensões. Existem várias formas. Você pode carregar de um arquivo. Você gera, por exemplo, numa planilha, num programa, todas as datas você carrega ou você pode criar um script que o código gera, a data, a data pula automaticamente.
O iterativo é um código que nós vamos executar passo a passo, então este script aqui é o mais importante, porque ele vai carregar o Data Warehouse, vai fazer os processos de carga e a gente vai verificando as mudanças que vão ocorrendo no nosso DataWarehouse passo a passo. Então, esse é o script mais importante e é o processo mais longo aqui do nosso curso.
Na desnormalização nós vamos rodar um script, vai criar uma tabela desnormalizada, você sabe, já que é uma tabela desnormalizada, uma tabela que não tem a normalização, que não está na terceira forma normal, que é utilizada para ferramentas específicas de BI e também para BI self-service, por exemplo. E por fim, o último script 12 Nós vamos criar um copy e nós vamos criar um que vai colocar dados de meta nele. Nós vamos fazer algumas consultas nesse copy, vamos ver aqui. Então os scripts deles estão todos incompletos, então eles continuam aqui. A gente tem só o início dele.
Eu sugiro que você abra lá o script, dê uma estudada nele.

Então, o script dimensional, primeiro que ele faz, lembra o que a gente tinha lá a criação do esquema relacional, que é a primeira coisa que ele faz aqui, ele cria o schema dimensional. Todas as tabelas vão ser criadas dentro desse schema e depois ele começa a criação das tabelas dimensional, as cinco tabelas que nós vamos usar para o nosso modelo.
Então aqui está criando a dimensão vendedor e ter a criação da sequência para a chave primária para a chave substituta.
Esse script aqui ele faz a inserção da dimensão, tempo a que o script está completo.
Está tudo aqui, então ele faz o insert na dimensão tempo. A dimensão tempo foi criada no script anterior. Ela não aparece ali, mas ela está dentro do script oito.
A dimensão tempo tem data, dia, mês, ano, dia da semana e trimestre.
Então, o que ele faz aqui? Ele faz um select na data e extrai o dia, o mês, o ano, o dia da semana e o trimestre deste select aqui. E ele faz a inserção disso dentro da tabela dimensão tempo.
Então assim ele pula automaticamente a nossa dimensão, tempo.
Aqui a gente tem 1/1 do script interativa, um script bastante grande.
Nós vamos comentar esse script ainda antes da aula prática.
Passo a passo no próximo vídeo aqui.
O vídeo de desnormalização ele também não está completo.
A gente vai ver ele, mas o que ele faz?
Ele faz um select de, normaliza os dados e faz o Into o inteiro aqui.
No caso, ele cria uma outra tabela, que é o resultado de Select.
Então ele cria essa tabela dimensional, que é o esquema ponto dez, onde slide vendas.
Então ele vai criar uma tabela dez normalizada.
Uma tabela grande dez normalizada, quer dizer, sem chaves primárias e sem chaves estrangeiras das vendas, tudo em uma única tabela.
E, por fim, o último script é o que é ponto SQL.
Também aqui o script está incompleto, mas ele faz a criação também de uma tabela que vai se chamar aqui.
PI coloca dados das vendas.
Depois a gente altera esta tabela que pi e coloca uma coluna de cria, uma nova coluna meta e a gente vai pular esta coluna meta com os valores da meta.
Então como a gente vai ter venda, o total de vendas, linha, a gente pode comparar com a meta de cada venda.
