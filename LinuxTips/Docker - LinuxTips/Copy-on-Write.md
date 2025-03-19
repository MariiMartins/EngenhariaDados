<!--
# Copy-On-Write (COW) e Docker

Antes de entender as camadas propriamente ditas, precisamos entender como um dos principais requisitos para essa coisa acontecer, o *Copy-On-Write* (ou COW para os íntimos), funciona. Nas palavras do próprio Jérome Petazzoni:

*It's a little bit like having a book. You can make notes in that book if you want, but each time you approach the pen to the page, suddenly someone shows up and takes the page and makes a xerox copy and hand it back to you, that's exactly how copy on write works.*

Em tradução livre, seria como se você tivesse um livro e que fosse permitido fazer anotações nele caso quisesse, porém, cada vez que você estivesse prestes a tocar a página com a caneta, de repente alguém aparecesse, tirasse uma xerox dessa página e entregasse a cópia para você. É exatamente assim que o *Copy-On-Write* funciona.

Basicamente, significa que um novo recurso, seja ele um bloco no disco ou uma área em memória, só é alocado quando for modificado.

Tá, mas o que isso tudo tem a ver com o Docker? Bom, como você sabe, o Docker usa um esquema de camadas, ou layers, e para montar essas camadas são usadas técnicas de *Copy-On-Write*. Um container é basicamente uma pilha de camadas compostas por N camadas read-only e uma, a superior, *read-write*.