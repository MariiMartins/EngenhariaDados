98. Orientado a Colunas
Vamos falar rapidamente sobre os bancos de dados orientados a colunas, ou colunas ordenadas.
•	Também são conhecidos como Wide Column Store, Column Oriented Database.
•	Os dados são armazenados em colunas e não em linhas.
•	Keysapce é o equivalente ao esquema do relacional do banco de dados relacional, ele faz o agrupamento dessas colunas.
•	Column families equivale a uma tabela do relacional: tem os dados.
•	Column Family: várias linhas.
•	Cada linha pode conter diferentes número de colunas, não precisa haver uma equivalência entre as colunas, como gente vai ver no próprio slide.
•	Cada coluna contém uma chave valor, mais um campo, data e hora obrigatório, então sempre vai ter uma chave além dos valores, mais a data e hora.
•	Cada linha, então, tem uma chave única.

Então, aqui, um exemplo do schema de colunas ordenadas, então o conjunto todo representa uma família, Aqui a gente tem a chave que, como toda chave, ela é única. Aqui nós temos as linhas e as colunas. Então, vejam que as colunas não são obrigatórias em todas as linhas. Então a gente pode ver que existe em colunas que não são representadas em todas as linhas.

Agora, qual que é a vantagem do modelo ordenado ou orientado a colunas? Então a gente possa imaginar o seguinte caso imagine uma tabela com centenas de colunas e milhões de registros.

É comum modelos dimensionais, armazéns de dados, as fatos ou as tabelas de consultas, tabelas desnormalizadas, terem dezenas ou até centenas de colunas. Isso é bastante comum.
Então o que acontece quando você vai fazer uma consulta?
Ele nãovai fazer um Select * from tabela.
Na verdade, ele vai pegar algumas colunas específicas. E vai fazer um select, coluna1, 2 ou 3, por exemplo, da tabela, mesmo que haja lá centenas, dezenas de colunas. Ele não vai usar todas. Ele vai usar algumas especificamente.
Só o que acontece, como está orientado a linhas, mesmo que haja índices.
O gerenciador de banco de dados vai precisar carregar todas as colunas com todos os dados e isso traz um grande problema de performance.

Agora, o modelo orientado a coluna.
Como cada coluna armazenado é um arquivo fisicamente separado, o gerenciador de banco de dados precisa carregar apenas as colunas da consulta. Então, por exemplo, se você faz lá um select coluna1 e coluna 3, por exemplo.
O que acontece? Estas colunas estão armazenadas fisicamente no sistema de arquivos e estão armazenadas separadamente, então ele precisa carregar apenas estas colunas. Além disso, é um ótimo modelo para compressão, para reduzir o tamanho do banco de dados.

Por quê? Porque na coluna os valores tendem a ser mais repetidos. E quando a gente tem valores repetidos, a gente tem uma maior taxa de compressão.

Então imagine assim numa coluna, por exemplo, se for lá o status do cliente, do nosso modelo dimensional, a gente tem três valores e tem Silver, Platinum e gold.
Já quando a gente olha por linha, a compressão aqui é muito mais difícil, porque gente vai ter dados completamente diferentes. Então a gente tem o nome, outro de tem cliente no outro produto, o outro valor. São informações diferentes, então o modelo também é ótimo para compressão.

O que acontece se eu precisar de alguma forma retornar uma linha a linha aqui, no caso, ela vai estar aqui.
O que acontece? Bom, o armazenamento das colunas aqui ela mantém a ordem, então as linhas estão armazenadas na mesma ordem. Então se consegue recuperar aqui uma linha, caso seja necessário. Claro que se perde os benefícios de você selecionar as colunas inteiras.

Então, esse modelo orientado a colunas, organizado por colunas ou orientado a colunas, ele vem se tornando cada vez mais o modelo mais utilizado e melhor para armazenar armazenamento de bancos de dados para consultas, ou seja, armazéns de dados analíticos.