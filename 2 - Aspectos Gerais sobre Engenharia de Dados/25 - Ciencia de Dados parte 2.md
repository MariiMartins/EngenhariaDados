25. Ciência de Dados Parte II
Continuando então com machine learning, Agora a gente vai falar de agrupamentos.
Então, agrupamento é uma técnica conhecida como não supervisionada, porque? Porque não existe aqui um rótulo.
Lembro que a gente falou lá em classificação que, por exemplo, eu queria classificar os clientes como bons ou maus pagadores. Uma transação como fraudulenta ou não, a espécie de uma planta. 

Bom, quando eu estou agrupando, eu não tenho uma classe, eu não tenho um rótulo, Eu não tenho algo para classificar, na verdade, apenas quero agrupar elementos de acordo com um grau de semelhança e esse grau de semelhança, quem vai decidir, quem vai definir o algoritmo de agrupamento que eu estou usando.
Então, diferentes algoritmos podem criar grupos diferente, e o que geralmente o que vai acontecer.

Então imagine, por exemplo, que você tem acessos a uma rede, você tem acesso a uma rede e esses acessos à rede eles produzem diversos dados.Então, por exemplo, lá vai ter o IP, o tempo, a porta, o usuário, enfim, diversos acessos.
E você tem dados desse acesso, então, supondo que isso aqui sejam os acessos, você submete isso a um algoritmo de agrupamento e ele vai criar grupos de acordo com a equação, a fórmula matemática que ele utiliza.Então, vejam aqui os elementos aqui em verde, ele classificou como um grupo os em vermelho como o outro e os azuis e como o outro.

Existem algoritmos de agrupamento que podem não classificar alguns elementos que são esses aqui que eu deixei em branco e isso é chamado como ruído, ou seja, matematicamente não existe um agrupamento natural para esses elementos.

Existe outros algoritmos de agrupamento que vão agrupar todos. Então, como eu falei, o tipo de agrupamento depende muito do algoritmo.Depende bastante do algoritmo que está sendo utilizado.
Então, para que isso serve? Para que serve o agrupamento?
Bom para detectar, por exemplo, invasão de rede. Para segmentar clientes, você tem lá uma base de clientes.
Você quer criar campanhas direcionadas, você pode segmentar clientes, entre vários outros tipos de aplicação.

E, por fim, aqui a gente vai falar de regras de associação, falando ainda de machine learning. Então, regras de associação, busca associação entre itens. Então, o caso clássico é a cesta de compras. Cliente que comprou A, mas B também comprou C.
Então você já deve ter entrado em algum site de comércio eletrônico. Você coloca um produto na sua cesta de compras ali. No local do site aparece quem comprou esse produto também comprou este. Então, isto é um algoritmo de regras de associação.Então o algoritmo ele sabe já a partir de quem comprou um produto, um determinado produto que tem uma determinada probabilidade de ele comprar um outro produto também.
Ele sabe isso a partir de dados históricos.
Então, por exemplo, quem compra macarrão também compra molho branco. 
Qual é a ocorrência dessa transação em todas as transações? Isso é chamado de suporte.
E qual é a probabilidade delas ocorrerem junto?Ou seja, a compra do macarrão com molho branco com molho branco. Isso é chamado de confiança.

Suporte e confiança são o que a gente chama de métricas de regras de associação.
Por que existem essas métricas? Porque imagine, por exemplo, um supermercado. Todo produto que é comprado por um cliente, ele gera regras de associação. Então, em um grande mercado vão existir bilhões de regras de associação. Você precisa separar apenas as mais relevantes para separar as mais relevantes, Você precisa de métricas.
E as principais são essas. Aqui, o suporte e a confiança.
Então, o suporte, ele diz. Qualquer ocorrência dessas transações entre todas as transações, ou seja, são transações frequentes e a confiança e a ocorrência das duas juntas.
Então, a gente falou aqui que um exemplo clássico de aplicação de regras, a associação, é a cesta de compra, mas existem muitas outras aplicações.Por exemplo, você pode verificar que um determinado conjunto de sintomas estão associados a uma determinada doença ou não. Você cadastra lá os sintomas.
E o algoritmo ele vai procurar se isso está associado a alguma doença e vai mostrar o suporte e a confiança dessa associação.

O Machine Learning, como a gente falou, ele trata de algoritmos que usam dados. Para criar modelos e fazer previsões. Agora a gente vai começar a falar de algumas técnicas que não trabalham com dados, não necessariamente com dados históricos.

A primeira delas aqui é a Reinforcement Learning. A proposta dele é um método de tentativas com acertos e erros.
E esses acertos e erros eles recebem recompensas ou não, então os acertos são recompensados. Então a gente está falando de um agente de inteligência artificial que interage com o ambiente a fim de resolver um determinado problema.

Então aqui um exemplo bem simples o jogo é quente ou frio. Então você tem aqui, por exemplo, uma menina E aqui você tem uma casa em um dos quartos da casa, você tem um brinquedo. Então, através do aprendizado por reforço, essa menina tem que aprender o caminho para chegar até o urso. Cada sala da casa é chamado de Estado.
Então, o S1 O estado atual é o estado onde a menina se encontra, S2 é um novo estado. Ação e mudança. Então, ir de da sala três à sala cinco é a ação que faz a mudança de estado. E a gente tem o R, que é a recompensa.
Ou seja, se ela mudar desta sala para essa, a recompensa pode ser -1, porque aqui não agregou, não melhorou a performance dela, não trouxe ela mais próximo da solução do problema. Agora, supondo, por exemplo, que ela mude aqui do S2, que é aqui para o S1, ela pode ter uma recompensa que seja um, ou seja, ela fez uma ação que trouxe uma recompensa. Então, com esse processo de erros e acertos, o aprendizado para o reforço. Ele cria as chamadas políticas que as políticas dizem. O que a partir de um estado atual, qual que é  a melhor ação para um novo Estado.Então, por exemplo, depois que foi construído o modelo, você coloca lá, por exemplo, esses dois para política, a política. Ela vai dizer que para o S2 o melhor estado é S1. Antes, quando você não tinha ainda o modelo, não estava maduro, ele não tinha aprendido bastante. A política poderia ser, por exemplo, que do S2 o melhor seria ir para o S4.Então esse é o funcionamento básico do aprendizado por reforço.

Agora a gente entra em outra área que é chamada de busca e otimização.
Então existem problemas computacionais que não podemos resolver por uma equação ou uma fórmula. Precisa buscar uma solução entre todas as soluções possíveis e todas as soluções possíveis. É chamado ao que se conhece como espaço de busca.
Para muitos desses problemas, a gente falou que não existe uma equação ainda para muitos desses problemas. Se acredita que nunca vai existir tal equação. Tal fórmula para solucionar o problema. Então é que alguns exemplos de problemas de busca e otimização.
O primeiro que a gente está vendo aqui, que a gente tem o mapa, é o problema do caixeiro viajante. Então, não se trata apenas de encontrar a rota mais curta entre dois caminhos, mas achar o menor percurso, passando por vários pontos, sem repetir nenhum local. Então vejam aqui não se trata de você colocar os caminhos, as distâncias e as ligações. A gente tem aqui um grafo numa fórmula e ele vai achar a melhor, o melhor caminho. Não existe essa fórmula que você faça o input, a entrada desses dados e ele te traga o melhor caminho. Você vai ter que usar o algoritmo de busca e otimização.

Depois a gente tem jogos de tabuleiro. Que são, por exemplo, o jogo de xadrez. Nesses jogos, o espaço de busca e as opções do sua e do seu adversário são todas conhecidas. Diferente, por exemplo, de um jogo de carta que você não sabe quais são as cartas do seu adversário. Então, aqui também tem um problema de busca e otimização. Você tem que buscar o melhor caminho.
Depois que a gente tem os tescs, os caminhos. Aqui, o problema não é achar a rota mais curta, mas simplesmente achar um caminho. Esse tipo de problema é especialmente complexo porque fica difícil avaliar o progresso em outros problemas.
Então você pode até valer o progresso pela distância que você está desde o início. Só que você pode estar indo para um caminho sem saída, que a gente chama de louca óptima, que a gente vai falar mais adiante.

Depois a gente tem problemas de agendamento. Então esse é um problema clássico. Imagine, por exemplo, um comissário de voo. Você deve considerar as escalas o tempo máximo que o comissário pode trabalhar, as folgas, os tipos de linha que ela pode fazer, as rotas ou um determinado tipo de aeronave, ou se ela só pode fazer rotas domésticas, por exemplo, a cidade que ela mora, porque ela deve voltar para a cidade de origem, Férias, feriados.
Ou seja, ela não pode ser escalada em todos os feriados, nem todos os domingos. E você deve considerar também que ela pode ficar doente, que ela tem que ter uma reserva.

Depois, problemas lógicos e matemáticos diversos, desde equações simples até as mais complexas, podem, em alguns casos ser resolvidas através de problemas de busca e otimização, problemas de otimização de espaço, otimizar o arranjo de cargas, por exemplo, ou de peças publicitárias em uma em uma impressão.

Depois, otimização de equipamentos, obter alta eficiência, mas também obter consumo, disponibilidade, manutenção, impacto ambiental, entre outras. Quando a gente fala de busca e otimização, alguma coisa assim que geralmente o que se pergunta por que não se faz uma busca completa? Então eu tenho lá o espaço de busca, por exemplo, no xadrez. Por que eu busco todas as soluções possíveis e assim eu avalio qual que é melhor.
A questão é que, na maioria dos problemas, é impossível do ponto de vista de tempo e custo computacional.
Então, aqui eu vou dar um caso extremo.

O jogo GO tem um tabuleiro de 19 por 19. O espaço de busca dele, esse número gigantesco aqui, esse número é mais e maior do que o número de átomos do universo conhecido. Então, se você pegar todo o universo que nós conhecemos, o número de átomos não chega ao número de combinações do jogo. Então, como que você vai usar uma busca completa que é chamada a força bruta e impossível Nem que você tivesse. Quer dizer, mesmo que se você tivesse todo poder computacional do mundo, você ia levar alguns bilhões ou trilhões de anos para processar isso.Então, por isso que nem sempre é viável você buscar todas as soluções.

Se não é viável buscar todas as soluções, o que você faz? Você fica com um local óptima.
Então existe o global ótima, que é a solução melhor possível e o local ótima. Então, alguns algoritmos eles buscam uma solução nas proximidades. Então, por exemplo, falando do jogo Go, o AlphaGo, que é o programa do Google que ganhou lá o campeão mundial de Go, ele não fez uma busca. Ele não faz uma busca completa. A cada jogada, ele usa uma busca aproximada. Ele analisa algumas jogadas nas vizinhanças. 

Então, nessas vizinhanças, ele pode encontrar uma solução que localmente é melhor. Quanto menos a vizinhança estabelecida, ou seja, menor, mais rápido ele vai encontrar a menor, a melhor solução local. Não há garantia, obviamente, de que essa solução global louca, ótima seja a melhor solução global. Provavelmente não é, mas às vezes não precisa ser. Então, falando do caso do jogo GO, se a solução ótima local que foi encontrada pelo algoritmo do Google levou o computador a ganhar o jogo, quer dizer que ela foi suficiente?

Não é preciso sempre encontrar, encontrar a solução ótima, global.