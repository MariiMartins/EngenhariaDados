83. KPIs
Um último conceito que a gente vai ver aqui de forma bem simplificada, bem rápida, é o de um conceito de criar uma KPI ou um indicador de performance.

E muitas ferramentas são capazes de criar isso automaticamente na própria ferramenta. Ou você pode ter isso através de um campo calculado ou criado em um banco de dados.

Então vou mostrar que um exemplo simples.
Então o KPI é uma forma de você ter uma métrica, uma performance, primeiro que eu vou criar aqui uma tabela. Então você pode vir aqui que a gente tem aqui um Select que faz o INTO a gente tá querendo dimensionar o KPI.
A gente está colocando a dimensão Tempo como mês, e a soma da dimensão da fato vendas, o valor total como realizado. Então a gente vai ter aqui, como resultado dessa consulta, duas colunas.

Então a gente está criando aqui uma sumarização de dados, vou fazer um select dimensional.q (ela tem o mês e o realizado), então, esse é o total de vendas. O total de vendas por mês que foi tirado lá da nossa Fatto Vendas.

Bom, supondo que existisse uma meta, então para cada mês eu teria uma meta. Só que eu não tenho essa meta aqui, então eu vou adicionar na minha tabela.
Altera a tabela dimensional KPI, adicionei a coluna meta do tipo numérico.
Vou executar aqui. A tabela foi criada e agora eu vou inserir para cada mês um valor pra meta, que é esse script de update aqui.

Então, vejam, eu atualizei. Cada update desses atualiza uma meta para cada mês, então vamos rodar novamente aqui a nossa consulta da nossa KPI.
Select * from dimensional q KPI
Então veja que agora eu tenho um mês o realizado, quanto vendi e qual que era a meta. Então, por exemplo, essa informação de que ela pode ir para um dashboard e os indicadores lá vão mostrar, por exemplo, no mês, o quanto eu vendi e se eu estava acima da meta.

Ele vai mostrar, uma informação, por exemplo, uma seta verde para cima quando está acima, e quando estou abaixo da meta, ele vai mostrar uma seta vermelha para baixo, por exemplo, ou qualquer outro tipo de gráfico.
Então, para a gente entender que o conceito de que KPI é gerado a partir do nosso banco de dados dimensional.
