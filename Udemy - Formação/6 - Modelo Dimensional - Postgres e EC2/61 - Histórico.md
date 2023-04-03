- 61. Histórico
A gente falou que uma das características de um banco de dados dimensional é que ele é capaz de manter o histórico. Um banco de dados operacional ou relacional que a gente estudou na sessão passada, ele não mantém o histórico das informações.

Vamos tentar entender, com exemplo o que isso quer dizer, o que quer dizer manter ou não manter o histórico.

Então, vejam aqui a gente tem uma fração de um modelo de dados, de um banco de dados relacional e uma fração aqui é o modelo de banco de dados analítico.
Então, veja que a gente tem uma tabela de clientes, a gente tem aqui o nome do cliente, data de atualização, o código do status dele, esse código de status vem de uma tabela de status. A gente viu lá, por exemplo, Silver, Gold e Platinum.
Já o modelo analítico, ele está modelado de outra forma. A gente tem o fato vendas que nós vamos entender depois, que é um fato, o que é uma dimensão, mas a gente tem uma fato vendas, a gente tem uma dimensão cliente. Então a gente tem o código do cliente, o nome do cliente, o status do cliente. Então, parece aqui, em princípio, muito parecido às duas estruturas, embora aqui a nomenclatura seja diferente. As suas estruturas aqui, principalmente do cliente, é bastante semelhante, só que a forma como a informação é mantida e atualizada é diferente. Então a gente vai entender isso já.

Vejam só a gente vai cadastrar um novo cliente, então a gente vai cadastrar o cliente aqui, nessa tabela, o cliente vai receber um código, CL001, por exemplo, o nome do cliente, a data que ele foi atualizado, o status dele.
Como ele é um cliente novo, o código de status vem da tabela Status, qual é o que vai ser o código de status dele?
Vai ser um, ele é um cliente Silver.

Como que isso vai ser armazenado no banco de dados analítico?
Bom, a gente vai ter aqui. Ele foi cadastrado como cliente, mas ele realizou uma venda, então a gente vai ter aqui no fato vendas, um identificador da transação e uma chave que liga ele com a dimensão do cliente. Lá na dimensão cliente, a gente tem o que um identificador desse cliente no modelo dimensional, o identificador do cliente que veio lá do banco de dados relacional, o nome do cliente e o status do cliente. 
Até aí, tudo normal. Parece que os dois modelos são bastante semelhantes, a não ser que pela estrutura, pela nomenclatura, pelos nomes, certo. 

Vamos supor que esse cliente ele começa a comprar bastante e ele sofre um upgrade. O status dele passa de Silver para Gold, certo? Então, o que acontece lá no banco de dados operacional, eu vou ter o update, eu vou ter uma atualização do registro do cliente. Então vejam o código do status dele, que era um passou para dois, certo? No mesmo registro, passou de um para dois a informação que ele tinha o status um se perdeu, ela foi atualizado.

Agora eu vejo como isso é feito no banco de dados analítico.
Então, veja só, a gente tinha na primeira transação, que era a 001, e agora a gente tem uma outra transação aqui no
Fato Vendas, que é esse K099  para fins de exemplo. E como que isso aconteceu na dimensão cliente? Esse registro aqui a gente já tinha que e quando ele foi cadastrado, o status dele era Silver. O que aconteceu agora que o status dele mudou, vejam que não houve uma atualização. A gente incluiu um novo registro com o novo status aqui na tabela Fato vendas vão existir, claro, um Campos dizendo a data. 

O que acontece? Eu tenho histórico. Eu sei quando esse cliente passou de Silver para Gold aqui no meu banco de dados operacional, eu não tenho a informação que foi atualizada e eu perdi essa informação.
Aqui no banco de dados analítico, eu consigo ver, por exemplo, em determinada data, quantos clientes eu tinha com o status silver, quantos eu tinha com o status gold. Além de eu ver a mudança de status do próprio cliente, eu consigo retirar informações gerenciais de todos os meus clientes. 

No banco de dados operacional Não, a informação foi atualizada. Eu consigo fazer um Select lá e ver hoje quantos clientes eu tenho Silver e quantos clientes eu tenho Gold, mas as mudanças de status entre Silver e Gold, por exemplo, eu não sei. Essa informação é perdida porque foi atualizada. Então, esta é uma grande diferença entre o modelo operacional e o modelo analítico.

Qual o que está certo com o que está errado? Não existe essa questão de certo ou errado. São modelos de dados diferentes, com propósitos diferentes. 
A gente já discutiu o modelo operacional: Ele é feito para manter a integridade, para manter a baixa redundância, baixa repetição de dados e manter a empresa funcionando, ele registra as operações que ocorrem na empresa.
Já o banco de dados analítico não, o objetivo dele é prover informação gerencial, então, ele não tem problema de redundância.

Vejam aqui o que, toda vez que o cliente mudar de status, vai repetir que o nome dele é o status dele.
No modelo operacional, isso não acontece, os dados não são repetidos. Eu tenho apenas uma tabela de status e apenas o nome do cliente, apenas um local.
Não analítico, não. Não temos problema de redundância de volume de dados, certo? Aqui a informação tem que ser repetida para que a gente mantenha o histórico. Então, são modelos diferentes, com finalidades com propósitos diferentes.
