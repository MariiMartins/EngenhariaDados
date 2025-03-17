150. AIM para o Glue
Bom a primeira etapa que nós vamos fazer e a gente vai criar a função IAM
para que o Glue possa executar funções no AWS durante a sua execução.
Então a gente vai criar aqui uma função IAM com bastante privilégio, porque aqui é um ambiente de ensino. Então, a gente vai criar aqui uma função de administrador especificamente para o serviço do Glue.

Então a gente quer criar uma nova função para que o Glue possa utilizar.
Então eu vou clicar aqui, criar função.Vejam que aqui a gente quer uma função para um serviço. O Glue é um serviço AWS, então a gente pode manter o serviço da AWS marcado.
Casos de uso comuns aqui tem o dois. O Lambda e o EC2, no caso não vai ser nenhum desses dois. Então ele vai ter que pesquisar aqui o que vamos digitar aqui Glue, e clicar em próximo. Agora aqui a gente vai escolher as políticas e, como eu falei, vamos dar uma política de administração aqui.
Vamos buscar aqui o administrator Access.
Aqui, selecionamos próximo. A gente tem que dar um nome para a função.
E como a função está definida em Json e vamos aqui criar a função. Então, agora a nossa função está criada e a gente pode, então, a partir desse momento, utilizá-la no Glue.
