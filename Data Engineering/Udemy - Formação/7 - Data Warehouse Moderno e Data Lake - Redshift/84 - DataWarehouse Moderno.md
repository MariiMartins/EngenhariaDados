84. Data Warehouse Moderno
Olá, seja muito bem vindo a mais essa sessão onde a gente vai falar e a gente vai conhecer na prática um modelo de DataWarehouse moderno.

Na sessão passada a gente estudou o modelo dimensional e, como foi mencionado lá durante a sessão, o modelo dimensional, ele foi idealizado nos anos 90, ele tem um foco em negócio, que são os fatos, por exemplo, a gente viu lá vendas ele tem uma modelagem fácil, ele tem um foco em sumarização dos dados, que são as medidas. Ele trabalha apenas com dados limpos e carrega apenas a informação estritamente necessária, até porque na época o armazenamento ele tinha um custo muito grande e a utilização do modelo dimensional, assim como os bancos de dados relacionais, é principalmente baseado em índice.

Porém, se a gente for utilizar o modelo, ou se for analisar o modelo dimensional hoje, a gente não tem mais um problema de custo de armazenamento, o custo de armazenamento é praticamente insignificante, o custo de processamento baixou muito.

Então, calcular dimensões e medidas sob demanda quando você precisa pode ser muito melhor do que você ter que fazer um grande processo para tratar e armazenar dados no modelo estrela. E às vezes uma tabela normalizada é muito mais fácil de ser compreendida e consultada do que o modelo estrela.
Então a gente pode afirmar hoje que o modelo dimensional, ele é um modelo em desuso, mas eu garanto para você que não. Você não perdeu nada do seu tempo estudando os modelos dimensionais e praticando os modelos dimensionais na seção passada, primeiro que muitos dos conceitos do que você aprendeu lá ainda são válidos, e segundo, no seu dia a dia como engenheiro de dados, é bem provável que você vá se deparar com muitos modelos que com muitos armazéns de dados que foram modelados na forma dimensional e vão estar presentes e ativos ainda durante décadas.

Então existe modelos dimensionais que foram construídos ao longo de muitos anos. Então, mesmo hoje, provavelmente ninguém começaria a construção de um DataWarehouse utilizando um modelo dimensional, com certeza eles vão existir ainda por muito tempo.
Então, hoje a gente fala em DataLakes e DataLakehouses e a gente já estudou esses conceitos lá no início do curso. Então eles são otimizados para processar grandes volumes de dados.

Então DataLakes e DataLakeshouses são os armazéns de dados modernos da era Big Data, então eles são otimizados, são desacoplado dos dados. Isso quer dizer que, por exemplo, você vai ter DataLakes que os dados estão por exemplo, num formato ORC (é um formato de arquivo) que pode ser acessado por qualquer ferramenta. Diferente, por exemplo, de um banco de dados do Postgres que apenas o postgres de consegue ler o arquivo então está acoplado aos dados. 

DataLakes modernos, eles usam infraestruturas desacoplado de qualquer um formato de dado que não está vinculado exclusivamente à ferramenta.
São baseados em SQL e tabelas, então são muito semelhantes ao que a gente tinha antigamente. São mais amigáveis e têm um custo muito menor.

Então, essas aqui eu diria que são as principais ferramentas.
Quando a gente fala de DataWarehouse moderno, a gente tem o HIVE, que é uma ferramenta baseada no sistema Hadoop, e HDFS.
Você está fazendo aqui a segunda versão dessa formação de engenheiro de dados.A primeira versão nós construímos um DW no Hive.
Outra ferramenta existente, o Snowflake (outro popular da ferramenta para DataWarehouse), o Google Big Quarry e o Amazon Redshift.
O Amazon Redshift é a ferramenta que nós vamos utilizar nesta seção e é uma ferramenta que foi construída pelo Amazon, faz parte da infraestrutura do AWS e neste momento é a ferramenta de construção de DataWarehouse mais utilizada no mundo e a ferramenta mais popular do mundo, que então a gente vai ver aqui nessa seção como é que ela funciona.
