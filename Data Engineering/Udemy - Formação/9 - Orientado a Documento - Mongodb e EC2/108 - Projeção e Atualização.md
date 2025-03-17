108. Projeção e Atualização
Uma outra opção que nós temos é você limitar o número de registro que você quer ver.
dB.clientes.find().limt(2)
Ele vai trazer os 2 primeiros registros.
Eu também posso ordenar:
dB.clientes.find().sort({nome:1})
E aqui eu vou passar a coluna que eu quero, o campo que eu quero ordenar e o 1 para ordenar em ordem crescente. Vejam que dentro de find eu ainda poderia passar um filtro, limitar ele ordenar dentro daquele filtro que nós já estudamos ali anteriormente. Se eu quiser ordenar de forma decrescente, é só trocar que um, pelo -1, então ele vai trazer de forma decrescente.

E agora, se eu quiser Atualizar um cliente da minha coleção. Primeiro vou listar que um cliente para gente ver as informações dele, pra gente ver que deu certo depois da atualização, então eu vou pegar o que o cliente de nome Pedro. Vamos supor que eu quero atualizar a idade dele. Então, eu tenho que passar um campo que me diga quais documentos eu vou atualizar que seria equivalente a uma cláusula where do SQL, Obviamente, se tiver mais de um mês, ele vai atualizar mais de um.
Mas eu posso também utilizar o updateOne que vai atualizar apenas um registro.
dB.clientes.updateOne ({Nome: “Pedro”},{$set:{idade: 29}})
Então o acknowledged me deu true e o matchcount um e modificou.
Agora vamos achar o Pedro de novo e ver a idade. A gente está vendo que a idade era 26. A gente pode ver agora se a idade é 29.

E se a gente quiser excluir, assim como tem o cliente Pedro na nossa coleção a gente tem vários clientes. A gente quer excluir só o Pedro. Então, para isso a gente pode utilizar o deleteOne().
dB.clientes.deleteOne ({Nome: “Pedro”})
Acknowledge: True quer dizer que deu certo operação.
Agora vamos ver que o dB.clientes.find({nome: “Pedro”}), agora ele não acha nada, então, com isso a gente confirma que ele excluiu o Pedro com sucesso, documento onde o nome era Pedro.

E se a gente quiser excluir a coleção inteira, então a gente pode fazer um 
db. clientes. drop()
Então eu não vou escolher apenas um documento, Eu vou escolher toda a coleção, Então, qualquer um que você buscar aqui, você não vai encontrar mais nada. A gente excluiu a coleção toda.
No próximo tutorial, então, a gente vai ver como utilizar o modelo Import, que é um utilitário que instala já como algo para importar dados.
