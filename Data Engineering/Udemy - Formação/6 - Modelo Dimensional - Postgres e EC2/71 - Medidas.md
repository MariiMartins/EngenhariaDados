71. Medidas
Vamos detalhar, então, outro elemento importantíssimo do modelo dimensional, que são as medidas.
Então, as medidas são características numéricas de um fato. Então, por exemplo, as vendas do fato vendas, eu posso ter a quantidade de vendas, os descontos, os percentuais, o imposto total de vendas, então, são normalmente modelados como atributos como campos de um fato podem envolver. 
É comum que envolvam cálculos complexos que não existem no modelo relacional. Eles têm que ser calculados pelo sistema dimensional.

As medidas têm três principais tipos aditivas, não aditivas e semi aditivas.
•	As aditivas são aquelas que podem ser operadas matematicamente, então você pode somar a elas, por exemplo, quantidade de vendas.
•	As não aditivas, elas não podem ser operadas matematicamente. Você não pode somar, por exemplo, o percentual de vendas.
•	E a semi aditivas pode ser operadas matematicamente, mas de uma maneira não uniforme.

Então, por exemplo, balanços contábeis, existem ferramentas que os cálculos são extremamente complexos e as formas de calcular que se fazem esses cálculos variam. A gente vai falar um pouquinho disso mais adiante e obrigatoriamente um fato vai ter uma medida (pelo -1 medida é obrigatório). Então, não existe uma modelagem dimensional com um fato que não tem medida, não faz sentido não ter uma medida, um cálculo para ser demonstrado. Então, aqui, por exemplo, o fato a gente pode ter aqui como medida o valor, a quantidade e o desconto, são exemplos de medidas de um fato vendas.

Com relação ao cálculo da medida, então, ela pode ser calculada no processo de carga. Pode ser calculado dinamicamente automaticamente pelo servidor OLAP. Em vez de você estar armazenando o seu banco de dados dimensional em um banco de dados relacional comum, você pode ter um servidor especializado dimensional como o Microsoft SQL Service Analise Server, ele vai fazer já os cálculos das medidas automaticamente e dinamicamente.

Existe ferramentas de visualização que podem fazer esse cálculo já no cliente funciona para cálculos mais simples, para dados não muito pesados, para sistemas dimensionais mais simples, 
E as medidas podem conter hierarquias de cálculos elas são capazes de contemplar hierarquias de cálculos. Então a gente viu lá exemplo de hierarquias, a medida por país, por estado, por cidade ou por bairro. Então, as medidas são capazes de calcular estas hierarquias.