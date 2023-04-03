Bom, nessa última parte a gente vai falar de segurança com relação ao S3 especificamente, que a gente vai falar de criptografia de objetos para o S3. Então, existem quatro métodos de que de criptografia para objetos no S3.

Então a gente tem primeiramente o SSE –S3. E se esse significa server side encryption, ou seja, que o servidor ele cuida da criptografia.
Então existem três métodos de criptografia do lado do servidor.
Existe também criptografia do lado do cliente. O SSE-S3 a criptografia dos objetos usam chaves criadas e gerenciadas pelo AWS, então você não tem acesso a essas chaves.Você não vai cuidar dessas chaves geralmente, a criptografia é composta por uma chave, uma chave privada, e quem vai fazer o gerenciamento dessas chaves é o próprio a AWS.

Depois existe o SSE-KMS, que usa o serviço de gestão de chaves do AWS para fazer a gestão dessas chaves. Você tem uma segurança adicional, você tem acesso a essas chaves e existe uma trilha de auditoria dessas chaves.

Depois existe o SSE- C. Então, lembrando que aqui também é gerenciado pelo servidor e aí você faz o gerenciamento completo da sua chave não é mais o a AWS. Você faz o gerenciamento e também você pode fazer a criptografia dos dados no lado do cliente, ou seja, antes de enviar para o S3.

De uma perspectiva de análise de dados engenharia de dados, o SSE-S3 e o SSE-KMS são as mais utilizadas.
Voce  colocar o SSE-C quando você faz o gerenciamento das suas chaves, você coloca um complicador a mais aí no gerenciamento dos dados, a gente vai ver um pouquinho melhor então.

SSE-S3 e o SSE- KMS.
Então esse SSE-S3 então você tem um objeto, você tem lá o a AWS, o serviço de S3 do AWS. Lá dentro você vai ter um bucket e você vai enviar esse objeto por HTTPS e você vai ter uma chave gerenciada pelo AWS, que vai realizar a criptografia e vai disponibilizar esses dados no Bucket. Então como eu mencionei, você não tem ideia que chave é essa que a gente não tem contato, então faz o gerenciamento dessa chave.

No SSE-Kms você tem gerenciamento, você tem controle da chave, então você tem um pouco mais de sensação de segurança, mas você tem que cuidar das chaves. Então você tem o objeto, você envia o objeto para o S3 através de HTTPS e  vai ter lá um gerenciamento de chaves. Você vai ter lá o Custom Master Key que você vai criptografar esse objeto e ele vai ficar disponível lá no S3.

Bom, outros aspectos de segurança do S3, então você pode controlar a segurança baseado no usuário, você pode criar políticas IAM e você pode definir quais chamadas vão ser permitidas para usuários específicos. E você pode controlar a segurança baseada em recursos. Então, por exemplo, você pode criar políticas de buckets, então são regras que são baseadas nos buckets.
Você pode ter listas de controle de acessos a objetos, que são ACL que você dá um controle mais detalhado e você pode ter uma lista de controle de acesso ao bucket. Então, veja você pode controlar o acesso diretamente individualmente a cada objeto, dentro do bucket ou a todo o bucket.

Políticas de bucket do S3:
Você tem políticas baseadas em configuração de JSON. Onde você vai definir buckets e objetos, definir APIs que vão permitir ou negar.
Você vai ter uma  conta ou usuário que aplica essa política ao bucket através de uma configuração JSON.
 
Você pode usar a política do Bucket S3 para dar acesso público ao bucket.
É muito comum ter Buckets que têm acesso público, Você pode forçar objetos a serem criptografados já no upload, a gente vai ver isso na aula prática e você pode dar acesso a outra conta que a conta cruzada.

Então você dá uma outra conta do S3 Você pode dar acesso ao seu bucket
Outros aspectos de segurança do S3 você pode ter uma VPC, que é uma rede privada, em vez de ela estar a ter acesso público à internet.
Você tem uma VPC e você garante que seus serviços privados, por exemplo, SageMaker, que é uma aplicação de dados possa acessar o S3.
Você pode habilitar log de auditoria log de acesso ao S3, que pode ser armazenado no próprio bucket do S3.
E chamadas do API podem ser ligadas a AWS CloudTrail, que é um serviço do a AWS.

Baseado em Tags, então você combina políticas a ele, políticas do bucket e por exemplo, você pode adicionar a tag classificação igual a PHI, que são dados de saúde pessoais a seus objetos.
Então a gente vai ver alguns desses aspectos agora, na prática, lá no S3.
