- 70. Hierarquia e Compartilhamento
Existem informações, do ponto de vista de negócios, que elas têm uma hierarquia.
Então, por exemplo, uma hierarquia de data ano, mês, trimestre, dia, eu posso ter, até às vezes, informação por hora, uma hierarquia de localização de local, país, estado, cidade, bairro. Por exemplo, outra hierarquia de categoria de produtos em subcategoria e no produto propriamente dito.

Num modelo relacional normalmente existem diferentes entidades, diferentes tabelas para representar, por exemplo, produtos, subcategoria e categoria.
Por que? Porque lá não pode haver redundância dos dados e deve se manter a integridade. Então você armazena essas informações em tabelas diferentes e você mantém a integridade e a relação entre essas tabelas.

Já no modelo dimensional, essas categorias normalmente são colocadas em uma única entidade, numa única dimensão, por exemplo, produtos, claro que dessa forma, vai ocorrer redundância. Então, por exemplo, dez produtos que são da mesma categoria vão ser repetido dez vezes.

Mas a gente já viu que há redundância no modelo dimensional ela não é um problema, não é um grande problema. É um trade off que o modelo dimensional tem para prover informação gerencial de qualidade com histórico. Então, esse é um trade off, é a redundância.

Existe uma outra abordagem no modelo dimensional, que é chamada de Snowflake, que ela usa terceira forma normal para esse tipo de situação.
Então ela vai ter uma modelagem, por exemplo, de uma hierarquia semelhante à de um modelo relacional. Porém, ela torna as consultas mais complexas e pode degradar a performance, e uma opção de modelagem é decidido por quem está modelando o sistema dimensional.

Outro assunto são as dimensões compartilhadas, então uma dimensão ela pode ser compartilhada dentro de um  DataWarehouse para diferentes Data Marts uma dimensão compartilhada e importante não apenas por aspectos computacionais, ou seja, você vai carregá la apenas uma vez. Ela vai ocupar espaço em disco apenas uma vez, mas por questões de integridade e de negócio.

Então, por exemplo, imagine que a dimensão cliente, o fato cliente tem um status e se a dimensão não for compartilhada, ele pode aparecer como inativo. Os cliente podem aparecer com como inativo e um Data Mart e ativo em outros Data Marts. Então o cliente lá tem um status e esse status pode estar diferente se a se houverem dimensões diferentes deste mesmo cliente.
Se a gente está buscando informação desse cliente, sistemas transacionais diferentes, ou seja, na área de vendas e no departamento de Finanças é comum a informação estar diferente e ocorre de empresas em certo ponto, por exemplo, querer unificar dimensões que antes eram isoladas. Isso é possível, mas obviamente tem um custo operacional, financeiro e de tempo.

Então, aqui a gente tem um exemplo:
Uma dimensão cliente. Os dados do cliente aqui, mantendo o histórico, estão em uma dimensão, essa dimensão é compartilhada entre várias fatos, entre as vendas em que as devoluções, entre as reclamações, entre as entregas e o CRM (lá, as prospecções). E esses fatos podem estar em partes diferentes, mas que fazem parte de um mesmo Data Watehouse corporativo. Então, é um exemplo clássico de uma dimensão que é compartilhada entre diferentes DataMart.
