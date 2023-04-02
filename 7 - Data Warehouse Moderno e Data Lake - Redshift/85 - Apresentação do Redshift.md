85. Apresentação do Redshift
Bom, então a gente já sabe que o Red Shift é uma solução de dentro da nuvem, faz parte do AWS.
Ele é projetado para processar grandes volumes de dados, é orientado a coluna. Ele foi construído a partir de uma versão anterior, uma versão mais antiga do Postgres. Então, você vai encontrar muita semelhança, principalmente no SQL, nos comandos, na sintaxe SQL. Mas ele é um produto completamente diferente hoje em dia.

Ele teve a sua base criada a partir de uma versão do ponto de vista, mas é um produto diferente. E por ser um DataWarehouse, ele não tem a maioria das restrições de integridade referencial que você encontra em um banco de dados relacional, como o próprio postgres, por exemplo.

Que chaves estrangeiras é uma restrição em Unix? Isso porque, por ele ser um DW, se entende que isso é causar uma degradação, degradação de performance. Então não é necessário por ele ser um armazém de dados. Mas o curioso é que se você, por exemplo, utilizar uma cláusula Unix, por exemplo, em um script de criação de uma tabela, ela vai rodá-lo. Não vai dar erro, mas a restrição não vai ser criada. 

Bom, é orientado a coluna. Quer dizer que as colunas são armazenadas individualmente, os valores são armazenados de forma contínua. Então, criar uma linha, um select, onde você recupera várias linhas e quer recuperar o valor de várias colunas.

Por que a gente está dizendo que o redshift é orientado a coluna? Por que os bancos de dados relacionais, como o postgres que nós estudamos, ele é orientado à linha e isso traz uma grande diferença com relação a performance.

Então vamos ver aqui algumas características.
Orientado a linha quando você lê uma coluna, por exemplo, lá no postgres que é orientado a linha, você vai ler todas porque você tem o armazenamento da linha. Como uma linha pode ter vários tipos diferentes de dados, a gente sabe que um banco de dados relacional, cada coluna pode ter um tipo de dados.
A compressão que é aplicada no resultado da compressão desses dados é menor. Só que você for ler todas as colunas vai ter um custo menor do que orientado a coluna e inserir ou atualizar colunas também tem um custo menor. Então, orientado a linha, ele traz algumas vantagens e por isso ele é o modelo utilizado nos bancos de dados relacionais.

Agora orientado a coluna como o redshift.
Quando você lê uma coluna, você vai ler apenas a coluna, então você não precisa ler os dados das outras colunas. E como uma coluna vai ter sempre o mesmo tipo, a compressão ou a compactação é maior. Você consegue um efeito de compactação maior.
Então você tem uma performance muito maior de leitura, que é o que se mais se usa um banco de dados dimensional por ele ser orientado a coluna.
Agora, se você vai ler todas as colunas, você vai ter um custo alto, porque você vai ter que ler dados de diferentes arquivos e inserir o atualizar colunas.
Também vai ter um custo maior, porque exatamente ele está orientado.

A coluna, então é uma troca o orientado à linha.
Ele é menor para bancos de dados operacionais e orientado a coluna para bancos de dados orientada ou orientados a tomada de decisão a banco de dados analítico. Aqui, um exemplo vamos supor que a gente tivesse uma tabela com essas quatro colunas e que cada uma ela ocupasse um giga.
Se a gente precisasse fazer uma consulta, que fosse ler as colunas A e B no orientado a coluna, todas as linhas que a gente quer consultar a coluna A e B de todas as linhas num banco de dados orientada a coluna. A gente ia ter que recuperar dois gigabytes de informação porque cada coluna tem um gigabyte.
Já no orientado a linha, ele ia ter que ler as quatro colunas, mesmo a gente precisando ler apenas duas ou colocando apenas duas lá no Select, então, seria preciso recuperar quatro gigabytes. Agora, quando fosse inserir dados, por exemplo, no orientado a coluna, você vai ter que inserir informação em quatro registros diferentes. Já no orientado a linha não, elas vão estar, provavelmente em um mesmo arquivo.