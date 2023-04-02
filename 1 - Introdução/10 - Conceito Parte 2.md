10. Conceitos parte II
Outra questão importante é o de change data capture, change data capture são tecnologias ou processos de capturar mudanças em dados transacionais a partir do log de transação ou de outros tipos de formas de captura.
Ele pode ocorrer de duas formas incremental que ele faz carga de mudanças.Ele pode ser síncrono que captura à medida que as mudanças ocorrem ou assíncrona, ele faz a captura em intervalos.
Ou ele pode ser bulk, ele faz a carga de todos os dados, então ele pode ser incremental, que carrega essas mudanças ou bulk que faz a carga toda.

Os sistemas de Change Data Capture são bastante importantes, principalmente em sistemas de streaming, que são aqueles que capturam os dados e processam em tempo real. Outro conceito que a gente vai falar a partir daqui dos próximos slides é o de disponibilidade.
Então, um sistema distribuído, um sistema em cluster, ele tem vários riscos. Ele pode sofrer falhas de software, ele vai estar rodando com uma diversidade de software, não apenas o próprio software de processamento de dados, mas ele vai ter uma grande gama de software operando que podem falhar, ele pode ter falhas de hardware, de rede.
Ele pode sofrer ataques, pode sofrer erros humanos ou pode passar por upgrades que podem causar algum problema. Então, o conceito de disponibilidade e o quanto o sistema ele vai estar disponível, mesmo que ocorram determinadas tipos de falha.

E aí a gente vem para o conceito de tolerância a falhas. São as garantias de que um sistema, em caso de uma falha como as que a gente viu no slide anterior, vai continuar operando. 
Existem dois tipos principal de falta de tolerância o execute recovery ele tolera falha em slave, que é replicado.
E o full, que tolera falha tanto no Master quanto no slave. Então, lembrando do conceito de Master Slave que nós falamos, é o Master em um cluster, é o computador e o nó que faz a coordenação que distribui essas tarefas para os Slaves e o Slave é aquele que tem os dados e faz o processamento dos dados.

Então, no modelo execute recovery, ela tolera falha em o slave. Se o nós leve falhar, ele já tem uma réplica e o processamento continua. Mas se ocorrer uma falha no Master no Executive Cover Aí não há tolerância falha.O sistema para. No modo full tanto se houver falha no Master quanto no slave, o sistema tem tolerância a falha.

State management é o que ocorre com o estado do sistema em caso de falha, o que é o estado do sistema? Vamos imaginar um sistema de Big Data. Eu vou desenhar aqui um pequeno fluxo, que ele passe por várias etapas até produzir aqui ao final, o dado a informação produzida.
Então, por exemplo, aqui ele acessa uma fonte de dados. Aqui ele faz um processo de transformação. Aqui ele tem uma etapa de criação de um modelo de machine learning (ele tem um processo todo).

O state management, ele quer dizer o quê? Se ocorreu uma falha, por exemplo, nesta etapa, que o que vai acontecer? Ele é capaz ou não de manter o Estado se ele é capaz de manter estado? É, por exemplo, que a falha da rede que a rede volta a funcionar. Ele continua o processo daqui. Isso quer dizer que ele é capaz de manter o Estado agora, se ele não consegue manter o Estado, tudo se perde e o processo inicia desde lá do início.

Então, uma ferramenta é um pipeline, um processo de análise de dados e tem que ser analisado quanto a manutenção de estado. 

Um outro conceito simples é importante que você deve conhecer, e o Cloud e On-primese, cloud são aquelas aplicações que rodam na nuvem, on-primese que rodam internamente na estrutura da infraestrutura da empresa.
Então, geralmente o modelo cloud, ele pode trazer custos menores porque você terceiriza, além do serviço de armazenamento de dados, questões como backup, segurança, manutenção, atualização, entre outros.
É claro também que existem bastante tipos de soluções híbridas.

Conceito de ETL e ELT
Então ele ter os conceitos ELT e eles tratam do processo de extração dos dados da fonte onde eles foram produzidas até o ambiente analítico.
O ETL trata de extrair, transformar e carregar.
O ELT trata de fazer a extração, a carga e a depois a transformação.

Aqui a gente tem o modelo utilizado pelo Data Warehouse clássico [ETL]. Aqui a gente tem um modelo do Data Lake[ELT].
Então o Data Lake em princípio, o que ele faz? Ele extrai, carrega, ou seja, ele pega os dados da forma bruta, da forma que se encontram e carrega para o Data Lake para o sistema de arquivos distribuído, só depois, conforme a demanda, ele faz a transformação.
No modelo clássico, que é o ETL, ele faz a extração, ele faz a transformação antes da carga, e só carrega dados de qualidade, de valor e já tratados e transformados. 

Ou seja, é uma mudança de paradigma bastante grande. Por que houve essa mudança?
Por vários fatores, mas principalmente porque antes, no Data Warehouse clássico, armazenar dados era muito caro.
Então se armazenava apenas os dados necessários, já tratados e limpos Hoje não armazenamento e ele tem um custo muito menor e é muito mais fácil armazenar dados. Então, o conceito principal do Data Lake, é você carregar todos os dados para Data Lake no formato cru, no formato que ele já se encontra e depois você faz o tratamento conforme a necessidade.
Aqui no ELT eventualmente, pode haver pequenas transformações na carga, mas jamais no nível que ocorre em um ETL no Data Warehouse clássico.No caso do Data Lake que as transformações de fato ocorre quando os dados são consumidos, como, por exemplo, por um processo de criação de um modelo de machine learning falando de metadados.

Metadados são dados sobre os dados, então você tem o tipo do dado, a precisão, as restrições, diversas informações sobre os dados e a gente geralmente associa metadados apenas a tabelas de banco de dados relacionais, se produz lá algumas informações sobre as tabelas, os relacionamentos, os tipos de dados, mas as boas práticas de governança de dados elas vão muito além. Nós temos que produzir dados não só dos dados do banco de dados, mas de dados em trânsito, dados anuais que a gente vai falar no próximo, slides das fontes de dados, dos relatórios, dos dashboards dos processos de ETL e ELT, dos logs de auditoria, da linhagem dos dados, do processamento de transformação dos dados ao longo do pipeline dos dados. Então, o conceito de metadados, um conceito bem amplo, é importante quando a gente fala de governança de dados.

Um outro conceito aqui que a gente vai estudar o penúltimo conceito é o Data at rest, e o data at Wire.
A gente fala de um conceito de data at rest e são os dados que estão parados, eles estão, como o nome diz, descansando em um banco de dados.
O Data at Wire são dados que estão em trânsito, por exemplo, sendo transmitidos entre um nó ou entre o nó e o cliente ou a ferramenta de processamento de dados e o cliente.

Por que esse conceito é importante? Porque, por exemplo, você tem que tratar questões de segurança dos dados quando eles estão at Rest, ou seja, quando eles estão no banco de dados.
E você também tem que tratar de questões de segurança quando eles estão sendo transmitido, você tem que ver ferramentas, você tem que utilizar ferramentas, por exemplo, de segurança para os dois casos, para as duas situações de dados, além de ferramentas de transformação de carga de dados. Todas essas dizem respeito tanto aos dados em descanso quanto aos dados sendo transmitidos.

Então, o último conceito que a gente vai estudar nessa aula é dos dados orientados a coluna e os dados orientados a linhas (aqui falando sempre de dados estruturados).
Então, no banco de dados relacional nós temos dados orientados a linha. Isso quer dizer o quê?
Supondo que isso aqui seja uma tabela, você tem aqui as colunas e aqui você tem as linhas.Então aqui você tem a coluna e a coluna B, a coluna C, a coluna D e assim sucessivamente. Como que o banco de dados ele vai tratar um banco de dados relacional vai tratar esses dados?
Bom, ele vai armazenar esses dados aqui, por exemplo, em blocos. E ele vai fazer a compressão desses dados em blocos.Esse modelo aqui é bastante eficiente para escrita e leitura. Que é que um banco de dados relacional precisa?
Quais são as desvantagens desse modelo de dados?

Primeiro que ele tem baixa taxa de compressão, ou seja, ele vai ocupar bastante espaço quando armazenado em disco, quando carregado em memória. E a outra grande desvantagem dele é que a leitura de algumas colunas, o sistema vai precisar ler todas as colunas. Então, por exemplo, uma tabela, às vezes uma tabela de banco de dados relacional pode ter dezenas ou centenas de colunas.
Quando você vai fazer o Select, por exemplo, você vai selecionar apenas, por exemplo, a coluna A e C, mas o sistema gerenciador de banco de dados ele vai precisar carregar todas as colunas para produzir a informação que você precisa, que você colocou no seu SQL muito embora você coloque apenas as colunas, ele vai precisar carregar todas as centenas de colunas que você colocou lá na tabela que você selecionou.

O modelo orientado a colunas ele funciona assim as colunas são armazenadas separadamente, então, por exemplo, eu vou ter aqui a coluna A, a coluna B e a coluna C são armazenadas separadamente.
O que acontece? Qual que é a primeira vantagem? Maior taxa de compressão
Porquê? Porque você concorda comigo que os dados têm uma tendência maior de se repetir por coluna do que por linha. Então, por exemplo, aqui, se a coluna A fosse por exemplo o status do cliente para saber se ele é um cliente supondo lá um caso de fidelidade que a gente vai estudar posteriormente. Ele é um cliente do tipo Gold, Silver ou Platinum.
Aqui na coluna, por exemplo o tipo de dado mais comum lá, que é o Silver, ele vai aparecer muitas vezes. Por dados repetidos, eles tendem a ter uma alta taxa de compressão.
Agora, aqui, se a gente olhar em linha, vai aparecer aqui o Silver. Mas na coluna B, por exemplo, se for o sexo dele, já vai aparecer outra informação. Se aqui for o endereço, já vai ser outra. Então, aqui a taxa de compressão é muito pequena e a outra grande vantagem dos dados orientados a coluna que eles são melhor para leitura. 
Porque no caso do select la, que só se pegou, por exemplo, a coluna A e B. O sistema gerenciador de banco de dados vai precisar ler em disco apenas a coluna A e B. Ele não vai precisar fazer a leitura de todas as colunas, como no orientado a linhas. Então essas são algumas das grandes vantagens dos sistemas de armazenamento do sistema gerenciador de banco de dados orientado a colunas.

Então eles vem se tornando uma tendência nos sistemas de processamento de dados como a gente vai ver ao longo do curso, então a gente vai falar mais sobre dados orientados a coluna ou a linha ao longo do curso e  especificamente na seção que vai tratar de banco de dados No C#.
Então aqui, nos nossos conceitos que a gente está estudando, você já percebeu que uma das características de sistemas resilientes, que são aqueles tolerantes a falha é ser capaz de continuar operando, mesmo que ocorra alguma falha. Isso é feito de várias formas, mas a principal é a replicação os dados são copiados com a cópia dos dados em outros nós do cluster, caso você tenha algum problema em um nó. Você reduz os riscos do sistema todo parar então, que tipos de problemas que existem?
Então a gente já falou falhas de rede, problemas de software, problemas de disco rígido. E aqui uma questão em especial é com relação a falhas em disco rígido. Se fala muito em falha de disco rígido e se associa isso como uma das grandes vantagens de sistemas de processamento de dados distribuídos, como Hadoop. Agora, até que ponto isso, de fato, é um grande problema? Falhas em discos é um grande problema para sistemas distribuídos.
A gente vai ver que, de fato, isso é um grande problema, porque se o cluster é composto por um volume significativo de discos, certamente haverão falhas. 

E aqui eu trago alguns dados para deixar isso mais claro. A média de falhas em discos rígidos é de 4,81%, ou seja, quase 5%. Então, se você tiver 1000 discos rígidos em um cluster, isso quer dizer que o ano você terá 48 falhas em discos aproximadamente, quatro falhas por mês, em média. Ou seja, uma falha por semana. Claro que pode ser mais ou menos. Esses números são médias que vêm dessa fonte que está aqui.
Agora, uma coisa é certa se você tem um cluster com uma grande quantidade de discos rígidos e a lei dos grandes números nos diz que ocorreram falhas, nós vamos enfrentar falhas nos discos, então esta é uma grande e uma das grandes vantagens dos sistemas distribuídos. Como ele replica os dados e, por padrão, ele replica o Hadoop, replica os dados pelo menos em três nós. Você está reduzindo significativamente os riscos de que, se ocorra uma falha em um disco rígido, o seu sistema pare que você tem uma falha que causa alguma parada no seu sistema.