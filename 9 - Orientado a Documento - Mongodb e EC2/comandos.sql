#Insere um unico documento na coleção posts
> db.posts.insert({nome:"José", postagem: "Bons Produtos!", data:"31-06-2019"})
WriteResult ({"nInserted": 1 })

#Para criar a coleção primeiro:
> db.createCollection("clientes")

#Para inserir varios documentos
db.posts.insert([
    {nome: "Antonio", postagem:"minha bike quebrou", data:"26-05-2013"},
    {nome: "Maria Silva", postagem:"Encontri tudo que procurava", data:"14-06-2019"},
    {nome: "Lucas Andrade", postagem:"ótimo atendimento", data:"12-04-2019"}
    ])
    BulkWriteResult({
        "writeErrors" : [],
        "writeConcernErrors" : [],
        "nInserted" : 3,
        "nUpserted": 0,
        "nMatched" : 0,
        "nModifield": 0,
        "nRemoved": 0,
        "uoserted" : []
    })


#Ler documetos: find
> db.posts.find()
{ "_id": ObjectId("5d90bc10ee1100c307004d5"), nome: "Antonio", postagem:"minha bike quebrou", data:"26-05-2013"},
{ "_id": ObjectId("5d90bc10ee1100c307004d6"),nome: "Maria Silva", postagem:"Encontri tudo que procurava", data:"14-06-2019"},
{"_id": ObjectId("5d90bc10ee1100c307004d7"),nome: "Lucas Andrade", postagem:"ótimo atendimento", data:"12-04-2019"}

#Ler documetos: pretty
> db.posts.find().pretty()
{
    "_id": ObjectId("5d090bc10ee1100c307004d4"),
    "nome": "José",
    "postagem": "Bons Produtos!",
    "data": "31-06-2019"
}

#Ler documentos: findOne
> db.posts.findOne()
{
    "_id": ObjectId("5d01129c1dd51b69599c3110"),
    "nome": "José",
    "postagem": "Bons Produtos",
    "data": "31-06-2019"
}