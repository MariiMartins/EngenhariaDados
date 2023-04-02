12. Operacional VS. Analitico

Uma distinção importante que você precisa ter claro durante o curso são que existe um modelos de dados, existe uma grande variedade de modelos de dados, mas existe aqueles modelos de dados que são criados para questões operacionais, para produção de dados. Então algum evento natural ou empresarial produz informação e esse modelo de dados armazena essa informação. 

Existem aqueles modelos de dados analíticos que servem apenas de repositório de container, de armazém da informação para que se produza conhecimento, para que se produza informação e conhecimento desses dados.

Então, exemplos de modelos de dados, armazéns de dados operacionais são: Sistemas transacionais, também conhecidos como OLTP, Sistemas de banco de dados NoSQL, muito embora se utilizem os dois transacionais e NoSQL não para questões operacionais, mas são exemplos clássicos de armazéns de dados que registram operações.

E os modelos de dados analíticos são o Data Warehouse, os modelos dimensionais, os Data Lakes e os sistemas OLAP.

Então, o modelo transacional tem o objetivo de manter operações. O modelo analítico tem objetivo de apoiar a decisão, gerar informação analítica, gerar relatórios, gerar dados para apoiar a tomada de decisão.

Então aqui a gente traz algumas distinções entre esses dois modelos.

|Operacional	| Analítico|
| ------------- | ------------- |
|Produz dados |	Carrega dados produzidos de várias fontes|
|Consulta, Inclusão, Exclusão, Atualização	| Inclusão e Consulta|
|Não mantém histórico |	Mantém Histórico|
|Redundância mínima ou nula	| Redundância|
|Pode ter grande volume	| Volume sempre maior|
|Objetiva Integridade |	Objetiva Informação de Qualidade|
|Orientado a processo |	Orientado a negócio|

O modelo operacional; Lá se produzem dados, então os dados são gerados, armazenados lá. No  analítico, se carregam dados produzidos de várias fontes, inclusive do modelo operacional.  Então, no modelo analítico, não se encontra dados que foram produzidos normalmente. Eles foram carregados de outras fontes de dados de onde o dado foi produzido.

No modelo operacional, as principais operações são de consulta, inclusão, exclusão e atualização. No analítico se faz inclusão e consulta, não existe problema de deadlock encontrados em modelos relacionais. Aqui no analítico também a gente vai estudar o que é um deadlock durante o curso. Mas aqui o que acontece no modelo analítico não existe, por exemplo, leituras sujas.O dado não está sendo atualizado, uma vez que você só inclui e só consulta.

O modelo operacional não mantém histórico se você atualiza uma informação, por exemplo, de um cliente ou a informação que você perde, se você atualiza o endereço, o endereço, então se perde no modelo analítico. Então, ele mantém o histórico no modelo operacional, não tem redundância ou redundância, é pouca e mínima, ou seja, os dados não são repetidos.

O modelo analítico tem redundância de dados. O operacional ele pode ter um grande volume, mas no analítico sempre o volume de dados vai ser maior porque, por causa da redundância operacional, ele objetiva manter integridade.

Você tem que manter todos os aspectos da venda.Por exemplo, você não pode ter a venda repetida, o cadastro do cliente repetido. No Analítico  objetivo é informação de qualidade se você cadastrar lá, se você repetir o registro do cliente várias vezes, não tem problema. Aqui ele é orientado ao processo e aqui ele é orientado a negócio.

Por que existem dois modelos?
- O modelo operacional, como já falou, não mantém histórico o modelo operacional ele é voltado para minimizar redundância e manter integridade.
- O modelo analítico mantém histórico , ele é ideal para apoio e decisão para apoio à tomada de decisão.
## São modelos diferentes.
O modelo analítico ele responde perguntas como por exemplo, quais produtos vendem mais? Que campanhas de marketing foram mais efetivas? Que clientes retomaram o controle de novo? Qual a margem de lucro por produto?
São questões que são respondidas no modelo analítico.

O modelo transacional/operacional. Ele não traz a resposta certa e pode executar algumas consultas a algumas consultas e extrair alguma informação analítica. Mas não é a principal. Não é o principal objetivo dele. Em vez de responder quais produtos vendem mais? O objetivo daquele modelo é registrar a venda e manter o processo. A operação de venda funcionando, então, é importante de ter essa distinção no restante do curso.