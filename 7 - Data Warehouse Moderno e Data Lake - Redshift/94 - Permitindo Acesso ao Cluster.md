94. Permitindo Acesso ao Cluster
Nós criamos a nossa fato vendas e a gente quer criar este dashboard, onde os usuários poderão consultar esta fato Vendas Como explicou lá na introdução.
A gente vai fazer isso usando a ferramenta Google Data Studio.
Só que o que acontece é por padrão com DW aqui, o RedShift, ele não vai estar disponível publicamente. Então eu vou mostrar que uma configuração que você vai ter que mudar depois de você mudar essa configuração, você vai ter que esperar o cluster estar disponível novamente.

Aqui você tem um status dele, no momento ele está indisponível e depois que estiver disponível, então a gente pode passar para a criação do Dashboard.
Eu vou também mostrar rapidamente como você configura outras formas de acesso, caso você queira configurar ou restringir o acesso ao cluster.
Ok, então existem configurações específicas para isso.

Bom, eu estou aqui na página de gerenciamento do meu Cluster Redshift 
Quando você abrir a página do Redshift, você nesse menu aqui ao lado, você pode acessar clusters, E aí você clica no Seu Cluster.
Bom, se a gente vir aqui em propriedades, primeiro eu vou mostrar o que a gente precisa mudar  em Configurações de Rede Segurança o vejam aqui publicamente, acessível, desabilitado. Então a gente não vai conseguir acessar este cluster de outra ferramenta. Então, a gente tem que habilitar isso. Como é que a gente faz isso? Bom, aqui existe esse botão Ações ou eu vou clicar nele e vejo aqui o modificar a configuração publicamente acessível.
Então aqui ele está perguntando se eu quero desabilitar ou habilitar o acesso público. Eu vou clicar em Habilitar. Ele pede que o endereço IP (acho que você não precisa se preocupar com isso) e ele está dizendo que seu cluster pode ficar indisponível até dez minutos depois que você alterar essa propriedade.
Mas eu garanto que não vai levar dez minutos, sempre é um tempo bem menor. Às vezes, em menos de um minuto ele já vai estar disponível novamente. Bom, aqui eu vou salvar as alterações.

E você pode ver que o status aqui está modificando. Então você vai aguardar alguns minutos aqui você pode atualizar a página e quando ele voltar aqui fica disponível. Então aqui eu atualizei, ele já está acessível novamente.
Agora o que a gente vai precisar para acessar a nossa tabela é ID que nós criamos, é a nossa tabela Fato que a gente criou.
Bom, a gente vai precisar primeiro deste endpoint aqui. Então você pode clicar aqui e copiar.A gente vai precisar do nome do usuário e da senha.
Se você lembrar lá da configuração do cluster, o nome do usuário era AWS User e a senha. 
E a outra coisa que você vai precisar é o banco de dados, a gente precisa também da porta, mas a porta já vai estar aqui nesse endereço, ok. Quando a gente colar, ela já vai estar endereçado. Isso aqui, tendo o usuário e sem o banco de dados, é tudo o que a gente precisa para fazer a conexão no GDS.

Caso você precise fazer alguma configuração de acesso específica do cluster, eu vou mostrar aqui para vocês como funciona.
Então, eu vou clicar aqui em Propriedades, configurações de segurança e aqui tem grupo de segurança da VPC (Virtual Presente Cloud), esse grupo de segurança tem um identificador aqui, eu vou clicar nele nesse identificador, e aqui ele traz o detalhe esse grupo de segurança, agora vou clicar no CD do grupo de segurança. E agora que embaixo existem as regras de entrada, você não vai precisar mudar nada aqui e eu estou apenas mostrando como é que funciona.
E eu vou clicar aqui e editar regras de entrada. Então, aqui estão as regras para em que o AWS vai permitir o acesso à sua instância de redshift. Então, vejam aqui que esta regra que foi criada pelo próprio redshift durante o nosso processo de configuração do cluster.

Ele está dando acesso a todos os IP's com protocolo TCP IP de todas as portas. Então é uma regra que ele criou aqui tem outra regra de todo o tráfego.
Ok, então você se você quiser epr exemplo, restringir o acesso a seu cluster ser exclui essas regras. Ou você pode excluir essas regras e criar uma regra específica, por exemplo.
Vamos supor que você queira um IP personalizado e aqui você vai colocar meu IP, então ele já pega aqui o seu IP. Se eu excluísse essas duas regras aqui e colocasse TCP IP personalizado com meu IP, apenas o meu IP ia conseguir acessar esse cluster. Ok, então é só pra gente ver como que funciona?

Eu vou cancelar aqui que, como eu falei, eu não vou precisar alterar nada, ok?
Mas caso você tenha algum problema de acesso de alguma restrição que você queira, dá uma configuração especial no acesso por seu que você pode vir aqui e personalizar isso.
Bom, então aqui a gente com isso, a gente está pronto.
Agora a gente pode ir para o Google Data Studio.
