37. Arquitetura Relacional
O modelo relacional foi proposto pelo matemático Frank Codd e ele foi proposto como o sucessor ao modelo hierárquico e ao modelo de rede que era amplamente utilizado até então, principalmente em mainframes e em grandes servidores.

Então, o modelo relacional hoje é um modelo amplamente adotado, ele é extremamente maduro, ou seja, as aplicações, os produtos que oferece sistemas gerenciadores de banco de dados relacional são produtos extremamente maduros devido ao grande tempo em que esses produtos estão no mercado. Existem centenas de implementações, ou seja, existem centenas de produtos de banco de dados que oferecem o banco de dados relacionais, tanto implementações opensource quanto soluções proprietárias, quanto produtos em nuvem. Existe centenas de implementações, então você tem muitas opções e ela é sem dúvida uma das mais importantes, senão a mais importante e alguns projetos fontes de dados para projetos de BigData, então isso é muito importante.
Se você ainda ouve falar do conceito de que BigData é apenas aplicações Edusp ou no SQL, você está enganado ou quem lhe falou isso está enganado.
O modelo relacional ele é amplamente difundido, ou seja, eles existem dados em grande escala nesse tipo de modelo de dados e ainda se implementam se criam novas aplicações usando esse tipo de modelo.

Os outros modelos que nós vamos estudar depois, como os modelos NoSQL ou Streaming, foram modelos criados para outros tipos de aplicação, que é sobre os quais o modelo relacional não era apropriado.

Mas isso não quer dizer que ele está sendo substituído. Não, porque ele é um modelo de dados para tipos de aplicações específicas, que são aplicações bastante importantes. A gente vai ver a seguir aqui algumas implementações da DB2, Firebird, Informix, o Microsoft SQL Server, Oracle que é o mais utilizado no mundo, PostgreeSQL, que é o banco de dados que nós vamos implementar Alguns casos a gente vai fazer uma parte prática; Teradata que são algumas implementações proprietárias e opensource de bancos de dados relacionais.

Então por que o Banco Relacional?Ele é importante? Porque ele é bom para suportar grandes volumes de transações. Quando a gente fala de transação, a gente está falando de operações, ou seja, incluir registros, excluir, alterar, consultar. Você vai incluir uma venda, excluir um cliente, alterar os dados de um cliente.
Você vai consultar uma venda.
Ele é bom. Ele é rápido para esse tipo de aplicação. Ele tem uma característica importante, que é o que ele mantém a integridade. Ele reduz consideravelmente problemas de integridade. Ele reduz a redundância, a repetição dos dados e ele controla o acesso concorrente.

Ele não é bom para o quê? Então ele é bom para as questões transacionais, para manter a operação. Mas ele não é bom para análise de dados, porque a sua estrutura não comporta, não suporta de forma apropriada consultas complexas e também porque ele não mantém o histórico. Ele não é bom para ser escalável.

Se você precisa criar uma aplicação, ela tem que crescer muito, que ela precisa se desenvolver bastante. Existem, claro, produtos que oferecem questões escaláveis, mas não é uma característica principal. Não é uma característica chave primordial de bancos de dados relacional. E ele também não é bom para manter a redundância.

Ok, existem produtos que têm suporte a redundância, enfim, diversas possibilidades desse tipo. Mas isso é feito com o alto custo e um alto custo, tanto do ponto de vista de implementação, custo de retorno de investimento, de petición que é o custo total de aquisição do produto.
Então ele suporta, mas ele não é bom. Isso não é uma característica principal desse tipo de banco de dados, então ele é muito bom para sistemas de operação. Que são sistemas de operação? São sistemas responsáveis por suportar o negócio. A gente vai entender isso um pouco melhor depois .Ele mantém a integridade, ele reduz a redundância, ele controla transações.
Vamos ver cada um desses itens.

Então, o que quer dizer quando a gente diz que ele é responsável por suportar o negócio? Bom, quando uma empresa é criada, a primeira coisa que a empresa vai fazer é contratar. E ela vai comprar um sistema de gestão e um sistema de gestão que em 99% dos casos vai ser implementado em um banco de dados relacional.
Por que ela precisa desse tipo de sistema? Porque esse sistema vai manter a empresa funcionando. É nesse sistema que ela vai ter a contabilidade que ela vai ter a folha de pagamento que ela vai ter, os recursos humanos.
Ela vai controlar as contratações, por exemplo, que ela vai controlar a produção dela, as viagens. Então, antes de qualquer coisa, antes de ter uma solução de big data, um software de BI, uma solução de análise de dados, ela vai ter um sistema de transação, o sistema operacional, que vai ser implementado no modelo relacional, porque esse tipo de sistema mantém a empresa funcionando e onde ela vai incluir os clientes.
Ela vai incluir as vendas, ela vai controlar as contratações, os salários, a linha de produção.
Ele vai controlar a empresa toda, ele vai manter a empresa funcionando. Ele não é bom, como a gente já falou, para fornecer informações gerenciais, informações para os gerentes, para os executivos, para o presidente, para o conselho de administração. Não, ele não é um sistema bom para fornecer esse tipo de informação, mas para manter a empresa funcionando.

Ele é o melhor tipo de sistema de banco de dados que existe integridade.
Então, você imagine, por exemplo, que um cliente com contas a pagar é excluído. Você vai mandar o Contas a pagar para quem? Há cobrança? Para quem? Então o banco de dados relacional ele é bom pra isso. Ele não vai permitir que o cliente seja excluído, por exemplo, ele mantém a integridade das informações. É claro que integridade é um conceito muito mais amplo, mas esse é um exemplo importante. Tem essa outra característica importantíssima de um banco de dados relacional. Ele reduz a redundância. Então, existem sistemas de bancos de dados, sistemas de armazenamento de dados que eles têm um problema muito sério, com redundância.

Então, por exemplo, você imagina que você tem lá o cliente cadastrado, o cliente um, cinco, cinco, que lá no cadastro do cliente, ele tem lá o endereço Vicente da Fontoura um, sete, quatro. Lá, por exemplo, ele foi cadastrado lá na parte de vendas, ok. Então ele se vender um produto para ele. Eu criei o endereço dele.
Depois, quando vai ser feito o faturamento, se cadastra lá um outro endereço Alto Uruguai três quatro um, por exemplo, lá no sistema de faturamento.

Então, vejam que a gente tem o cliente cadastrado duas vezes com endereços diferentes e o mesmo cliente está cadastrado duas vezes. O vendedor lá cadastrou, o cliente colocou o endereço. Lá no faturamento, se cadastrou o cliente e colocou outro endereço. Você tem um problema de integridade, de redundância. O cliente está repetindo e depois a questão do controle de transações. Outra característica muito importante que é o controle de transações.

Existem operações, operações e operações que são executadas em um negócio que são independentes. Então, imagine se você tira fundos de um cliente a você atualiza saldo.
Você credita no cliente? Bem, você atualiza o saldo. Mas imagine, por exemplo, que quando você depois que você tirou o saldo daqui, você fez a atualização do saldo que está aqui. Você teve um problema e o sistema não atualizou o saldo no cliente B.

Quer dizer, este valor simplesmente desapareceu. Ele foi para o limbo. Ele deixou de existir. Então, é outra característica do sistema de bancos de dados relacional.
Ele tem um controle forte de transações. A gente vai estudar depois. A sigla é esse que fala bastante sobre isso. A gente vai entender esse conceito, bem mais aprofundamento aprofundadamente. Mas esse é um conceito também importantíssimo de um banco de dados relacional.