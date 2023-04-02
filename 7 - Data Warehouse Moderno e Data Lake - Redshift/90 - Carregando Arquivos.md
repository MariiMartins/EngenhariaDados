90. Carregando Arquivos
Agora, no material do curso a gente tem alguns arquivos CSV que nós vamos utilizar para popular, ou seja, para carregar para o redshift utilizando o comando copie. Então, agora a gente precisa fazer o upload desses arquivos, que é o botão aqui carregar. Então você vai clicar no botão Carregar e você vai localizar esses arquivos no seu computador.Então aqui eu estou na pasta onde os arquivos se encontram. Pode existir outros arquivos aqui, mas você vai importar apenas os arquivos CSV. São cinco clientes itens venda, produtos, vendas e vendedores.

Ok, então a gente vai abrir.
Vejam que quando eu abri, ele não importou ainda, ele só colocou a lista desses arquivos, e está dizendo que são cinco no total. E agora sim, vou clicar em carregar, veja que o upload foi bem sucedido. Vou fechar aqui e aqui estou de volta dentro da pasta dados dentro do bucket que foi criado, os cinco arquivos já estão aqui.

Eu vou clicar em um desses arquivos, e vejam que interessante. Ele traz várias informações aqui sobre o arquivo.
Agora, uma coisa aqui interessante tem esse motor que copiar you in o Uri do S3, ou seja, ele vai copiar o caminho desse arquivo, que é isso aqui.
Eu posso também copiar clicando aqui. Então, como eu tinha falado o nome do bucket, ele tem que ser exclusivo. Por que você vai ter um caminho universal para acessar esse arquivo, existe também um caminho de internet com uma URL https com o nome do bucket, porém um caminho um pouco mais comprido.

Então, é este caminho aqui que a gente vai precisar. Quando a gente for utilizar o comando, copie para importar esses dados para o redshift que a gente vai copiar, importar todos esses cinco arquivos, cada um para a sua tabela no redshift.
Porém, antes a gente precisa criar credenciais que são uma forma de um acesso que a gente precisa criar para que seja possível o redshift vir aqui até o bucket.
