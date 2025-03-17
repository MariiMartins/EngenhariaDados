Eu estou aqui no arquivo vendo as propriedades do arquivo e se a gente descer aqui até criptografia. Você pode ver que a criptografia padrão está desabilitada e a criptografia do lado do servidor nenhuma.
Agora eu vou voltar no bucket. Então aqui está o bucket. No início do caminho, vou clicar aqui, vou vir aqui em propriedades e vou buscar aqui a criptografia padrão.
Como a gente já sabia, está desabilitado.
Eu vou clicar em Editar e vou mudar aqui de desativar para ativar. E aí aqui está os tipos de criptografia que nós estudamos ou as chaves gerenciadas pelo SSS (S3) e as chaves do AWS Key Management Service.
Eu vou clicar aqui só pra ver quando eu escolho as chaves do AWS ele abre aqui, algumas. Opções chave gerenciada pelo AWS. Escolher entre suas chaves da AWS, que ele vai pedir para mim, escolher a chave ou criar.
Inserir ARN das Chaves do AWS KMS.
Chave do bucket eu posso desativar o ativar.

Eu vou voltar aqui pra primeira opção. Que é chaves gerenciadas pelo Simples Storage Service . O próprio S3 que vai gerenciar as chaves e a criptografia ela ficar ativada.Eu vou salvar aqui as alterações e ele está me dizendo que a criptografia padrão foi habilitada com êxito.

Agora eu vou voltar lá pro arquivo. Então vamos aqui em objetos. Mês, Dia, hora.
Cheguei aqui no arquivo. Cliquei no arquivo, no objeto. Aqui em Propriedades, vamos buscar novamente aqui.
Criptografia, configurações de criptografia. Veja que está tudo desabilitado ainda e que não há criptografia.
Isso porque? Por que isso aconteceu? Porque o arquivo já estava aqui quando eu habilitei a criptografia no bucket, então imagine se você, se você tem aqui alguns milhares, milhões de arquivos terabytes de informação e você habilita a criptografia depois que esses arquivos já estão no Bucket, que então ia ser um custo muito alto criptografar todos esses arquivos.
Então, se você habilitar a criptografia no bucket, essa criptografia ela vai fazer com que os objetos que já estavam no banco não vão ser criptografados, mas novos objetos incluídos vão ser criptografados. Agora, é claro, eu posso pegar aqui o objeto, editar criptografia e ativar manualmente a criptografia.
Vou salvar as alterações. Vou fechar aqui. Agora a gente vê que em configuração de criptografia, criptografia habilitado, tipo de chave está aqui. Então eu habilitei manualmente a criptografia para este arquivo. Agora vamos excluir esse arquivo e carregar ele de novo para o banco para ver o que acontece.
Se ao carregar ele para o bucket ele já vai estar por padrão criptografado, já que eu apliquei a criptografia no bucket de lá no início deste tutorial, então eu vou em ações do objeto no nível 13, vou selecionar aqui o arquivo e vou clicar em Excluir.

Ele me pede para digitar aqui, excluir permanentemente. Vou copiar o texto aqui, vou excluir o objeto.
Então vejo a pasta 13 do Bucket está vazia. Agora eu vou carregar este objeto novamente. Vou clicar aqui, carregar, adicionar arquivo. Ali está meu arquivo vendas.
Então  eu estou na pasta 13,aqui está o objeto VendaCSV, que eu acabei de carregar.
Vou clicar nele. Estou em Propriedades e vamos vir aqui em Configurações, que ficam na fila do servidor. 
Então VEJA está habilitado porquê? Porque quando eu fiz o upload do arquivo, a criptografia já estava habilitada a nível de bucket.
Então, no momento em que o arquivo é carregado para o bucket, ele já fica criptografado.
A última questão que a gente vai ver aqui, eu vou voltar aqui para o Bucket.
Vou clicar aqui em Propriedades. E aqui há opção de tags. Então, tags são informações conjunto de chaves e valores que você pode utilizar para gerenciar, por exemplo, questão de segurança.
Então, por exemplo, eu vou clicar aqui no editar, adicionar uma tag. A chave eu vou botar aqui, vou chamar uma chave de classificação.
E o valor PHI, é o acrônimo para Informação de Saúde Pessoal ou Informação Relacionada à Saúde do Paciente.

Então, por exemplo, eu posso adicionar essa tag.
Vou salvar aqui o e esta tag aqui que agora está salva. Classificação com o valor PHI.
Ele pode indicar que essa informação aqui é sensível, então eu poderia ter uma outra chave que se chama classificação, mas que o valor, por exemplo, poderia ser público, que indicaria que a informação seria pública.