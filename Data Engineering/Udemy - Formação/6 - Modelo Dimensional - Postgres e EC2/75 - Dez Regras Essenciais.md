75. Dez regras Essenciais
Nós vamos falar agora das dez regras essenciais da modelagem dimensional.
Essas dez regras você encontra no link que está aqui na tela, E elas foram propostas pelo Ralph Kimball. Ralph Kimball é um autor clássico, talvez um dos mais conhecidos e renomados na área de construção de armazéns de dados de modelagem dimensional. Entre as obras dele tem o clássico de DataWarehouse Toolkit.

Outra referência na área de modelagem dimensional é o Bill Simon, que é conhecido como pai do DataWarehouse  moderno.

Então vamos ver as dez regras. Obviamente que você pode consultar também lá o link que está no slide anterior.
•	Primeira regra então carregue dados atômicos e detalhados na estrutura dimensional.
•	Estrutura e modelos dimensionais a partir de processos de negócio. Então, o foco do modelo dimensional é os processos de negócio.
•	Garanta que cada tabela fato tem uma dimensão de data relacionada. Então lembra que a gente falou que a data, dimensão, data é uma dimensão obrigatória e que a tabela fato deve estar relacionado, obviamente, com a data. Não faz sentido você ter uma dimensão, data ou qualquer outra dimensão que não esteja relacionada com o fato.
•	Garanta que todos os fatos de uma mesma tabela fato têm o mesmo nível de grão. Tem que ter o mesmo nível de detalhamento.
•	Resolva relações muito para muitos na tabela Fato. Isso aqui é importante. A gente já falou, né? Relações muito para muito elas vira um fato.
•	E relações, um para muito. E elas virão Dimensões.
•	Armazene rótulos e valores de filtros em tabelas dimensões.
•	Tenha certeza que tabelas, dimensões usam uma chave substituta.Então a gente falou também que é uma coisa importantíssima, relembrando que eu já comentei é muito comum em aulas e aulas de modelagem dimensionar o que eu dou em atividades práticas os alunos não criam a chave substituta ou eles criam a chave substituta com a chave primária do banco de dados E sempre falta alguma falta outro. Então você tem que ter a chave substituta mais a chave primária do modelo relacional, que obviamente no modelo dimensional não vai ser uma chave substituta. Vai ser apenas mais um atributo da dimensão.
•	Crie dimensões compartilhadas para integrar todos os dados por toda a empresa. A gente já falou também na questão da dimensão cliente, você ter uma verdade única, uma fonte de informação única compartilhada para todos os armazéns, para todos os Data Marts, de todas as áreas de negócio da empresa. 
•	Avalie os requisitos continuamente e garanta entregar uma solução de DataWarehouse BI que é aceita pelos usuários de negócio e que suporta suas tomadas de decisão.
Então são essas dez regras essenciais da modelagem dimensional