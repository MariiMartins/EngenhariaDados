- 78. Detalhando o Modelo
Então aqui o objetivo é a gente detalhar um pouco mais como que nós chegamos naquele modelo dimensional.
É importante salientar que inicialmente as empresas tinham apenas sistemas transacionais e tinham bancos de dados relacionais, que eram sistemas para manter transações, para manter a empresa funcionando e manter a empresa operando armazéns de dados dimensionais.

Foram construídos posteriormente a partir dos modelos transacionais que já existiam nas empresas, então isso como regra geral, na maioria dos casos, não quer dizer que foi sempre assim.
O tema, como regra geral, primeiras empresas tinham sistemas transacionais, posteriormente implementaram modelos armazéns de dados dimensionais.

Então, quando é feita a modelagem do modelo dimensional, normalmente já existe um banco de dados transacional.
Já existe um modelo de negócios consolidado, já existe bastante informação. 
Qual a abordagem para se construir modelos Dimensionais é uma mistura de duas coisas uma abordagem técnica e uma abordagem de negócio.

Qual a abordagem técnica? Bom, relações n para n, muito para muitos, para muitos que são modeladas em fatos, então toda a relação n para n ela vai gerar um fato em relações um para n são modeladas em dimensões. Então toda relação n para n vira dimensão, e isso, claro, no modelo de negócio que se quer colocar dentro de um armazém de dados. Não quer dizer que você vai sair no seu banco de dados relacional procurando tudo que relacionamento, muitos para muitos que cria um fato e toda relação um para ele. Você cria dimensões e não quer dizer isso.
Você vai modelar a partir de modelos de negócio que têm que ser carregados para dentro do armazém de dados.

A outra abordagem e abordagem de negócio você vai analisar o processo de negócio, ver quais são as necessidades do modelo de negócio e, o mais importante, você vai analisar o grão. Qual o nível de detalhamento que as informações têm que ser carregadas para o banco de dados dimensional? Como a gente já falou, isso é uma decisão muito importante, que vai afetar tanto os processos de carga quanto o espaço de armazenamento.

Enfim, lembrando que a tabela fato ela ocupa muito espaço. Ela é uma tabela que carrega muita informação, muitas informações e ocupa muito espaço. Ela tem uma rede muito grande. Portanto, a definição do grão é uma decisão importante.

Então, se a gente olhar aqui o modelo relacional que teoricamente já existiria na empresa, itens, venda aqui é uma relação muitos para muitos.Então, aqui nós temos um fato. Então itens, venda com venda, a gente faz aqui um fato.

Agora, relações um para muitos, a gente tem clientes, a gente tem vendedores e a gente tem produtos. Mas a dimensão, data, dimensão, tempo que é obrigatória, a gente tem que ter também sempre uma dimensão, tempo.

Então, qual é a conclusão que a gente chega aqui? Que nosso modelo dimensional vai ter um fato e vai ter quatro dimensõe tempo, então a gente está vendo aqui a gente tem uma, duas, três, mais a dimensão tempo. A gente tem quatro dimensões, então a gente já tem alguns elementos para modelar o nosso modelo dimensional. 

Então, aqui a gente vendo um modelo dimensional pronto. A gente tem aqui o relacionamento Muitos para muitos, Aqui nós temos os relacionamentos, um para ele e aqui nós temos nossa dimensão Tempo.
Que atributos a gente tem que colocar no nosso modelo dimensional? Bom, primeiro, toda a dimensão tem que ter uma chave primária. Então aqui está chave, cliente, chave, produto chave, vendedor e chave tempo. Todas as dimensões com relação, com exceção da dimensão tempo, ela tem que ter uma chave do banco de dados relacional.
A chave primária que a gente colocou aqui é chamada sororidade, que é a chave substituta. Além da chave substituta, a gente vai manter a chave primária do banco de dados relacional.

Então, aqui está o identificador de cliente identificador do produto e o identificador do vendedor também é a nossa foto Venus. Ela vai ter que ter uma chave primária. Para distinguir as transações. Bom, aqui a gente tem que relacionar todas as chaves substitutas de chaves primárias, como a foto, vê las.
Então aqui esteja produto, chave, vendedor, chave, cliente e chave tempo.

Bom, aí veio uma decisão importante o grão. Então a gente tem vendas, vendedor, produto e clientes por dia.
O que torna esse modelo com o grão bem detalhado? Não é nem no caso, se o usuário ou o cliente ou a pessoa da área de negócios precisar que seja o grão detalhado por dia. Mas o que torna esse modelo muito detalhado, com grão bem detalhado e inclusão do cliente no modelo é porque, como regra geral, o cliente não vai voltar na loja é o mesmo grão de tempo, ou seja, no mesmo dia. Isso quer dizer que cada transação do mesmo cliente do mesmo dia do mesmo produto vai ter uma inserção nas vendas.

Então a gente tem aqui o modelo bem detalhado. Bom, com relação aos atributos, o que a gente precisa?
Data, início, data de início e fim de validade em todas as dimensões. E as demais informações vêm da área de negócio. Então, eles querem saber o nome do cliente, o estado, o sexo, o status dele. É que a gente viu que uma questão importante do produto eles querem saber qual é o produto do vendedor. O nome do vendedor é suficiente e a dimensão, tempo. Então, usa atributos da dimensão tempo.
Quais que vão ser bom são aqueles atributos que permitem que a gente execute consultas no nosso modelo dimensional de forma simplificada. Então, por exemplo, se eu quero filtrar um determinado mês, eu vou ter um mês aqui. Então, eu posso filtrar o mês fazendo simplesmente um mês igual a tanto ou o ano igual a tanto. Eu não preciso fazer nenhum tratamento, nenhum filtro especial na data certo. Eu quero ver, por exemplo, todas as transações que ocorrerão aos sábados para ver o quanto eu vejo quanto eu vendo. No sábado, eu tenho aqui o dia da semana.
Eu quero saber as transações, as vendas que foram feitas no segundo trimestre. Eu tenho pronto o trimestre.
Eu não preciso pegar a data, que, embora exista aqui, eu não preciso pegar a data e fazer nenhum tipo de tratamento nela para ver qual trimestre, qual mês, qual o dia, ou qual ano ou qual dia da semana. E quero ter essas informações já detalhadas no meu, na minha dimensão tempo depois.

Por fim, nós temos as medidas. Então, as medidas dependem da área de negócio. Então, eles querem ver, por exemplo, a quantidade, o valor unitário, o valor total e o desconto que foi aplicado nas vendas. Você aqui deu pra gente ter uma ideia de como a gente chega no modelo dimensional. Então, de mistura um pouco de questões técnicas, olhando o modelo relacional e também observa a área de negócio. A área de negócios é tão importante quanto a questão técnica e é importante lembrar que o grão deve ser muito bem pensado, muito bem analisado.
E também é importante lembrar que não quer dizer que tudo que exista no banco de dados existem bancos de dados com milhares e dezenas de milhares de tabelas. Não quer dizer que tudo que exista no banco de dados vai virar fatos e dimensões no modelo dimensional, que não precisa existir uma relação um para um com relação a estes itens.