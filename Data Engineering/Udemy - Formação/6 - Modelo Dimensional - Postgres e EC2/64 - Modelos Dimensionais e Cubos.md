- 64. Modelos Dimensionais e Cubos
A gente está falando de dados multidimensionais, de dados com mais de uma dimensão de modelagem dimensional. 

Mas, afinal, o que são dados multidimensionais? Então são dados que podem ser vistos sob diversas perspectivas, de forma dinâmica e cujos valores, que são as medidas, são calculadas automaticamente.

Então, o que quer dizer de ver valores sob determinadas perspectivas? Por exemplo, se eu tenho um armazém de dados em fato vendas, eu posso ver as vendas sob a perspectiva do vendedor, do produto, do estado, da filial. E eu posso fazer isso de forma dinâmica, de forma interativa. Não preciso rodar novas consultas.
As medidas, os cálculos, por exemplo, o total de vendas ou a quantidade de vendas, e me é demonstrada automaticamente. A ferramenta calcula isso automaticamente na medida que aumenta ou diminui o nível de detalhe, o cálculo é feito automaticamente.
Então, portanto, se eu estou vendo a venda por país, ele me traz já o total de vendas por país. Se eu aumento, o nível de detalhe eu aumento o grão.

E eu vejo lá, por exemplo, a venda a nível de Estado. Automaticamente ele vai me abrir e calcular o total de vendas a nível de estado.

Então, aqui a gente tem os cubos OLAP, que são chamados de cubo, porque a informação pode ser manipulada e visualizada sob diversas perspectivas, tanto na forma de grade que a gente vai ver no próximo slide quanto na forma de gráfico. Então, aqui a gente tem um exemplo clássico de um cubo.
Então, aqui eu tenho as dimensões, as dimensões são as perspectivas sobre o qual eu estou vendo os dados, todo o cubo me representa um fato, um fato e alguma operação importante da empresa. Então, por exemplo, tem o fato vendas. Isso é uma coisa importante. Eu posso ter um fato folha de pagamento são eventos importantes da empresa.
Então, o fato no cubo eu vou ver do ponto de vista de dimensões, por exemplo, a categoria aqui bebidas é uma dimensão. 
O país aqui a gente está vendo. Aqui um país é outra dimensão. Aqui eu tenho produtos, é outra dimensão. E aquilo está calculando automaticamente, como eu falei, a quantidade e o desconto que foi aplicado. Então, o cubo me permite ver a informação aqui de vendas, por exemplo, sob diversas perspectivas.

Eu estou vendo aqui sobre país e aqui pelo tipo do produto. Então a gente está vendo aqui bebidas, e aquilo está abrindo bebidas sobre os produtos, sobre as diferentes, os diferentes tipos de bebidas.
Eu posso aumentar o nível de detalhamento. Eu posso ver essa informação sobre outra perspectiva. Então, isso é um cubo que essa informação é me propiciada pela modelagem dimensional.

Então eu criei um modelo dimensional, carreguei esses dados, eu mantive o histórico e assim eu consigo ver essa informação sobre determinadas perspectivas. 
Nível de detalhamento a gente falou, que eu posso ter vendas em nível de país, categoria do produto e produto. Eu posso ter, por exemplo, medidas de quantidade de desconto e eu posso ter ainda o tempo, que é opcional.
Então, dados são carregados, consolidados, resumidos. Esse resumo ocorre durante o processo de carga e transformação dos dados.

E como a gente já viu, nós temos diferentes tipos de grão, se a gente carregar dados consolidados por estado, por exemplo, a gente não vai poder ver informação por cidade se o nível de detalhamento maior for por estado.
A gente não consegue ver a informação de venda, por exemplo, por cidade.
Se a gente carrega o grão de cidade, existe informação do Estado e a gente vai poder ver tanto nos dois níveis. Eu posso aumentar o nível de detalhamento de forma interativa à medida que eu vou navegando no meu cubo.