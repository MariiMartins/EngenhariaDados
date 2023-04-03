107. Buscando documentos
Então a gente viu que o find(), Ele retorna todos os documentos da coleção.
Agora, por exemplo, eu posso não querer ver todos os documentos, por exemplo, ver apenas um, Eu posso utilizar dB.clientes.findOne()
Então, findOne ele vai me retornar apenas um, Geralmente, o primeiro documento.

Eu posso também querer achar um documento específico e aí então existe várias formas de eu procurar um documento específico. Então eu posso procurar um documento específico pelo para um campo pelo valor de um campo.
Então, por exemplo, dB.clientes.find({nome:  “Pedro”})
Agora vamos criar uma condição um pouquinho mais sofisticada. Vamos buscar um sobrenome e uma idade que seja menor ou igual a um determinado valor. Então, você lembra lá? Se você não lembra, a gente vai ver agora que existe os operadores daquilo que a gente pode utilizar e o menor ou igual a é o cifrão.
db.clientes.find({sobrenome : “Rocha”, idade: {$lte: 12}})
Então ele retornou aqui é o Lucas, que tem o sobrenome Rocha, que foi a condição que eu coloquei e a idade dele é 12. Então ele incluiu a idade 12, porque eu coloquei menor, igual, e não apenas menor. Se não, o Lucas não seria incluído.

Agora vamos supor que eu queira utilizar uma condição ou eu quero buscar o nome de um cliente cujo sobrenome seja rocha ou o nome seja Maria.
Então, vejo que não necessariamente vai ser o mesmo cliente. Ele não tem que ser um nome Maria, ou o sobrenome Rocha. Ou então, se um tiver um sobrenome ou tiver o nome equivalente à minha busca, ele vai dar matched.
dB.clientes.find({$or: [{sobrenome: “Rocha”},{nome: “Maria”}]})
E vejo esse aqui tem sobrenome Rocha. Isso aqui tem o nome Maria e esse aqui tem o sobrenome Rocha. Então ele trouxe os três porque Eu coloquei uma condição ou não é uma condição And então qualquer um dos critérios sendo atendidos ele retorna como resultado.

Agora, o que a gente está vendo aqui é que quando eu faço uma busca, ele retorna todos os campos. Vamos supor que eu queira, por exemplo, que ele me retorne apenas o nome. Eu vou fazer uma busca, mas ele me deve retornar apenas o nome. Então, como que eu faria isso?
dB.clientes.find({sobrenome: “Rocha”}, {sobrenome: 0, idade: 0})
Então agora sim, ele me trouxe os dois resultados, mas eu informei aqui que o sobrenome era zero, idade também era zero, então ele não mostrou estes campos.

Eu posso também fazer aqui o que a gente chama de projeção, onde eu não vou querer mostrar o ID
dB.clientes.find({sobrenome: “Rocha”}, {_id: 0})
E eu tenho apenas o nome, o sobrenome e a idade de alguns casos.
Se você não tem interesse em ver aquele, aquele código lá que é gerado automaticamente, fica muito mais interessante.

Eu posso também criar uma consulta dizendo que eu vou colocar.
dB.clientes.find({sobrenome: “Rocha”}, {nome: 1})
Ele mostrou o Id   por padrão, mas ele trouxe apenas o nome. Ele não trouxe o sobrenome nem a idade, ok, então, aqui no novo que se chama Projeção, você define os campos da coleção que ele vai mostrar.
