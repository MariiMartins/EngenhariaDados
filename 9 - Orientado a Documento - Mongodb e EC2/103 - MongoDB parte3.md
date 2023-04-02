103. Mongodb Parte III
Então a gente vai ver a função IN que a gente pode vêr ela sendo utilizada aqui depois do cifrão característico, linha semelhante ao que nós vimos lá no SQL. No postgres, ele vai buscar o valor dentro do conjunto, ou seja, ele vai verificar postagens que estejam dentro do conjunto, que sejam ou produtos caros ou loja suja. Obviamente que aqui poderiam ter mais valores separados por vírgulas.
Então vejam aqui o resultado. Postagem loja suja ou postagem produtos caros. O resultado aqui é semelhante ao uso do OR. 

A projeção é como se eu eliminasse o asterisco de uma consulta select e definisse nomes de colunas específicas que eu quero que vendam o resultado. Só que aqui no mongo isso funciona um pouquinho diferente. Eu preciso colocar o nome da coluna, o zero (ele não inclui a coluna), o 1 ele inclui. Porém, você não pode misturar. Você não pode colocar zeros e uns você tem que escolher as colunas que ficam ou as colunas que não vão ser exibidas. Então, aqui, por exemplo, eu estou usando o post.find.
Estou criando um filtro para José para exibir apenas os documentos que tenho no campo nome José. E estou retirando Estou colocando como zero o ID e o próprio nome que eu já sei que os documentos que ele retornar aqui 
o nome são José. Então os campos que sobraram são postagem e data, eu tirei o ID e o nome.

O limite. Ele traz apenas os registros especificados aqui no parâmetro do limite. Então, eu estou usando aqui a função dB.post.find().limit(2), que a gente já conhece e delimitando a dois registros no resultado.
Num comando SQL, isso seria equivalente à função top depois do Select.


Aqui e o ordenar o que ia ser equivalente a um Order by
Eu tenho aqui um dB.posts.find() , Depois eu incluo a função sort()
Eu passo aqui o nome da coluna dois pontos, um para ordem crescente e -1 para ordem decrescente.
Obviamente que eu poderia colocar aqui vários campos. Eu só iria mudar aqui que eu teria que colocar um colchetes e separar esses campos por virgula delimitados, cada um dentro do seu parentes das suas chaves.
Lembrando então que a ordenação 1 é crescente e -1 é decrescente.

Uma função interessante do Mongo é que você pode concatenar funções.
Então vejam ele está usando aqui a função find que você já conhece.
A gente está usando aqui o sort, que nós acabamos de estudar e aqui também concatenar o limit que a gente também já tinha estudado. Então eu estou buscando ordenado por nome, de forma decrescente, limitando o meu resultado a dois registros.

Falando então de atualização de documentos.
Então, as principais funções de atualização do Mongo são o update, que faz uma atualização normal semelhante à de um banco de dados relacional.
E o Save, o save tem uma característica importante se o documento existe, ele atualiza, Se não ele inclui. Então ele é um misto de insert e update. Ele mistura as duas funções, é uma função interessante.
Então, vejam aqui: A gente localiza um documento onde o nome é André, ele retorna que este documento, e aqui, a gente tem essa função de um update, então aqui nesse primeiro parâmetro da função nós estamos fazendo a busca onde for André.  Ou seja, ele vai atualizar essa equivalente e cláusula where, no nosso select e aqui o cifrão set é o campo que eu vou atualizar.  De novo, aqui eu posso atualizar vários campos separando por vírgula e colocando entre colchetes. Então ele está me dizendo aqui que eu quero atualizar o registro que retorne com o filtro André passando a idade para 29.
E aqui aquilo está me dizendo que ele teve um Matched de um e modificou um registro. Depois, a gente faz aqui uma nova busca no registro de André e veja que a idade que era 15 passou para 29.

Excluir documentos. Então aqui tem várias funções:
•	o deleteOne(), ele exclui um único documento, mesmo que o critério retorne vários. Então, se você criar um critério lá que vai retornar vários, ele só vai excluir o primeiro.
•	O deleteMany(), exclui todos os documentos que atendam o critério.
•	e o remove(), exclui todos os documentos da coleção sem critério nenhum.
Então vejo aqui a gente localiza o registro do documento, cujo nome é André.
Depois a gente faz o deleteOne(), onde o nome é o André. Ele está dizendo aqui que a contagem de exclusão foi um e depois a gente faz uma busca novamente. A gente faz um find com o André e ele não retorna aqui nenhum registro.

Para excluir uma coleção. Você quer excluir a coleção inteira, então você pode usar a função DB no nome da coleção Drop. Ele está dizendo aqui que a exclusão foi feita aqui. A gente tentou excluir a coleção de novo e ele retornou falso porque a coleção não mais existia.

Outros comandos aqui bastante importantes que nós usamos no Mongo DB:
•	o comando DB verifica o banco que está sendo utilizado, então os comandos são executados sobre o banco de dados que está atualmente ativo.  Então você tem que verificar qual é esse banco. Você pode mudar o banco ativo usando o USE que a gente já viu.
•	show dbs lista todos os bancos de dados existentes no servidor.
•	o dB.dropDatabase() exclui o banco de dados corrente, o banco de dados que está sendo usado.
•	e o Show Collection exibe as coleções existentes no banco de dados.

Como é que a gente faz um backup no Mongo?
Então existe um aplicativo que é o Mongo Dump, então o Mongo Dump você não vai usar ele dentro do console do Mongo, você volta para o console do Linux, para o Shell, do Linux e o padrão é lá. Você vai executar o aplicativo Mongo Dump. Então aqui, um exemplo que nós vamos criar nós vamos executar na prática. Depois a gente, como superusuário, cria um diretório aonde a gente vai criar o nosso backup e aí sim a gente executa como superusuário o aplicativo Mongo Dump, Aqui ele está dizendo onde ele vai gerar este backup, A gente escolheu o diretório que a gente criou e aqui está dizendo qual banco de dados, porque a gente pode ter muitos bancos de dados no mongoDB Nós queremos fazer o backup depois, Aqui a gente executa o comando. LS Dentro lá do diretório que foi criado. Mas veja o que ele cria um diretório com o nome do banco de dados e o que a gente encontra lá? Dois arquivos, o arquivo BSON e o arquivo JSON, que são os backups do banco de dados. Então a gente confirma que o backup foi criado.

Restauração.
Então existe também um aplicativo para restauração que o Mango Restore para restaurar. Ele também é o aplicativo que você vai usar no Shell, não dentro do Mongo lá. Então qual o caso prático que a gente vai ver lá?
A gente vai logar no mongo através do Shell. A gente vai direcionar para o nosso banco de dados que a gente está utilizando. A gente vai excluir o nosso banco de dados que a gente criou na aula prática. A gente vai tentar encontrar os nossos documentos lá e aqui não vai retornar documento nenhum, porque a gente excluiu o que a gente vai fazer. Aí a gente sai do mongo, entra no Shell e executa este comando aqui:
sudo mongorestore/home/cloudera/bkpmongo
Porque aquele é o diretório onde nós criamos o backup, onde a gente já vai ter criado o backup. Depois a gente loga de volta no Shell do Mongo e testa lá se os dados estão restaurados. A gente tenta recuperar os documentos lá para ver se os dados estão restaurados.

Exportar dados.
Então existe uma função também para exportação de dados, um utilitário que é o Mongo Export. Você pode exportar por padrão no formato JSON, mas você também pode exportar em outros formatos, por exemplo, como o CSV.
Então, aqui a gente cria um diretório onde a gente vai salvar os dados. Depois a gente executa la como superusuário. Mongo Exports, o bom banco de dados que nós queremos exportar. Qual coleção do banco de dados é o arquivo de saída, o arquivo onde ele vai gerar os dados exportados e nós podemos também importar dados.

E para o caso prático de importação, nós vamos utilizar o arquivo que nós vamos baixar, que está no ambiente do curso. São um dos dois arquivos que você baixou dessa seção que está dentro do arquivo zip. Então, pra importar dados, a gente usa o utilitário Mongo Import, banco de dados, a coleção e o arquivo.A gente aponta lá para o local do arquivo. Aqui, no caso, ele vai estar no download. O nome do arquivo é pos ponto, Jason, então você deve baixar o arquivo Low Secure, o zip para a VM, para o diretório padrão de download.

