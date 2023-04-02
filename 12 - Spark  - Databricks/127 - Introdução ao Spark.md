<<<<<<< HEAD
<<<<<<< HEAD
127. Introdução do Spark
Nesta sessão a gente vai falar sobre o Spark. Que é uma ferramenta opensource que vem se tornando cada vez mais importante na área de dados.
Então, para uma formação em ciência de dados ela é fundamental e por isso a gente ter que esta seção
de Spark. O primeiro ponto é que é preciso entender que o Spark, ele não é uma linguagem. O Spark é uma ferramenta e uma ferramenta de processamento de dados e um software com relação à linguagem.

E você pode utilizar diversas linguagens para utilizar o Spark.
Você pode utilizar o Scala, Java, Python, SQL. A gente vai falar um pouquinho mais sobre isso depois e por ser um projeto open source, você pode simplesmente baixar e instalar o Spark na sua máquina.
Ou você pode utilizar o Spark através da nuvem. Você pode contratar um serviço na nuvem como AWS e enfim, qualquer um. E você vai assim utilizar o Spark na parte prática do nosso curso.

A gente, em vez de instalar o Spark, que pode ser um processo um pouco complicado, a gente vai utilizar
um provedor de serviços do Spark antes da gente entender especificamente o que o Spark faz.
Vamos aqui contextualizar a questão dos dados.

Então, um curso sobre formação de dados a gente tem que falar, tem que colocar isso em contexto.
Então, quando a gente fala de dados, a gente pode olhar os dados sobre dois aspectos principais o
armazenamento e o processamento. 

Então, vamos falar um pouquinho do processamento, porque a gente processa dados na medida em que os dados são gerados. A gente tem dados crus, que foram apenas produzidos, por exemplo, por um sensor ou por uma câmera, e eles não têm valor. 
A gente precisa processar esses dados, que daí eles vão gerar valor. Talvez os dados processados por desinformação e conhecimento Ou seja, eles vieram valor para uma empresa.Só que processar dados requer o que requer poder computacional.

Você precisa de CPU, você precisa de memória.Você precisa de disco, ou seja, você precisa de um computador, um servidor para processar esses dados.
Até aí, tudo bem. Então, se você tem lá um certo volume de dados, você vai precisa processar esses dados.
Você pode utilizar um computador para fazer esse processamento e produzir lá seu relatório, seu dashboard, seu modelo, enfim.

Só que o que acontece se você tiver mais dados? Se seu volume de dados tá aumentando, você vai precisar de um computador maior. Você vai precisar de mais CPU, mais memória, mais disco para processar esses dados. E a gente está na era de big data. Então se produz volumes gigantescos de dados e existe um limite do quanto você pode processar, do quanto você pode aumentar a capacidade de um de um computador.
Você não pode, de forma infinita, aumentar, por exemplo, a CPU e a memória de um computador.
É aí que entra o Spark. O Spark é uma ferramenta de processamento de dados distribuído em um cluster.

O que quer dizer isso? Quer dizer esse conceito de cluster. A gente vai falar um pouquinho mais depois, mas um cluster nada mais é do que um conjunto de computadores de uma rede que trabalham com o mesmo objetivo.
A gente pode ter uma rede de computadores com computadores fazendo coisas diferentes.
Você pode ter um computador que processa e-mail, outro que tem um RP, outro que armazena imagens.
Ou você pode ter computadores que estão em uma rede também, mas que trabalham em conjunto com o mesmo objetivo.
Então a gente tem um cluster, o Spark é basicamente de memória. Ele pode funcionar em disco, mas de forma natural ele trabalha em memória, é altamente veloz. Quando se fala de big data que ele é escalável, quer dizer, que você pode aumentar a capacidade a medida que você precisa de mais capacidade de processamento.

Se no caso do computador que a gente viu, se a gente aumentar a capacidade do computador, a gente
adiciona mais memória, troca CPU e bota mais disco em um cluster. Normalmente, quando a gente quer escalar e a gente quer aumentar a capacidade, a gente adiciona mais computadores, a gente coloca mais nós que são servidores neste ambiente e o Spark também, ele trabalha com o conceito de particionamento.

A gente já vai falar o que é especificamente o particionamento. Então o Spark ele escala horizontalmente, ou seja, você constrói com o Spark um cluster. Então, como eu falei, escalar horizontal ou horizontalmente.
Quer dizer que você tem um servidor que tem uma certa capacidade de processamento, seus dados aumentam.

Imagine que você tem um comércio eletrônico. Você tinha 1000 usuários por dia. De repente, você passa para 10.000. Para 100.000, você precisa aumentar a capacidade de processamento.
Então o que você vai fazer? Você vai escalar horizontalmente, você vai colocar mais servidores, mais nós no seu cluster, que vão trabalhar em conjunto, processando esses dados.
Porque então essa é a primeira característica que torna o Spark diferenciado.

A outra característica dele é a questão da replicação. O que é replicação e replicação é simplesmente copiar, criar cópias dos dados entre os nós do cluster. Então, isso traz uma característica importante, que é a tolerância à falha. Então, se você tem um cluster gigantesco com as centenas de computadores, existe uma probabilidade muito grande que eventualmente um computador ele vai ter um problema.
Ele vai perder conexão com a rede, o disco vai falhar, vai faltar energia, enfim, eventualmente alguma coisa vai acontecer com a replicação. O cluster se torna tolerante a falhas, mesmo que um desses nós falhe. Vão existir cópias desses dados em outros nós e o cluster continua funcionando.  Um usuário nem iria perceber isso.

Uma outra característica do Spark é a questão do particionamento. Particionar dados nada mais é do que dividir os dados no cluster. Mas vejo aqui que particionamento não é o mesmo que replicação. Na replicação eu copio os dados na rede.
No particionamento, pega o mesmo conjunto de dados e divido ele e coloco partes do mesmo dado em diferentes nós da rede. Vamos imaginar o seguinte você tem um sistema de varejo e um e-commerce que você tem, vamos supor, há bilhões de registros. há bilhões de transações e normalmente você precisa produzir informação mensal sobre vendas.

Só que você precisa produzir informação mensal sobre diversos aspectos, sobre por produto, por loja, por filial para o vendedor, mas sempre mensal. Se você tiver bilhões de registros, todos em um único computador, você vai ter mais dificuldade de processar isso agora. Como a gente disse que a gente precisa produzir informações mensais.

Que tal se eu pegasse particionar, se esses dados eu dividisse eles por mês?
Então todas as transações de janeiro iriam para um nó do cluster e todas as transações de fevereiro para outro, as de março para outra e assim por diante. E é claro, além de eu particionar esses dados, eles seriam, além de ter sido replicados, seriam copiados.
Caso, por exemplo, o mês de um nó que tem o mês de janeiro lá falhasse e tivesse um problema, existiria uma cópia deste mês de janeiro. Então, por exemplo, se você quer gerar nesse momento, se você quer gerar um relatório ou uma análise sobre as vendas do mês de janeiro, fica muito mais fácil porque você tem um nó apenas com os dados de janeiro.

Ok, então é esse outro conceito importantíssimo que o Spark traz. Então, o Spark é uma ferramenta de processamento de dados. Então a gente viu que processar dados tem um custo computacional.

Então ele é fantástico, porque ele tem arquitetura voltada para processar dados.Mas ele não substitui, por exemplo, uma linguagem como Python, falou. Já que o Spark não é uma linguagem de programação, ele não substitui SQL ou um sistema gerenciador de banco de dados relacional.
Ele tem outra característica, outro objetivo.

E também aqui eu falei com relação às linguagens. Eu falei lá no início que Spark não é uma linguagem. Ele é uma ferramenta. E você pode utilizar o Spark usando várias linguagens, diferentes linguagens, o Scala, que é a linguagem original dele, o Python, que é o que a gente vai utilizar dos nossos exemplos do curso Java, R e até SQL.

Então você tem essa flexibilidade com o Spark, mas aí a pergunta que fica aqui é por que você utilizaria o Spark.

Durante o curso a gente aprendeu a processar dados da que a gente fez, limpeza de dados, a gente fez tratamento de dados, a gente criou modelos de machine learning com Python e R.

Porque o Spark é tão importante? E, na verdade, isso já está respondido. A gente precisa do Spark pela sua natureza, pela sua arquitetura distribuída, que trabalha em cluster, que tem características de replicação, que têm característica de particionamento.
Então, a performance dele, a performance do Spark e dezenas ou até, em alguns casos, centenas de vezes superiores a outros tipos, a outras formas de você processar dados.

Então, se você precisa processar grandes volumes de dados, você é bem provável que você vai ter uma performance muito melhor utilizando o Spark do que, por exemplo, se você utilizar uma biblioteca como o Pandas e se você utilizar o Spark com Python, que é o PySpark, você tem tudo do melhor.

Porque vejam quando a gente está utilizando o Spark com Python, não é apenas a sintaxe que é para você.
De fato, está programando em Python.
Então, todas as bibliotecas que existe no Python você pode utilizar junto, então você tem aí o melhor dos dois mundos. Você pode utilizar o Panda, você pode utilizar o qualquer coisa e ao mesmo tempo que você está aí utilizando o o Spark.
=======
127. Introdução do Spark
Nesta sessão a gente vai falar sobre o Spark. Que é uma ferramenta opensource que vem se tornando cada vez mais importante na área de dados.
Então, para uma formação em ciência de dados ela é fundamental e por isso a gente ter que esta seção
de Spark. O primeiro ponto é que é preciso entender que o Spark, ele não é uma linguagem. O Spark é uma ferramenta e uma ferramenta de processamento de dados e um software com relação à linguagem.

E você pode utilizar diversas linguagens para utilizar o Spark.
Você pode utilizar o Scala, Java, Python, SQL. A gente vai falar um pouquinho mais sobre isso depois e por ser um projeto open source, você pode simplesmente baixar e instalar o Spark na sua máquina.
Ou você pode utilizar o Spark através da nuvem. Você pode contratar um serviço na nuvem como AWS e enfim, qualquer um. E você vai assim utilizar o Spark na parte prática do nosso curso.

A gente, em vez de instalar o Spark, que pode ser um processo um pouco complicado, a gente vai utilizar
um provedor de serviços do Spark antes da gente entender especificamente o que o Spark faz.
Vamos aqui contextualizar a questão dos dados.

Então, um curso sobre formação de dados a gente tem que falar, tem que colocar isso em contexto.
Então, quando a gente fala de dados, a gente pode olhar os dados sobre dois aspectos principais o
armazenamento e o processamento. 

Então, vamos falar um pouquinho do processamento, porque a gente processa dados na medida em que os dados são gerados. A gente tem dados crus, que foram apenas produzidos, por exemplo, por um sensor ou por uma câmera, e eles não têm valor. 
A gente precisa processar esses dados, que daí eles vão gerar valor. Talvez os dados processados por desinformação e conhecimento Ou seja, eles vieram valor para uma empresa.Só que processar dados requer o que requer poder computacional.

Você precisa de CPU, você precisa de memória.Você precisa de disco, ou seja, você precisa de um computador, um servidor para processar esses dados.
Até aí, tudo bem. Então, se você tem lá um certo volume de dados, você vai precisa processar esses dados.
Você pode utilizar um computador para fazer esse processamento e produzir lá seu relatório, seu dashboard, seu modelo, enfim.

Só que o que acontece se você tiver mais dados? Se seu volume de dados tá aumentando, você vai precisar de um computador maior. Você vai precisar de mais CPU, mais memória, mais disco para processar esses dados. E a gente está na era de big data. Então se produz volumes gigantescos de dados e existe um limite do quanto você pode processar, do quanto você pode aumentar a capacidade de um de um computador.
Você não pode, de forma infinita, aumentar, por exemplo, a CPU e a memória de um computador.
É aí que entra o Spark. O Spark é uma ferramenta de processamento de dados distribuído em um cluster.

O que quer dizer isso? Quer dizer esse conceito de cluster. A gente vai falar um pouquinho mais depois, mas um cluster nada mais é do que um conjunto de computadores de uma rede que trabalham com o mesmo objetivo.
A gente pode ter uma rede de computadores com computadores fazendo coisas diferentes.
Você pode ter um computador que processa e-mail, outro que tem um RP, outro que armazena imagens.
Ou você pode ter computadores que estão em uma rede também, mas que trabalham em conjunto com o mesmo objetivo.
Então a gente tem um cluster, o Spark é basicamente de memória. Ele pode funcionar em disco, mas de forma natural ele trabalha em memória, é altamente veloz. Quando se fala de big data que ele é escalável, quer dizer, que você pode aumentar a capacidade a medida que você precisa de mais capacidade de processamento.

Se no caso do computador que a gente viu, se a gente aumentar a capacidade do computador, a gente
adiciona mais memória, troca CPU e bota mais disco em um cluster. Normalmente, quando a gente quer escalar e a gente quer aumentar a capacidade, a gente adiciona mais computadores, a gente coloca mais nós que são servidores neste ambiente e o Spark também, ele trabalha com o conceito de particionamento.

A gente já vai falar o que é especificamente o particionamento. Então o Spark ele escala horizontalmente, ou seja, você constrói com o Spark um cluster. Então, como eu falei, escalar horizontal ou horizontalmente.
Quer dizer que você tem um servidor que tem uma certa capacidade de processamento, seus dados aumentam.

Imagine que você tem um comércio eletrônico. Você tinha 1000 usuários por dia. De repente, você passa para 10.000. Para 100.000, você precisa aumentar a capacidade de processamento.
Então o que você vai fazer? Você vai escalar horizontalmente, você vai colocar mais servidores, mais nós no seu cluster, que vão trabalhar em conjunto, processando esses dados.
Porque então essa é a primeira característica que torna o Spark diferenciado.

A outra característica dele é a questão da replicação. O que é replicação e replicação é simplesmente copiar, criar cópias dos dados entre os nós do cluster. Então, isso traz uma característica importante, que é a tolerância à falha. Então, se você tem um cluster gigantesco com as centenas de computadores, existe uma probabilidade muito grande que eventualmente um computador ele vai ter um problema.
Ele vai perder conexão com a rede, o disco vai falhar, vai faltar energia, enfim, eventualmente alguma coisa vai acontecer com a replicação. O cluster se torna tolerante a falhas, mesmo que um desses nós falhe. Vão existir cópias desses dados em outros nós e o cluster continua funcionando.  Um usuário nem iria perceber isso.

Uma outra característica do Spark é a questão do particionamento. Particionar dados nada mais é do que dividir os dados no cluster. Mas vejo aqui que particionamento não é o mesmo que replicação. Na replicação eu copio os dados na rede.
No particionamento, pega o mesmo conjunto de dados e divido ele e coloco partes do mesmo dado em diferentes nós da rede. Vamos imaginar o seguinte você tem um sistema de varejo e um e-commerce que você tem, vamos supor, há bilhões de registros. há bilhões de transações e normalmente você precisa produzir informação mensal sobre vendas.

Só que você precisa produzir informação mensal sobre diversos aspectos, sobre por produto, por loja, por filial para o vendedor, mas sempre mensal. Se você tiver bilhões de registros, todos em um único computador, você vai ter mais dificuldade de processar isso agora. Como a gente disse que a gente precisa produzir informações mensais.

Que tal se eu pegasse particionar, se esses dados eu dividisse eles por mês?
Então todas as transações de janeiro iriam para um nó do cluster e todas as transações de fevereiro para outro, as de março para outra e assim por diante. E é claro, além de eu particionar esses dados, eles seriam, além de ter sido replicados, seriam copiados.
Caso, por exemplo, o mês de um nó que tem o mês de janeiro lá falhasse e tivesse um problema, existiria uma cópia deste mês de janeiro. Então, por exemplo, se você quer gerar nesse momento, se você quer gerar um relatório ou uma análise sobre as vendas do mês de janeiro, fica muito mais fácil porque você tem um nó apenas com os dados de janeiro.

Ok, então é esse outro conceito importantíssimo que o Spark traz. Então, o Spark é uma ferramenta de processamento de dados. Então a gente viu que processar dados tem um custo computacional.

Então ele é fantástico, porque ele tem arquitetura voltada para processar dados.Mas ele não substitui, por exemplo, uma linguagem como Python, falou. Já que o Spark não é uma linguagem de programação, ele não substitui SQL ou um sistema gerenciador de banco de dados relacional.
Ele tem outra característica, outro objetivo.

E também aqui eu falei com relação às linguagens. Eu falei lá no início que Spark não é uma linguagem. Ele é uma ferramenta. E você pode utilizar o Spark usando várias linguagens, diferentes linguagens, o Scala, que é a linguagem original dele, o Python, que é o que a gente vai utilizar dos nossos exemplos do curso Java, R e até SQL.

Então você tem essa flexibilidade com o Spark, mas aí a pergunta que fica aqui é por que você utilizaria o Spark.

Durante o curso a gente aprendeu a processar dados da que a gente fez, limpeza de dados, a gente fez tratamento de dados, a gente criou modelos de machine learning com Python e R.

Porque o Spark é tão importante? E, na verdade, isso já está respondido. A gente precisa do Spark pela sua natureza, pela sua arquitetura distribuída, que trabalha em cluster, que tem características de replicação, que têm característica de particionamento.
Então, a performance dele, a performance do Spark e dezenas ou até, em alguns casos, centenas de vezes superiores a outros tipos, a outras formas de você processar dados.

Então, se você precisa processar grandes volumes de dados, você é bem provável que você vai ter uma performance muito melhor utilizando o Spark do que, por exemplo, se você utilizar uma biblioteca como o Pandas e se você utilizar o Spark com Python, que é o PySpark, você tem tudo do melhor.

Porque vejam quando a gente está utilizando o Spark com Python, não é apenas a sintaxe que é para você.
De fato, está programando em Python.
Então, todas as bibliotecas que existe no Python você pode utilizar junto, então você tem aí o melhor dos dois mundos. Você pode utilizar o Panda, você pode utilizar o qualquer coisa e ao mesmo tempo que você está aí utilizando o o Spark.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
=======
127. Introdução do Spark
Nesta sessão a gente vai falar sobre o Spark. Que é uma ferramenta opensource que vem se tornando cada vez mais importante na área de dados.
Então, para uma formação em ciência de dados ela é fundamental e por isso a gente ter que esta seção
de Spark. O primeiro ponto é que é preciso entender que o Spark, ele não é uma linguagem. O Spark é uma ferramenta e uma ferramenta de processamento de dados e um software com relação à linguagem.

E você pode utilizar diversas linguagens para utilizar o Spark.
Você pode utilizar o Scala, Java, Python, SQL. A gente vai falar um pouquinho mais sobre isso depois e por ser um projeto open source, você pode simplesmente baixar e instalar o Spark na sua máquina.
Ou você pode utilizar o Spark através da nuvem. Você pode contratar um serviço na nuvem como AWS e enfim, qualquer um. E você vai assim utilizar o Spark na parte prática do nosso curso.

A gente, em vez de instalar o Spark, que pode ser um processo um pouco complicado, a gente vai utilizar
um provedor de serviços do Spark antes da gente entender especificamente o que o Spark faz.
Vamos aqui contextualizar a questão dos dados.

Então, um curso sobre formação de dados a gente tem que falar, tem que colocar isso em contexto.
Então, quando a gente fala de dados, a gente pode olhar os dados sobre dois aspectos principais o
armazenamento e o processamento. 

Então, vamos falar um pouquinho do processamento, porque a gente processa dados na medida em que os dados são gerados. A gente tem dados crus, que foram apenas produzidos, por exemplo, por um sensor ou por uma câmera, e eles não têm valor. 
A gente precisa processar esses dados, que daí eles vão gerar valor. Talvez os dados processados por desinformação e conhecimento Ou seja, eles vieram valor para uma empresa.Só que processar dados requer o que requer poder computacional.

Você precisa de CPU, você precisa de memória.Você precisa de disco, ou seja, você precisa de um computador, um servidor para processar esses dados.
Até aí, tudo bem. Então, se você tem lá um certo volume de dados, você vai precisa processar esses dados.
Você pode utilizar um computador para fazer esse processamento e produzir lá seu relatório, seu dashboard, seu modelo, enfim.

Só que o que acontece se você tiver mais dados? Se seu volume de dados tá aumentando, você vai precisar de um computador maior. Você vai precisar de mais CPU, mais memória, mais disco para processar esses dados. E a gente está na era de big data. Então se produz volumes gigantescos de dados e existe um limite do quanto você pode processar, do quanto você pode aumentar a capacidade de um de um computador.
Você não pode, de forma infinita, aumentar, por exemplo, a CPU e a memória de um computador.
É aí que entra o Spark. O Spark é uma ferramenta de processamento de dados distribuído em um cluster.

O que quer dizer isso? Quer dizer esse conceito de cluster. A gente vai falar um pouquinho mais depois, mas um cluster nada mais é do que um conjunto de computadores de uma rede que trabalham com o mesmo objetivo.
A gente pode ter uma rede de computadores com computadores fazendo coisas diferentes.
Você pode ter um computador que processa e-mail, outro que tem um RP, outro que armazena imagens.
Ou você pode ter computadores que estão em uma rede também, mas que trabalham em conjunto com o mesmo objetivo.
Então a gente tem um cluster, o Spark é basicamente de memória. Ele pode funcionar em disco, mas de forma natural ele trabalha em memória, é altamente veloz. Quando se fala de big data que ele é escalável, quer dizer, que você pode aumentar a capacidade a medida que você precisa de mais capacidade de processamento.

Se no caso do computador que a gente viu, se a gente aumentar a capacidade do computador, a gente
adiciona mais memória, troca CPU e bota mais disco em um cluster. Normalmente, quando a gente quer escalar e a gente quer aumentar a capacidade, a gente adiciona mais computadores, a gente coloca mais nós que são servidores neste ambiente e o Spark também, ele trabalha com o conceito de particionamento.

A gente já vai falar o que é especificamente o particionamento. Então o Spark ele escala horizontalmente, ou seja, você constrói com o Spark um cluster. Então, como eu falei, escalar horizontal ou horizontalmente.
Quer dizer que você tem um servidor que tem uma certa capacidade de processamento, seus dados aumentam.

Imagine que você tem um comércio eletrônico. Você tinha 1000 usuários por dia. De repente, você passa para 10.000. Para 100.000, você precisa aumentar a capacidade de processamento.
Então o que você vai fazer? Você vai escalar horizontalmente, você vai colocar mais servidores, mais nós no seu cluster, que vão trabalhar em conjunto, processando esses dados.
Porque então essa é a primeira característica que torna o Spark diferenciado.

A outra característica dele é a questão da replicação. O que é replicação e replicação é simplesmente copiar, criar cópias dos dados entre os nós do cluster. Então, isso traz uma característica importante, que é a tolerância à falha. Então, se você tem um cluster gigantesco com as centenas de computadores, existe uma probabilidade muito grande que eventualmente um computador ele vai ter um problema.
Ele vai perder conexão com a rede, o disco vai falhar, vai faltar energia, enfim, eventualmente alguma coisa vai acontecer com a replicação. O cluster se torna tolerante a falhas, mesmo que um desses nós falhe. Vão existir cópias desses dados em outros nós e o cluster continua funcionando.  Um usuário nem iria perceber isso.

Uma outra característica do Spark é a questão do particionamento. Particionar dados nada mais é do que dividir os dados no cluster. Mas vejo aqui que particionamento não é o mesmo que replicação. Na replicação eu copio os dados na rede.
No particionamento, pega o mesmo conjunto de dados e divido ele e coloco partes do mesmo dado em diferentes nós da rede. Vamos imaginar o seguinte você tem um sistema de varejo e um e-commerce que você tem, vamos supor, há bilhões de registros. há bilhões de transações e normalmente você precisa produzir informação mensal sobre vendas.

Só que você precisa produzir informação mensal sobre diversos aspectos, sobre por produto, por loja, por filial para o vendedor, mas sempre mensal. Se você tiver bilhões de registros, todos em um único computador, você vai ter mais dificuldade de processar isso agora. Como a gente disse que a gente precisa produzir informações mensais.

Que tal se eu pegasse particionar, se esses dados eu dividisse eles por mês?
Então todas as transações de janeiro iriam para um nó do cluster e todas as transações de fevereiro para outro, as de março para outra e assim por diante. E é claro, além de eu particionar esses dados, eles seriam, além de ter sido replicados, seriam copiados.
Caso, por exemplo, o mês de um nó que tem o mês de janeiro lá falhasse e tivesse um problema, existiria uma cópia deste mês de janeiro. Então, por exemplo, se você quer gerar nesse momento, se você quer gerar um relatório ou uma análise sobre as vendas do mês de janeiro, fica muito mais fácil porque você tem um nó apenas com os dados de janeiro.

Ok, então é esse outro conceito importantíssimo que o Spark traz. Então, o Spark é uma ferramenta de processamento de dados. Então a gente viu que processar dados tem um custo computacional.

Então ele é fantástico, porque ele tem arquitetura voltada para processar dados.Mas ele não substitui, por exemplo, uma linguagem como Python, falou. Já que o Spark não é uma linguagem de programação, ele não substitui SQL ou um sistema gerenciador de banco de dados relacional.
Ele tem outra característica, outro objetivo.

E também aqui eu falei com relação às linguagens. Eu falei lá no início que Spark não é uma linguagem. Ele é uma ferramenta. E você pode utilizar o Spark usando várias linguagens, diferentes linguagens, o Scala, que é a linguagem original dele, o Python, que é o que a gente vai utilizar dos nossos exemplos do curso Java, R e até SQL.

Então você tem essa flexibilidade com o Spark, mas aí a pergunta que fica aqui é por que você utilizaria o Spark.

Durante o curso a gente aprendeu a processar dados da que a gente fez, limpeza de dados, a gente fez tratamento de dados, a gente criou modelos de machine learning com Python e R.

Porque o Spark é tão importante? E, na verdade, isso já está respondido. A gente precisa do Spark pela sua natureza, pela sua arquitetura distribuída, que trabalha em cluster, que tem características de replicação, que têm característica de particionamento.
Então, a performance dele, a performance do Spark e dezenas ou até, em alguns casos, centenas de vezes superiores a outros tipos, a outras formas de você processar dados.

Então, se você precisa processar grandes volumes de dados, você é bem provável que você vai ter uma performance muito melhor utilizando o Spark do que, por exemplo, se você utilizar uma biblioteca como o Pandas e se você utilizar o Spark com Python, que é o PySpark, você tem tudo do melhor.

Porque vejam quando a gente está utilizando o Spark com Python, não é apenas a sintaxe que é para você.
De fato, está programando em Python.
Então, todas as bibliotecas que existe no Python você pode utilizar junto, então você tem aí o melhor dos dois mundos. Você pode utilizar o Panda, você pode utilizar o qualquer coisa e ao mesmo tempo que você está aí utilizando o o Spark.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
