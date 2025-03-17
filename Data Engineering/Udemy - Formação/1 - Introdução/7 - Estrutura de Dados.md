7. Estrutura de Dados
Existem três estruturas principais de dados.
Dados estruturados, dados semiestruturados e dados não estruturados.

Dados estruturados são aqueles que têm uma estrutura rígida. 
Eles estão armazenados nessa mesma estrutura.
Exemplo tabelas de sistemas, gerenciador de banco de dados, uma planilha eletrônica. Então a estrutura de dados estruturados. Normalmente ela é rígida. O que você tem que seguir? Você tem que incluir dados seguindo essa estrutura que está pré-definida de acordo com o tipo de dado.

Depois, nós temos os dados semiestruturados.
Eles têm uma estrutura heterogênea. Eles não são completamente se estrutura. Existe uma representação de estrutura, porém ela não é muito rígida. Ela é evolutiva. Ou seja, é mais fácil a ocorrer uma mudança na sua estrutura do que com relação aos dados estruturados que nós vimos anteriormente.
Exemplos de dados semiestruturados são um arquivo XML ou um arquivo de um arquivo XML, por exemplo, de uma nota fiscal eletrônica, um arquivo JSON e formatos específicos de documentos. Então, aqui, um exemplo de um arquivo JSON que é uma lista de alunos, então a gente vê que existe uma, uma estrutura, porém não é uma estrutura rígida e não está completamente estruturado.

E, por fim, temos os dados não estruturados.
São dados sem estrutura nenhuma. Não há nenhuma definição de estrutura. Você vai criar esse tipo de dado sem qualquer padrão, sem qualquer definição. Não existe metadados, ou seja, não existe uma descrição dos dados.
Que tipo de dados? Qual é o tamanho?  Aonde o dado deve estar? Qualquer ordenação.
Não existe nenhuma restrição com relação aos dados.
A maioria dos dados existentes no mundo de 80 a 90% são dados não estruturados porque são documentos e também é também o formato que mais cresce. É o tipo de dado que mais se produz e que mais cresce na era de Big Data.
Exemplos de dados não estruturados.
Então, tudo o que é tipo de informação, que não tem estrutura nenhuma, não tem estrutura definida. Então, vídeos, imagens, páginas de internet, recibos eletrônicos, e-mails, o tweet. Como está vendo um tweet do Barack Obama?
Qualquer tipo de documento, um documento sem estrutura. 

Independente da estrutura existem formatos de documento.
A gente vai falar bastante sobre esses formatos ao longo do curso, mas a gente está vendo aqui alguns. A gente vai adiantar alguns. 
Então existe um formato chave, o valor, esse formato chave, o valor. É um formato que a cada linha existe uma chave, que normalmente é um valor único, seguido de um valor qualquer. 
Existe o formato texto, que é o famoso, por exemplo, CSV, que são os arquivos separados por vírgulas ou por ponto-vírgula ou, 
ORC são arquivos colunares ou em colunas que também armazenam chave-valor. É um dos modelos mais importantes do ecossistema, reduto que a gente vai estudar bastante.
O AVRO também é um modelo do ecossistema, reduto da Fundação Apache. Ele é um formato serializado, então ele tem uma taxa de compressão maior.
E aqui tem o Parquet, que também é um formato ordenado por colunas.

A gente vai entender mais para diante a diferença entre dados orientados a linhas e dados orientados a colunas.

Por fim, a questão da arquitetura de dados.
Então, existe uma distinção bem grande, bem importante entre sistemas que fazem produção e guarda e os sistemas que fazem armazenamento e análise.

Quando a gente fala de produção e guarda, a gente está falando do famoso ambiente transacional, ou seja, você está registrando fatos e depois você vai recuperar registros. Então é um sistema de contas a pagar um sistema de linha de produção, um sistema de folha de pagamento, o sistema contábil. São todos sistemas que produzem e guardam informações. Normalmente, o objetivo deles é manter a operação da empresa, processar eventos, processar eventos diversos. Como eu falei, vendo a folha de pagamento, não tem aqui informação, não tem fins gerenciais. Não existe aqui um objetivo de se produzir informação e conhecimento. O objetivo é manter uma operação qualquer.

E depois é que a gente tem no armazenamento e análise o ambiente analítico. O objetivo aqui é manter os acontecimentos a longo prazo, servir de depósito central de informações, processar dados e gerar informações e conhecimento para a organização. Então, aqui os dados não são produzidos, aqui eles não são gerados.
Eles são transformados e armazenados em um ambiente especificamente criado para produção de informação e conhecimento. 

A gente vai também falar bastante sobre tanto os ambientes de produção, os ambientes transacionais quanto dos ambientes analíticos ao longo do curso.