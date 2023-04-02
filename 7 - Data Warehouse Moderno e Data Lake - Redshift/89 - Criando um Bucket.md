89. Criando um Bucket
Então um bucket do S3 é um serviço de gerenciamento de arquivos.
Então, através de um bucket, você consegue criar um repositório para você colocar arquivos, e é isso que a gente vai criar.

A gente vai criar um bucket, eu vou explicar aqui passo a passo.
Então, a primeira coisa que você pode clicar aqui em S3, leio na minha listagem de buckets. Aqui eu tenho já alguns buckets criados, mas, se você criou a conta aqui para esse curso, provavelmente você não vai ter nenhum.

Então, a primeira coisa que a gente vai ter que criar um bucket. Bom, a primeira coisa que você precisa para criar um banquete é o nome, só que o bucket do S3 é um serviço que pode ser acessado globalmente. Então ele vai ter um endereço como se fosse uma URL de um site, por isso o nome do bucket, ele tem que ser único globalmente. Quer dizer, você vai ter que dar o nome para o seu bucket (Um nome único que ninguém mais no mundo tenha criado um nome com o mesmo bucket). Então eu vou que eu vou dar um nome aqui e você pode dar o nome que você quiser, e nem adianta tentar coisas simples, como o redshift ou dados, ou o curso que provavelmente alguém já criou um bucket com esse nome.

O que você precisa saber que você precisa escolher o nome?
Esse nome tem que ser o único, e depois a gente vai utilizar o nome desse bucket, mas a pasta durante o curso e você vai precisar substituir. Quando a gente for utilizar o co-op lá, por exemplo, você vai precisar substituir os parâmetros lá com o nome do seu bucket, que vão ser diferentes do meu, você precisa ter isso, claro.

A região aqui a gente vai precisar saber essa região. Então, eu sugiro que você procure aqui a região de São Paulo. Veja que aqui embaixo é a América do Sul, que é a região essa que esse atraso.
Aqui há séries desabilitadas,  ele vem com o padrão bloquear todo o acesso público. Você pode desmarcar essa opção porque é apenas para um curso.
Assim, você consegue ter um acesso mais irrestrito para o bucket quando você desmarca. Aí você tem que marcar aqui que você reconhece que as configurações.
Pode fazer com que objetos dentro do banco se tornem públicos. Então, lembrando, a gente só está fazendo isso porque é um curso ver seu método bucket, Você pode desativar tags que são marcações.

Ele pode ter por padrão criptografia atrás, ou seja, com os dados lá parados, pode já aplicar a criptografia. A gente não precisa. E aqui, configurações avançadas a gente não precisa. Então eu vou criar aqui o bucket.
Então vejam que, no meu caso, aqui ao lado é redshift1234 não existia.
Então ele criou o bucket e o bucket está aqui, está criado com a região.

Agora eu vou clicar nesse bucket, vejam que ele assume a forma de link, eu vou clicar nesse bucket e dentro deste bucket você vai buscar aqui ‘criar pasta’ e você vai clicar em Criar Pasta.
Você vai dar um nome para a pasta, agora a pasta, ela não precisa ser única.
Porque? Porque a pasta, dentro do seu bucket, eu digo não precisa ser a única globalmente, dentro do bucket, sim.

Mas, por exemplo, se você colocar aqui a pasta de dados dentro do seu bucket, você não vai ter problema, ok?
Então vou tirar aqui a pasta Dados e vou clicar aqui em Criar Pasta.
Eu vou clicar aqui na pasta, então estamos dentro do bucket ‘Aula redshift1234’.
