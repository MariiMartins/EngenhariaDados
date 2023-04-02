95. Construindo Dashboad "ad roc"
Então agora, com tudo pronto, o nosso objetivo é criar um dashboard no Google Data Studio. 
E como eu mencionei, o que a gente vai fazer aqui é o que a gente chama de uma criação, de um objeto de dados ad hoc, ou seja, sem nenhum planejamento.

Aqui a gente vai pegar uma conexão com uma tabela que foi modelada de forma bem simples. Eu não vou ter que fazer nenhum tipo de junção, eu tenho todas as informações deles normalizadas e eu vou explorar essa tabela criando alguns objetos visuais sem nenhum planejamento, como se eu fosse, de fato, o usuário final.

Então a gente vai utilizar o Google Data Studio. Como se chega até o Google do estúdio? Você pode pegar o próprio Google, pesquisar Google Data Studio e você vai clicar no link que vai trazer aqui.
Se essa for a primeira vez que você vai logar com sua conta do Google, com certeza você já tem uma conta no Google, você pode usar a sua conta do Google para logar. Uma vez que você logou no Google Data Studio, você vai estar nessa interface aqui. Então, vejam que aqui existem alguns modelos de dashboards, que ele chama aqui de relatório.

Bom, o que a gente vai fazer? Que a gente vai criar um relatório novo. Então, para isso você vai clicar aqui relatório em branco e é claro que o Google quer saber de onde esses dados vão vir. 
E o Google te sugere uma integração muito grande já com as ferramentas do próprio Google. Então vai aparecer que o Google Analytics, Google ADS, planilhas do Google, Big Query, que é a ferramenta de DataWarehouse do Google. Mas se você navegar aqui, existe conexão praticamente para tudo o que a gente quer. A gente quer o redshift. Se não está aparecendo para você, é só você vir aqui e pesquisar e digitar. 

Então vejam que ele está pedindo aqui uma autenticação do tipo básica ou uma URL JDBC. A gente pode fazer das duas formas ok. A gente vai utilizar o básico aqui, que é pelo IP. Então, se você lembrar, eu pedi para você copiar aqui o endpoint. Então você vai colar o endpoint do seu cluster, que vai ser diferente do meu. Agora, quando você copia o endpoint, ele já vem aqui com a porta e com o banco de dados padrão. Então a gente vai ver e vai remover isso.
Importante você vai remover daqui a porta e o banco de dados, Então você vai deixar só o endereço do cluster redShift (e aí é que importa).
Você vai colocar a porta que é 5439 em um banco de dados.
Então, assim você está pronto para autenticar. Então eu vou clicar aqui em Autenticar e vejam que ele me traz aqui tabelas. Então tem todas as tabelas que a gente criou lá no nosso banco de dados, mas o que interessa para nós é o fato vendas.

Opcionalmente, eu posso criar uma consulta personalizada, que é um SQL que vai ser abstraído e vai aparecer lá para o usuário.
Como? Uma tabela desnormalizada. Só que a gente já fez isso que é nossa fato Vendas..

Então eu vou clicar aqui em Fato Vendas se você tiver algum problema aqui, se você não conseguir conectar. Primeiro verifica se você copiou direitinho o nome, copiou e colou direitinho o nome do endPoints.

Se ele está sem a porta e sem o banco de dados, certifique se de que o acesso público do banco está liberado e você também pode ir lá. Naquelas configurações que eu mostrei da VPC também, você pode revisar lá se a permissão, vamos dizer sim, para o cluster ser acessado externamente.

Bom, nesse ponto, então eu vou clicar em Adicionar. Então agora ele vai adicionar que a fonte de dados é ele cria já uma componente visual aqui, com os dados que foram adicionados com a fonte de dados. Então, se você olhar aqui, onde tem origem de dados, aqui, Amazon Redshift ID, banco de dados ID e ele já adicionou um componente aqui eu vou excluir esse componente aqui, esse controle e vejo que aqui existem vários tipos de gráfico, então você pode colocar qualquer gráfico aqui de forma bem simples, configurar ele.

Então, como eu falei, a gente está criando aqui um relatório adhoc que o usuário ele foi fornecido pra ele, o acesso à tabela de vendas. Ele quer construir, modelar seu próprio relatório. Então, vamos supor que ele queira ver vendas por produtos. Então, um tipo de relatório interessante para ver vendas por produtos é um gráfico de barras. Então cliquei em gráfico de barras e vou colocar aqui. Então vejam que ele configurou aqui já o gráfico, mas ele também mostrando que como dimensão, o cliente é métrica contagem.

Então, na verdade ele está contando as vendas por cliente. Eu quero o total de vendas por produto. Então eu vou mudar aqui. Eu vou arrastar o produto para a dimensão. É a métrica que eu não quero. A contagem de registros eu quero total. Então eu vou arrastar o total pra métrica e vou excluir aqui o recorte.
Vou excluir e vou deixar só o total. Então, pronto.

Eu tenho um gráfico de barras aqui que me mostra as vendas por produto.
Eu posso personalizar esse gráfico. Então você está vendo aqui nessa guia gráfico aqui, o setup e a configuração do gráfico. E aqui, em estilo, você muda o tipo do gráfico. Então você pode mudar aqui o número de barras. Você pode mostrar o rótulo dos dados, mostrando os números lá em cima, a cor e linhas de inferência. Ou seja, você pode explorar aqui à vontade o as configurações do gráfico.

Então aí fica o seu critério. A gente tem o nosso primeiro gráfico aqui.
Agora vamos supor que você queira ver o total de vendas pelos maiores vendedores. Vamos supor que você queira ver os quatro maiores vendedores e quanto o resto representa. Então, você pode fazer isso, por exemplo, com o gráfico de pizza num gráfico do setor. Então, vou colocar aqui o gráfico de setor, aqui, a dimensão de período da data, a dimensão que produto eu vou mudar para vendedor? É só pegar o vendedor aqui e arrastar para o gráfico.
A métrica pra mim já está total. Vejam que aqui a classificação está decrescente, ou seja, do maior para o para o menor. Agora ele está mostrando aqui todos e fica bastante poluído o gráfico. Então vamos ver que estilos vão vir aqui em estilo. Aqui ele diz o número de fatias. Então vamos colocar aqui. Em vez de dez, vamos mudar para cinco fatias. Vamos ver o que acontece.

Então ele me trouxe aqui os principais vendedores e esses aqui são os cinco principais, os cinco maiores. Eu sei que são os cinco maiores, porque está ordenado aqui de forma decrescente, do maior para o menor. Ok, aí eu posso, por exemplo, que vim estilo. Vamos ver aqui eu posso mudar a cor.
Eu posso mudar aqui o rótulo. Legenda.