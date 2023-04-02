<<<<<<< HEAD
<<<<<<< HEAD
134. Introdução
O nosso objetivo aqui nesta sessão é mostrar como a gente utiliza Python para engenharia de dados.

O Python ele é, sem dúvida nenhuma, de forma ampla a principal linguagem na engenharia e na ciência de dados. Então este essa seção vai ser interessante para você ver como a gente pode utilizar o Python em engenharia de dados.
Você vai conhecer mais um serviço do AWS, que é o RDS, para serviços de bancos de dados relacionais. Você vai conhecer o Google Collab, que é uma interface de em que você pode utilizar código Python. E o mais interessante você vai ver como você pode utilizar o Python para interagir com serviços na nuvem, no caso aqui serviços do AWS.

Então a gente vai utilizar no Python duas principais bibliotecas, que é o Psycopg2, que é para conectar com o banco de dados relacional PostgreSQL que nós já conhecemos, e o Boto3. O Boto3 é para você conectar com o serviço do AWS através de uma aplicação Python.

Como já mencionei, rapidamente a gente vai utilizar o Google Colab. O Google Colab é um serviço na nuvem em que você pode utilizar notebooks se você não sabe o que é o notebook, você vai logo em seguida, um tutorial para você conhecer o Colab. Mas o Colab, em resumo, é o ambiente mantido pelo Google em que você pode criar e executar código Python. Então, para você não precisar instalar uma IDE no seu computador ou para você não ter custo em rodar um notebook. A gente vai utilizar o Colab, que ele nos atende perfeitamente.

A gente vai ter um bucket S3 e nesse bucket S3, a gente vai fazer o upload de algumas imagens. E a gente vai criar uma aplicação Python que vai inventariar essas imagens em um banco de dados Postgres SQL. Então inventará nada mais é do que pegar todos os nomes dessas imagens e gravar um banco de dados.

Então, supondo que seja uma agência de publicidade, ela quer ter uma relação de todas as imagens que ela tem disponível. Então vamos criar uma aplicação Python que vai fazer isso.

O que é o AWS RDS? O AWS RDS é um serviço de bancos relacionais. Então no RDS você tem várias opções de bancos de dados, o Postgres que nós já conhecemos, o Aurora, o SQL Server, o Oracle. O importante de destacar aqui é que no RDS você cria uma instância apenas do banco de dados. Não é uma instância de sistema operacional como nós utilizamos lá na sessão em que nós estudamos Postgres, lá nós criamos uma instância do EC2 ou seja, nós tínhamos um sistema operacional à nossa disposição e nesse sistema operacional nós instalamos um banco de dados. 

Aqui não, aqui a gente vai criar apenas um banco de dados que vai estar rodando um serviço de banco de dados, um gerenciador de banco de dados relacional que vai estar rodando no servidor do AWS e a gente vai utilizar o Postgres e você vai ver que existe lá a opção freetear e que você não vai ter custo.

A gente vai criar um banco de dados que a gente vai chamar de inventário e nesse banco de dados a gente vai criar uma tabela. Essa tabela ela vai ter um ID e o nome do arquivo. Então vai ser uma tabela com apenas duas colunas ID  e nome do arquivo. 

Quais são as etapas que a gente vai executar para cumprir aí o nosso objetivo de criar essa aplicação de inventário. Primeiro lá, nesse texto que você já conhece, vai criar um bucket. Dentro desse bucket você vai tirar uma pasta, você vai fazer o upload de imagens. Essas imagens estão junto ao material do curso. A gente vai criar um banco de dados Postgres no serviço RDS Folder. Então não vai ter custo.

Depois se vai conhecer o Colab, se você já conhece e pode pular essa etapa.
Depois a gente vai tirar a chave de acesso, assim como já fez em sessão anterior, por exemplo. Lá quando a gente utilizou o redshift. A gente tinha um par de chave de acesso. Se você já tem salva, você pode utilizar as mesmas.
E depois a gente vai lá pro Colab, utilizando o Python e a gente vai executar várias etapas lá, então a gente vai conectar a esse gerenciador de banco de dados. A gente vai criar um banco de dados, vai criar uma tabela, a gente vai conectar ao bucket S3 do AWS através da biblioteca. A gente vai listar as imagens. A gente vai gravar essa lista de imagens, o nome dessas imagens no banco de dados que nós criamos e depois a gente vai executar o Última Etapa lá, que é verificar se a gravação deu certo, ok, então é uma sessão bem legal.
=======
134. Introdução
O nosso objetivo aqui nesta sessão é mostrar como a gente utiliza Python para engenharia de dados.

O Python ele é, sem dúvida nenhuma, de forma ampla a principal linguagem na engenharia e na ciência de dados. Então este essa seção vai ser interessante para você ver como a gente pode utilizar o Python em engenharia de dados.
Você vai conhecer mais um serviço do AWS, que é o RDS, para serviços de bancos de dados relacionais. Você vai conhecer o Google Collab, que é uma interface de em que você pode utilizar código Python. E o mais interessante você vai ver como você pode utilizar o Python para interagir com serviços na nuvem, no caso aqui serviços do AWS.

Então a gente vai utilizar no Python duas principais bibliotecas, que é o Psycopg2, que é para conectar com o banco de dados relacional PostgreSQL que nós já conhecemos, e o Boto3. O Boto3 é para você conectar com o serviço do AWS através de uma aplicação Python.

Como já mencionei, rapidamente a gente vai utilizar o Google Colab. O Google Colab é um serviço na nuvem em que você pode utilizar notebooks se você não sabe o que é o notebook, você vai logo em seguida, um tutorial para você conhecer o Colab. Mas o Colab, em resumo, é o ambiente mantido pelo Google em que você pode criar e executar código Python. Então, para você não precisar instalar uma IDE no seu computador ou para você não ter custo em rodar um notebook. A gente vai utilizar o Colab, que ele nos atende perfeitamente.

A gente vai ter um bucket S3 e nesse bucket S3, a gente vai fazer o upload de algumas imagens. E a gente vai criar uma aplicação Python que vai inventariar essas imagens em um banco de dados Postgres SQL. Então inventará nada mais é do que pegar todos os nomes dessas imagens e gravar um banco de dados.

Então, supondo que seja uma agência de publicidade, ela quer ter uma relação de todas as imagens que ela tem disponível. Então vamos criar uma aplicação Python que vai fazer isso.

O que é o AWS RDS? O AWS RDS é um serviço de bancos relacionais. Então no RDS você tem várias opções de bancos de dados, o Postgres que nós já conhecemos, o Aurora, o SQL Server, o Oracle. O importante de destacar aqui é que no RDS você cria uma instância apenas do banco de dados. Não é uma instância de sistema operacional como nós utilizamos lá na sessão em que nós estudamos Postgres, lá nós criamos uma instância do EC2 ou seja, nós tínhamos um sistema operacional à nossa disposição e nesse sistema operacional nós instalamos um banco de dados. 

Aqui não, aqui a gente vai criar apenas um banco de dados que vai estar rodando um serviço de banco de dados, um gerenciador de banco de dados relacional que vai estar rodando no servidor do AWS e a gente vai utilizar o Postgres e você vai ver que existe lá a opção freetear e que você não vai ter custo.

A gente vai criar um banco de dados que a gente vai chamar de inventário e nesse banco de dados a gente vai criar uma tabela. Essa tabela ela vai ter um ID e o nome do arquivo. Então vai ser uma tabela com apenas duas colunas ID  e nome do arquivo. 

Quais são as etapas que a gente vai executar para cumprir aí o nosso objetivo de criar essa aplicação de inventário. Primeiro lá, nesse texto que você já conhece, vai criar um bucket. Dentro desse bucket você vai tirar uma pasta, você vai fazer o upload de imagens. Essas imagens estão junto ao material do curso. A gente vai criar um banco de dados Postgres no serviço RDS Folder. Então não vai ter custo.

Depois se vai conhecer o Colab, se você já conhece e pode pular essa etapa.
Depois a gente vai tirar a chave de acesso, assim como já fez em sessão anterior, por exemplo. Lá quando a gente utilizou o redshift. A gente tinha um par de chave de acesso. Se você já tem salva, você pode utilizar as mesmas.
E depois a gente vai lá pro Colab, utilizando o Python e a gente vai executar várias etapas lá, então a gente vai conectar a esse gerenciador de banco de dados. A gente vai criar um banco de dados, vai criar uma tabela, a gente vai conectar ao bucket S3 do AWS através da biblioteca. A gente vai listar as imagens. A gente vai gravar essa lista de imagens, o nome dessas imagens no banco de dados que nós criamos e depois a gente vai executar o Última Etapa lá, que é verificar se a gravação deu certo, ok, então é uma sessão bem legal.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
=======
134. Introdução
O nosso objetivo aqui nesta sessão é mostrar como a gente utiliza Python para engenharia de dados.

O Python ele é, sem dúvida nenhuma, de forma ampla a principal linguagem na engenharia e na ciência de dados. Então este essa seção vai ser interessante para você ver como a gente pode utilizar o Python em engenharia de dados.
Você vai conhecer mais um serviço do AWS, que é o RDS, para serviços de bancos de dados relacionais. Você vai conhecer o Google Collab, que é uma interface de em que você pode utilizar código Python. E o mais interessante você vai ver como você pode utilizar o Python para interagir com serviços na nuvem, no caso aqui serviços do AWS.

Então a gente vai utilizar no Python duas principais bibliotecas, que é o Psycopg2, que é para conectar com o banco de dados relacional PostgreSQL que nós já conhecemos, e o Boto3. O Boto3 é para você conectar com o serviço do AWS através de uma aplicação Python.

Como já mencionei, rapidamente a gente vai utilizar o Google Colab. O Google Colab é um serviço na nuvem em que você pode utilizar notebooks se você não sabe o que é o notebook, você vai logo em seguida, um tutorial para você conhecer o Colab. Mas o Colab, em resumo, é o ambiente mantido pelo Google em que você pode criar e executar código Python. Então, para você não precisar instalar uma IDE no seu computador ou para você não ter custo em rodar um notebook. A gente vai utilizar o Colab, que ele nos atende perfeitamente.

A gente vai ter um bucket S3 e nesse bucket S3, a gente vai fazer o upload de algumas imagens. E a gente vai criar uma aplicação Python que vai inventariar essas imagens em um banco de dados Postgres SQL. Então inventará nada mais é do que pegar todos os nomes dessas imagens e gravar um banco de dados.

Então, supondo que seja uma agência de publicidade, ela quer ter uma relação de todas as imagens que ela tem disponível. Então vamos criar uma aplicação Python que vai fazer isso.

O que é o AWS RDS? O AWS RDS é um serviço de bancos relacionais. Então no RDS você tem várias opções de bancos de dados, o Postgres que nós já conhecemos, o Aurora, o SQL Server, o Oracle. O importante de destacar aqui é que no RDS você cria uma instância apenas do banco de dados. Não é uma instância de sistema operacional como nós utilizamos lá na sessão em que nós estudamos Postgres, lá nós criamos uma instância do EC2 ou seja, nós tínhamos um sistema operacional à nossa disposição e nesse sistema operacional nós instalamos um banco de dados. 

Aqui não, aqui a gente vai criar apenas um banco de dados que vai estar rodando um serviço de banco de dados, um gerenciador de banco de dados relacional que vai estar rodando no servidor do AWS e a gente vai utilizar o Postgres e você vai ver que existe lá a opção freetear e que você não vai ter custo.

A gente vai criar um banco de dados que a gente vai chamar de inventário e nesse banco de dados a gente vai criar uma tabela. Essa tabela ela vai ter um ID e o nome do arquivo. Então vai ser uma tabela com apenas duas colunas ID  e nome do arquivo. 

Quais são as etapas que a gente vai executar para cumprir aí o nosso objetivo de criar essa aplicação de inventário. Primeiro lá, nesse texto que você já conhece, vai criar um bucket. Dentro desse bucket você vai tirar uma pasta, você vai fazer o upload de imagens. Essas imagens estão junto ao material do curso. A gente vai criar um banco de dados Postgres no serviço RDS Folder. Então não vai ter custo.

Depois se vai conhecer o Colab, se você já conhece e pode pular essa etapa.
Depois a gente vai tirar a chave de acesso, assim como já fez em sessão anterior, por exemplo. Lá quando a gente utilizou o redshift. A gente tinha um par de chave de acesso. Se você já tem salva, você pode utilizar as mesmas.
E depois a gente vai lá pro Colab, utilizando o Python e a gente vai executar várias etapas lá, então a gente vai conectar a esse gerenciador de banco de dados. A gente vai criar um banco de dados, vai criar uma tabela, a gente vai conectar ao bucket S3 do AWS através da biblioteca. A gente vai listar as imagens. A gente vai gravar essa lista de imagens, o nome dessas imagens no banco de dados que nós criamos e depois a gente vai executar o Última Etapa lá, que é verificar se a gravação deu certo, ok, então é uma sessão bem legal.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
A gente vai aprender bastante coisa interessante.