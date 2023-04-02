124. Map e Reduce
Vamos agora, então, falar um pouco mais sobre o Hadoop propriamente dito, e depois vamos falar um pouco mais sobre ele.
Então, o Hadoop é uma ferramenta especificamente exclusivamente para processamento em Batch, baseado no conceito de MapReduce de mapeamento e redução, que é aquele conceito de dividir para conquistar e trabalhar em conjunto em paralelo.
Então, você divide a tarefa e a tarefa dividida, você trabalha em paralelo e assim você consegue finalizar a tarefa mais rápido.
Então, o Hadoop é desenvolvido em Java, É uma ferramenta opensource.
Gente, vai ver que existem distribuições, a distribuição original apache, open source e existem distribuições de terceiros.
É um produto distribuído, ou seja, ele opera em clusters, Ele distribui o processamento em rede.
Outra característica que chamam muito atenção com relação ao Hadoop é a questão do hardware commodity isso quer dizer que ele pode operar em hardware comum em hardware e não especial em qualquer tipo de hardware, você pode construir um cluster com dezenas ou centenas ou milhares de nós usando equipamento comum barato. Você não precisa ter equipamento especializado, appliance, equipamento de alto custo, ele vai rodar equipamento comum.
Capaz de distribuir o processamento em dezenas ou milhares de nós em um cluster. Então você pode criar um cluster composto por dois, três, dez, 100.000, 10.000, 100.000 nós, porque entretem essa capacidade de distribuir o processamento em milhares de nós, se for preciso.
Rem suporte a dados estruturados e não estruturados e ele vai processar terabytes ou petabyte de dados.
Como a gente já falou, não faz sentido você desenvolver uma aplicação redutora e você construir uma infraestrutura, criar um programa em Java para processar, por exemplo, um giga, dois giga, três giga de bits de dados aqui.
Então ele é feito para grandes volumes de dados, falando de terabytes de dados para cima.
 
O Hadoop, ele opera no conceito de master slave.
Então você vai ter um master e você vai ter os nós Slave.
Claro que depois a gente vai ver que o Master ele pode também ter replicação.
O que o Master faz?
O Master, ele mantém os metadados, que são metadados. Aonde estão os arquivos, qual o tamanho do arquivo, a permissão que o arquivo tem, a hierarquia desses arquivos. O Master mantém os logs, os logs de funcionamento. Ele adiciona encontro e exclui, copia os arquivos, distribui as tarefas de mapeamento e redução entre os Slaves, entre nós Slaves, Essas tarefas são tarefas de mapeamento e redução. Ele cuida do agendamento e do balanceamento da carga. Então, obviamente, se você tem, por exemplo, lá dez terabytes de dados, você não vai colocar tudo em dois lotes. Se você tem 50 nós disponíveis, ok, então o hadoop master ele vai fazer esse balanceamento.

E os Slaves que ele faz? Qual é a função deles?
Eles mantêm os dados e eles mantêm réplicas de bloco dos dados.
O conceito importante do hadoop é que ele é um sistema distribuído, redundante. Então, eventualmente, um nó pode falhar. Se o nó slave por exemplo, ele falhar e ele não for mais acessível a rede cair. Vão existir réplicas de blocos dos módulos, dados que estavam naqueles nós distribuídos em outros nós.

Então o Hadoop, ele vai perceber que aquele nó que aquele slave que continha dados parou e ele vai acionar o nó que tem uma réplica daqueles dados.

Então o master ele tem um NameNode que faz a gestão do sistema de arquivos, o HDFS e o nó mantém metadados log, adiciona, encontra, exclui e copia arquivos.  
Ele tem o job tracker, que distribui as tarefas de mapeamento e redução entre os nós e o Task Tracker: Ele recebe as tarefas de mapeamento e redução que vêm aqui do Job Tracker e ele cuida de agendamentos, balanceamento de carga e gestão de falhas.

E o Slave? Os Slaves, como ele falou, são os DataNodes: Eles mantêm os dados e as réplicas dos dados. 

Então, a partir da versão dois do Hadoop, um NameNode pode ser replicado.
DataNodes: são configurados em modo ativo standby. O que quer dizer isso? Você vai ter, por exemplo, dois data nodes com um determinado conjunto de dados, alguns blocos. Este aqui ele vai estar ativo e esse aqui vai estar em standby. E você tem lá o Master. Ele vai estar em contato com o nó ativo.
O que acontece se ocorrer algum problema com esse nó, automaticamente.
O nó que estava em stand by, Ele vai ser acionado e ele vai passar a ser o nó ativo. Como que isso é coordenado através do heartbeat e enviado do DataNodes  ao Name Node regularmente como sinal de saúde.
Então o que acontece?
O DataNodes eventualmente, ele se comunica com o Name Node, dizendo que está tudo bem, que ele está funcionando perfeitamente. Então, no modo standby, nenhum node fica passivo até o Name Node ativo ficar inoperante.
Se acontecer, sempre quem vai comandar isso, quem vai orquestrar isso é o Name Node, ele que vai fazer essa gestão.


Então é que a gente tem uma arquitetura simplificada do Hadoop, a gente tem a camada HDFS, que é onde estão os dados. Então a gente tem o Name Node, Data Node e aqui a gente tem um slave com o Data Node. No Master a gente tem o Task Tracker, o Job Tracker, e no Slave a gente tem também um Task Tracker  cuidando lá dos dados que estão, naqueles que estão, que foram distribuídos para aquele nó.

E o Yarny, o Yarny ele faz a locação de recursos de forma global e unificada no cluster, então, imagine que você tem um cluster com muitos dados, com muitos recursos você pode ter equipamentos físicos dividindo máquinas virtuais, então você precisa de uma ferramenta que faça a gestão, alocação de recursos de forma global e unificada e resumo que vai fazer a gestão do cluster. Então o Yarn vai cuidar de agendamentos, de priorização e da tolerância a falhas. Quais são os componentes dele?
•	O ResourceManager, vai existir um por cluster. Então todo o cluster ele vai ter, seja lá um cluster com 50 nós, Com 1000 nós, ele vai ter um ResourceManager.
o	O ResourceManager, ele tem o AplicationManager, que faz gerenciamento, atividades, otimização, distribuição de recursos 
o	E um agendador, um Scheduler.
•	E depois a gente tem o NodeManager que você vai ter um por nó, que é responsável pela execução dos jobs. Então um nó ele vai ter dados que tem, que têm que ser processados de alguma forma, isso tem que ser processados, Então nem minutos ele vai ter um nó que é responsável pela execução das tarefas de processamento dos dados.
•	E o Application Master faz a distribuição das tarefas aos containers.
•	E os contêineres mantêm essas tarefas que precisam ser executados.

Então, aqui pra gente encerrar esta aula aqui, alguns cases de uso do Hadoop.
Em 2008, o Yahoo coleta em produção, Ele coloca em produção um cluster de Hadoop com 10.000 cores. Obviamente que 10.000 cores não significam que são 10.000 máquinas físicas dessa ideia. São computadores com 10.000 núcleos operando num mesmo cluster Hadoop sobre HDs processando uma mesma tarefa.
Este cluster processou cinco petabytes de dados, então a gente pode ler sobre este case aqui neste link. 
Você provavelmente pode perguntar mas este é o maior cluster que existe.
Não existem clusters ainda maiores. O destaque aqui é que foi o primeiro grande caso de uso de aplicação de Hadoop com um cluster tão grande.
A gente pode ver que isso aqui data de 2008. Então foi um case que comprovou a grande eficácia a grande capacidade do reduto de processar grandes volumes de dados em Batch em processamento.
