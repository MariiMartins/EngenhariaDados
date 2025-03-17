<<<<<<< HEAD
<<<<<<< HEAD
133. Exemplo de Machine Learning
Vamos então agora ao nosso próximo exemplo que o exemplo de machine learning especificamente a gente vai criar um projeto de regressão e a gente vai utilizar o mesmo arquivo.

A gente vai ver que utilizar usar a machine learning com o Spark é bem intuitivo. Existem algumas diferenças do ponto de vista de arquitetura, mas é bem intuitivo.
A gente vai utilizar uma outra consideração, vamos utilizar bibliotecas nativas do Spark para criar os nossos modelos, para fazer previsão.

Mas, como eu mencionei ao longo dessa seção, como editá lo utilizando Python? 
Voce pode, inclusive, utilizar outras bibliotecas do Python, como por exemplo, pandas, mas aqui a gente vai utilizar bibliotecas nativas do Spark de machine learning.

Então a gente vai avaliar a performance até o final usando RMS.

A gente vai criar o nosso modelo utilizando apenas três variáveis independentes, de uma variável dependente. Isso você pode pensar para o que a gente está fazendo isso por várias razões. Primeiro, porque essas são as melhores variáveis para prever. Bom, então aqui a gente entra numa função de transformação de dados, que é o vector assembler. Até então, o que o vector assembler faz é uma virtualização das colunas. O que isso quer dizer?

Bom, a gente viu aqui que as nossas variáveis independentes são consumo, cilindros e cilindradas. Quando a gente for criar o modelo, o algoritmo que vai criar esse modelo, ele espera que todos os atributos estejam em uma única coluna. Então é isso que o vetor assembler faz, que é uma característica aqui das técnicas de machine learning com o Spark.

A próxima etapa que a gente como a gente vai treinar o modelo e depois a gente vai testar. Precisa dividir os nossos dados em treino e teste. E o Spark aqui tem o método Random Split, que é semelhante ao que a gente viu lá com R, com o Python, que vai fazer a divisão dos dados em treino e teste.
Então eu estou dizendo aqui que uma proporção de 70% para treino, 30% para teste. Ele vai fazer esse split aqui. Vai colocar 70% no objeto, carros treino e 30% no objeto carros teste. 
Depois a gente vai imprimir uma contagem.
Para a gente verificar quantos registros ficaram em cada um desses objetos, então eu vou executar.

Bom, então eu tenho meus dados divididos entre teste, agora eu posso criar o meu modelo de regressão linear. Existem vários parâmetros aqui que a gente vai deixar com o valor default. Mas os dois parâmetros principais que eu preciso é dizer para o objeto linear o ingresso que eu estou criando e qual o que a coluna que tem as características e qual é o que a coluna que tenho levou à classe. Então, veja, nós criamos aqui uma coluna características que tem um vetor das características.
=======
133. Exemplo de Machine Learning
Vamos então agora ao nosso próximo exemplo que o exemplo de machine learning especificamente a gente vai criar um projeto de regressão e a gente vai utilizar o mesmo arquivo.

A gente vai ver que utilizar usar a machine learning com o Spark é bem intuitivo. Existem algumas diferenças do ponto de vista de arquitetura, mas é bem intuitivo.
A gente vai utilizar uma outra consideração, vamos utilizar bibliotecas nativas do Spark para criar os nossos modelos, para fazer previsão.

Mas, como eu mencionei ao longo dessa seção, como editá lo utilizando Python? 
Voce pode, inclusive, utilizar outras bibliotecas do Python, como por exemplo, pandas, mas aqui a gente vai utilizar bibliotecas nativas do Spark de machine learning.

Então a gente vai avaliar a performance até o final usando RMS.

A gente vai criar o nosso modelo utilizando apenas três variáveis independentes, de uma variável dependente. Isso você pode pensar para o que a gente está fazendo isso por várias razões. Primeiro, porque essas são as melhores variáveis para prever. Bom, então aqui a gente entra numa função de transformação de dados, que é o vector assembler. Até então, o que o vector assembler faz é uma virtualização das colunas. O que isso quer dizer?

Bom, a gente viu aqui que as nossas variáveis independentes são consumo, cilindros e cilindradas. Quando a gente for criar o modelo, o algoritmo que vai criar esse modelo, ele espera que todos os atributos estejam em uma única coluna. Então é isso que o vetor assembler faz, que é uma característica aqui das técnicas de machine learning com o Spark.

A próxima etapa que a gente como a gente vai treinar o modelo e depois a gente vai testar. Precisa dividir os nossos dados em treino e teste. E o Spark aqui tem o método Random Split, que é semelhante ao que a gente viu lá com R, com o Python, que vai fazer a divisão dos dados em treino e teste.
Então eu estou dizendo aqui que uma proporção de 70% para treino, 30% para teste. Ele vai fazer esse split aqui. Vai colocar 70% no objeto, carros treino e 30% no objeto carros teste. 
Depois a gente vai imprimir uma contagem.
Para a gente verificar quantos registros ficaram em cada um desses objetos, então eu vou executar.

Bom, então eu tenho meus dados divididos entre teste, agora eu posso criar o meu modelo de regressão linear. Existem vários parâmetros aqui que a gente vai deixar com o valor default. Mas os dois parâmetros principais que eu preciso é dizer para o objeto linear o ingresso que eu estou criando e qual o que a coluna que tem as características e qual é o que a coluna que tenho levou à classe. Então, veja, nós criamos aqui uma coluna características que tem um vetor das características.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
=======
133. Exemplo de Machine Learning
Vamos então agora ao nosso próximo exemplo que o exemplo de machine learning especificamente a gente vai criar um projeto de regressão e a gente vai utilizar o mesmo arquivo.

A gente vai ver que utilizar usar a machine learning com o Spark é bem intuitivo. Existem algumas diferenças do ponto de vista de arquitetura, mas é bem intuitivo.
A gente vai utilizar uma outra consideração, vamos utilizar bibliotecas nativas do Spark para criar os nossos modelos, para fazer previsão.

Mas, como eu mencionei ao longo dessa seção, como editá lo utilizando Python? 
Voce pode, inclusive, utilizar outras bibliotecas do Python, como por exemplo, pandas, mas aqui a gente vai utilizar bibliotecas nativas do Spark de machine learning.

Então a gente vai avaliar a performance até o final usando RMS.

A gente vai criar o nosso modelo utilizando apenas três variáveis independentes, de uma variável dependente. Isso você pode pensar para o que a gente está fazendo isso por várias razões. Primeiro, porque essas são as melhores variáveis para prever. Bom, então aqui a gente entra numa função de transformação de dados, que é o vector assembler. Até então, o que o vector assembler faz é uma virtualização das colunas. O que isso quer dizer?

Bom, a gente viu aqui que as nossas variáveis independentes são consumo, cilindros e cilindradas. Quando a gente for criar o modelo, o algoritmo que vai criar esse modelo, ele espera que todos os atributos estejam em uma única coluna. Então é isso que o vetor assembler faz, que é uma característica aqui das técnicas de machine learning com o Spark.

A próxima etapa que a gente como a gente vai treinar o modelo e depois a gente vai testar. Precisa dividir os nossos dados em treino e teste. E o Spark aqui tem o método Random Split, que é semelhante ao que a gente viu lá com R, com o Python, que vai fazer a divisão dos dados em treino e teste.
Então eu estou dizendo aqui que uma proporção de 70% para treino, 30% para teste. Ele vai fazer esse split aqui. Vai colocar 70% no objeto, carros treino e 30% no objeto carros teste. 
Depois a gente vai imprimir uma contagem.
Para a gente verificar quantos registros ficaram em cada um desses objetos, então eu vou executar.

Bom, então eu tenho meus dados divididos entre teste, agora eu posso criar o meu modelo de regressão linear. Existem vários parâmetros aqui que a gente vai deixar com o valor default. Mas os dois parâmetros principais que eu preciso é dizer para o objeto linear o ingresso que eu estou criando e qual o que a coluna que tem as características e qual é o que a coluna que tenho levou à classe. Então, veja, nós criamos aqui uma coluna características que tem um vetor das características.
>>>>>>> d9f734c334f4b5e550e5383e11b878ea9d28d555
