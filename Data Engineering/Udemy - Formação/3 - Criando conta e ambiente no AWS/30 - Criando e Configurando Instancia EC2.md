30. Criando e configurando uma Instância EC2
Olá!
Então eu vou explicar agora como que a gente cria uma instância do EC2, uma instância Linux do EC2 que nós vamos utilizar em várias, não em todas, mas em várias sessões durante o curso. E alguns pontos que eu quero destacar é que a gente vai utilizar aqui uma configuração free tier, ou seja, que ela deve ser gratuita. Mas é bom sempre, você confirma isso, porque isso pode mudar. E também outra recomendação é que você desligue as Instâncias quando você terminar o curso ou quando você não estiver utilizando, mesmo quando seja free tier, porque elas costumam ter um tempo de gratuidade.

Bom, então eu já com a conta criada aqui você pode ver que para mim aqui aparece EC2, mas você pode buscar qualquer serviço aqui.
Então vou digitar EC2, e ele vai aparecer aqui. Uma outra característica da AWS é que às vezes a interface muda, mas as opções estão sempre lá.
Se você criou a conta agora, você nunca usou EC2, você não vai ter nenhuma instância aqui sendo executada.
Então mesmo que você tenha, eu sugiro que você crie uma instância especificamente aqui para o curso que com as configurações que eu vou passar.

Então, o que a gente vai fazer?
Você vai clicar aqui e executar instância. E aqui você vai dar um nome para sua instância. Esse nome é obrigatório.
Então vou digitar aqui curso e envio de dados e você pode botar o nome que você quiser.

Então eu diria assim uma das partes mais importantes é o tipo da instância, e você vai escolher aqui um tipo Ubuntu.
Agora, outra questão importante é com relação à versão. Do Linux Ubuntu e você pode tender a querer escolher a versão mais atualizada, mas a minha recomendação é que não. O que eu vou pegar aqui no meu caso e vou escolher a versão 20.04. Vejo que a mais atualizada aqui é 22.

Eu recomendo que você se tiver a 20.04 você selecione essa. Se a 20.04 não estiver mais disponível no momento que você estiver fazendo vídeo de preferência pegue uma versão mais antiga, mas sempre cuidando aqui para que ser qualificado para o nível gratuito.

Por que eu não recomendo que você pegue a última instância? Porque existem eventualmente produtos que vão ser utilizados que ainda não estão compatíveis com as últimas versões, e é o caso agora, por exemplo, nesse momento do MongoDB para a versão do Ubuntu serve22. Então eu sempre recomendo que você pegue uma versão anterior e se possível, a mesma versão aqui que eu estou que eu estou utilizando. Se não tiver a versão 20, não tem problema.
Só não dê preferência pegar a última, ok?
Então peguei aqui, selecionei a versão. Vejam que ela está qualificada para o nível gratuito aqui. A arquitetura 64 bits.Você não precisa alterar. 

O tipo de instância aqui também não precisa alterar nada. 
E aqui é outra coisa importante. Par de chaves a gente vai conectar neste servidor de forma remota, ou seja, do nosso computador a gente vai conectar nele lá no servidor do AWS e a gente vai fazer isso por SSH.
E para a gente autenticar no servidor, a gente precisa ter uma chave privada, ok?
Essa chave privada vai nos permitir que a gente autentica que ele saiba que aqui de fato somos nós que estamos fazendo essa conexão.

Então eu vou clicar aqui em Criar um novo par de chaves. Você dá um nome aqui para o novo par de chaves.
Eu vou fazer aqui como teste, mas você pode botar no momento que você quiser a AWS Teste de dados você pode botar aí como quiser.
Os tipos aqui você não precisa mudar e você vai clicar em Criar par de chaves.
Quando você clicar em Criar para Chaves ele vai abrir aqui esta essa janela para você salvar.
Veja o que eu já tenho ali uma chave é AWS  e eu tenho aqui essa chave que ele vai criar agora eu vou salvar.

Então você vai dar um nome qualquer para sua chave. Então, por exemplo, curso Eng dados e você vai clicar aqui em Criar par de chaves. Quando você clicar em Criar para deixar ele, ele vai pedir para você salvar esta chave. Eu não vou salvar porque eu já tenho uma chave criada anteriormente, mas você salve a sua chave, ok?
Eu vou cancelar aqui.

E quando você criou e salvou a sopa de chaves, ela vai aparecer listada aqui e aí você vai selecionar. 
Então é importante que você selecione aqui uma chave privada que você tenha salvo em disco que eventualmente você salvou e excluiu, ou você não sabe onde está. Você não vai conseguir conectar no EC da sua estância pelo SSH, ok?
Então use uma chave que você acabou de criar e sabe onde está, ou que uma que você criou anteriormente, mas você sabe onde ela está salva.

Bom, aí aqui as configurações de rede você não precisa alterar nada e é importante que esteja habilitado a permitir tráfego SSH. Isso vai criar uma regra nos grupos de segurança lá, permitindo que essa instância seja conectado remotamente, por SSH. Você também pode criar regras para permitir tráfego HTTP ou HTTPS pela internet. Se você estivesse desenvolvendo um API WebService, por exemplo, que não é o caso aqui, então você não precisa habilitar.

Armazenamento também você pode deixar padrão, né?
Lembrando aqui que o nome é também essencial e eu vou aqui clicar para executar a instância. Quando a gente clica em executar instância, ele cria a instância. E vejam que ele diz que a instância foi criada com sucesso.
Agora eu vou clicar aqui em Visualizar Instâncias e vejam que a instância que eu acabei de criar ela está pendente. Leva alguns minutos até o estado dela estar running. Estar rodando geralmente é bem rápido.Ok, você pode esperar.

Você pode até inicializar aqui quando ela estiver verde e que estiver em execução. Eu vou mostrar como a gente conecta remotamente a ela. Então vejo aqui já está verde, ela já está sendo executada.
O que eu vou fazer agora? Eu vou selecionar aqui a estância e eu vou clicar aqui em Conectar se a interface para você estiver aí um pouquinho diferente, só você achar a opção Conectar.
Quando você clicar em conectar, vejo que existem tipos de conexão, você tem que usar buscar a opção SSH cliente individual, então aqui ele tem instruções de como você conecta por ssh, Então veja o que você precisa mais ou menos do que a gente já falou.

Você precisa de um cliente SSH. Você pode utilizar utilizando PUT que também já havia falado. Se você tem um sistema Unix like ou uma versão mais recente do Windows, você já tem um cliente SSH.
E ele diz aqui que você precisa achar a sua chave privada. Vejo aqui que ele coloca já o nome da chave privada que eu selecionei.

Então vai aparecer diferente para você se sua chave privada por outra. 
E aqui ele dá alguns exemplos. Se você estiver utilizando o sistema Unix like para conectar, você pode precisar da permissão para ela. Se você estiver com o Windows, não precisa e você pode conectar usando uma DNS pública.

No meu caso aqui que eu estou com Windows.
Veja o que esse exemplo de conexão aqui. Ele é um exemplo, mas ele já está adequado para mim. Então ele já tenha o nome da minha chave que eu selecionei na criação da instância e já tem aqui o endereço correto, o endpoint para mim conectar no meu servidor. Então o nome da chave é o endereço (endpoint) vai estar diferente para você. Mas é isso aqui que você precisa para fazer conexão, então basta você copiar. Uma vez copiado, você pode ir para o shell do seu computador para fazer conexão por SSH.

Então aqui eu abri o shell do meu computador e você pode ver que eu estou posicionado aqui no diretório onde a minha chave está. Então isso torna mais fácil a conexão.
Porque? Porque eu posso copiar o comando diretamente ali do site da AWS. Eu vou copiar aqui novamente.
Nicolau Olha aqui então, como a chave já está aqui no diretório que eu estou posicionado e o endereço já está correto, então teoricamente basta teclar enter aqui que ele vai fazer a conexão com sucesso.
Aqui ele pede uma confirmação apenas a primeira vez.
E pronto.
Você está agora conectado ao Linux e Ubuntu que está rodando num servidor em algum lugar do AWS.
Ok?

E desse ponto em diante você está pronto para começar as partes práticas do curso. Então, por exemplo, na próxima seção, quando a gente estudar bancos de dados relacionais, a gente vai ver alguns tutoriais explicando conceitos e ao final a gente vai ter a parte prática.  Na parte prática você deve estar já neste ponto aqui, com a sua instância criada e rodando, e você vai conectar a sua instância e vai iniciar a parte prática.
Lembrando que a próxima sessão relacional e dimensional você precisa ter a mesma instância porque é uma continuação, mas nas atividades posteriores que usarem um uma instância do EC2, você pode criar uma nova instância especificamente para isso e até a forma recomendada.Você vai lá e cria uma nova instância especificamente para aquela aula. Não é obrigatório, mas é uma, é uma recomendação.
E lembrando mais uma vez para a próxima, para a sessão dimensional que é daqui duas sessões, você deve.
Ela é uma continuação da sessão relacional.