Bom, agora a gente vai ver outra característica do S3, que são as camadas. Então eu vou colocar um exemplo. Imagine que você tenha muitos arquivos de áudio, músicas que você baixou durante os anos, durante algum tempo e você tem isso armazenado. Só que hoje, como a gente consegue acessar qualquer música, por exemplo, em um aplicativo de música online como o Spotify, por exemplo, você não tem mais necessidade de guardar essas músicas, mas também você não quer se desfazer delas.Você, de alguma forma que guardava, você sabe o que você não vai utilizar mais, pelo menos não frequentemente essas músicas. Então, em vez de você colocar no seu HD, que é um SSD que você tem e um espaço limitado, você vai pegar um disco rígido tradicional que você tem guardado lá, que você não está utilizando. E você vai colocar essas músicas lá. E você sabe que se um dia você precisar, você não vai ter acesso imediato a essas músicas, mas elas estão lá. Elas estão guardadas lá e no dispositivo, cujo acesso é mais demorado, mas que você consegue acessar as músicas.

O sistema de storage do S3 é o mesmo princípio, então você pode armazenar os seus dados em diferentes camadas.
Então a camada padrão é a standard, que é para uso geral. Então, sempre que você cria um bucket o armazenamento você vai estar usando a camada padrão, e existe outros tipos de camada.

E, é claro, quando você muda a camada, muda o preço. Então, normalmente o esperado que o preço que o preço reduza. Então, por exemplo, existe a camada de acesso infrequente(IA).

Existe o S3,  OneZone , que é para acesso infrequente. O OneZone  não quer dizer que ele vai ser armazenado em apenas uma única zona do S3. Então, isso quer dizer que, eventualmente, você pode perder esses dados, porque eles vão estar aí apenas em apenas um lugar.

Depois, tenho a camada inteligente que o Amazon vai decidir onde fica melhor para otimizar os preços.
E depois tem o Glacier. O Glacier é para arquivos que você quer arquivar. Seria o exemplo clássico das músicas lá que você não vai utilizar.

Então, vejo aqui a comparação das camadas.
 
Então, a gente traz aqui a durabilidade, a disponibilidade, as zonas de acesso, acesso concorrente e a tolerância a falhas. Então, o padrão aqui você vê que é o melhor a durabilidade em termos de disponibilidade.
As zonas de acesso são mais de três e o acesso, concorrentes tolerantes a falhas Dois.
●	O padrão acesso infrequente é semelhante. Depois tem OneZone onde você pode ver que a disponibilidade ela diminui um pouco as zonas de acesso. Apenas uma é o acesso com rede. Já falha a tolerância é zero, depois você tem o S3, camada inteligente onde a AWS, onde o Amazon vai decide o que é melhor. Você vê que a disponibilidade é um pouco menor e depois você tem lá o Glacier, que a disponibilidade está ali como ele é. Porque ela pode não ser imediata, que ela pode levar de minutos até um tempo mais.
Então, quanto mais você vai para a direita, mais o valor diminui. E quanto mais você vai precisar usar os dados, mais você vai querer estar em um padrão. E um tipo de camada à esquerda.
Então o padrão para ser frequente depois pra acesso não frequente, O inteligente e, finalmente, o arquivo.

Então o arquivo é quando eu já expliquei que você não vai precisar ter acesso imediato aos dados, mas você sabe que eles estão lá. 

Bom, aí entra a questão das regras de ciclo de vida do S3.
Então na prática, a gente pode no S3 criar regras de ciclo de vida.
Vamos imaginar o seguinte vamos imaginar que você armazene logs, logs de acesso ao seu sistema no S3. Então a gente sabe que no momento em que o log é gerado, até vamos supor alguns dias esse log, ele vai ser bastante acessado. Depois de alguns dias ele não vai ter mais o acesso frequente. Passando mais um tempo, ele você sabe, já que ele não vai ser mais acessado, mas mesmo assim você vai guardar ele lá por um tempo.

Você pode colocar ele lá no Glacier para caso por alguma circunstância, algumas circunstâncias não precise, você consegue ainda acessar ele e, depois disso, você simplesmente exclui.

Então, regras de ciclo de vida é exatamente isso.
Você pode criar regras no S3 para ele gerenciar esse ciclo de vida para você. Então, o exemplo de uso você pode ter uso geral, uso infrequente e Glacier. Você define o tempo que isso vai acontecer. Então você pode criar ações de transições, então você pode definir que os objetos eles vão fazer uma transição para outra classe de armazenamento. Então você pode mover da classe padrão para a de acesso infrequente depois de 60 dias.
Você pode mover para o Glacier para arquivamento depois de seis meses e você pode ter as ações de expiração, que é quando o S3 vai excluir os objetos. Então, o caso que eu dei de exemplo, os logs de acesso, pode ser configurado para exclusão, por exemplo, depois de seis meses, então a gente vai ver na prática como a gente cria, como a gente define essas regras de ciclo de vida do S3.