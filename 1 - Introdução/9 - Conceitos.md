9. Conceitos 
Nas próximas aulas nós vamos estudar vários conceitos que estão relacionados ao universo Big Data, a engenharia de dados, e eles são importantes para as seções seguintes. Então são conceitos que a gente precisa entender e compreender para quando a gente falar. Por exemplo, na teoria lá do Methodus ou de Noyce, que são conceitos que a gente precisa entender para entender também o funcionamento e a parte prática, mesmo do curso.

Então, a gente vai começar aqui com cluster diz respeito a computação distribuída, ou seja, você pega o processamento. Você imagina que você precisa processar um grande volume de dados e você distribui esse processamento em vários computadores. Cada computador de um cluster é chamado de nó.

Não é a mesma coisa um cluster de uma rede. Numa rede de computador, você pode ter vários computadores executando tarefas diferentes com finalidades diferentes. 

No cluster, não no cluster, eles estão trabalhando em conjunto com o mesmo objetivo. Eles estão se ajudando a cumprir uma determinada tarefa, que, no caso aqui do nosso curso, seria processamento de dados. Então, eles operam em conjunto, conectados com o mesmo objetivo.

Então, o que eles querem fazer? Qual é o conceito de cluster? Se a gente pudesse resumir uma frase e dividir para conquistar. Então, em vez de você colocar tudo em um único computador que iria levar semanas para fazer um processamento, você pega a tarefa, divide em vários e eles dividem esse processamento e terminam mais rápido.

Os computadores de um cluster que a gente chama de nó. Como a gente viu aqui, eles podem estar dispersos fisicamente, inclusive em diferentes continentes. Então, eles podem estar num meio, numa mesma sala, no mesmo hack. Eles podem estar, inclusive, no mesmo equipamento físico, ou seja, eles podem estar virtualizados. 
Da mesma forma que eles podem estar separados fisicamente em cidades diferentes, em estados diferentes, em países diferentes, eu já tive, por exemplo, projetos de processamento de dados que foi contratada, solução na nuvem que você descobriu depois, por questões técnicas, que parte dos serviços estavam em um país, parte estavam em outra. Para nós, claro, obviamente isso era transparente.

Normalmente, um cluster. Ele trabalha numa estrutura master/ slave, o que é uma estrutura Master/Slave. 
Ou você tem um ou mais computador que coordena e distribui agendas, tarefas e os slaves que armazenam e processam. Então você pode ter, por exemplo, um computador que é o Master, e todos os demais são slaves. 
Ok? Então eles trabalham com essa estrutura. Tantos slides quanto os master podem ter redundância que a gente vai falar nos próximos slides.

Outro conceito importante é o de replicação e partição.
Então, em um cluster, normalmente ele opera replicando dados. O que é replicar os dados são o processo de executar cópias dos dados para diferentes nós, para diferentes computadores. O principal objetivo desta cópia desses dados é você ter alta disponibilidade. Se, por exemplo, uma falha se o nó que falha, você tem uma cópia desses dados em um outro nó que continua o processamento da mesma forma.

O outro conceito é o particionamento. O particionamento é você dividir os dados, então, por exemplo, você tem um arquivo grande. Lá, você pode dividir esses dados. Você se faz o particionamento dele, também conhecido como charging. Você faz o particionamento deles e eles fazem o processamento em partes. Então, se você dividiu esse arquivo aqui em três nós, cada nó vai fazer o processamento de parte desse arquivo.Então este é o conceito de partição. Você divide os dados fisicamente em uma rede ou outro conceito importante aqui com relação ao particionamento e que, por exemplo, você pode colocar supondo lá que você tenha dados financeiros, você pode colocar os dados referentes a um estado neste nó.
Então, por exemplo, as notas fiscais do Rio Grande do Sul neste nó e as notas fiscais de Santa Catarina, por exemplo. Nesses nó, se você precisa fazer uma operação de análise de dados apenas com os dados relativos ao Rio Grande do Sul, os dados estão centralizados. Você não vai ter que acionar três nós, por exemplo, supondo que aqui tenha um outro estado, você não vai precisar acionar os três nós para processar. Esses dados, eles vão estar centralizado em um mesmo nó rede.

 Geralmente a replicação e a partição são utilizadas em conjunto. Então, além de você dividir os dados, eles são copiados. Ou seja, você dividiu os dados, por exemplo, e esta parte de dados aqui, além de estar dividida, ela vai estar replicada. Ela vai ter uma cópia dela e em outro nó. Então, normalmente os sistemas de processamento de dados que operam em cluster e eles fazem replicação e partição.

Quais são os tipos de partição?
A mais comum é centralizada, então você tem um serviço central que faz o gerenciamento dos dados na partição. Ele possui todos os metadados, todas as informações do dado, que tipo de dado e onde ele está. Qual é o tamanho isso de você ter um. Particionamento centralizado pode se tornar um gargalo por ser um ponto único de partição.

Outra forma é você ter um rei que você divide em intervalos. Aqui, o problema é que ele pode ficar desbalanceado. Você pode ter mais informações em um nó do que o outro; e a outra forma é o hash, Ele usa uma rede de tempo para distribuir os dados de forma balanceada entre os nós.

O conceito de mutation, então, é o conceito de mutation ou de mutação. Ele diz respeito ao suporte do sistema em alterar dados. Mas aí talvez você pense como assim? Que tipo de sistema? Que tipo de banco de dados não vai ter suporte para alterar dados? Bom é que a gente tem normalmente em mente. Quando a gente fala de banco de dados, a gente está falando de bancos de dados relacionais, que são bancos de dados orientados a linha e que têm uma estrutura propícia para alteração de dados.

Quando a gente está falando de armazéns, de dados analíticos e, principalmente, que estão distribuídos e em formato de colunar, orientados a coluna. O processo pode ser bem mais complexo você ter que alterar uma informação. Então, imagine que você tenha, por exemplo, uma informação que está distribuída em vários nós. A alteração de um dado significa alterá- la em vários nós, em mais de um nó, e também a questão das colunas dos dados orientados a coluna que vem se tornando um padrão nos bancos de dados analítico. A alteração desse tipo de dados é um pouco mais complexa.  Então, normalmente, os sistemas analíticos têm suporte a alteração. Ele suporta o mutation, mas não é um processo tão simples quanto em sistemas de operação. 

E a gente precisa lembrar também que bancos de dados analíticos, que são os que mais usam as formas de arquivos colunar orientadas a colunas, eles representam eventos que já aconteceram e não são produtores de informação. Eles estão armazenados, armazenando processos que já ocorreram e disponibilizando isso em um armazém, em um formato específico para ser analisado. Então, a necessidade de alteração é menor.
O que mais ele precisa suportar é a inclusão de novas informações e a leitura, a leitura de dados para produzir informação gerencial, informação para tomada de decisão.

Data Warehouse versus Data Lake que o Data Warehouse que a gente vai falar aqui ao longo do curso. Ele se refere sempre a um armazém de dados, a um banco de dados ou um sistema de arquivos cujo propósito específico é armazenar dados para fins analíticos para tomada de decisão. Porém, existe o Data Warehouse clássico, que é aquele que a gente falou lá, que foi criado, que começou a ser implementado a partir dos anos 90. E existe um armazém de dados, atual armazém de dados da era Big Data, e este é mais conhecido como Data Lake, que aqui é uma estrutura mais complexa, mais heterogênea, mais diferenciada e que a gente vai falar ao longo do curso.

O Data Warehouse clássico, esse que foi implementado a partir dos anos 90, ele suporta dados estruturados no modelo dimensional. O Data Lake de Big Data. Ele suporta todo o tipo de informação e geralmente ele é construído dentro de um sistema de arquivos distribuído que nem é um banco de dados, que é o HDFS, que é um sistema de arquivos que faz parte do ecossistema Hadoop, enquanto o Data Warehouse  clássica é armazenado em um banco de dados estruturado com uma modelagem dimensional. A gente vai falar bastante sobre a diferença entre esses dois modelos de armazéns de dados e a gente vai fazer algumas implementações práticas também.

Um outro conceito importante que você precisa dominar para o nosso curso é a questão do BATCH VS Streaming VS Interativo. Então, aqui a gente está falando de produção, de informação analítica, de analisar dados.

No Batch, os dados são coletados, ou seja, eles são extraídos, tratados, armazenados e processados. Isso pode levar horas, semanas ou até meses. Então, não é um processo cujo resultado é imediato. Aqui estamos falando de informação que não precisa ter um resultado imediato e que normalmente compõe um volume muito grande de dados gigabites, terabytes ou até mais esse é um tipo de processamento conhecido como Batch. 
A gente vai ver que existem sistemas do ecossistema, hadoop de Big Data específicos para produção de gestão, para a execução de processos em Batch.Então, vamos citar um exemplo assim se você quer fazer uma auditoria de folha de pagamento, você precisa aguardar a folha de pagamento ser fechada depois que a folha de pagamento foi fechada. Você roda em Batch o processo de auditoria de folha de pagamento.

Já em streaming. São dados processados em tempo real à medida que são produzidos a saída, ou seja, o resultado aqui, em tempo real, próximo ao tempo real, existe uma, pode existir uma latência de segundos ou minutos. Então a gente tem um processo constante, um fluxo diferente do Batch, que é um processo que ocorre eventualmente e que pode levar horas, dias ou semanas. Então, por exemplo, o que seria um exemplo de streaming? 
Um processo de fraude, por exemplo. Um sistema para detecção de fraude. À medida que as transações vão sendo produzidas, o que faz? Existe um processo que vai coletar os dados, analisar e produzir o resultado, indicando se aquela transação é fraudulenta ou não. Obviamente que aqui eu não posso ter um processo em Batch.Não adianta pegar todas as transações do mês e processar depois que o cliente, por exemplo, já recebeu o produto.É tarde demais. Então, é um tipo de aplicação cuja demanda é diferente da, por exemplo, da aplicação em Batch.

 E o outro modelo, que a gente tem é um modelo interativo que é também conhecido como ad hoc, que é onde o usuário tem uma interface onde o processamento é requerido e o resultado é analisado. Então, por exemplo, uma interface que ele vai rodar uma consulta SQL ou ele vai rodar um relatório para resolver algum problema pontual.
O que é uma mistura de Batch com streaming e não é nada estruturado, não é nada planejado, é alguma coisa casual. 

Então aqui pra gente diferenciar o BATCH versus streaming, é o Batch ele tem início e tem o fim. E o streaming não. Ele não termina nunca. Ele é um processo contínuo. Ele é um processo que continua, que fica rodando sempre.

Então, aqui é Batch, sistema de busca de produtos de varejo online, milhões de termos pesquisados por dia. Diariamente, os dados são processados para criar um ranking das palavras mais buscadas. 
Então você quer fazer uma indexação dos termos pesquisados durante o dia.Você executa um processo em Batch.

Agora, falando aqui de streaming, sistema de busca de produtos de varejo online, avaliação de transações de pagamento e fraudulenta. As transações são processadas à medida que são executados.

E o interativo é rodar uma consulta para ver as vendas do dia de determinado produto. Gerente de vendas lá ele quer saber quanto um determinado produto vendeu.

Tipos de streaming então, falando de processamento em tempo real de streaming, a gente tem dois tipos de sistemas que fazem processamento desse tipo de aplicação o nativo que os dados são processados assim que chegam, sem esperar por demais dados. E o micro-baching que os dados são agrupados e processados em grupo, então aqui tem um delay que normalmente esse delay é definido por quem desenvolveu a aplicação, que tem uma diferença significativa no nativo a informação chega, ela já é processada imediatamente.
No micro-baching junta um determinado grupo de informações durante o intervalo, que pode ser, por exemplo, de segundos, e assim ele faz o processamento, o nosso processo para o nosso projeto prático O nosso exemplo prático vai ser com o Spark Streaming, que ele usa Micro-Beaching.

Aqui, alguns conceitos relativos a streaming, então um evento é um dado. Então, por exemplo, os dados da compra online é lá que foram gerados. Isso é um evento.
O Producer é o gerador dos dados. Então a aplicação lá, o formulário onde o usuário colocou os dados do sistema que produziu a transação da compra.

E o Subscriber é quem consome. Então, por exemplo, o modelo de machine learning que vai analisar se aquela compra é fraudulenta ou não é um subscriber.Ele é um assinante do processo de streaming para verificar se a transação é fraudulenta ou não.

Como o assinante sabe que o Producer gerou um evento que ele gerou dados? Existem várias formas. Depende do tipo de sistema e da aplicação.

Pode ser através do monitoramento, um diretório, uma trigger em um banco de dados ou mesmo uma assinatura e um processo de mensagem que pode ser, por exemplo, disparado por TCP, IP. Então  existe em várias formas do Subscriber receber,ser informado de que houve um evento.

Outro conceito aqui pra gente vê o de latência. A latência é o intervalo de tempo entre a produção da informação e o seu processamento. Então, em Batch, obviamente tem uma alta latência. E em streaming a gente tem uma baixa latência.

A gente vai falar também de bastante de aplicações real time ou seja, em tempo real e  near real time: próximo ao tempo real.

Normalmente, quando a gente fala de RealTime, a gente se refere a nerd real time. A maioria das aplicações ocorrem próximo ao tempo real, que mesmo a gente está falando de aplicações de streaming. A gente está falando de aplicações que ocorrem próximo ao tempo real. Existe sempre uma pequena latência.

A gente falou de processamento distribuído, então a gente precisa entender que um processamento, em Batch, um streaming, memória pode ou não ser distribuído. Ele pode rodar em um único equipamento. Ele pode ser distribuído em um cluster.

É o último conceito aqui desta aula que se ouve falar.Aqui a gente fala bastante.Quando a gente fala de Big Data do ecossistema Hadoop é o conceito de commodity hardware, commodity hardware, o que é um equipamento barato, compatível, altamente disponível e intercambiável. Por que isso é usado como uma bandeira em sistemas de Big Data open source? Bom, isso em comparação aos famosos appliance de soluções de Data Warehouse clássicas que rodavam em hardware proprietário de altíssimo custo de manutenção (Difícil)

Não só sistemas de análise de dados, mas também sistemas de processamento de transação. Eles precisavam de hardware muito especializado, muito caro de manutenção, muito cara. Por outro lado, aplicações de Big Data do ecossistema hadoop que a gente vai estudar ao longo do curso, elas têm essa característica de poder rodar em qualquer tipo de hardware. Elas não precisam de hardware especializado para sua execução. Você pode montar um cluster, por exemplo, com centenas, dezenas, centenas, milhares de nós rodando em equipamento comum, nada de hardware especializado.