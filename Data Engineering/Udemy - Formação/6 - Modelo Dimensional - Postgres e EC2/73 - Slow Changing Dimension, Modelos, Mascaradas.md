73. Slow Changing Dimension, Modelos, Mascaradas
Então a gente viu que as dimensões em um banco de dados dimensional elas mudam, as mudanças são atualizadas mesmo para uma mesma entidade.

Então, por exemplo, você tem um cliente, o cliente pode aparecer várias vezes, ele pode se repetir no banco de dados dimensional. É por isso que a gente diz que um banco dimensional, ele tem redundância de dados e isso não é um problema, é uma característica.

Bom, como você mantém as dimensões? Existem várias formas de você manter e atualizar essas dimensões quando os dados são atualizados, por exemplo, dados do cliente. O tipo mais comum, que é o que a gente vai falar aqui, é o chamado slow change dimension type 2.
Existe uns tipos de mudança de dimensão de um asset, mas o mais comum é o tipo dois. No tipo dois, o que você faz? Você inclui o novo registro quando há uma mudança naquela informação.
É o caso aqui que a gente viu do cliente, ele mudou do status silver para Gold.
Eu não vou atualizar o registro, eu vou incluir um novo registro deste cliente, então, supondo que aqui seja a minha chave substituta, aqui a chave primária do banco de dados mudou o status, eu inclui um novo registro.

Então, Slow Change Dimension Type 4 é o tipo mais comum, outros tipos, como eu disse, são 7. O tipo 0 mantém o original, o tipo 2 você sobrescreve, então você atualiza a dimensão, o tipo 3 você cria um novo atributo. Mas, como eu falei, sempre o tipo mais comum, o mais usual, é o tipo 2.

A modelagem dimensional, assim como a modelagem relacional, ela tem boas práticas, mas muitas coisas, muitas decisões dependem da pessoa que está fazendo a modelagem e do analista de banco de dados ou do analista que está fazendo a modelagem. É uma técnica comum que você vai encontrar em modelos dimensionais quando você, por exemplo, tiver que desenvolver processos de carga de dados. São as dimensões com validade ou mesmo as dimensões com status.

Nas dimensões com validade. Ela pode receber um atributo de validade, indicando que o período que elas estavam válidas. Então, veja só esta dimensão aqui cliente ela tem o atributo, data, início de validade e data fim de validade. Então, quando você for fazer o processo de carga, você atribui esses valores. E quando você for relacionar com o fato, você for relacionar uma dimensão cliente com a fato, você vai verificar a validade dela.

Uma outra opção é a dimensão. O cliente tem o atributo de status dizendo aquela dimensão, ela é ativa ou não. Se você coloca apenas o status, você não tem informação do período que ela ficou válida e as a validade nas dimensões.
Então, como eu falei, elas são usadas para fins de recarga dos dados transacionais ou mesmo recálculo. Se você precisa recarregar o seu banco de dados por algum motivo, você tem que fazer a recarga. Você tem direitinho lá qual foi a validade que serviu cada dimensão.
Se você nunca vai precisar fazer recarga, você poderia, por exemplo, pegar sempre o último registro daquela informação que foi inserido. Por exemplo, o último registro do cliente de chave substituta de número X, por exemplo.

Dimensões mascaradas: nas dimensões mascaradas, ao invés de entidades, a gente implementa um atributo no fato. A gente usa as dimensões mascaradas para dimensões que possuem um número fixo de opções, por exemplo: sexo, então vejam aqui: A gente tem aqui o sexo do cliente, uma vez de implementado na dimensão cliente, ele está implementado na fato. Então, como a gente está falando aqui, a gente usa esse recurso para dimensões que possuem número fixo. Então, por exemplo, se o sexo vai ser apenas masculino ou feminino, eu posso implementar ele através de uma dimensão mascarada diretamente na fato vendas.

As dimensões degeneradas são dimensões que derivam da tabela fato, mas que elas não têm sua própria tabela de dimensão. A gente usa as dimensões degenerados quando precisa manter o grão, o mesmo grão do sistema transacional, então, por exemplo, de uma dimensão degenerada, o número de nota o número do pedido.

Dimensões junk. As dimensões junk são dimensões que agrupam vários atributos relacionados a uma fato. Então, se você tem atributos simples do tipo sim ou não, zero ou um, ativo ou inativo, você pode colocar todos esses atributos em uma mesma dimensão se precisar mais de uma vez com a fato, então uma dimensão de uma dimensão lixo. Ela reúne todos esses atributos simples em uma mesma tabela, obviamente que é uma mesma tabela fato.  Então uma outra técnica de modelagem. 

E os modelos dimensionais,  são modelados de duas formas principais e o chamado star schema e o schema estrela, dimensão Snowflake que é o floco de neve.
O mais comum é o Star. Então vejam aqui esse exemplo.
Eu tenho uma fato vendas e eu tenho aqui uma dimensão produto. Então eu tenho da dimensão do produto, eu tenho um produto e uma categoria, vejam que aqui eu estou botando o produto e a categoria em uma mesma dimensão. Esses elementos aqui eles compõe uma hierarquia. Então um produto ele pertence a uma categoria. Então você tem vários produtos que pertencem a uma mesma categoria, isso é uma hierarquia, eu coloquei essa hierarquia aqui em uma mesma tabela. 

Então, por exemplo, aqui, o que pode acontecer? A categoria Ela vai repetir.
Muitas vezes eu vou ter um produto a que vai ser da categoria A, eu vou ter um produto B, que vai ser da categoria B e o produto que vai ser da categoria A, por exemplo.

Ok, então eu vou ter uma regra, uma redundância de dados aqui e uma forma desnormalização dos dados. Então esta é modelagem estrela. Eu tenho a dimensão produto, a hierarquia modelada toda dentro da mesma tabela e relacionada com o fato.

Agora no modelo floco de neve snowflake.
O que eu vou fazer? Eu vou modelar a dimensão na forma normal, na terceira forma normal. Então, vejam que a categoria que em vez de eu ter a categoria aqui, eu tenho um ID de categoria e eu estou cadastrando a categoria em outra tabela. Então, essa é uma modelagem válida, ela é utilizada, não é tão comum quanto a modelagem. Estrela. Esse tipo de modelagem reduz a redundância porque a categoria vai ficar registrada aqui apenas uma vez. Você não vai repetir a categoria, reduz o tamanho do banco de dados, da necessidade de armazenamento, porém complica as consultas, tornam o modelo mais complexo e afeta o desempenho. Você vai precisar de mais joins, de mais junções entre as tabelas.

Então é uma avaliação que tem que ser feita na modelagem dos dados, quando há, quando o analista de banco de dados estiver estudando o problema e fazendo a modelagem dos dados. Mas, como eu falei, são duas técnicas válidas. São duas técnicas utilizadas.
