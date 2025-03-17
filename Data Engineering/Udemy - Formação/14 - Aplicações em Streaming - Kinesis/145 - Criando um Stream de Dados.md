145. Criando um Stream de Dados
Eu estou aqui já com o console do AWS e eu tenho também aqui o Jupiter com um notebook aberto que eu não dei o nome de Prod e o outro notebook criado que eu dei o nome de Console 1.
Então, para onde eu vou criar o produtor e o primeiro consumidor. Depois a gente vai criar um outro consumidor a gente só vai replicar o código.

Mas primeiro a gente precisa criar aqui o nosso streaming, a nossa ferramenta de streaming, e a gente vai então utilizar os Kineses e a gente vai criar um streaming de dados.
Então você vai ver aqui você tem as opções de streaming de dados, o estilo de entrega que o Data FireHouse e o aplicativo de analytics que é o analise de dados.

Então a gente quer o stream de dados, eu vou clicar em Criar fluxo de dados.
Primeira coisa é o nome, você pode dar o nome que você quiser, mas você vai precisar deste nome quando a gente for criar os produtores e os consumidores, os assinantes aqui, a capacidade sob demanda neste modo sob demanda é uma forma que ele vai se adaptar conforme a demanda.

E o provisionado, eu vou só clicar aqui para mostrar e aqui a gente define o número de shards, então ele vem aqui, e ele começa.

Com o sob demanda, é automático. No provisionado a gente que define o número de shards que a gente quer lidar.

O sob demanda ele passa aqui algumas informações sobre a capacidade de fluxo de dados que a gente já tinha comentado. Então, a capacidade de gravação e a capacidade de leitura. Aqui ele diz que o modo sob demanda tem um modelo de preço por taxa de transferência e aqui algumas configurações então. É tal que, como padrão de capacidade sob demanda, período de retenção é o padrão.

Algumas questões de monitoramento, configuração alvo, então você pode mudar que a capacidade dele dentro dos limites ou a criptografia. Retenção de dados que por padrão é 24 horas (Você pode aumentar que esse este período).

Então, se o nosso time já está ativo, isso quer dizer que a gente já pode começar a produzir dados. Então eu vou criar aqui a aplicação de produção de dados. A primeira coisa que a gente tem de fazer aqui é instalar o módulo quatro três, porque este módulo aqui, neste ambiente aqui do Colab, ele não vem instalado por padrão.
Então, a primeira coisa que eu vou instalar?
Um Boto3, se você quiser ir adiantando, você pode já instalar aqui no outro. No consumidor, porque cada notebook é como se fosse uma instância diferente.
É uma máquina virtual diferente, que é isolada. Então, se você instalar aqui o Boto3.

Então, a primeira coisa que a gente vai fazer é criar um produtor.
Então, vamos lá, eu vou importar aqui o Boto3.
A gente instalou, mas eu preciso também importar, eu vou importar o JSON, porque a gente precisa ser alisar os dados do formato JSON.
Então, primeiramente, aqui eu preciso criar um cliente do Boto3 para os Kineses. Então, vou chamar aqui de cliente, poderia chamar a variável de Kineses, o nome que eu quiser.
Boto3.client 
Primeiramente, o serviço, então, é o Kineses, e aqui eu preciso passar as credenciais.

Bom é quando a gente vai fazer um stream de dados. A gente precisa passar, obviamente, alguns dados e esses dados têm que ser serializados no formato JSON.
Então a gente vai utilizar o método de JSON pro dump. A forma mais fácil de a gente fazer isso é criar um objeto dicionário do Python, um objeto do dicionário do Python é formado por uma chave e um valor por pares de chave-valor.
Então eu vou chamar aqui de registro. Então esse registro vai conter os dados que vão ser serializados. Então, vamos dizer aqui que eu quero passar o ID de um vendedor com o código dele.

Bom para enviar. Para mim produzir uma informação, eu tenho que chamar o método Put Record do meu cliente, o cliente que é um cliente do Kineses, que vai autenticar lá na AWS e o resultado deste método Put Record traz uma resposta, então a gente pode ler essa resposta para ver se o processo foi bem sucedido.

Então, o primeiro parâmetro que precisa passar aqui é o streaming.
O stream nem nada mais é do que o nome do stream que a gente criou aqui.

Bom, o partition key tem uma forma de você dividir esses dados que vão ser produzidos entre diferentes shards. Então, ele vai aplicar uma função de hash sobre os dados para decidir em qual qual o shard que vai ser utilizado. A gente tem apenas aqui um Shard e é claro que ele pode poderia provisionar mais se tivesse um grande fluxo. Ok, mas de qualquer forma, a gente precisa informar que uma chave de partição. Isso quer dizer que uma outra produção que tiver a mesma chave de partição vai gerar o mesmo hash e vai ir para o mesmo shard.