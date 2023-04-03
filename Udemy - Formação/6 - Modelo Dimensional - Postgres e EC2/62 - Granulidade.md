- 62. Granulidade
Na sessão passada, quando a gente falava de sistemas transacionais, nós estávamos falando de transações de informação que vinha detalhada operação por operação.

Nesta sessão nós estamos tratando de informações gerenciais e quando a gente fala de informação gerencial, uma questão é super importante. Normalmente, informação gerencial não precisa vir no detalhe, então, lembrando lá o caso de vendas, um gerente não tem que saber venda a venda, isso não é um tipo de informação que apoie a decisão.

Então, nesta aula a gente vai falar de granulidade,  a granulidade ela diz o nível de detalhe da informação do ponto de vista gerencial, então a informação não precisa vir detalhada, do ponto de vista de transação, de operação sim.

Então, quando você precisa ver informação em detalhe, o que você vai fazer? Você vai provavelmente consultar um relatório e o tipo de informação que serve para conferência e vem lá diretamente do sistema transacional não vem do banco de dados analítico do banco de dados dimensional.
Então, a granulidade o nível de detalhe que você vai fornecer informação para o gerente que você vai carregar no seu sistema de informação gerencial?
É uma informação importantíssima para o projeto. Porque?Porque vai impactar em infraestrutura, em tempo de carga, no design do projeto, e a gente também deve lembrar que o mesmo fato, uma mesma informação gerencial, pode atender áreas diferentes. Se você usar o grão errado, o nível de detalhe errado, pode ser que você precise refazer o fato ou até criar.

Com relação a granulidade também é preciso lembrar que ela tem que ter o nível necessário para apoiar a decisão. Então, não adianta ter informação muito resumida. Eu vou mostrar apenas a venda pelo país. Então, hoje, no país inteiro, se vender o X, essa informação também, ela pode não ajudar em nada.
Talvez você tenha que descer o grão um pouco mais, mostrar o nível de estado de produto, de vendedor.

Então aqui um exemplo vendas vou fornecer um relatório gerencial para um gestor nesse nível. Aqui isso não tem valor e essa informação não tem valor gerencial, não serve para nada, é uma informação operacional para conferência, por exemplo.
Agora, se eu carrego no meu armazém de dados informações consolidadas, eu mudo o grão dela. Eu tenho, então, informações gerenciais aqui, os dados são carregados, consolidados, resumidos. Esse resumo ele ocorre durante o processo de carga e transformação de dados.

Então, eu vejo aqui que a gente tem grãos diferentes.
Aqui eu carreguei a informação consolidada por estado, eu resumi a informação por estado. Aqui eu tenho um nível de grão mais baixo, estou vendo por cidade, então, por exemplo, eu vejo a informação por estado. Eu acesso normalmente a operação por estado. Eu clico aqui em determinado estado, por exemplo, ao Rio Grande do Sul, que é esta área aqui e ele me desce o nível do grão. Ele me traz informações mais detalhadas, uma operação que a gente chama de grudar ou detalhar informação. Eu poderia ter carregado meu armazém de dados sobre esse nível de informação por estado. A informação mais resumida, um grão maior ou eu poderia ter carregado a informação com o grão mais detalhado até nível de cidade.
Eu poderia, por exemplo, descer até nível de bairro, por exemplo, ou de filial.

Então essa é uma informação que deve ser definida na construção da modelagem dos dados. Quanto mais detalhes, quanto menor o grão, mais volume de dados, maior o tempo de carga, mais infraestrutura você vai precisar. Porque você vai ter mais dados, vai precisar de mais tempo para processamento e você vai ter um sistema gerencial mais lento do ponto de vista também de usuário. Então, mais uma vez repetindo, essa é uma informação importantíssima que deve ser definida no design do sistema e que deve ser tomada em conjunto com a área de negócios.