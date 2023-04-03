126. Limitações do Hadoop
Para quem acompanha o universo de Big Data de uma forma mais superficial e não mais tecnicamente, assim como nós que estamos fazendo este curso.
Parece que Hadoop é um sinônimo de big data. É uma solução única que resolve todos os problemas de grandes volumes de dados, de dados em grande variedade, em dados com grande velocidade. Mas você está entendendo até agora você está percebendo até agora que não. Até pela nossa aula inicial nessa seção que você viu lá, que o Hadoop é composto por um ecossistema de diversas soluções que resolvem problemas diferentes.

Então, na verdade, é isso que vem acontecendo, se antigamente nós tínhamos bancos de dados relacionais que praticamente atendiam todo e qualquer problema relacionado a dados, hoje na área de Big Data não, temos ferramentas específicas para resolver problemas específicos.

E o Hadoop é mais uma dessas ferramentas. Ele não é uma ferramenta universal, mas é uma ferramenta para resolver problemas específicos, problemas bem especializados e a tendência cada vez mais no universo de Big Data, ferramentas especializadas para resolver problemas específicos.

Então, vamos ver no que o Hadoop não é bom, no que você não vai usar o Hadoop: 
•	Ele não é bom para processamento em tempo real, porque por ter uma ferramenta de processamento em lote distribuído, ser uma ferramenta de Batch. Você vai ter que colocar o volume de dados do sistema de arquivo. Esse sistema de arquivo vai ser distribuído em uma rede, você vai ter que criar um programa.Você vai ter que compilar, rodar esse programa.Esse programa vai executar uma série de processos espalhados por uma rede, para uma para um cluster.Esse cluster ele vai ter que aguardar a primeira etapa, que é de mapeamento. Depois do fim da etapa de mapeamento, vai se iniciar a etapa de redução e só então você vai ter um resultado. Então isso não é processamento em tempo real. 
•	E o processamento em lote é demorado, que pode levar algum tempo, muito menos acesso interativo. Não é uma ferramenta que você vai lá rodar uma consulta. Aqui você vai fazer uma pergunta, tirar uma dúvida, você tem que criar um programa para ter um resultado. E você vai ter que esperar vezes horas, muitas horas para ter esse resultado. Então não é uma ferramenta interativa.
•	Também não é uma ferramenta para pequenos volumes de dados que não vale a pena você criar tudo isso, você construir tudo isso para analisar uma pequena quantidade de dados. Você tem outras ferramentas que são mais especializadas para isso. 
•	Também não é uma ferramenta feita para problemas complexos ou como, por exemplo, grafos. A gente vai ver que ela opera com um conjunto chave-valor.

O que o Hadoop também não é bom:
•	Para operações que precisam de grande tráfego de dados de uma rede. Vejam que o Hadoop, ele não causa constantemente um grande tráfego de dados na rede, porque ele processa dados nos nós.
•	Ele não é feito para problemas transacionais.
•	Ele funciona apenas com um programa com programação, então você tem que criar um programa em Java. Você tem que compilar o programa para rodar uma aplicação. 

Então ele não é bom para problemas que trafeguem muitos dados.
Problemas de streaming de grandes volumes de dados, problemas transacionais e que requerem programação para problemas que requerem programação.

Ele é insuperável para:
•	Quando a gente tem grandes volumes de dados, volume de dados realmente grandes. 
•	E quando a gente tem uma questão de processamento em batch, não é RealTime não precisa do resultado imediatamente.
Nós vimos lá vários exemplos de processamento que são RealTime, Streaming, em Batch, Interativo. O Hadoop é uma ferramenta de processamento em batch.
