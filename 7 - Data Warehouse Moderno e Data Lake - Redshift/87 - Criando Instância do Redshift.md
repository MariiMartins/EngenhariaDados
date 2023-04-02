87. Criando Instância do Redshift
Bom, lá na seção três, que cuida de configuração de ambiente, a gente fez passo a passo a criação de uma conta no AWS e depois a gente utilizou o serviço EC2 para criar ambientes virtuais. E com esses ambientes virtuais a gente utilizou eles nas sessões, estudando o modelo relacional e modelo dimensional. 
A gente vai utilizar este mesmo ambiente, um ambiente virtual com Linux, utilizando EC2.

Com seções posteriores em várias seções posteriores ainda, porém, nesta seção vai ser um pouco diferente.
Você pode utilizar a mesma conta do AWS que você criou anteriormente, mas a gente vai utilizar um serviço especificamente do AWS.

Não que EC2 não seja um serviço, mas agora a gente vai utilizar um serviço específico, que é o Amazon Redshift.
Então, a primeira coisa quando você acessar o ambiente, você deve procurar aqui. Você pode digitar que redshift, você tem que vir aqui e procurar por clusters em algum lugar. Aqui você vai achar em clusters e se vai clicar em clusters e você vai clicar aqui nesse botão Criar cluster aqui.

Então, essa primeira etapa, então, o que a gente vai fazer? A gente vai criar um cluster do redshift; A primeira coisa é identificação do cluster; Isso aqui é um nome, porque se você pode ter mais de um rodando, você pode deixar o padrão.
E aqui, veja, ele está perguntando aqui por que você está usando esse cluster para produção ou avaliação gratuita? Então, vejam que aqui a gente tem também a opção do Flicker, que é uma avaliação gratuita.
Só que esta avaliação gratuita não é para sempre, ok, então é sempre bom você consultar.
Obviamente que aqui para o curso você não vai ter problema nenhum, você não vai ser cobrado. Uma outra coisa aqui ele diz que quando a avaliação gratuita terminar, exclua o cluster para evitar a taxa sob demanda.
Então, não exatamente o que a gente vem falando, quando você terminar, você exclui o cluster. E aqui está falando para obter snapshot final do cluster e o  armazenamento e vai ser aplicado uma taxa. O que ele está falando, então que quando você excluir o cluster final, ele vai criar um snapshot, que é uma espécie de backup. Isso vai ser cobrado. Só que quando você for lá excluir o cluster, você pode desmarcar lá que você não quer esse snapshot final, ok?

Bom, então o importante é que você marcou a avaliação gratuita.
Aqui ele tem resumo do nó, Aqui ele dá estimativa de preço, Como eu falei, a gente está usando aqui a avaliação gratuita. Este banco de dados aqui ele criado junto com o cluster, porque a gente não vai utilizar ele, mas ele é criado automaticamente. E é que configuração? Muito banco de dados, então ele pede que o nome do usuário, administrador e uma senha para o usuário administrador.
Eu vou colocar uma senha aqui e vou colocar aqui 12345678AA.
Se você esquecer a senha é bem fácil. Depois lá tem uma ferramenta de gerenciamento para você trocar a senha. 
Isso é tudo que a gente precisa. Vou criar o cluster, e agora que ele está criando o cluster, eu vou voltar aqui para o Amazon Redshift e aqui vai ter uma listagem dos clusters de todos os clusters que a gente tem.
E você pode ver que o cluster que a gente acabou de criar aqui ele está com o status Notify. Ou seja, ele está sendo criado aqui, então vai levar alguns minutos, até que ele fique verde e que esteja pronto para ser utilizado.

Bom, então aqui, depois de alguns minutos, você pode ver que o redshift ele está disponível, e então a primeira etapa do nosso roteiro está pronta.

Mas existe também uma versão não gerenciada, um serverless, mas já é possível para o seu negócio, se você for usar de forma empresarial, por exemplo, existe também uma opção de servidor não gerente de serviço não gerenciado do redshift.
