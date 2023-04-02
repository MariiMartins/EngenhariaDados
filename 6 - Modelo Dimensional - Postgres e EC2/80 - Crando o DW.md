- 80. Criando o DW
Eu estou conectado na mesma instância da sessão anterior, onde a gente estudou o modelo relacional.
Por que? Porque, como já explicou anteriormente, é uma continuação daquela aula.

Antes a gente criou um modelo relacional e a gente vai criar um modelo dimensional, mas no mesmo banco de dados, que a gente vai carregar o nosso modelo dimensional com os mesmos dados, então ele vai carregar dados Operacionais de um banco de dados operacional para um banco de dados analítico, para um banco de dados
dimensional.

Então é importante você conectar na mesma instância que já tem o post e o banco de dados instalado.
Primeira coisa aqui é ter certeza a gente vai estar com o usuário postgres, então, se você desconectou, ele não vai estar mais. Você precisa conectar de novo.
Vamos fazer que um PWD para a gente ver aqui o nosso diretório Home. Antes a de baixar os arquivos dos scripts, vamos criar aqui uma pasta e mkdir dimensional vai executar aqui, vamos criar um diretório chamado dimensional.
Vamos nos posicionar nesse diretório e vamos baixar o arquivo Zip.
Então wget HTTPS://www.datascientist.com.br/engdados/dimensional.zip
Vão ver que está tudo certo.Baixou, Vamos dar aqui um LS. Ali está ele.
Agora vamos descompactar unzip dimensional.zip e pronto. Aqui estão os scripts que nós vamos utilizar neste tutorial.

Então os 2 primeiros scripts a gente vai executar e os demais a gente vai rodar passo a passo pra gente entender o que está acontecendo. Vamos dar uma olhada no interativo, então eu vou dar um gat no oito que é o createtable.

Este script, ele faz a criação de todas aquelas tabelas que nós olhamos lá, nos nas aulas passadas.
A dimensão vendedor, a dimensão cliente, a dimensão produto, a dimensão tempo que nós vamos rodar  o script para popular ela. A fato, nós temos uma única fato que é fato venda, então nós temos a nossa fato com as suas dimensões, que vão ser carregadas a partir do banco de dados.

Relacionar o medo da operação da empresa.
Ou então agora, se a gente pode se conectar ao PSQL Vamos alternar aqui para o banco de dados Ed.
Então é //CD Então agora estamos conectados ao banco de dados do IDH e agora a gente pode carregar os scripts.
Então o primeiro vai criar toda a estrutura de tabelas, dimensões, as tabelas dimensionais e a tabela, as tabelas, fatos e as dimensões.
A única tabela fato com suas tabelas, dimensões e depois o script nove vai inserir dados na dimensão, tempo que, como a gente comentou, geralmente ela e ela vem pré carregada, então vamos lá.
Barra var barra lib, barra post grey SQL, barra barra var bali lib barra post gris, SQL dimensional e o primeiro item aqui é o oito ponto.
Ceate tempo este create they voltar. Ele cria também um esquema dimensional.
Ok, então está no mesmo banco de dados, porém, antes é o esquema relacional.
Agora a gente criou n. Você pode ver que o primeiro passo ali eu criei sistema. Ele cria o esquema dimensional.
Agora a gente vai rodar o script nove, que vai pular a tabela, dimensão, tempo.
Ok, então ele cria, ele, faz.
Ele pula um intervalo de tempo aí para essa tabela, certo?
Bom, então aí a gente tem a nossa estrutura de tabelas prontas, ok?
E pra gente ter certeza aqui, por exemplo, como é um banco que vai ser populado ainda, com exceção da dimensão tempo, as demais tabelas deve estar vazia. Vou dar uma olhada aqui. 7* então agora o esquema é o dimensional e aqui tem, por exemplo, a dimensão, tempo, a dimensão, tempo.
A gente pode consultar ela que ela está já populada com um grande intervalo de datas.
Mas agora, por exemplo, se a gente pesquisar, a gente consultar a tabela Fato Vendas, que é a nossa única tabela, fato ela está vazia ou você vê só o esquema da tabela aqui?
Então, a partir do próximo tutorial, então a gente vai começar a construir este armazém de dados, a popular aí colocar dados nesse armazém de dados.