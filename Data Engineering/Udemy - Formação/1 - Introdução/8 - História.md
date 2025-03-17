8. História
Vou falar um pouco da história dos bancos de dados.
Então, aqui, a história dos bancos de dados, então, mais ou menos ela inicia em 1960 com os mainframes.
Então existiam lá os modelos Cobalt e o IMS.

Em 1970.
O famoso modelo relacional foi proposto por Codd. Ele trabalhava para a IBM e publicou um documento com a proposta do modelo relacional.

Em 1974, começaram a ser produzidos os primeiros sistemas baseados no modelo relacional. Foi  Igres da UBC e  System R da IBM que tiveram relativo sucesso. Obviamente que os produtos, as tecnologias de armazenamento e o hardware não era algo tão acessível como ficou sendo há algumas décadas depois.

Em 1976, o Shaheen. Ele propôs o modelo, entidade de relacionamento que também se tornou um padrão.

Em 1980, começou a popularização do modelo relacional e ele se tornou um padrão e é até hoje o modelo muito popular e padrão. Junto com ele surgiu a linguagem SQL, que também é uma linguagem declarativa fácil de alto nível e que até hoje é muito utilizada e é uma linguagem bastante popular, tanto que a gente vai ver ao longo do curso que ambientes de processamento de dados para Data Warehouse de Big Data, como o River, tiveram a preocupação de criar uma linguagem declarativa de alto nível compatível com SQL.

Em 1990 surgiram alguns bancos de dados orientados a objeto porque banco de dados orientado a objetos porque o modelo relacional ele tinha uma diferença entre os objetos do mundo real. E isso e trazia algumas dificuldades, alguns problemas na modelagem, principalmente entre a interação da aplicação e o banco de dados.
O modelo orientado a objeto.
Ele não precisava dessa abstração entre o modelo relacional e a aplicação, porque você podia representar entidades do mundo real no próprio banco de dados.Existe alguns bancos de dados orientado a objetos, mas ele nunca se tornou tão popular quanto os modelos relacionais.

A partir dos anos 90, também começou a popularização dos armazéns de dados.
Até então se produzia informação gerencial diretamente do banco de dados relacional, se rodavam consultas e se produziam relatórios. Só que isso começou a trazer vários tipos de problemas que a gente vai ver ao longo do curso.
Então, a partir de 1990, começou a se criar modelos de dados exclusivamente para fins de análise de produção e informação. Os famosos armazéns de dados que, em vez de serem modelados no modelo relacional, eles tinham uma modelagem conhecida como dimensional e praticamente toda grande empresa começou a construir Data Warehouses e ambientes.

Bom por volta do ano 2000, quando começou o fenômeno que a gente já estudou, conhecido como Big Data, se percebeu que os bancos de dados relacionais eles não tinham uma boa performance ou um bom suporte para determinados tipos de aplicações. Eles eram ótimos. Eles são ótimos para aquelas questões que a gente estudou lá, de manter transações, de manter operações, vendas, enfim. Mas para outros tipos de aplicações, eles não tinham uma boa performance. Então, começou a se criar uma série de outros modelos de dados e estes modelos passaram a ser conhecidos como No SQL, que inicialmente queria dizer não SQL mesmo, mas que depois se mudou e se propôs que se quisesse dizer não apenas, not only SQL. Porque algumas dessas ferramentas têm suporte também a SQL é um dialeto semelhante ao SQL. Então, o NoSQL, como são quatro principais grupos de bancos de dados que nós vamos estudar. Na teoria, alguns deles e na prática também.
Então, são os bancos de dados orientados a gráfico, os bancos de dados orientados a documento, chave-valor e os orientados a coluna.

Sem dúvida. Aqui, os mais populares, os mais utilizados quando a gente fala de NoSQL são os orientados a documento. Mas, claro, também bancos de dados orientados a gráfico e chave-valor também são bastante populares.
E também começou a ocorrer então uma grande migração de banco de dados e de aplicações para nuvem. 
Por quê? Porque principalmente tem um custo menor, você não precisa lidar com infraestrutura, energia, suporte, conexão. Todas as questões de segurança, elas ficam por conta, podem ficar por conta do provedor de serviço.
O crescimento sob demanda é praticamente instantâneo. Você não precisa, por exemplo, cotar o novo storage e esperar ele chegar com 60 dias de atraso, por exemplo. Então, você pode, por exemplo, contratar um serviço com tudo incluso manutenção, backup, segurança.
Então, existe hoje uma grande tendência de aplicações também de Big Data ser importados para a nuvem.
E, é claro, existe aplicações híbridas que partes estão dentro da empresa, parte estão na nuvem.
Existe, claro, aqueles tipos de negócios que, por questões de governança, como empresas na área financeira, que por esses requisitos elas mantêm toda a infraestrutura, toda a aplicação prime seu, seja dentro da empresa, mas de maneira geral. As aplicações de Big Data cada vez mais são encontradas, são produzidas, mantidas numa nuvem.
 