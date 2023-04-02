26. Ciência de Dados Parte III

Então eu tinha falado de algoritmos, de técnicas de ciência, de dados que buscam imitar a natureza e a gente tem outro exemplo, que são os algoritmos genéticos.
Então, os algoritmos genéticos eles buscam imitar o processo da evolução das espécies proposto por Charles Darwin.
Eles são utilizados principalmente em problemas de busca e otimização. Ele é simplificado e limita o processo de evolução, porém ele é bastante eficiente. Então, todos aqueles problemas que a gente viu lá normalmente podem ser solucionados por algoritmos genéticos.

A diferença de um algoritmo genético para natureza é que, na natureza não existe uma condição de parada, um algoritmo genético.Ele vai ter alguma forma, algum mecanismo de parada. Ou seja, quando ele chega a um determinado valor ou um determinado número de interações ou até um determinado tempo, ele funciona com o processo de adaptação ou seja, a cada geração, quanto maior a adaptação dos descendentes, maior chance de ele ser escolhido para produzir a próxima geração e assim, aumentam as chances de sucesso. Da mesma forma que ocorre na natureza, na natureza, a evolução ela não funciona por quem vence o processo evolutivo não é o mais forte nem o mais bonito, mas sim aquele que se adapta melhor ao ambiente.

Aqui é a mesma coisa.
Como funcionam os algoritmos genéticos?
Então você tem um problema, um problema, por exemplo, que pode ser encontrar uma rota.
O que o algoritmo genético vai fazer?
Ele vai produzir uma primeira vez uma solução, algumas soluções aleatórias, essas soluções aleatórias é chamado de população, que é composto por conjuntos de cromossomos.
O que o algoritmo genético faz? Ele submete essa proposta a uma função de avaliação, que é a função fitness. E essa função de avaliação ela vai retornar um valor dessa avaliação.

O que essa avaliação? Por exemplo, que se o objetivo for encontrar a melhor rota, o algoritmo genético, lá ele propõe, por exemplo, quatro rotas. 

O que a função de avaliação vai fazer? Ela vai calcular a distância dessas rotas propostas. Então, supondo que na primeira solução a distância seja 50, na segunda, 40, na outra 45 e na outra 38. Então, obviamente que a esta que ela está mais adaptada, ela atende melhor o requisito do problema.

O que vai acontecer? Ccom essa solução o algoritmo genético vai avaliar se este valor é o ideal ou é o melhor.
Em alguns casos, a gente nunca vai saber se é o melhor possível, ou seja, se é o ótimo global, por exemplo a gente tem uma busca de uma rota complexa você nunca vai saber se a solução proposta é a melhor, talvez sempre seja possível melhorá-la

Como que você configura o algoritmo genético? Você configura a ele para um valor mínimo. Por exemplo, quando ele chegar em 35, ele parar ou ele tentar 1000 gerações ou ele processar, por exemplo, cinco minutos.
Você define algumas condições de parada ou, em alguns casos, você pode ter o valor, que é o valor ideal um caso, por exemplo, de um valor ideal e um quebra-cabeças. Você soluciona o quebra cabeças, você tem o valor ideal.

Bom, aí essa solução é proposta. O algoritmo genético ele avalia. Se ela é a melhor, o ideal ou acabou. O tempo termina. Se não, ele segue. E vai haver algumas técnicas aqui específicas de algoritmos genéticos.
O primeiro é cruzamento, então essas soluções propostas aqui, essas quatro soluções, elas vão ser misturadas nessa mistura há soluções que estão melhor adaptadas.
Por exemplo, aqui, 38 e 40. Eles têm mais chance de passar sua carga genética, entre aspas, para a próxima geração.
Então, há esse cruzamento que geram descendentes. Então, aqui esses cruzamentos vão gerar mais quatro descendentes. Pode ocorrer também um processo de mutação, que é um processo de mutação, processo de mutação e que alguma característica é alterada de forma aleatória.

É o terceiro processo que acontece aqui. É o chamado elitismo no elitismo, um elemento, uma solução mais bem adaptada e passada para a próxima geração sem cruzamento. Então eu posso aplicar elitismo, por exemplo, nessa solução aqui, que o resultado me deu 38. Eu passo ela sem cruzar ela. E com isso eu tenho uma nova geração com quatro novos descendentes. E aí o processo continua até acabar. Por o tempo por ser a melhor solução ou por acabar o número de interações e assim você consegue resolver diversos problemas típicos de otimização.

Agora a gente vai falar de um outro tipo de problema, que são os sistemas especialistas.
Sistemas especialistas são usados quando não existem dados. Por que não existe em dados? Porque pode ser um problema novo. Por exemplo, viagem a outro sistema solar, seguro de um novo tipo de veículo, quando o problema é sigiloso, por exemplo, uma ameaça terrorista ou uma fusão nuclear. 

Então, quando notei ausência de dados. O que você faz? Você consulta um especialista, ele cria uma base de conhecimento que é proposta, que é submetida a uma base de inferência que gera uma base de conhecimento.
Então, o sistema especialista vai emular a forma de pensar do sistema Especialista.
Então o que acontece? Sistemas especialistas são utilizados para reduzir a incerteza. Então, todos nós, todos os dias, somos submetidos a resolver tipos de problemas que resolvem incertezas. A gente não tem certeza da solução que a gente deve propor. Então, por exemplo, o que a gente está vendo é um Médico pensando qual é a dose de um determinado remédio que ele deve prescrever?
Então, algumas características dos especialistas, o especialista humano. Então, o especialista humano é o perito especialista no assunto. Ele não é um generalista, não é especialista. Ele se especializou através de estudo, treinamento e experiência. Ele tem capacidade de aprender e se aperfeiçoar e ele é capaz de reconhecer exceções.
Porém, alguns problemas aqui com especialistas, ele é raro. Ele é perecível, ele envelhece, ele morre, ele cansa.
Ele não pode trabalhar 24 horas. Ele não pode estar em toda parte. E ele geralmente custa caro.

E aí, então entram os sistemas especialistas. São sistemas de informação que buscam emular a capacidade de decisão de um perito humanos. Tentam simular as decisões que um perito humano e especialista no assunto vai tomar. 
Ele tem a aplicação limitada a uma área específica do conhecimento. Então não são sistemas generalistas, são sistemas bem especializados. Ele tem a capacidade de aprender e se aperfeiçoar, assim como um humano, e ele é heurístico, ou seja, não possui uma resposta pronta e exata. Ele busca uma aproximação.

Quais são as vantagens do sistema especialista?
Alta disponibilidade opera 24 horas, baixo custo e duração infinita. Ele não cansa. Ele não descansa, ele não envelhece. E ele é replicável. Ou seja, você pode copiar ele. Você pode replicar ele para diversos lugares.

Quais são as aplicações de sistemas especialistas?
Bom, aqui a gente tem alguns exemplos.
Diagnóstico médico. Diagnóstico de mau funcionamento de sistema ou equipamento. Agendamento decisões financeiras.Monitoramento de processos. Classificação segurança pública. Questões de segurança pública. Mudanças climáticas.

E agora que a gente vai falar de lógica difusa, a lógica difusa é utilizada para criar sistemas Especializam a técnica de criação de sistemas de tomada de decisão. Então, é uma metodologia de tomada de decisão e resolução de problemas que simula ou tenta emular o pensamento humano, a forma que o pensamento humano faz.
Então você tem uma entrada. Você tem um processamento lógico e uma saída.
A gente ouve falar bastante da lógica booleana. A lógica booleana, Ela é sim ou não é uma lógica binária. Ligado ou desligado.
Já a lógica difusa, em vez de assumir apenas zero um ligado ou desligado, ela vai poder qualquer ter qualquer valor real entre 0 e 1. Ou seja, é uma verdade parcial, então não vai ser uma decisão. É concreta, absoluta. Então, por exemplo, em vez de você classificar um problema como zero ou um sim ou não, você pode classificar como muito baixo, baixo, médio, alto, muito alto. Super lento, lento, rápido, muito rápido.

A lógica difusa. Você usa para criar sistemas especialistas que tomam decisões que são difusas, que não são lógicas,
que não são binárias. Então, aqui a gente tem uma comparação da lógica booleana ou ela é zero ou um.
É a lógica difusa que pode ter qualquer valor entre 0 e 1. É o que a gente chama de verdade parcial ou graus diferentes de pertinência.

Então, por exemplo, aqui, se a gente está falando de um copo.
A gente quer saber se o copo está cheio. Apenas uma forma de comparação.
Na lógica booleana, ele vai estar vazio e em determinado momento ele vai passar a estar cheio. Vai ter uma medida aqui, o que vai me dizer que de repente o copo está cheio.
Na lógica difusa, não.
Ele pode estar parcialmente vazio. Ele pode estar pela metade. Ele pode estar parcialmente cheio e ele pode estar ao mesmo tempo pela metade, parcialmente cheio, com diferentes graus de pertinência a cada uma dessas categorias.
Então, a lógica difusa é utilizada amplamente na inteligência artificial para criação de problemas e especialistas para tomada de decisão para a emulação do pensamento humano e para criar sistemas especialistas de tomada de decisão.

E, por fim, o último assunto que a gente vai falar, encerrando a nossa parte de ciência de dados e processamento de linguagem natural, que é uma área ampla e bastante complexa da área de ciência de dados, o processamento de linguagem natural. Ele trata da interpretação produção de linguagem humana pelo computador. 
Aqui, algumas aplicações : 
Tradução.
Respostas e perguntas.
Análise de Sentimentos.
Correção ortográfica.
CR.
Reconhecimento de fala.
Sintetização da fala.
Previsão de digitação.
Classificação de documentos.
Resumos.

Então existe aqui algumas aplicações que são mais fáceis. Por exemplo, sintetização de fala a gente encontra, por exemplo, em GPS. Existem outras que são mais complexas. O próprio reconhecimento de fala é uma atividade e uma aplicação de processamento de linguagem natural mais complexa. E tradução também, dependendo dos idiomas.
Também é uma atividade bastante complexa. Então, em uma área, o processamento é mais natural. É uma área muito ampla e com vasta aplicação na inteligência artificial.
 
