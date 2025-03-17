Nesta sessão a gente vai falar de armazenamento de arquivos e a gente vai ver alguns exemplos práticos
utilizando o serviço S3 do AWS.
E você vai entender durante essa sessão que um armazenamento de arquivos do ponto de vista de engenharia de dados não se trata apenas de um repositório de documentos. Quando a gente pensa em um sistema de arquivos, você pode pensar e lembrar onde, por exemplo, vão ser armazenados documentos da organização.

Na verdade, sistemas de arquivos orientados a dados, a objetos. Eles muitas vezes armazenam, armazenam dados vivos que são mantidos em sistema de arquivos. O que o que eu quero dizer com dados vivos? Quer dizer, por exemplo, que você pode ter um data warehouse, cujos dados eles são permitidos em um arquivo do tipo parquet, por exemplo. Ou o RCD, que são um sistema tipos de arquivos de big data que ficam armazenados no S3, no sistema de arquivos do AWS, que é o S3.  Também esse tipo de sistema de arquivos é muito utilizado para transmissão de dados entre diferentes sistemas. A gente vai ver alguns exemplos durante o nosso curso.

E o que um sistema de armazenamento de arquivos apresenta como característica?
São muitas as características, além de simplesmente armazenar os arquivos. A primeira característica que ele permite você versionar os arquivos, então você pode manter diferentes versões de um mesmo arquivo. A outra característica importantíssima é a segurança, tanto do ponto de vista de controle de acesso, quem vai ter acesso àquele arquivo quanto do ponto de vista de criptografia.
E uma outra característica importante é com relação ao ciclo de vida, então a gente vai ver durante esta sessão que você, em muitos casos, você vai ter um requisito de acesso diferente aos dados conforme seu ciclo de vida.  Então, logo que o arquivo é criado, você pode querer um acesso mais frequente, mais veloz. Mas com o passar do tempo, não, e depois você pode querer até excluísse arquivo. Então você pode fazer esse gerenciamento do ciclo de vida do arquivo.

As outras são características relacionadas a big data.
O que seria isso, por exemplo, particionamento. Você pode dividir os dados em partições para aumentar a performance. A gente vai falar que algumas vezes durante o curso, que o particionamento é uma das técnicas de otimização de dados na era Big Data. Antigamente, quando eu tinha apenas bancos de dados, a gente falava em indexação, hoje a gente fala em particionamento.

E a outra é a escalabilidade, você poder aumentar sua capacidade.  Então, é isso que um sistema de arquivos para dados disponibiliza.
Alguns exemplos de sistema de arquivos.
Então o S3 que do AWS, que é o que a gente vai estudar mais a fundo e a gente vai ver na prática o
HD FS, que faz parte do ecossistema Hadoop. Ele é um sistema mais antigo, mas eu diria ser o percursor de um sistema de arquivos voltado para Big Data e um outro é o Azure Blob Storage.

Para citar alguns exemplos, vamos falar então do AWS S3.
Então o AWS, S3 permite que a gente armazene dados arquivos que podem ser objetos, qualquer tipo de arquivos nos chamados buckets, você pode pensar no buckets como uma pasta raiz.
O buckets tem uma característica que ele deve ter um nome único global. O que quer dizer isso?
Quer dizer que quando você vai criar um buckets, você tem que dar um nome para ele que não vai existir outro nome igual no mundo. Isso é em função de que o nome é usado como a URI, o endereço de acesso do que está dentro do buckets. Então esse nome tem que ser único.
Então, os objetos, ou seja, os arquivos que você coloca no S3, eles vão ter uma chave. Essa chave é formada pelo caminho completo do arquivo. Então você vai ter um buckets, por exemplo Arquivo Vendas. CSV. Ou você vai ter um buckets com o nome o único dentro dele, uma pasta um, depois uma pasta dois e lá no último nível, o arquivo de vendas. Ou você pode ter outro arquivo dentro da pasta um ou da pasta dois. Como um era um sistema de arquivo normal.
Então esse tipo de possibilidade de você dividir isso em pastas é interessante quando a gente falar de partições, aí a gente vai ver alguns, alguns exemplos. Bom, o tamanho máximo de um objeto para o S3 é de cinco terabytes.
Se você precisa armazenar algo maior que cinco terabytes no S3, você vai precisar dividir esse arquivo antes de colocar no S3. 

Outra característica de um buckets no S3 é que você pode criar tags de objetos que são conjuntos de até dez chaves, valores que são úteis para você controlar a segurança e o ciclo de vida dos objetos.
Então eu vou citar um exemplo aqui você pode criar uma chave dizendo que um determinado arquivo ele tem informações sensíveis do cliente, por exemplo.

Para citar  um exemplo bom, falando do S3, do ponto de vista de ciência e engenharia de dados.
Então, como eu já havia mencionado ele, ele tem o suporte para muitos. Ele oferece o suporte para muitos serviços de ciência de dados e Machine Learning do AWS, como por exemplo

SageMaker, que é uma ferramenta de machine learning do AWS. Você pode no próprio criar um Data Lake, você no S3 que tem tamanho infinito, sem provisionamento. Isso quer dizer que você não precisa provisionar anteriormente.
Antes de usar, você simplesmente vai utilizando e é claro que você vai pagar conforme o uso. Você tem uma durabilidade aqui de 99,999%.

O que é durabilidade? A durabilidade seria uma medida do quanto o serviço na nuvem ele é saudável e resiliente.
Então, o bucket do S3, ele tem uma durabilidade altíssima. Uma outra questão importante é que o armazenamento do S3 ele é desacoplado do processamento. Isso pode, em princípio, não parecer importante, mas é.

Vamos pensar, por exemplo, num banco de dados relacional tradicional, você tem os dados, o armazenamento acoplado à ferramenta. Então, um faz parte do outro, um depende do outro. Com o S3, você consegue criar sistemas em que não há esse acoplamento. Você pode ter dados independentes da ferramenta e, dessa forma, esses dados ou esses arquivos podem ser utilizados por diferentes ferramentas. Não existe essa relação direta.

Bom, a outra característica é a arquitetura centralizada, ou seja, você vai ter todos os seus dados em um único lugar.
Se você está utilizando o EC2 lá, por exemplo, a gente vai utilizar ou o Red Shift também vai utilizar. Todos eles vão, eles podem acessar o mesmo ou os dados do mesmo lugar.

Armazenamento de objetos suporta qualquer tipo de arquivo e os formatos mais comuns, como a gente quando
a gente fala de engenheiro de dados são CSV, JSON, o Parquet, ORC, AVRO e o Protobuf.
Bom, vou falar um pouquinho então de particionamento.
Então o particionamento é uma técnica de otimização de operação de aplicações orientadas a dados modernas, e ela é muito, muito interessante para você acelerar as consultas.
Como? Então eu vou explicar aqui o exemplo: Vamos supor que você vai carregar, você vai analisar dados de vendas.
Você vai ter alguns terabytes ou até petabytes de dados de vendas. Então, em vez de você ter um único arquivo que não necessariamente precisa ser um arquivo CSV, pode ser um ORC. Por exemplo, em vez de você ter um único arquivo e você trabalhar com um único arquivo, você vai particionar isso, você vai dividir isso.
Então, por exemplo, você pode ter um Bucket com nome único. Você vai ter dentro do bucket uma pasta, vendas, ano, mês, dia, hora. Então, neste caminho único, você vai ter apenas as vendas daquela hora. Então, quando você fizer uma consulta de determinada hora ou  se o particionamento fosse até um determinado dia, as vendas daquele dia ou daquela hora estariam em um local único. Por isso, você teria uma otimização muito grande nas consultas. Você não precisaria carregar as vendas, por exemplo, do dia inteiro. Você teria apenas da hora que você precisa.

Outro exemplo de particionamento você poderia particionar por produto. Então você teria o Bucket, as vendas, que é o tipo de aplicação, o identificador do produto, então você teria os dados.

Então o S3 é, em geral, esse tipo de sistema.
Ele permite que você defina a estratégia de particionamento que você quer utilizar e fica mais interessante ainda.
Quando eu falar para você que você pode que algumas ferramentas do AWS, elas próprias criam e gerenciam o particionamento. Então, por exemplo, o Glue é uma ferramenta que faz isso.
O Athena, que é um serviço para consultar dados. Então eles interagem de forma muito amigável, muito simples, com dados particionado. Ok, então agora a gente vai começar a ver na prática, algumas características do S3
