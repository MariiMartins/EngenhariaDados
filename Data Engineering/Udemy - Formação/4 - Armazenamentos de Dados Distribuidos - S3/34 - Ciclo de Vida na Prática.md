Bom, então vamos ver na prática as classes de armazenamento e também as regras de ciclo de vida.
Então eu estou continuando aqui com o bucket, com o arquivo que a gente já tinha criado.
Então você pode ver aqui que está o bucket. E aqui está o particionamento que eu fiz ao mês, dia, hora,13, vendasCSV.
Bom, aqui em propriedades a gente vai procurar aqui a classe de armazenamento. Então vejam aqui o Classe de armazenamento e como a gente já esperava, a classe de armazenamento aqui é padrão e eu posso mudar.Eu posso alterar essa classe manualmente.

Depois a gente vai ver como a gente cria regras para o próprio S3 ainda neste vídeo a gente vai ver como a gente muda, como configura para o S3, faz isso automaticamente.
Mas se eu quiser, já eu posso vir aqui diretamente e mudar a classe de armazenamento. Então vejo aqui que as classes existem, as classes que a gente estudou lá e algumas outras, então, a padrão.
Dados acessados com frequência, mais de uma vez por mês, com acesso a milissegundos a descrição é que é bem interessante.

Aqui, ele diz que as disponibilidades são mais que três. Então, você tem redundância desse arquivo. Se você olhar que a duração mínima não existe aqui por padrão, depois do tamanho mínimo do objeto, taxas de monitoramento, taxas de recuperação, ou seja, a cobrança que isso, que existee depois aqui as outras classes: Intelligent Tiering. Então dados com padrões de acesso alterados ou desconhecidos.
Aqui, uma zona que vai ter um custo menor, mas ela vai estar num único local.
Recuperação instantânea do Glacier.
Então vejo que dados de arquivamento de longa duração, processados uma vez por trimestre, com recuperação instantânea milisegundos.
Então vejo que esse é um Glacier que com a recuperação instantânea, agora veja aqui esse outro Glacier flexível.
Dados de longa duração acessados uma vez por ano, com recuperação de minutos ou por horas.Isso quer dizer o que? Isso quer dizer que se você precisar de seu arquivo aqui, ele pode estar disponível para você desde minutos ou pode levar horas.
Então você não pode colocar aí algo que você possa precisar com frequência.

Agora, olhe se outro aqui: Glacier Deep Archive. Dados de arquivamento de longa duração acessados menos de uma vez por ano, com recuperação de horas.
Então o anterior aqui ainda diz que pode ser minutos ou horas. Mas isso aqui já está dizendo que a recuperação vai levar horas.
Então é para aquelas coisas que você não vai mais utilizar ou o que você não espera mais que você vai precisar, mas em caso você precise desses dados, você tem ali como recuperar ele.

Veja aqui se você quiser aplicar essa classe, é o tempo mínimo que o arquivo tem que ficar lá.
O tamanho mínimo do objeto, então. E existe uma recomendação de tamanho mínima, até por questões de custo. Aqui há questões e ele mostra que as questões da taxa da cobrança eu não vou mudar, que a classe eu vou cancelar.
E agora aqui a gente vai voltar para o bucket, então você vai clicar aqui no nome do seu bucket.
A gente está aqui. No final, a gente vai lá para o bucket, a gente vai clicar aqui em bucket, então a gente vai ver que regra de ciclo de vida a gente vai criar aqui uma regra de ciclo de vida. Então, você tem que vir aqui em gerenciamento ou clique aqui em gerenciamento. Aqui você tem regras e ciclo de vida. Ele já é o primeiro aqui.
A gente não tem nenhuma regra de ciclo de vida e eu vou clicar aqui em Criar Regra de ciclo de vida. Ele pede pra mim criar um nome para uma regra.
Obviamente que num bucket eu posso ter mais de uma regra.
Eu vou chamar aqui de regras, arquivos de vendas, por exemplo.
Aqui, ele me pede o escopo da regra. Posso limitar o escopo dessa regra usando um ou mais filtros ou aplicar a todos os objetos do bucket.
Então, eu posso dizer essa regra se aplica só a um determinado filtro ou não se aplica tudo?
Vamos supor que a gente queira aplicar o filtro e o filtro é o que o prefixo, ou seja, o início do arquivo, seja vendas. Então, essa regra ela vai se aplicar apenas o arquivo cujo início do nome do arquivo seja vendas.
Aqui, o tamanho do objeto, eu posso especificar o tamanho mínimo ou o tamanho máximo. Quando essa regra vai ser aplicada (não vamos mexer aqui) e aqui as ações que eu quero.
Então, veja os tipos de ações, mover versões atuais de objetos entre classes de armazenamento, e mover versões desatualizadas do objeto entre classes de armazenamento.

Mover versões desatualizadas de objetos é quando você tem versionamento do objeto, que não é o nosso caso aqui, então essa aqui não se aplicaria no nosso contexto, que a gente não habilitou a versionamento.

Aqui eu tenho expirar versões atuais de objetos, excluir permanentemente versões desatualizadas de objetos e excluir marcadores de exclusão de objetos.

Vamos escolher, então, aqui mover versões atuais de objetos entre classes de armazenamento e excluir permanentemente versões desatualizadas do objeto.
Então a gente marcou essas duas opções para essa primeira opção.
Ele abre esta configuração aqui, ir para a segunda, que eu escolhi permanentemente. Ele abre essa configuração aqui.

Bom, então, para mover versões atuais de objetos entre classes de armazenamento, eu tenho que definir aqui como vai ser essa transição.
Então, por exemplo, ele está lá a gente viu que a classe de armazenamento lá é a padrão.
Depois de padrão para qual classe ele vai?
Então a gente vai selecionar aqui para qual classe ele vai estar selecionada, que padrão IA que é o que eu uso com pouca frequência.
Então vamos manter esse padrão IA e depois de quantos dias depois da criação do objeto ele vai passar para essa classe?
Então ele pode colocar que 30 e a gente pode adicionar uma nova transição aqui. Depois de 30 dias, ele pode ir para o Glacier Flexible Retrieval, e a gente pode definir que isso vai acontecer depois de 60 dias.

Este aviso aqui é que você lembra lá naquela tabela que existia um tamanho mínimo para o Glacier. Ele está dizendo aqui que pode ter uma cobrança que vai ser desproporcional ao tamanho do arquivo. Então, como a gente está só praticando aqui, não precisa se preocupar.

Então, só explicando o que vai acontecer aqui quando você adicionar um arquivo para esse bucket 30 dias, a classe de armazenamento dele vai ser padrão. Depois de 30 dias, ele vai passar para o padrão IA, que é infrequente access ou acesso infrequente. Depois de 60 dias, ele vai para o Glacier.

Então a gente tem que marcar aqui depois para salvar. Agora depois de 60 dias, ele passou para o Glaciar.
Agora a gente pode querer que depois de um tempo ainda ele seja excluído, que é o que a gente marcou aqui, o excluir permanentemente.
Então a gente tem que dizer quantos dias após o objeto vai ser excluído permanentemente. Então vamos colocar que 120 dias. Isto é, o número de versões mais recentes serem retiradas é opcional. A gente não precisa marcar.
Então, recapitulando, o arquivo chega no bucket, ele tem a classe padrão.
Depois de 30 dias, ele vai para o padrãoIA e depois de 60 dias ele vai para o Glacier de 60 dias até 120 dias. Ele continua no Glacier em 120 dias.
Ele é excluído permanentemente, depois excluído permanentemente, não tem mais volta ele e ele é excluído mesmo.

Agora que o pessoal fez um equívoco excluir permanentemente versões, na verdade é expirar versões atuais. Para isso, a gente vai colocar aqui 120 dias.
Então vejam aqui que ele traz pra nós uma análise. Essa análise que delinearam dia zero o objeto carregado, ele vai estar na classe de armazenamento padrão. Com 30 dias, ele move para o IA. Em 60 dias, ele vai para o Glacier e em 120 dias o objeto expira.

Dizer que o objeto expira quer dizer que ele vai ser excluído, que ele vai entrar numa fila de remoção. Embora não esteja dizendo explicitamente que ele vai ser excluído, vai expirar. Mas ele vai ser também excluído. Então, a gente pode criar a regra. Ô é a regra que está salva.
E, é claro, a gente pode ter diferentes regras dentro de um mesmo bucket.
A gente pode colocar lá, como um filtro, diferentes tipos de arquivos.
Então aí a gente viu de forma bem interessante como funciona as classes de armazenamento e as regras de ciclo de vida.