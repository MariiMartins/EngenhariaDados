143. Kinesis Streaming
Bom, então vamos falar sobre o a AWS Kinesis e a gente vai ter uma visão geral sobre ele, sobre as ferramentas que compõe o Kinesis.

Então o Kinesis é uma alternativa diferenciada do Apache Kafka. O Apache Kafka é um produto open source da Fundação Apache, e você pode também utilizar o Apache Kafka no AWS, o AWS também provê um serviço para o Apache Kafka, porém o que dizes é um produto proprietário da AWS do Amazon. E é uma aplicação serverless, embora a gente vai ver depois que você possa definir o número de shards, ou se pode ou não definir o número de Shards, mas você não precisa provisionar servidores.

Então, entre os exemplos de aplicações log de aplicações de IOT, o exemplo da Fórmula 1, clickstreams, vídeo são infinitos tipos de aplicações.
Clique Streams são ou é um tipo de aplicação que faz que registra a trajetória de um usuário conforme ele percorre um website. Então, o Kinesis para processar dados ‘em tempo real’, em tempo real aqui, entre aspas, porque não é, de fato, em tempo real.

Bom, então são três ferramentas principais aqui que compõem o Kinesis .
•	Kinesis Streams então a ingestão de streams com baixa latência e em grande escala. Então você vai ver o Kinesis Streams, mencionado, por exemplo, na AWS como simplesmente streams de dados. Do ponto de vista de serviço ela é mais simples, do ponto de vista de arquitetura bem complexa, mas você vai ver que você simplesmente cria um serviço e esse serviço vai ser como se fosse um intermediário entre produtores de dados e consumidores. 
Então, é como se fosse uma aplicação que centraliza isso. Aí você até pode pensar Mas por que eu preciso ter uma aplicação centralizando? Não pode o produtor entregar diretamente para o consumidor? Num caso bem simples, até poderia, mas uma ferramenta como o que não existe. Primeiro que ele não fica acoplado à aplicação. Então, ela é uma ferramenta independente do dos produtores ou dos consumidores. Uma outra coisa que é processar dados, produzir dados e ler dados ou consumir dados em tempo real com grande volume pode trazer muitos problemas. Imagine, por exemplo, se o seu consumidor, se a aplicação que precisa ler esses dados, ela fica indisponível. Ela não consegue, por algum período, ler esses dados. Se ela está acoplada diretamente com quem está produzindo com o dispositivo IOT lá, por exemplo, ela vai ter uma perda desses dados. 
Uma outra coisa que pode acontecer é que você pode ter muitos consumidores e o produtor ele tem um período lá que ele produz uma carga muito grande de dados e os consumidores não conseguem ler isso. Isso se cria um gargalo desses, desses dados. Então, você ter essa aplicação central, ela faz o gerenciamento disso. 
Uma outra questão é a garantia de entrega: Você, às vezes, conforme o tipo de aplicação, você precisa ter certeza que o consumidor ele recebeu a informação que foi produzida. 
Um exemplo lá que a gente já falou, por exemplo, você precisa ter certeza que o dado gerado pelo Sensor Lab caiu de forma que não foi recebido lá pela aplicação do engenheiro da equipe. Então, quando a gente fala de cenário, de big data e de produção de dados, a gente tem cenários que podem ser extremamente complexos e que uma aplicação, como que níveis de streams, ele traz essas garantias e essa alta disponibilidade.

•	Depois, uma outra ferramenta, Kinesis Analytics, executa a análise em tempo real em streams usando SQL.
•	E a outra, deita Alcanizes Data Firehouses: ele carrega dados no S3 do AWS, que a gente já conhece e pode integrar Redshift, pro ElasticSearch e Splunk, então você pode ver no AWS como streaming de entrega.

Qual é a diferença entre o Kinesis Streams e o Kinesis Data Firehouse?
O Kinesis Streams, ele é simplesmente o intermediário, o Kinesis Firehouse  não,  ele entrega dados. Então, por exemplo, o Kinesis Data Firehouse, ele pode receber dados, por exemplo, do Kinesis Streams.
Você pode ter um produtor que entrega dados pro Kinesis Streams e o Kinesis Data Firehouse pode ser um consumidor desses streams, então são aplicações diferentes.
E o Kinesis Analytics ele executa análises de dados.

Então, aqui a gente tem um diagrama de uma aplicação de tempo real. Então você tem Click streams, dispositivos de IOT, métricas e logs. Então você tem o Kinesis streams recebe esses dados, você tem o Kinesis Analytics, que está associado a esses streams de dados e o Kinesis Data Firiehouses que pode fazer a entrega desses dados, por exemplo, lá para um bucket do S3 ou para o redshift. Então a gente pode, por exemplo, usar o Firehouses para pegar os dados e colocar no S3 ou no redshift.
Se você estiver, por exemplo, criando um DW lá.

No nosso caso prático, a gente vai utilizar o FireHouse para colocar os dados num bucket do S3.
Então vamos ver que uma visão geral do Kinesis stream: Então os estilos são divididos em shards, que são ordenados e particionados.

O Kinesis Stream é uma aplicação intermediária, então ela está aqui no centro.
Ela pode conter shards, você pode provisionar shards. Você pode dizer lá, por exemplo, que a sua aplicação, Kinesis Streams ela vai ter três shards ou você pode definir que ela vai escalar automaticamente.

•	Então você tem os produtores, os shards, o Kinesis Streams, formado por um ou mais shards e os consumidores. Então os shards podem ser provisionados com antecedência, ou você pode simplesmente definir que o próprio AWS vai definir.

•	Retenção de dados é de 24 horas por padrão, podendo chegar até sete dias. Então, o consumidor ele pode ler dados que foram produzidos já, até, por exemplo. No caso, se tiver configurado por padrão 24 horas depois, ele pode definir um timestamp lá e recuperar esses dados, caso ele não tenha conseguido ler esses dados próximo ao tempo real, ou a medida que eles foram produzidos, então ele é capaz de processar os dados.

•	Uma outra coisa que várias aplicações pode consumir o mesmo streaming. Então, quando estamos falando de consumidores, a gente pode ter vários consumidores. Então, no caso do exemplo do carro de Fórmula 1, os dados dos sensores pode estar indo para várias aplicações, são vários consumidores.

•	E uma vez que os dados são inseridos no Kinesis ele não pode ser mais excluído e o conceito de imutabilidade, ele está lá e não pode mais ser excluído. Mas claro que depois do período de retenção, ele não vai estar mais disponível.

•	E um registro ele pode ter até um megabyte de tamanho.


Uma questão que é a respeito dos shards, obviamente que quanto mais shards mais velocidade de processamento você tem.
Eu falei aqui, por exemplo, que os registros pode ter até um megabyte de tamanho Isso é ok para streaming, mas não é feito pra você, por exemplo, processar petabytes de dados. Se você precisar processar a base de dados, você precisa de uma aplicação em Batch.

Então, o Kinesis é usado para processar pequenos registros em streaming em tempo real, que são produzidos em tempo real.

Então, aqui, as características do Kinesis. 
•	Produtores:
o	Os produtores pode produzir 1 megabits por segundo ou 1000 mensagens na escrita por Shard. Então, se você precisar mais que isso, você precisa provisionar mais shards.
o	Se ultrapassar esse limite, você vai ter uma exceção: “ProvisionedThroughputException”
•	Consumidor Classico:
o	O consumidor típico ele pode ler 2 megabytes de leitura por Shard entre todos os consumidores, como já falou lá, já falou, pode ter vários Consumidores.
o	5 chamados de API por segundo por shard entre todos os consumidores.
•	Retenção de Dados:
o	24 horas por padrão e pode ser estendido até sete dias.

Por que tem essa questão de retenção de dados?
Porque o Kinesis não é um banco de dados, ele não tem o objetivo de armazenar dados, Ele é apenas um intermediário (A gente está falando aqui do Kinesis streaming).
O Kinesis Firehouse, por exemplo, ele nem sequer vai ter período de retenção.
Ele vai simplesmente fazer a entrega desses dados.

Outra coisa que precisa ficar clara aqui é que os Kinesis escala com a adição de shards. Isso pode ser feito automaticamente ou você pode provisionar esses shards.

Bom, o Kinesis Data FireHouse, então, é um serviço totalmente gerenciado.
Nesse caso, o que você não precisa provisionar nada, não tem nenhum tipo de administração. Ele é próximo ao tempo real. Ele tem uma latência de 60 segundos. (Você vai ver lá quando a gente executar a nossa parte prática lá, que os dados eles vão ser entregues lá depois de um de um tempo. Não é que nem o Kinesis Stream, que os dados estão sendo processados o mais rápido possível).

Que o Kinesis DataFirehouse ele tem uma latência maior. Ele pode ter a ingestão de dados do redshift do S3, do ElastickSearch, do Splunk.

Escala automaticamente, a gente já falou que ele não é gerenciado. Ele suporta vários formatos de dados. Ele pode fazer conversão de dados de CSV ou JSON para Parquet ou ORC.

Você pode utilizar uma função lambda do AWS para fazer transformação de dados. Ele suporta compressão dos dados e você paga pela quantidade de dados que entra no Firehouse então,  aproveitando aqui um lembrete esses serviços não têm aqui FreeTier, mas se você executar as aulas, o valor que você provavelmente vai gastar, ele vai ser irrisório.

Uma comparação aqui do Kinesis streaming versus o FireHouse.
Então o Kinesis streams você pode escrever com código customizado, então você pode criar o seu produtor, seu consumidor, Ele é em tempo real. Então a latência é de 70 milissegundos a 200 milissegundos. Você deve gerenciar escalabilidade, então tem a divisão. O Merge de Shards a gente vai ver melhor, a gente vai entender melhor essa questão de Shards. Então, o armazenamento de dados que já falou de 1 a 7 dias, capacidade de replay e múltiplos clientes.

O FireHouse é um serviço totalmente gerenciado e ele envia os dados para o S3, Splunk, Redshift, ElasticSearch. Ele é serverless Pode ter uma transformação com lambda.
Próximo a tempo real então o menor tempo de buffer é um minuto, então os dados não vão aparecer no destino imediatamente. Escala automaticamente e não tem armazenamento de dados. Então ele vai simplesmente fazer a entrega de dados lá no destino. Ele não tem um período de retenção como o que níveis Streams tem, então são serviços com características diferentes.