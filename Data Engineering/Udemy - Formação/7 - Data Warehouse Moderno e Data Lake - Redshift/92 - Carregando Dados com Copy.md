92. Carregando Dados com Copy
Vamos começar o processo para a gente carregar esses dados.
Eu estou aqui no banco e vou voltar aqui, a minha pasta dados, você pode ver aqui que esses são os arquivos, clientes, itens, venda, produtos, vendas e vendedores.
Cada um equivale a uma tabela que nós criamos no redshift. Eu vou voltar aqui para o editor de consultas do RedShift e vou criar aqui uma nova guia no editor e agora que sim, a gente vai então fazer o nosso copy.

A função de load do redshift chama Copy. É o primeiro parâmetro que tem que informar e para onde eu quero importar esses dados. Então, como eu falei, a gente criou uma tabela para cada itens desse. E a gente tem um arquivo para carregar em cada uma dessas tabelas.

Então, vamos começar com clientes. Então, se você olhar aqui onde tem a tabela de clientes, então eu vou copiar para tabela, clientes, eu não tenho aqui um schema, eu estou no público, então eu não preciso colocar o schema, se eu tivesse criado, iria ia colocar aqui, por exemplo, vendas, ponto, clientes. Alguma coisa assim.

Bom, o próximo parâmetro de from. De onde eu vou fazer este comando de load? E aí a gente tem que copiar o endereço do arquivo, então a gente vai começar com clientes ou eu vou clicar aqui em clientes e vou clicar aqui Copy Yuri do S3. Ele me diz aqui que foi copiado.

O próximo parâmetro são as credenciais.
Então, aqui eu vou botar credencial aos credenciados, e você vai preencher as credenciais da seguinte forma AWS sublinhado a esses, sublinhado que.
Sublinhado ID é aqui o seu ID e eu já vou preencher com o meu e aqui um ponto de vírgula. 
E aqui vem a chave secreta AWS Secret Key Access (aqui vem a chave e você fecha com aspas). Então você vai colar aqui o seu ID e a sua chave que nós criamos na sessão anterior. Então estou colocando aqui o meu ID (remova os espaços e vou copiar que a minha chave) O próximo parâmetro é a região, então, se você se lembrar lá, eu mencionei que era para a gente criar na região da América do Sul, São Paulo.
Como você pode confirmar isso? Você vê aqui no bucket, na raiz do Bucket Propriedades. E aqui está a região da AWS América do Sul, São Paulo.

O outro paralelo que a gente precisa delimitar delimita que no nosso arquivo aqui é ponto e vírgula.
Mas um parâmetro de precisão e ignorar, a gente vai colocar como um.
Ou seja, ele vai ignorar cabeçalho. Por que? Porque se você lembrar lá quando estudou, quando a gente olhou o nosso arquivo, a primeira coluna, a primeira linha desculpa era o cabeçalho ok.
E a gente não quer importar. Hoje a gente não pode. O povo tem que saber que é a primeira linha e o cabeçalho a gente não vai importar. Então a gente está colocando o parâmetro aqui para ignorar o cabeçalho.

E por fim, que vou colocar um Date Format, que é o formato que está data de datas do nosso arquivo e dd/mm/yyyy (bom, aqui a gente utilizou os parâmetros)

Mas existem vários outros tipos de parâmetros que você pode utilizar no quando você for usar o copy do red shift. Se você estiver utilizando, por exemplo, um arquivo de JSON e você vai precisar também de um arquivo de mapeamento que vai mapear o caminho do campo do JSON para o campo do banco de dados.

Aqui, então, um arquivo a mais que você vai precisar configurar e preparar.
Bom, vamos ver se deu tudo certo aqui. Vamos tentar executar.
E ver se a gente tem aqui algum possível erro. Às vezes a gente tem que fazer algum ajuste. É normal. Às vezes não funciona de primeira.

A gente não teve erro. Então, provavelmente deu certo. 

A gente pode usar um select * from clientes, que foi o que a gente importou.
Então aqui está o todos os clientes importados, veja que existe essa limitação de senha. Aqui eu vou desmarcar, executar de novo. São 250 clientes que foram importados. Bom, agora a gente só precisa repetir o processo para os outros arquivos do nosso bucket.
