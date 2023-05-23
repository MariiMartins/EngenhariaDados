<!--
# 3. Fundamentos de Machine Learning

## 3.1 - [Ebook] Aprendizagem Humana x Aprendizagem de Máquina

~texto reescrito~
O processo de aprendizagem humana é responsável pela aquisição, compreensão e incorporação do conhecimento. Ele é caracterizado por transformações mentais que ocorrem em resposta a estímulos e experiências. Geralmente, esse processo envolve três fases distintas:
    - Aquisição: Durante essa fase, o indivíduo é exposto a novas informações ou estímulos, os quais são processados e armazenados na memória.
    - Retenção: Nessa fase, o foco está na manutenção das informações adquiridas. Isso inclui a capacidade de acessar essas informações quando necessário e evocá-las para uso futuro.
    - Recuperação: Essa etapa concentra-se na aplicação do conhecimento adquirido. Envolve a capacidade de utilizar o conhecimento em novas situações ou problemas, bem como adaptá-lo para se adequar a diferentes contextos.

Existem várias teorias e modelos que tentam explicar como o processo de aprendizagem ocorre, abrangendo abordagens cognitivas, neurobiológicas e comportamentais. Além disso, diferentes tipos de aprendizagem são reconhecidos, como aprendizagem declarativa, não declarativa, por condicionamento e por observação, entre outros.

Por outro lado, o processo de aprendizagem em inteligência artificial (IA) refere-se à forma como os algoritmos de IA são treinados para executar tarefas específicas. Normalmente, esses algoritmos são treinados usando conjuntos de dados extensos, chamados de conjuntos de treinamento, e seus parâmetros são ajustados para que possam realizar a tarefa desejada com maior precisão e eficiência.

Diversos tipos de aprendizagem em IA são empregados, como aprendizado supervisionado, não supervisionado e por reforço. Cada tipo de aprendizagem é utilizado para resolver problemas específicos e apresenta vantagens e desvantagens distintas.

Além disso, há outras formas de aprendizagem, como aprendizagem por transferência e aprendizagem profunda, que combinam diferentes abordagens e possuem aplicações específicas.

Em linhas gerais, o processo de aprendizagem em IA envolve as seguintes etapas:
    - Coleta e preparação dos dados.
    - Escolha do algoritmo e configuração dos parâmetros.
    - Treinamento do modelo utilizando os dados de treinamento.
    - Avaliação do modelo com dados de teste.
    - Ajuste do modelo e, se necessário, retreinamento.
    - Utilização do modelo para realizar previsões em novos dados.

## 3.2 - O que é Machine Learning?

O Aprendizado de Máquina, é um campo da ciencia da computação, que se concentra em criar sistemas, que sao capazes de aprender, a partir de um conjunto de dados, sem precisar de programação direta.

Pode ser aplicado em:
    - Reconhecimento de Voz
    - Análise de Sentimentos
    - Recomendação
    - Detecção de Fraudes
    - Previsões Empresariais

## 3.3 - Tipos de Aprendizado de Máquina

- Aprendizado Supervisionado
- Aprendizado Não-Supervisionado
- Aprendizado por Reforço
- Aprendizado Profundo

## 3.4 - [Ebook] O que é um Modelo de Machine Learning?

Aqui está a reescrita do texto:

Os modelos de aprendizado de máquina são algoritmos que examinam grandes volumes de dados em busca de padrões ou para realizar previsões. Como baseados em dados, esses modelos são os componentes matemáticos essenciais da inteligência artificial.
Por exemplo, um modelo de aprendizado de máquina para visão computacional pode identificar carros e pedestres em tempo real a partir de vídeos. Da mesma forma, um modelo de aprendizado de máquina para processamento de linguagem natural pode traduzir palavras e frases.
Esses modelos representam matematicamente objetos e suas relações. Esses objetos podem variar desde "curtidas" em uma postagem de rede social até moléculas em um experimento de laboratório.
Portanto, não há limites para o uso da inteligência, as possibilidades são infinitas.
Cientistas de dados e engenheiros de IA criam inúmeros modelos de aprendizado de máquina para diversas finalidades.
    A tecnologia está em constante evolução.

## 3.5 - [Ebook] Processo de Aprendizagem em Machine Learning

No processo de aprendizagem em machine learning, um modelo é exposto a um conjunto de dados de treinamento e aprende a fazer previsões precisas sobre novos dados. Esse aprendizado é alcançado através do ajuste dos parâmetros do modelo usando algoritmos de otimização, com base na avaliação da acurácia das previsões feitas sobre o conjunto de treinamento.

Esse ajuste dos parâmetros do modelo por meio de algoritmos de otimização ocorre em dois passos principais. O primeiro passo é definir uma função de perda (ou erro), que mede a diferença entre as previsões feitas pelo modelo e os valores reais para cada exemplo no conjunto de treinamento.

Em seguida, a otimização da função de perda é realizada para encontrar os valores dos parâmetros que minimizam essa função. Isso é feito utilizando algoritmos de otimização, como o gradiente descendente, conjunto quasi-Newton, entre outros. Durante a otimização, o algoritmo itera sobre os parâmetros, atualizando-os com base na derivada da função de perda em relação a cada parâmetro. O processo de otimização é encerrado quando a função de perda atinge um mínimo ou quando o número máximo de iterações é alcançado. Ao final desse processo, os parâmetros do modelo são ajustados para minimizar a perda ou erro sobre o conjunto de treinamento.

O objetivo é encontrar a combinação ideal de parâmetros que minimize a perda ou erro entre as previsões e os valores reais. Uma vez treinado, o modelo pode ser utilizado para fazer previsões sobre novos dados, aplicando o conhecimento adquirido durante o processo de aprendizagem.

## 3.6 - [Ebook] O que é Treinamento em Inteligência Artificial?

O treinamento, validação e teste são etapas fundamentais no desenvolvimento de modelos de inteligência artificial.

O treinamento é o processo pelo qual o modelo aprende os parâmetros necessários para fazer previsões precisas a partir de um conjunto de dados de treinamento. Durante o treinamento, os parâmetros do modelo são ajustados de forma iterativa com base nas entradas e saídas dos dados de treinamento. O objetivo é otimizar o desempenho do modelo para que ele possa fazer previsões acuradas.

Os dados de treinamento são compostos por exemplos que são utilizados para ensinar o modelo a fazer previsões corretas. Eles consistem em entradas, que são as características dos exemplos, e saídas, que são os valores que o modelo deve prever. Por exemplo, se o objetivo do modelo for prever se uma pessoa tem diabetes, as entradas podem ser idade, peso, pressão arterial e níveis de açúcar no sangue, e a saída seria uma previsão de diagnóstico.

Os dados de treinamento podem ser rotulados ou não rotulados. Dados de treinamento rotulados são usados no aprendizado supervisionado, onde o modelo aprende a associar características específicas aos rótulos correspondentes. Isso permite que o modelo classifique novos dados com base nas características aprendidas. Por outro lado, dados de treinamento não rotulados são utilizados no aprendizado não supervisionado, onde o modelo procura por padrões ou similaridades nos dados sem a presença de rótulos pré-definidos.

Além do treinamento, é importante realizar a validação do modelo. Isso envolve o uso de um conjunto de dados separado, chamado conjunto de validação, para avaliar o desempenho do modelo durante o treinamento. A validação ajuda a verificar se o modelo está generalizando bem para dados não vistos anteriormente e auxilia na seleção dos melhores hiperparâmetros e configurações do modelo.

Após o treinamento e validação, o modelo passa pela fase de teste. Nessa etapa, ele é avaliado usando um conjunto de dados de teste, que é separado dos conjuntos de treinamento e validação. O conjunto de teste fornece uma avaliação final do desempenho do modelo em dados completamente novos. Essa etapa é importante para garantir que o modelo seja capaz de fazer previsões precisas em situações reais.

O processo de treinamento, validação e teste é iterativo, e pode envolver ajustes adicionais no modelo, como a seleção de diferentes algoritmos ou a modificação de parâmetros, com o objetivo de melhorar o desempenho do modelo.

Em resumo, o treinamento, validação e teste são etapas cruciais no desenvolvimento de modelos de inteligência artificial, permitindo que o modelo aprenda a fazer previsões precisas a partir de dados de treinamento, seja avaliado quanto ao seu desempenho e seja testado em dados não vistos anteriormente. Essas etapas garantem que o modelo seja confiável e capaz de lidar com diferentes situações da vida real.

## 3.7 - [Ebook] O que é Validação em Inteligência Artificial?

A validação é o processo de avaliar o desempenho do modelo com novos dados que não foram utilizados durante o treinamento. Esse processo auxilia na identificação do overfitting, que ocorre quando o modelo "memoriza" os dados de treinamento, mas não consegue generalizar para novos casos.

Os dados de validação geralmente possuem entradas e saídas semelhantes aos dados de treinamento. A diferença é que esses dados nunca foram utilizados durante o treinamento, o que os torna uma medida da capacidade do modelo de generalização para novos casos.

Esses dados de validação são utilizados para selecionar os melhores hiperparâmetros do modelo e identificar possíveis casos de overfitting.

Quando se dispõe de uma quantidade limitada de dados, pode-se utilizar uma técnica chamada validação cruzada para estimar o desempenho do modelo. Nesse método, os dados de treinamento são aleatoriamente divididos em vários subconjuntos, reservando um deles para avaliação.

É comum as pessoas usarem os termos "dados de teste" e "dados de validação" de forma intercambiável. No entanto, a principal diferença entre eles é que os dados de validação são usados durante o treinamento para validar o modelo, enquanto o conjunto de dados de teste é usado para avaliar o modelo após o treinamento ser concluído.

O conjunto de dados de validação fornece ao modelo a primeira exposição a dados não vistos previamente. No entanto, nem todos os cientistas de dados realizam essa etapa de validação inicial. Alguns pulam diretamente para o uso dos dados de teste. No entanto, essa prática não é recomendada.

Em geral, os dados de validação são utilizados para auxiliar na seleção da melhor configuração do modelo, antes de usar os dados de teste para avaliar o desempenho final do modelo.

## 3.8 - [Ebook] O que é Teste em Inteligência Artificial?

O teste é o processo de avaliar o desempenho do modelo usando um conjunto de dados que ainda não foi visto, a fim de medir sua performance final. Essa etapa é importante para verificar se o modelo é capaz de generalizar para dados desconhecidos.

Os dados de teste geralmente contêm entradas e saídas semelhantes aos dados de treinamento e validação. A diferença é que esses dados nunca foram utilizados durante o treinamento ou validação, permitindo assim uma avaliação precisa do desempenho final do modelo.

Os dados de teste são usados para avaliar a precisão do modelo, sua capacidade de generalização para novos casos e também para comparar o desempenho do modelo com outros modelos.

É fundamental que os dados de teste representem o conjunto de dados real e sejam suficientemente grandes para gerar previsões significativas.

Na área de ciência de dados, é comum dividir os dados em 80% para treinamento e 20% para teste.

Essa etapa é a última antes de implantar o modelo em produção, e é crucial ter um conjunto de dados de teste que seja representativo do conjunto de dados que será utilizado para tomar decisões.

## 3.9 - O que é Classificação?

## 3.10 - O que é Regressão?

## 3.11 - [Ebook] O que é Overfitting?

Overfitting é um conceito da ciência de dados que ocorre quando um modelo estatístico se ajusta exatamente aos seus dados de treinamento. Quando isso acontece, o algoritmo infelizmente não consegue ter um desempenho preciso em dados não vistos, anulando sua finalidade.

A capacidade de um modelo de generalizar para novos dados é o que nos permite usar algoritmos de aprendizado de máquina todos os dias para fazer previsões e classificar dados.

Quando os algoritmos de aprendizado de máquina são criados, eles aproveitam um conjunto de dados de amostra para treinar o modelo.

Entretanto, quando o modelo é treinado por muito tempo com os dados de amostra ou quando o modelo é excessivamente complexo, ele pode começar a aprender o "ruído" ou informações irrelevantes dentro do conjunto de dados.

Quando o modelo memoriza o ruído e se ajusta muito bem ao conjunto de treinamento, ele se torna "superajustado" e não consegue generalizar bem para novos dados.

Se um modelo não puder se generalizar bem para novos dados, ele não conseguirá executar as tarefas de classificação ou previsão para as quais foi projetado.

Baixas taxas de erro e alta variação são bons indicadores de sobreajuste. Para evitar esse comportamento, uma parte do conjunto de dados de treinamento é normalmente reservada como o "conjunto de teste" para verificar o excesso de ajuste.

Se os dados de treinamento tiverem uma taxa de erro baixa e os dados de teste tiverem uma taxa de erro alta, isso indica um ajuste excessivo.

## 3.12 - [Ebook] Como detectar e evitar Overfitting?

Para avaliar a adequação dos modelos de aprendizado de máquina, é importante realizar testes de precisão. Uma das técnicas mais populares para avaliar a precisão do modelo é a validação cruzada k-fold.

Na validação cruzada k-fold, os dados são divididos em k subconjuntos de tamanho igual, chamados de "dobras". Uma das k dobras é usada como conjunto de teste ou validação, enquanto as dobras restantes são usadas para treinar o modelo.

Esse processo é repetido até que cada dobra tenha atuado como conjunto de teste. Após cada iteração, uma pontuação é registrada e, ao final, é calculada a média das pontuações para avaliar o desempenho geral do modelo.

Embora o uso de modelos lineares ajude a evitar o overfitting, muitos problemas do mundo real são não lineares. Além de compreender como detectar o overfitting, é importante também saber como evitá-lo.

Abaixo estão algumas técnicas que podem ser utilizadas para evitar o overfitting:

    1. Parada Antecipada: Interromper o treinamento antes que o modelo comece a aprender o ruído presente nos dados. No entanto, é preciso encontrar o equilíbrio ideal entre underfitting e overfitting.

    2. Treinar com Mais Dados: Aumentar o conjunto de treinamento, incluindo mais dados, pode aumentar a precisão do modelo, desde que os dados sejam limpos e relevantes. No entanto, adicionar mais complexidade ao modelo sem dados adequados pode levar ao overfitting.

    3. Aumentar os Dados: Em alguns casos, adicionar dados ruidosos pode tornar o modelo mais estável, mas é importante fazê-lo com cuidado.

    4. Seleção de Recursos: Identificar os recursos mais importantes nos dados de treinamento e eliminar os irrelevantes ou redundantes. Isso ajuda a simplificar o modelo e identificar a tendência dominante nos dados.

    5. Regularização: Aplicar uma "penalidade" aos parâmetros de entrada com coeficientes maiores para limitar a variação do modelo. Métodos de regularização, como L1 regularization, Lasso regularization e dropout, ajudam a reduzir o ruído nos dados.

    6. Utilizar Métodos Ensemble: Utilizar um conjunto de classificadores, como árvores de decisão, e combinar suas previsões para obter o resultado mais comum. Métodos ensemble, como bagging e boosting, são amplamente utilizados para reduzir a variação em conjuntos de dados ruidosos.

Ao aplicar essas técnicas, é possível evitar o overfitting e melhorar a capacidade de generalização dos modelos de aprendizado de máquina.

## 3.13 - [Ebook] O que é Underfitting?

Underfitting é uma situação em ciência de dados na qual um modelo não consegue capturar adequadamente a relação entre as variáveis de entrada e saída, resultando em uma alta taxa de erro tanto nos dados de treinamento quanto em dados não vistos.

Isso geralmente ocorre quando o modelo é muito simples e não possui capacidade suficiente para representar a complexidade dos dados. Pode ser resultado de um treinamento insuficiente, falta de recursos de entrada relevantes ou falta de regularização adequada. Assim como o overfitting, o underfitting compromete a capacidade de generalização do modelo, levando a erros de treinamento e desempenho insatisfatório.

Se um modelo não for capaz de generalizar bem para novos dados, ele não poderá ser utilizado com eficácia para tarefas de classificação ou previsão. A capacidade de generalização é essencial para aproveitar algoritmos de aprendizado de máquina e realizar análises precisas em dados desconhecidos.

Altos viés e baixa variância são indicadores típicos de underfitting. Como esse comportamento pode ser observado durante o treinamento com o conjunto de dados, modelos subajustados geralmente são mais fáceis de identificar do que os superajustados.

O underfitting ocorre quando um modelo de aprendizado de máquina não é suficientemente complexo para capturar a relação presente nos dados de treinamento. Isso pode acontecer quando o modelo é muito simples ou quando os recursos de entrada não são relevantes para a saída desejada. Para resolver o underfitting, é necessário aumentar a complexidade do modelo ou adicionar recursos relevantes para melhor representar a relação nos dados.

## 3.14 - [Ebook] Como evitar Underfitting?

Para detectar o underfitting com base no conjunto de treinamento e evitar o subajuste, podemos utilizar algumas técnicas. Aqui estão três abordagens que podem ser aplicadas:

Aumentar a complexidade do modelo:
Se o modelo é muito simples e não consegue capturar a relação dominante nos dados de treinamento, é necessário aumentar sua complexidade. Isso pode envolver adicionar mais camadas em uma rede neural, aumentar o número de neurônios ocultos, aumentar o número de árvores em um algoritmo de floresta aleatória, ou escolher um modelo mais sofisticado que seja capaz de lidar com a complexidade dos dados. Aumentar a complexidade do modelo permite capturar relações mais sutis entre as variáveis de entrada e saída, melhorando o desempenho e reduzindo o underfitting.

Coletar mais dados relevantes:
Se o conjunto de treinamento é insuficiente em termos de quantidade ou diversidade de dados, o modelo pode ter dificuldade em aprender as relações presentes nos dados. Coletar mais dados relevantes pode ajudar a melhorar a capacidade de generalização do modelo. No entanto, é importante garantir que os dados adicionais sejam limpos e representativos do problema em questão. A adição de dados ruidosos ou irrelevantes pode levar ao overfitting, então é necessário ter cuidado ao aumentar o conjunto de treinamento.

Ajustar os hiperparâmetros do modelo:
Os hiperparâmetros são configurações ajustáveis que afetam o desempenho e a complexidade do modelo. Ao ajustar adequadamente os hiperparâmetros, é possível encontrar um equilíbrio entre um modelo muito simples e um modelo excessivamente complexo. Por exemplo, na regularização, pode-se experimentar diferentes valores para o coeficiente de penalidade ou usar diferentes métodos de regularização (L1, L2, etc.). Além disso, é importante realizar uma busca sistemática pelos melhores hiperparâmetros por meio de técnicas como a validação cruzada para obter resultados mais confiáveis.

Ao aplicar essas técnicas, é possível reduzir o underfitting e melhorar a capacidade do modelo de capturar a relação entre as variáveis de entrada e saída, resultando em previsões mais precisas. No entanto, é importante encontrar o equilíbrio certo, pois um modelo muito complexo pode levar ao overfitting, comprometendo a capacidade de generalização.

## [3.15 - Quiz](link)
