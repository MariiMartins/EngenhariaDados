112. Hashes
Um outro tipo de dados que nós vamos estudar agora que o Redis suporta são os hashes. Os hashes são conjuntos de campos valores associados a uma chave. Então, qual é a sintaxe? Você sempre vai ter uma chave única campo-valor, campo-valor, campo-valor e assim sucessivamente. Então, os comandos associados a Hashes eles têm sempre o H na frente.

Então HMSET você cria um hash.

Esta definição é importante porque depois você pode, por exemplo, recuperar só os valores dos campos de determinados campos. E é importante a gente deixar claro aqui que eu tenho uma chave que aqui é texto, mas podia ser um número e que também deve ser única. Então, com a HMSET eu crio um Hash.
Todo este registro aqui ele está associado ao mesmo dado e o mesmo hash com uma chave única.

Com HDEL eu consigo excluir de uma determinada chave um campo e um valor. Então, por exemplo, aqui eu estou dizendo que da chave cadastro eu quero excluir o campo cidade. 
Então vejam aqui eu tinha anteriormente aqui Cidade Santa Maria, que eu criei aqui com o HDEL Cadastro. Deu o cadastro, que é minha chave, exclui o campo cidade e eu recuperei o registro, cadastro e vejo que a cidade não está mais aqui.

HGETALL é outro comando importante que me retorna todos os valores de um determinado registro. Então eu vejo que eu não tenho os nomes dos campos, eu tenho apenas aqui todos os valores, a cidade não aparece porque a gente excluiu.

Para mim, recuperar valores de campos. Então aqui eu vejo HMGET chave, nome e profissão.
Então veja que eu estou passando dois campos. Nome e profissão da chave cadastro. E ele me retornou aqui o nome e a profissão.

Se eu quiser retornar todos os campos, eu uso HVALS chave e aquilo me retorna. José e engenheiro, eu não preciso especificar aqui os campos.

Para mim, recuperar todo o HASH que a gente já viu rapidamente HGETALL cadastro. Então ele me está trazendo aqui todos os valores daquele de um mesmo hash, conforme a chave ali, que é cadastro.

Para mim, verificar uma chave e um valor, se eles existem, eu uso HEXISTS.
Eu uso a chave e o valor, então o nome (Ele me diz que nome é um campo que existe), Agora eu uso cadastro, nomes (É um campo que não existe), ele me retorna zero.

Para mim e retorna o número de campos de um Hash. Eu uso a HLEN em cadastro, então ele está me dizendo que cabaço tem dois campos.

Para mim, tem uma lista dos campos, não dos valores, eu uso HKEYS cadastro. Ele está me dizendo aqui que os campos são nome e profissão.
Então esses são os principais comandos utilizados com hashes.
