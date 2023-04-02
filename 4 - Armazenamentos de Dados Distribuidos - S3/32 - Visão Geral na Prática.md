Bom, eu estou então logado aqui no AWS e a gente vai ver então o funcionamento do banco de um bucket dentro do S3 na prática.
Então você pode vir aqui e buscar serviços, digitar aqui S3, aqui eu não tenho nenhum serviço criado. Aparece pra mim aqui o botão Criar Bucket ou se eu vir aqui no menu ou buckets, vai aparecer a lista de todos os buckets criados aqui eu não tenho nenhum. Então a primeira coisa que é criar um bucket, eu vou fazer aqui uma simulação de como a gente estivesse, criando dados particionado, então, semelhante ao exemplo que a gente viu lá no tutorial de você ter as vendas adicionadas por dia, então vamos lá, eu vou criar um bucket. A primeira coisa que então o nome do bucket. Então, lembrando que o nome do bucket tem que ser uma coisa universal, tem que ser o nome único universal.
Não é apenas para você ou para sua empresa, Globalmente, tem que ser único.
Então eu vou colocar aqui vendas123ABC.  Vamos torcer para ninguém que tenha escolhido esse bucket ainda na região. Aqui você pode botar: A América do Sul São Paulo.
Aqui você pode configurar copiar configurações de um bucket. Aqui você tem as listas de controle de acesso vão ficar desabilitadas. Configurações de bloqueio de acesso público. O acesso público está bloqueado. A gente não precisa liberar, ver se o momento do Bucket.
Podemos deixar desativado, as tags que eu expliquei lá rapidamente, qual que é a função são chaves, valores que você pode colocar por questão de segurança. Você pode, por exemplo, indicar que esse bucket tem informações pessoais, informações sensíveis, criptografia também vão deixar desativado. E vamos aqui criar o bucket.
Então vejam que o Bucket Vendas123ABC foi criado lembrando que você não vai conseguir criar um bucket com o mesmo nome que o meu, porque ele tem que ser único. Então você pode aí colocar o nome qualquer. Você pode ver que o nome do bucket é um link. Eu vou clicar aqui.
E aqui você tem várias configurações esse Bucket ou então você tem as propriedades dele. 
A questão de versionamento, a região aqui, que posteriormente a gente vai precisar em outras sessões do curso, a questão de permissões. As métricas do bucket não existe aí a gente recém criou, aqui gerenciamento, as regras de ciclo de vida que a gente vai ver exemplos posteriormente, pontos de acesso.

Vamos voltar aqui para objetos. Então, vamos simular que o exemplo que a gente viu lá no slide, que a gente vai ter um particionamento de vendas.
Então, vendas123ABC. Então eu vou criar dentro de vendas, dentro desse bucket, eu vou criar uma pasta.
Você vê que tem um botão, criar pasta. Então eu vou criar uma pasta mês, uma pasta dia.É uma pasta hora, e depois uma pasta da hora específica. E dentro dessa pasta vai ter o arquivo.

Então vamos lá. Eu vou criar aqui uma pasta mês. Não precisa habilitar aqui a criptografia do lado do servidor.
Vejam que ele criou dentro desse Bucket Vendas123ABC, a pasta mês. Vou clicar na pasta mês, agora, dentro de meses, vou criar outra pasta. Então, aqui eu vou chamar da pasta dia. Também aqui padrão cria pasta. Então, vejam dentro de mês criei a pasta dia vou clicar na pasta dia. Agora, dentro de dia eu vou criar mais uma pasta que vai ser hora. Vou criar a pasta hora dentro de dia, hora e agora dentro de hora eu preciso ter uma pasta, por exemplo, para cada hora e dentro de cada hora eu vou carregar os dados. Então vou criar uma última pasta aqui.
Vamos supor que você já passa das 13h00 às vendas das 13h00 ou que a pasta vou clicar aqui em 13.
Então vejo aqui a gente tem vendas123ABC, mês, dia, hora 13.
Então, obviamente que a gente vai ter Dentro de meses a gente vai ter A gente não fez o exemplo completo aqui, mas a gente teria uma pasta, janeiro, outra pasta, fevereiro, o dia um, dois, três, quatro dentro de cada mês, depois as horas, ok.

Então, uma simulação aqui de como, de como funcionaria. Então, dentro de 13, 13h00, a gente vai carregar aqui os dados. Então eu vou clicar aqui, encarregar.
E você pode carregar o arquivo Vendas CSV que ele foi disponibilizado junto com o material do curso.
Então eu clico aqui carregar e ele vai vir aqui para uma outra tela adicionar arquivos. Então clique aqui e localize o arquivo com o material do curso que você baixou. Então aqui está o Arquivo Vendas. Vou clicar aqui em Abrir ele mostra o arquivo.Veja que ele ainda não colocou no bucket Olha, ainda não carregou. Você tem que clicar e carregar. Então ele não faz isso automaticamente, porque eu posso adicionar outros arquivos de outros locais
e carregar tudo simultaneamente.

Agora sim, eu vou clicar em carregar.
Ou então ele diz que o upload foi bem sucedido. Eu posso fechar.
Então, veja só, dentro da pasta 13 eu tenho o arquivo vendasCSV. Eu posso clicar neste arquivo aqui e ele me traz várias propriedades aqui deste arquivo.
Então, por exemplo, aqui URI do S3 é o caminho do arquivo, então é um caminho universal (É o identificador do arquivo.)

Por exemplo, se um outro serviço a AWS quiser, acessar esse arquivos, este é o caminho do arquivo.
Você tem uma URL para acesso pela internet também. Mas é claro que você não vai conseguir acessar de um outro navegador, por exemplo, por questões de segurança. Você tem que dar permissão para esse arquivo.
Veja aqui a definição de chave: mês, dia, hora, 13.
O nome do arquivo que você tem outras configurações desse arquivo. Então, aqui você pode, por exemplo, copiar o URI desse arquivo. Ele coloca na área de transferência e pode fazer download, abrir.

E aqui tem várias ações do objeto.
Você pode fazer download e compartilhar com um URL pré- assinado. Isso vai criar o endereço que quem tiver um endereço tem uma URL e com hash, quem tiver essa URL vai conseguir baixar o arquivo. Isso é muito utilizado por exemplo, se você vai compartilhar um determinado arquivo, você pode simplesmente compartilhar ele através de uma URL pré- assinado, que copiar, mover você pode mover para outro bucket.
Você pode fazer uma consulta com S3 Select, renomear, editar, editar metadados, tags, enfim, você pode fazer diversas ações aqui sobre o arquivo.
Então a gente viu o básico aqui do S3  partido para estruturar o que a gente vai ver mais funcionalidades do S3 e depois também vai ter. A gente vai voltar aqui para falar na prática, então você não precisa excluir nada que ainda.
