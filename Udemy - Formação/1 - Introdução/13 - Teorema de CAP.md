13. Teorema de CAP

Quando a gente fala de sistemas distribuídos, uma questão importante é o teorema de CAP (Cap Theorem).
E ele é usado no design.Ele é usado em consideração quando a gente faz o design de sistemas distribuídos, que normalmente são sistemas de big data. São sistemas distribuídos.

Então é importantíssimo. Teorema Talvez o mais importante quando a gente fala de engenharia de dados.
Ele foi proposto pelo cientista Eric Brewer no final dos anos 90, mas ele se popularizou já na década seguinte.

Então o que o teorema diz então com relação a três aspectos consistência, disponibilidade e Partição tolerante a falhas, é impossível ter mais de dois, ou seja, você vai ter que escolher dois desses elementos.
Então, um sistema de dados distribuído só pode garantir duas de três propriedades.
•	Consistência que é que todos os nós da rede retornem a mesma versão dos dados.
•	Disponibilidade: Todos os nós respondam a leituras escritas em um tempo razoável
•	Partição tolerante à falhas: o sistema continua a funcionar, mesmo tendo perdido os dados entre os nós (na comunicação entre os nós.)
Então aqui vamos falar um pouquinho de consistência, né? Então todos os nós na rede retornam a mesma versão dos dados. Então, imagine o seguinte um cliente ele enviou uma transação, por exemplo, ele fez uma insert, uma inserção e um nó. Um determinado nó que o servidor estava a chamar recebe essa informação depois de um tempo razoável. Se um cliente, o mesmo cliente ou um outro cliente ele solicitar essa mesma informação, esse mesmo dado, ele tem que receber a mesma versão. Então, por exemplo, se for o caso, uma atualização ele depois de um tempo razoável. E esta informação tem que estar consistente entre todos os nós do cluster, de forma que se um cliente solicitar essa mesma informação, ele receba a mesma versão. Então, é um conceito que nós já conhecíamos de consistência.

O outro conceito de disponibilidade, o que quer dizer isso? Que todos os nós respondem a leituras e escritas em tempo razoável. Então você faz uma solicitação ao cliente, ele faz uma solicitação de uma informação a um nó e ele recebe um retorno dessa leitura, por exemplo, em um tempo razoável, em um tempo aceitável.

E tolerâncias a falhas em partição. Então, o sistema tem que ser capaz de funcionar corretamente, mesmo que ocorram falhas arbitrárias na rede. E, eventualmente, embora sejam eventos raros, falhas em partições em redes.
Eventualmente, elas vão ocorrer e o sistema na ocorrência dessas falhas nas partições na rede. Ele tem que ser capaz de funcionar corretamente.
Então aqui a gente tem as categorias de sistemas que cada uma dessas categorias atende dois dos requisitos, já que, segundo o teorema, não é possível atender os três.
Então, a gente tem sistemas que são aqui com a sigla CP (Eles têm a consistência e são tolerantes à partição).
Então aqui eles vão ter um menor atendimento no requisito de disponibilidade.
Depois, a categoria CA que é consistente e disponível disponibilidade (Então eles vão ter consistência e disponibilidade, mas eles vão ter menos tolerância a uma falha na partição ou uma falha e algum mal do cluster).
E o AP (Ele tem disponibilidade e tolerância à partição, mas ele não pode garantir a tolerância)

Então o que acontece? A forma correta de se pensar o teorema CAP é a seguinte.
Em caso de falhas de partição que, como eu falei, é um evento raro, mas que eventualmente vai acontecer e que é uma rede com muitos nós. A probabilidade de acontecer ela é alta.
Então, em casos de falha de partição, você deve escolher entre dois elementos consistência e disponibilidade. Então, essa é a decisão que deve ser tomada quando se desenvolve em sistemas distribuídos sistemas orientados a dados distribuídos.
Então, qual e qual é a escolha em caso de falha de partição? A escolha é entre a consistência, ou seja, o sistema retorna um erro, mas não fornece informações inconsistentes. Ou disponibilidade o sistema sempre retorna à consulta, mesmo que não haja garantia de que a informação seja consistente.

Então, vejam que é um trade off, é uma troca ou uma escolha que tem que ser feita.
Então, por exemplo, um sistema consistente.
Quer dizer que se houver um erro Ele não retorna dados inconsistentes. Ele vai dizer que houve um erro na rede e que ele não conseguiu recuperar informações.
Já é um sistema que privilegia a disponibilidade em vez da consistência. O sistema ele sempre vai retornar um valor em caso de uma falha no cluster, na partição.Mesmo que não haja garantia de que a informação seja consistente.

Então pense o seguinte um sistema financeiro o que você prefere quando se você for fazer o design de sistema financeiro, que ele seja consistente ou que ele tenha disponibilidade.
Bom, se ele tiver consistência, por exemplo, você fez uma transação.Houve um problema. Ele vai retornar porque ele não pode recuperar o valor da transação.
Agora, se a gente escolher a disponibilidade para o sistema financeiro, o que vai acontecer? Ele vai retornar, por exemplo, saldo anterior. Ele vai retornar uma informação inconsistente.
Então, obviamente que para um sistema financeiro, a consistência é mais importante do que a disponibilidade.
Agora vamos pensar um outro tipo de sistema, um sistema de busca  e vamos pensar o seguinte há um problema na rede É um problema de partição, uma falha de partição Se eu escolher consistência, quando feito busca o sistema, retorna um erro dizendo que não foi possível retornar o resultado da busca, o que ele não conseguiu acessar lá os dados indexados. Se eu escolho disponibilidade, ele vai retornar a um resultado para busca porém, pode ser os dados não mais atualizados.
Bom, para um sistema de busca, é mais importante eu ter um resultado, mesmo que ele não seja o último atualizado, do que não ter resultado nenhum.
Então, o sistema de busca eu vou escolher disponibilidade.
Por exemplo, se eu estou pesquisando, qual o que é, por exemplo, o endereço de uma determinada loja que eu quero visitar? É bem provável que o endereço não foi alterado.Desde que ocorreu a falha, muito improvável que houve uma nova indexação dos dados e mesmo que houve, mesmo que tenha ocorrido uma nova indexação dos dados, não quer dizer que o endereço mudou.
Então é muito melhor eu ter a última informação possível do que simplesmente me retornar uma mensagem de erro.
Então, é dessa forma que o teorema diz que tem que ser analisado.
A escolha em caso de partição. E se eu quero um sistema que privilegia a consistência do que disponibilidade.
Vejam que não quer dizer que essa escolha vai dizer que significa que o sistema não vai ter consistência nenhuma ou não vai ter disponibilidade nenhuma. A escolha aqui é o que o sistema vai privilegiar, o que vai ser mais importante para o sistema, a consistência, ou seja, retornar apenas dados consistentes, dados sempre íntegros e a disponibilidade. Ou seja, mesmo que os dados não estejam íntegros, eu vou retornar para o cliente algum valor.
Então, assim a gente teve um entendimento geral do teorema de CAP.