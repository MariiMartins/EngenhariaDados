147. Kinisses Delivery com Firehouse
Bom, então agora a gente vai mudar um pouquinho o cenário. A gente tinha dois assinantes, consumidores, que eram duas aplicações Python, então esses dois consumidores nós vamos fechar aqui que nós não vamos utilizar mais.

E a gente vai criar agora um serviço de stream de entrega, que é Kineses Firehouse. Então o produtor que é esta aplicação Python aqui ele vai produzir e a aplicação de streaming que a gente criou aqui, que está ativa, que é o stream1. Ele vai ter como um consumidor, não mais o aplicativo Python, mas o Kineses Firehouses.

O Kineses Firehouse é um serviço de entrega. Então, como um assinante, ele vai receber o stream e fazer entrega. E aonde ele vai fazer a entrega? Bom, nós vamos definir que ele vai fazer essa entrega num Bucket do S3.

Então a gente não vai precisar modificar nada. A gente só precisa, então, criar o nosso stream de entrega do FireHouse. A gente vai definir o bucket e a gente vai ter que vir aqui no nosso produtor e produzir. E depois a gente espera encontrar lá no bucket os dados produzidos. Só que, como a gente viu lá anteriormente, a latência que é maior, ok, então vamos lá.
Então a gente vai voltar aqui para o Kineses, a gente não vai alterar nada.
Então, vamos vir aqui no streaming e vamos clicar em streams de entrega. Não tem nenhuma que vou clicar aqui em Create Delivery Streame.

Bom, aí aqui a gente tem que definir a origem e o destino. Sendo um serviço de entrega de quem ele vai receber, para onde ele vai mandar; e como source aqui a gente vai definir que é Amazon Kineses streaming, que é o stream que nós criamos anteriormente, o stream que nós criamos e utilizamos, e nós temos o produtor pronto,  para ele como destino a gente vai dizer aqui que é um bucket do S3.

Então selecionamos, agora aqui a gente tem que fazer algumas configurações.
Então, primeiro, a origem. De onde vai estar vindo esses dados que ele vai entregar? Então a gente já sabe que é do streaming de dados que nós criamos anteriormente.

Agora é aqui o nome do delivery streaming. Você pode botar o nome que você quiser aqui, mas você não precisa alterar aqui. Ele pergunta se a gente quer transformar ou converter os registros.
Se a gente quer mudar o formato, ele pode transformar para o ORC, por exemplo, e aqui o destino, já que a gente definiu que ia ser num bucket.
Então, aqui a gente tem que navegar num bucket ou criar um bucket.

Eu vou clicar aqui em criar. Vamos criar, vou criar um bucket específico para isso.
Você, se quiser, pode utilizar um específico que Mises Field House.
Vou colocar aqui uns números aleatórios só pra não correr o risco de ter um igual.
Só botar aqui Firehouse região da AWS aqui em São Paulo.
CL Desabilitadas aqui.
Vou desmarcar o bloco de acesso público.
Vou marcar aqui pressionamento do ativar criar bucket. Bom o bucket foi criado.

Agora que eu vou em shows, buckets aqui. Eu posso agora navegar aqui e selecionar o que eu criei. 
Particionamento dinâmico. Você pode criar um particionamento dinâmico. Isso é importante, pois se você tiver um grande volume de dados, ele vai criar uma série de arquivos e pastas no bucket.

Como uma ferramenta de delivery, ele não vai entregar em tempo real. Então não vai ser sempre que você produzir dados que ele vai fazer a entrega desses dados. Ele vai criar um buffer que vai ser de 5 mega ou 300 segundos por padrão, que seriam cinco minutos.

Claro que você pode mudar esse buffer aqui. Eu vou clicar aqui em Edite eu vou manter que o buffer sai de 5 mega, mas o buffer em intervalo máximo eu vou botar 60 segundos, senão a gente vai ter que esperar cinco minutos ali até que haja a entrega dos dados. Independente se houver uma produção, ele vai aguardar o intervalo.
