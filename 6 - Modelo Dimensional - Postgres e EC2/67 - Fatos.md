- 67. Fatos
Nós vamos então começar a partir deste vídeo a falar de fatos, dimensões e medidas.

Você, como engenheiro de dados, quando você precisar interagir, por exemplo, extrair dados de bancos de dados modelados de intencionalmente. Você vai ter que identificar esses elementos dentro de um banco de dados dimensional, dentro de um banco de dados analítico.

Então, todas as tabelas que estão dentro de um banco de dados dimensional se encaixam em uma dessas categorias: Ou é fato, ou são dimensões ou são medidas.

•	Fato é o dado central, o tema do qual se quer analisar.
•	As medidas, como nós vamos ver, elas vão estar relacionadas ao fato. Elas vão estar armazenadas fisicamente junto com o fato, então, o fato é a tabela central. A informação central é o tema que se quer analisar. Então, por exemplo, eu posso ter um fato vendas que a gente vem vendo até agora.
•	Dimensões são os diversos pontos de vista, são as perspectivas sobre os quais se quer analisar um fato. Então, por exemplo, eu posso analisar um fato vindas da perspectiva do vendedor, do cliente, do produto. Existe uma dimensão tempo, que é uma dimensão obrigatória e uma perspectiva, um ponto de vista obrigatório sobre qualquer fato. Então você sempre em um modelo dimensional, você vai ter uma dimensão tempo, porque você precisa analisar um contexto de vendas, por exemplo, em determinado período. Se uma informação do ponto de vista gerencial ela fica sem sentido, ela não se torna histórica.
E as medidas são as métricas, os valores que serão analisados, então, falando de vendas, eu posso ter uma medida, que é o total de vendas, posso ter os descontos, eu posso ter impostos, eu posso ter informações a respeito da quantidade dos produtos, enfim, são diversas métricas que são consolidadas no modelo.

Então, aqui, um modelo dimensional simples não é o modelo que a gente vai usar aqui, no nosso caso prático, mas ele é bem semelhante.
Então vejo eu tenho o fato que é o elemento central, que é o evento que eu estou analisando. Então, aqui a gente tem a quantidade de vendas, o custo, descontos, impostos.
Então essas aqui são as mesmas medidas na parte de baixo do fato.
E aqui, ao redor do fato, nós temos as dimensões, essas perspectivas sobre qual eu estou olhando o fato.
Então eu tenho uma dimensão cliente, eu tenho uma dimensão, tempo, eu tenho uma dimensão, produto e eu tenho uma dimensão região onde o produto foi vendido.
Então, fato é o assunto central. Ele agrega medidas que, como a gente viu aqui, vão estar na mesma tabela e sempre várias dimensões, sempre agregadas ao fato.
Eu vou ter várias dimensões, relacionamento, muitos para muitos em uma tabela em um banco de dados relacional gera fatos. Uma forma interessante de buscar coisas de fatos para o modelo dimensional e buscando relacionamentos Muitos para muitos, então itens de venda gera o fato vendas aqui, alguns exemplos de fatos para a gente entender melhor o conceito, que é um fato.

Então a gente pode ter um fato vendas para a gente prover informações gerenciais a respeito de vendas.
A gente pode ter um fato de bugs, então a gente pode fornecer informação gerencial de bugs encontrados em um produto. A gente pode ver os bugs do ponto de vista, por exemplo, do módulo do desenvolvedor que criou a funcionalidade do cliente que reportou o bug.
A gente pode ter fatos, faturas, há um fato, por exemplo, da linha de produção.
Que tipos de produtos foram criados, o tempo que levou e quantos produtos foram criados, Quanto custou.Enfim, viagens, contas a pagar impostos são alguns exemplos aí de fatos. Mas claro que os exemplos possíveis são ilimitados, dependendo do tipo de negócio que se está modelando.
