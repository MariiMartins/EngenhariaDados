125. HDFS
Quando a gente fala de big data e de Hadoop, a grande estrela nos bastidores é aquela que não aparece nas mídias das grandes reportagens, nos artigos e o sistema de arquivos distribuído, o HDFS e o HDFS (Hadoop Distributed File System), ele é responsável por toda a infraestrutura de dados do Hadoop e não só do Hadoop, como a gente vai ver. Ele é utilizado por todo o ecossistema de aplicações orientadas a dados que compõe o ecossistema do Hadoop.

Mas antes vamos lembrar um pouco que é um sistema de arquivos. Vamos esquecer a questão do sistema de arquivos distribuído, que simplesmente é um sistema de arquivos.
Então um sistema operacional ele simplesmente não joga dados num disco rígido. Ele precisa fazer a gestão desses dados.
O que é fazer gestão?
Ele precisa manter a integridade desses dados. Ele tem que deixar os dados íntegros. Ele tem que, por exemplo, controlar que haja uma concorrência sobre o arquivo, que ninguém altere, que as pessoas não alterem o arquivo simultaneamente. Ele tem que cuidar da segurança para que pessoas indevidas não acessem o arquivo. Ele tem que cuidar da questão da privacidade, dos metadados, que são as informações, são os dados sobre os dados, a data em que o arquivo foi criado, que tipo de arquivo ele é, qual que é o tamanho do arquivo, enfim, são todas as informações de gestão dos dados e dos diretórios que compõem um sistema informatizado.

Os sistemas de arquivos são bastante comuns em sistemas operacionais.
Se você tem um conhecimento um pouco mais técnico de formato que você provavelmente já ouviu falar dos sistema de arquivos FAT, NTFS do Windows.
O Linux tem vários sistemas de arquivo, EXT2,EXT3, que é o mais comum. O MACOS que também aqui têm seus próprios sistemas de arquivos.

E o Hadoop ele tem seu próprio sistema de arquivos, que é o NTFS, o sistema de arquivos distribuídos do Hadoop. 

Mas por que o Hadoop, por exemplo, sendo uma aplicação que roda preferencialmente nativamente sobre um sistema operacional baseado em Unix, em Linux, por que ele não usa o próprio sistema de arquivos do Linux, por exemplo. A resposta é bem simples porque é um tipo de aplicação diferente, em que os arquivos precisam estar separados em blocos replicados e distribuídos em nós de redes.
Então, o que acontece? Uma aplicação hadoop, onde você vai processar grande volumes de dados não vai estar fisicamente em uma única máquina, nem logicamente nem fisicamente vai estar distribuído. E as unidades de armazenamento, embora em alguns casos virtualizados possa ser a mesma, mas até fisicamente serão distintas. Então você vai ter dados distribuídos em um cluster que pode ser composto por dezenas, centenas ou milhares de nós, o que para não dizer computador, é que o computador dá a ideia de uma máquina física. A gente usa o termo nó, que pode ser uma máquina virtual que pode estar ou não no mesmo rack. Então, precisava de um sistema de arquivos que tratasse dessa particularidade, dessa peculiaridade, que é diferente de você ter um sistema de arquivos que controla o arquivo e os dados em um mesmo computador.

E então a gente tem o HDFS, o sistema de arquivos distribuído do Hadoop.
Então, o HDFS ele armazena dados em blocos. Ele tem replicação transparente, onde o default é de 3 nós. 
O que quer dizer isso? Se você tem lá, vamos supor assim, um cluster com cinco nós, que são os slaves, E você está enxergando aqui, por exemplo, um sistema de arquivos em um computador. Quando você coloca um arquivo aqui, ele por default, ele vai replicar esse arquivo em três nós. Mas você não precisa fazer nada, porque isso é feito de forma transparente, por padrão.
Essa replicação é feita em três nós, então é outra característica de um sistema de arquivos distribuído o sistema de arquivos. Ele precisa ter redundância. Ele precisa dividir os dados em os nós da rede.

O HDFS então aqui a gente vê pra entender um pouquinho melhor. Logicamente, se você tiver um arquivo lá, você vai estar vendo ele de forma única no seu sistema de arquivos. Ele vai poder estar lá, por exemplo, no diretório, então você está vendo ele lá, logicamente, dessa forma, porém, fisicamente, ele pode estar distribuído entre vários nós da rede.

Por que eu falei pode? Porque você pode ter só um nó. Você pode estar rodando uma aplicação local de teste, como a gente vai ter aqui, obviamente que ele não vai estar distribuído. Mas se você tiver um cluster e você manter a configuração de distribuição lá de replicação, que é três, ele vai estar dividido pelo menos em três outros nós.

Então, obviamente que este diagrama aqui é uma abstração, pois o HDFS distribui o arquivo inteiro em nós, mas blocos do mesmo arquivo em diferentes nós.

Uma questão importante que a gente precisa compreender para o nosso estudo é que existem vários tipos de arquivo que são comumente usualmente utilizados em um sistema de arquivos, HDFS e pelas aplicações pelas soluções que compõe o ecossistema Hadoop. Então a gente vai ter obviamente arquivos texto, o arquivo texto padrão, a gente vai ter os chamados arquivos em sequência, Sequence File, que são arquivos que têm um conjunto chave valor binário que podem ser divididos ou unidos facilmente 
a característica desse tipo desse tipo de arquivo é que eles podem ser divididos ou unidos de forma bem fácil. Então, quando a gente pensar em processamento de dados, se você tem um arquivo simples, o custo de você unir eles ou você só incluir informação, ele é bem menor ele é bem inferior que, por exemplo, você tiver um banco de dados cheio de índices, por exemplo, que então é para alguns tipos de aplicação esse arquivo é bem interessante.

Depois gente tem um arquivo binário AVRO: ele tem formato binário para serialização, tem um formato binário, ele é mais compactado, então por isso ele é ótimo para trocar dados entre sistemas.

O ORC eu diria assim este aqui o arquivo mais importante, quando a gente fala de ecossistema Hadoop, o arquivo mais importante é o arquivo colunar, otimizado para consultas de linhas e, como eu falei, o formato favorito aqui mais recomendado do sistema é Hadoop.

Depois a gente tem o RC, que é orientado a coluna também, e chave-valor, e ele tem alta taxa de compressão por linha.

Outro arquivo, como é o Parquet, que é orientado a coluna e ele é binário.

Alguns conceitos aqui como chave-valor orientados a coleção conceito que a gente estudou já ao longo do curso, então são os mesmos do ponto de vista de estrutura. São os mesmos conceitos, porém em formatos específicos aqui que são utilizados pelo ecossistema Hadoop.
