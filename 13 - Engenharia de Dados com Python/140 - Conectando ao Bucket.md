<<<<<<< HEAD
<<<<<<< HEAD
140. Conectando ao Bucket
Agora, então a gente vai conectar ao S3. A gente precisa então aqui instalar a biblioteca, boto três, a biblioteca, Boto3 e a biblioteca para interagir com a AWS. Então, para a gente instalar ela, a gente vai digitar aqui Boto3!
Vamos executar! Aqui, então ele está fazendo o download. Eventualmente. Aqui pode aparecer aqui uma mensagem de erro, mas ele diz aqui que instalou com sucesso. Aqui, então não tem problema.
A mensagem de erro é feita, a instalação, então a gente vai criar aqui, vamos dizer assim, que é o código principal do nosso, do nosso projeto, que é ler os objetos do bucket S3 e gravar no banco de dados. Então, primeiro eu vou criar o código apenas para ler o objeto, os objetos do S3 para ver se está tudo certo, estando tudo certo.
Aí então a gente complementa esse código para que a gente consiga armazenar essas informações no banco de dados. Então a gente precisa importar o próprio Boto3. A gente precisa importar o IOR para leitura de arquivos from, A gente precisa importar também o Psycopg2 não vamos usar na primeira etapa, mas depois a gente vai utilizar quem estão essas são as bibliotecas.

Vamos só ver que está tudo certo, tudo ok.

Então, para a gente conectar no AWS, a gente vai utilizar o Boto3. O Boto3 tem dois métodos principais o Resource e o Client Resource. É uma conexão em mais alto nível, o cliente mais baixo nível. A gente vai utilizar aqui o Resource.
Então vou criar uma variável S3 e eu vou chamar que Boto3 ponto resource e aqui eu vou precisar passar algumas informações. Então, a primeira informação que eu preciso passar para ele é o service, existe uma infinidade de serviços da AWS, eu preciso dizer com qual o serviço interno irei interagir.

A esses sublinhado tem sublinhado Éder que vamos lá e agora precisa.
AWS Secret Access. E também você vai colar aqui o seu script ou a sua chave.
Então, com essas informações aqui a gente consegue interagir com o bucket do S3. Agora, claro que ele vai saber qual o banquete, em qual pasta você quer conectar. Então, pra gente ler os objetos que estão lá no banquete, eu vou criar aqui duas variáveis para ele saber qual bucket. Uma que vai ser o nome do bucket e outra que é o prefixo que é a pasta.
Então você vai lá no seu bucket, e você copia aqui o nome do bucket.
Estão na primeira variável aqui, apenas o nome do banquete na segunda variável, que é o prefixo e a pasta, então a pasta e imagem você pode copiar ou você pode digitar.
=======
140. Conectando ao Bucket
Agora, então a gente vai conectar ao S3. A gente precisa então aqui instalar a biblioteca, boto três, a biblioteca, Boto3 e a biblioteca para interagir com a AWS. Então, para a gente instalar ela, a gente vai digitar aqui Boto3!
Vamos executar! Aqui, então ele está fazendo o download. Eventualmente. Aqui pode aparecer aqui uma mensagem de erro, mas ele diz aqui que instalou com sucesso. Aqui, então não tem problema.
A mensagem de erro é feita, a instalação, então a gente vai criar aqui, vamos dizer assim, que é o código principal do nosso, do nosso projeto, que é ler os objetos do bucket S3 e gravar no banco de dados. Então, primeiro eu vou criar o código apenas para ler o objeto, os objetos do S3 para ver se está tudo certo, estando tudo certo.
Aí então a gente complementa esse código para que a gente consiga armazenar essas informações no banco de dados. Então a gente precisa importar o próprio Boto3. A gente precisa importar o IOR para leitura de arquivos from, A gente precisa importar também o Psycopg2 não vamos usar na primeira etapa, mas depois a gente vai utilizar quem estão essas são as bibliotecas.

Vamos só ver que está tudo certo, tudo ok.

Então, para a gente conectar no AWS, a gente vai utilizar o Boto3. O Boto3 tem dois métodos principais o Resource e o Client Resource. É uma conexão em mais alto nível, o cliente mais baixo nível. A gente vai utilizar aqui o Resource.
Então vou criar uma variável S3 e eu vou chamar que Boto3 ponto resource e aqui eu vou precisar passar algumas informações. Então, a primeira informação que eu preciso passar para ele é o service, existe uma infinidade de serviços da AWS, eu preciso dizer com qual o serviço interno irei interagir.

A esses sublinhado tem sublinhado Éder que vamos lá e agora precisa.
AWS Secret Access. E também você vai colar aqui o seu script ou a sua chave.
Então, com essas informações aqui a gente consegue interagir com o bucket do S3. Agora, claro que ele vai saber qual o banquete, em qual pasta você quer conectar. Então, pra gente ler os objetos que estão lá no banquete, eu vou criar aqui duas variáveis para ele saber qual bucket. Uma que vai ser o nome do bucket e outra que é o prefixo que é a pasta.
Então você vai lá no seu bucket, e você copia aqui o nome do bucket.
Estão na primeira variável aqui, apenas o nome do banquete na segunda variável, que é o prefixo e a pasta, então a pasta e imagem você pode copiar ou você pode digitar.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
=======
140. Conectando ao Bucket
Agora, então a gente vai conectar ao S3. A gente precisa então aqui instalar a biblioteca, boto três, a biblioteca, Boto3 e a biblioteca para interagir com a AWS. Então, para a gente instalar ela, a gente vai digitar aqui Boto3!
Vamos executar! Aqui, então ele está fazendo o download. Eventualmente. Aqui pode aparecer aqui uma mensagem de erro, mas ele diz aqui que instalou com sucesso. Aqui, então não tem problema.
A mensagem de erro é feita, a instalação, então a gente vai criar aqui, vamos dizer assim, que é o código principal do nosso, do nosso projeto, que é ler os objetos do bucket S3 e gravar no banco de dados. Então, primeiro eu vou criar o código apenas para ler o objeto, os objetos do S3 para ver se está tudo certo, estando tudo certo.
Aí então a gente complementa esse código para que a gente consiga armazenar essas informações no banco de dados. Então a gente precisa importar o próprio Boto3. A gente precisa importar o IOR para leitura de arquivos from, A gente precisa importar também o Psycopg2 não vamos usar na primeira etapa, mas depois a gente vai utilizar quem estão essas são as bibliotecas.

Vamos só ver que está tudo certo, tudo ok.

Então, para a gente conectar no AWS, a gente vai utilizar o Boto3. O Boto3 tem dois métodos principais o Resource e o Client Resource. É uma conexão em mais alto nível, o cliente mais baixo nível. A gente vai utilizar aqui o Resource.
Então vou criar uma variável S3 e eu vou chamar que Boto3 ponto resource e aqui eu vou precisar passar algumas informações. Então, a primeira informação que eu preciso passar para ele é o service, existe uma infinidade de serviços da AWS, eu preciso dizer com qual o serviço interno irei interagir.

A esses sublinhado tem sublinhado Éder que vamos lá e agora precisa.
AWS Secret Access. E também você vai colar aqui o seu script ou a sua chave.
Então, com essas informações aqui a gente consegue interagir com o bucket do S3. Agora, claro que ele vai saber qual o banquete, em qual pasta você quer conectar. Então, pra gente ler os objetos que estão lá no banquete, eu vou criar aqui duas variáveis para ele saber qual bucket. Uma que vai ser o nome do bucket e outra que é o prefixo que é a pasta.
Então você vai lá no seu bucket, e você copia aqui o nome do bucket.
Estão na primeira variável aqui, apenas o nome do banquete na segunda variável, que é o prefixo e a pasta, então a pasta e imagem você pode copiar ou você pode digitar.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
