28. O Ambiente

Bom, vamos falar aqui de alguns conceitos que o curso traz e também o ambiente que a gente vai utilizar no curso.
Então, o nosso principal objetivo é estudar conceitos. Só que, ao mesmo tempo que a gente precisa estudar conceitos, a gente precisa estudar ferramentas. Então eu vou dar um exemplo aqui.
O bancos de dados relacionais é indispensável para um engenheiro de dados, bancos de dados No SQL também.

Então a gente precisa estudar os fundamentos que não estão relacionados a um determinado produto.
Só que para estudar isso a gente precisa ter um produto.
Então, no caso de bancos de dados relacionais, a gente vai estudar o postgres (elefante)
No NoSQL, a gente vai estudar o MongoDB e o Redis. Porém, também existem ferramentas indispensáveis, que, no caso é o Spark. Então, a gente vai também estudar o Spark.

Uma outra coisa importante é que, como engenheiro de dados, a gente precisa ter uma familiaridade com a linha de comando e com o Linux. Então, a gente vai utilizar bastante aqui acesso a um servidor através de linha de comando, onde ele vai interagir com ferramentas de bancos de dados Spark, entre outras.

Uma outra coisa importante que a gente precisa trazer aqui no curso é a computação na nuvem. Então, o mercado de trabalho hoje as empresas, na sua grande maioria, se não têm toda a sua infraestrutura de dados na nuvem, parte dela provavelmente vai estar na nuvem.
Então, também é algo que o engenheiro de dados tem que ter familiaridade, Ele tem que ter acesso.

Então a gente vai utilizar durante o curso o ambiente do AWS, o Amazon Web Services.
Uma das ferramentas que a gente vai utilizar no AWS é o EC2.
Então o EC2 é um ambiente virtual na nuvem. Isso vai permitir o que você possa fazer o curso em qualquer computador, desde que você tenha acesso à internet. Então você vai acessar o AWS, criar uma conta, uma máquina.
Gente vai criar uma instância do EC2 com o Linux. A gente vai conectar a este servidor de forma remota. E aí a gente vai fazer os nossos estudos.
Então, esse é o ambiente que a gente vai estudar aqui durante o curso.

Vamos falar um pouco então do EC2.
Então EC2  é um ambiente, Um serviço do AWS que a gente pode criar uma máquina virtual como se fosse uma máquina virtual.
Existem várias opções de máquinas virtuais que você pode criar. A gente vai utilizar o Linux, Ubuntu e a gente vai conectar a esta máquina virtual por SSH.
Então, SSH é um protocolo que é utilizado para você gerenciar servidores remotamente.Então, esta configuração é a principal ferramenta do curso, mas não é a única.
Outras ferramentas serão utilizadas, mas sempre na nuvem no AWS . Então você não vai ter que ter o ambiente no seu computador.

Então você vai ter lá um ambiente na nuvem do AWS. Nesse ambiente na nuvem, a gente vai criar uma instância do EC2 com Linux e do seu computador, você vai conectar e você vai gerenciar essa instância (este servidor)  usando SSH.
Então você vai ver que no processo ali você eu vou explicar passo a passo, porque o que você precisa fazer.
Você vai baixar uma chave privada no seu computador que está identificada, que essa chave azul e essa chave vai permitir que você faça a conexão no servidor que você criou ela remotamente. Você faça o gerenciamento.
O gerenciamento nada mais é do que você instalar os sistemas, os bancos de dados e executar as operações.

Falando por que então do SSH, ele já é nativo em sistemas operacionais baseados em Unix e nas versões mais recentes do Windows. Então você não precisa instalar nada. Você só vai precisar abrir ali seu shell, a sua linha de comando e acessar o seu servidor remoto com SSH.

Caso seu sistema operacional não possua SSH. Para uma versão mais antiga do Windows, você pode baixar um cliente que é um software bem levezinho e gratuito, então você pode abrir, por exemplo, lá o seu mecanismo de busca. Você digita lá PuTTY que é o cliente de SSH mais conhecido, e aí você utiliza ele para conectar ao a AWS.

Qual serão as etapas que a gente vai estudar aqui nessa seção?
A gente vai criar uma conta no a AWS. A gente vai criar uma instância do EC2.
Então, a criação dessa instância inclui o processo de você criar um par de chaves privadas e salvar o seu computador.
E a gente vai conectar o seu computador a essa instância que a gente tirou por SSH. Então, algumas sessões ou a maioria das sessões do curso pressupõe que você chegou até aqui, que você vai estar com uma instância do EC2 criada e já conectada a ela pelo SSH.

Eu vou explicar tudo ainda nessa sessão. Como você deve fazer.
Bom, algumas considerações adicionais, então é indispensável atualmente você para uma formação em engenharia de dados, conhecimento e uso de serviços na nuvem. Então, por isso que a gente vai utilizar serviços nos serviços, na nuvem. A maioria dos serviços da nuvem da maioria dos provedores possuem opções gratuitas.
E elas têm recursos limitados, uma suficiente para o curso.
Então o EC2 você vai viajar logo a seguir que ele tem lá a opção de free tier, que é uma camada gratuita que você não precisa pagar.

Agora há aqui algumas observações.
As condições para os serviços gratuitos e quais serviços são gratuitos elas mudam. Então, é sempre bom você consultar o provedor de serviço. Então, nesse momento que você vai ver que a gente acessa o ambiente, cria uma instância EC2 com gratuitamente, a gente vai ter a opção lá do free tier.
Ok, mas é sempre bom você ficar atento a isso.

E é bom você ter o hábito de, principalmente se você estiver estudando de você, parar os serviços quando você não vai utilizar mais o, por exemplo, quando você terminou o curso mesmo para serviços gratuitos, porque às vezes eles têm uma limitação de tempo vai ser gratuito por um ano, por exemplo.

Então, como eu falei, as condições dos serviços mudam.
Agora, mesmo que ocorra alguma cobrança, você pode ficar tranquilo que para a execução desse curso os valores não devem ser significativos. Então, por exemplo, para um outro curso de AWS que eu utilizei serviços de machine learning que não tem opção free tier do curso todo várias horas gravando, Eu gastei menos de 20 $, ok?

Então, mesmo que ocorra alguma cobrança, você não deve se preocupar, assim como alguma coisa muito significativa. Agora é indispensável, como eu falei, para a formação de engenheiro de dados, que você cria um cadastro e um serviço na nuvem, especificamente na AWS, que é esse curso.

Você até pode acompanhar o curso, por exemplo, apenas assistindo. Ou você pode criar uma máquina virtual local com Linux. Você pode fazer tudo isso, mas não é o que eu recomendo. O recomendado é que você crie e utilize essa conta na nuvem.
Então, no próximo tutorial, você vai ver como criar uma conta no AWS e depois como criar uma instância do EC2 e como conectar a essa instância.

