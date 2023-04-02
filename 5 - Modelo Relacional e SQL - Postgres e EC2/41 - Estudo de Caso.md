41. Estudo de Caso
A gente vai falar a seguir sobre as formas normais, mas antes disso era bom a gente ver um caso prático. Pelo menos a gente visualizar um caso prático das implicações que ocorrem para o negócio, para uma empresa que mantém um negócio, se ela não utiliza um modelo relacional normalizado com integridade, então supondo que uma empresa ela abra um negócio de uma empresa nova, ela cria um negócio novo e ela resolva registrar em um banco de dados as operações de venda.

Então, o que ela faz? Ela cria uma estrutura como essa que a gente está vendo aqui.
Então você tem lá o nome do vendedor que fez a venda, o nome do cliente, o endereço do cliente, o produto que foi vendido, quantidade de valor e total. Então, esse foi o primeiro cliente, a primeira venda que acontece.
Bom, chegou o segundo cliente, Segundo o cliente o vendedor já é outro, a Maria. O cliente é o Rogério da Silva.
Aqui está o endereço do cliente. O que ele comprou, quantidade e valor e o total. E assim vai.

A Maria, por exemplo, ela teve outra venda. Ela vendeu para o Antônio. Aqui está o endereço do Antônio e depois foram vendido lá um suporte e assim a empresa foi tendo várias vendas. Então, o que a gente pode ver aqui, por exemplo, que algumas vendas não têm vendedor. Alguns clientes aqui não têm o produto e aqui as quantidades estão corretas.

O que a gente pode encontrar aqui de problemas?
Primeiro a gente está vendo aqui o Antônio Carlos do Amaral. A gente não tem certeza que se eles são os mesmos, mas se o endereço do Antônio for alterado, aonde que a gente deve mudar? Em qual desses registros a gente vai alterar o endereço do Antônio? E a outra pergunta será que este Antônio e este aqui são mesmo?
Quer dizer, existe uma possibilidade. Esse aqui está abreviado, aquele não.
Porém, tem um terceiro Antônio que será que é a mesma pessoa e qual desses três endereços aqui está correto?
Vejam que a gente tem mais um disse que esses dois são a mesma pessoa.
Rua Mariano, Rua Mariano, número 300. Aqui está número 30. Ali está o número 300. Pode ser que seja um erro de digitação. A gente não sabe qual desses endereços está correto.

Aqui está só Mariano. São três endereços cadastrados de forma diferente, o qual está correto. Por que as mochilas estão com preços tão diferentes? Então veja aqui tem uma mochila vendida por 69 e tem outra por 120, quase o dobro. Por que o preço é tão diferente? Será que é a mesma mochila? Será que um dos preços está errado?
Não pode ter sido um desconto tão grande.
Quem vendeu aqui? O Ivanildo tem duas vendas pra ele.
Quem que vendeu pra ele?Qual é o vendedor?
E a última venda aqui ela está duplicada. O Ivanildo realmente comprou quatro monitores. Ou será que é a mesma venda?

Então são vários problemas que a gente está encontrando aqui nesses dados que não estão normalizados, não estão no modelo relacional. Estão aqui alguns problemas: A gente tem um volume de dados desnecessário e, por exemplo, aqui o endereço repetido várias vezes, tem um problema de performance, de ter uma quantidade de dados muito grande, tem problemas de integridade. A gente não sabe qual dado é correto, qual dado é verdadeiro, qual o que está valendo. E a gente tem problema de concorrência.

Então, como isso não está em um sistema gerenciador de banco de dados, não existe uma aplicação controlando o acesso, controlando a integridade, por exemplo, controlando se, vão haver leitura sujas, leituras fantasmas controlando o acesso aos registros, as atualizações.

Então, se você tentar implementar um sistema de operações para manter as operações de uma empresa dessa forma, você vai ter esses e outros diversos tipos de problema que em algum ponto tornariam o produto, o software inviável pela questão, pela problemática causada no banco de dados, na implementação criada no banco de dados.
Então a gente vai ver nos próximos vídeos, como que a integridade referencial e as formas normais que implementam integridade de referencial. Resolvem se não totalmente, mas pelo menos minimizam a maioria desses problemas que nós vimos até aqui.