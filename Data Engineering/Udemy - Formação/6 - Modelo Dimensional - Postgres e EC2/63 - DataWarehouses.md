- 63. Data Warehouse
Construir o armazém de dados, seja um armazém de dados, um Data Warehouse  clássico, como um armazém de dados, um DataLake que a gente vai estudar em sessão posteriores. É sempre um processo complexo, demorado e caro, que requer mão de obra especializada. Então você precisa entender do negócio. Você precisa compreender estruturas de dados na sua origem e no seu destino. Você precisa desenvolver processos de carga e transformação desses dados. Isso envolve criação de scripts, uso de ferramentas. Então, não é uma tarefa simples, não é uma tarefa trivial.

Mas por que se constroem armazéns de dados? Por que a gente não extrai informação gerencial diretamente dos sistemas transacionais dos modelos relacionais dos sistemas de gestão? Bom, algumas pistas você já tem, a gente já viu alguns motivos, mas aqui a gente tem vários. Então, um ambiente analítico, ele não deve interferir no ambiente de transações. Então, imagine que você está lá faturando e, de repente, alguém roda uma consulta que faz uma junção entre dezenas de tabelas e milhares de registros. O seu sistema trava, ele cai e a sua empresa para. Então, esse é um motivo e um motivo importante.

Os dados no ambiente transacional não estão em formato apropriado para análise, então isso você já tem uma compreensão.
Lá no modelo transacional, os dados estão normalizados, divididos em várias tabelas, e eles não mantêm o histórico. Então não é um formato apropriado, bom para se executar análise de dados.
E outra questão importantíssima é que a informação gerencial para ser construída ela normalmente depende de dados que provêm de várias fontes, não de uma única fonte de dados, não apenas de um sistema transacional.

Então, por exemplo, um Data Warehouse de recursos humanos, ele vai, por exemplo, necessitar dados que vêm do sistema de recrutamento, do sistema de pontos, do sistema de folha de pagamento do sistema contábil. São várias informações que têm que ser consolidadas em um mesmo ambiente. Você não pode pegar de repente e rodar uma consulta que vai pegar e rodar uma consulta em vários sistemas e consolidar a informação. Você tem que buscar essas informações e extrair consolidar elas em um ambiente gerencial.

A expressão BI, abreviatura de business intelligence, significa o que ela se refere a um conjunto de ferramentas, tecnologias e processos que são usados para análise de dados.
Embora existam sistemas especializados em DataWarehouse, a maioria ainda é construídas em sistemas gerenciadores de bancos de dados relacionais, como a gente já falou anteriormente.
Em relatório, ele provê informação detalhada, informação estática, sem interatividade. Ela tem caráter operacional, não gerencial. A principal função de um relatório é conferência. Essa informação pode estar agrupada.
Ela pode trazer elementos gráficos e podem apresentar sumários, resumos por grupo, por página. Então um relatório não é uma ferramenta gerencial. O relatório é um detalhamento dos dados da operação, que normalmente são usados para fins de conferência.

Já um cubo aqui que a gente está tratando de informação gerencial. O cubo ele permite aumentar ou reduzir o nível de detalhe da informação.
Você pode aplicar filtros, agrupar sua forma elementar, a sua forma básica e textual. Porém, a maioria das ferramentas permite ainda que você produza gráfico.  

Um cubo normalmente ele representa um fato, ou seja, algum evento importante. Alguma operação importante da empresa, por exemplo, pode ter um fato Vendas Você tem dimensões nos eixos verticais e horizontais e as medidas no centro.

Então, aqui a gente tem um exemplo de um cubo que veio aqui, de um ERP, de um sistema de gestão que apresenta uma ferramenta de cubo. Então, aqui a gente tem ao centro as medidas e aqui nós temos dimensões, então eu posso resumir essa informação, por exemplo, aqui, se eu estou vendo aqui o apagar, eu receber da coligada, aberto por filiais e centros de cursos, eu posso fazer operações aqui que eu resumo e vejo o total consolidado, por exemplo, pela apenas pela coligada.

Dashboard são painéis visuais trazem informações resumidas, Informação gerencial do ponto de vista operacional, estratégico. Oferece características de navegação, não traz detalhes da informação gerencial, mas pode conter os maiores e os menores. Também pode ter os KPIs, que são os indicadores de performance, como por exemplo, as vendas com as metas de vendas. Então, aqui, um print de um dashboard é uma ferramenta que com certeza você já conhece, já teve interação.

Alguns problemas encontrados na construção de armazéns de dados. Diferentes plataformas e arquiteturas dos dados. Bancos de dados inacessíveis em formatos proprietários ou sem documentação. Qualidade de dados um problema global (problema crônico). Falta de documentação dos sistemas das fontes de dados e desconhecimento do negócio. Às vezes até 
as próprias pessoas da área de negócios têm dúvidas com relação a determinados cálculos ou determinados tipos de cálculos que devem ser feitos no banco de dados analítico no armazém do banco de dados. 

Então, são alguns dos problemas que a gente encontra na criação de armazém de dados. A gente vai ter uma exceção específica que a gente vai falar desses problemas, esses tipos de problemas, não só na construção de armazéns de dados clássicos, como de datalakes, de armazéns, de dados de big data e as principais ferramentas que a gente pode usar para mitigar esses tipos de problemas.
