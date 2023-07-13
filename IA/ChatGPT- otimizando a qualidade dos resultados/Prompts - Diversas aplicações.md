# Prompts - Diversas aplicações

Podemos escrever prompts para diversas finalidades, tanto para nosso dia-a-dia quanto no ambiente de trabalho. Nos vídeos anteriores utilizamos prompts para resumo de textos, tradução e até mesmo para analisar os sentimentos de pessoas que compraram um produto. Vamos explorar mais algumas possibilidades?

## Transformando o tom de voz

Vanessa é uma influenciadora digital que compartilha dicas de maquiagem e produtos de beleza em suas redes sociais. Ela recentemente publicou uma análise crítica sobre um novo lançamento de uma marca famosa de cosméticos, destacando alguns pontos negativos do produto. No entanto, ela percebeu que seu tom de voz inicial poderia ter sido um pouco duro. Ela teve a ideia de reescrever seu texto com o ChatGPT, usando um tom mais amigável e objetivo, para transmitir sua opinião de forma equilibrada e respeitosa aos seus seguidores(as).

Vamos tentar escrever um prompt com essa finalidade?

Reescreva o texto abaixo delimitado por “””, deixando seu tom de voz mais simpático e amigável:

Texto: “”” Eu testei o novo lançamento da marca XYZ e, para ser sincera, fiquei extremamente decepcionada. A qualidade do produto é simplesmente terrível. A embalagem é frágil e quebrou logo no primeiro uso, além disso, a pigmentação das sombras é fraca e a durabilidade é praticamente inexistente. Não entendo como uma marca renomada pode lançar algo tão ruim no mercado. Não recomendo de forma alguma! ”””

Como resultado temos o novo texto:

```
"Eu tive a oportunidade de experimentar o mais recente lançamento da marca XYZ e, para ser sincera, acabei me decepcionando um pouco. Fiquei surpresa com a qualidade do produto, que não atendeu às minhas expectativas. A embalagem acabou se mostrando um pouco frágil, infelizmente quebrou logo no primeiro uso. Além disso, percebi que a pigmentação das sombras não é tão intensa quanto eu gostaria, e a durabilidade deixou um pouco a desejar também. Confesso que fiquei um tanto perplexa, pois esperava mais dessa marca renomada. Enfim, minha opinião é de que talvez esse produto não seja o melhor investimento, então não o recomendaria com muita ênfase."
```

Note como dessa forma o texto está menos duro e agressivo! Usar o ChatGPT para mudar o tom de voz de um texto pode ser interessante por várias razões. Aqui estão algumas delas:

Versatilidade: O ChatGPT é capaz de gerar texto em diferentes estilos e tons de voz. Ele pode transformar um texto formal em um texto mais casual, ou vice-versa. Isso permite adaptar o conteúdo para diferentes públicos ou situações, tornando-o mais envolvente e adequado ao propósito desejado.

- **Personalização:** Com o ChatGPT, é possível personalizar o tom de voz para se adequar ao estilo de uma marca, empresa ou indivíduo específico. Isso é especialmente útil em áreas como marketing e publicidade, onde a consistência da voz da marca é crucial para construir uma identidade sólida.

- **Adaptação a diferentes plataformas:** Cada plataforma ou canal de comunicação tem suas próprias nuances e expectativas em relação ao tom de voz. O ChatGPT pode ajudar a adaptar o conteúdo para diferentes plataformas, como redes sociais, blogs, e-mails, entre outros, para que ele se alinhe com a linguagem e o estilo apropriados.

- **Criatividade e entretenimento:** Mudar o tom de voz de um texto pode ser uma forma de estimular a criatividade e criar conteúdo divertido e original. É possível experimentar diferentes estilos narrativos, tornando histórias mais cativantes e envolventes.

- **Acessibilidade:** O uso do ChatGPT para alterar o tom de voz de um texto também pode beneficiar a acessibilidade. Por exemplo, o ChatGPT pode ajudar a adaptar o tom para melhorar a descrição textual para que as pessoas cegas possam compreender com mais detalhes o conteúdo.

## Convertendo formatos
Allan, um analista de dados, recebeu um conjunto de informações no formato de dicionário Python. Porém, ele precisa converter esses dados para o formato CSV (comma-separated values) para poder importá-los para o Google Sheets e realizar análises mais avançadas. Ele decidiu usar o ChatGPT para ajudar na tarefa de conversão.

Como poderíamos escrever um prompt para isso? É importante contextualizar o ChatGPT, dizendo que temos alguns dados que estão armazenados em um dicionário Python e também é bacana dizer qual é o nome desse dicionário. Depois disso, podemos pedir que ele escreva os dados no formato desejado e que retorne apenas os dados nesse formato.

O prompt segue uma sequência lógica de informações, começando com a contextualização, passando pela descrição do problema e finalizando com a solicitação específica ao modelo:

Temos alguns dados armazenados em um dicionário Python chamado “funcionários” . Escreva esses dados no formato CSV. Retorne apenas o CSV.

```
funcionarios = {
    '001': {
        'nome': 'João',
        'idade': 30,
        'cargo': 'Gerente',
        'salario': 5000.00
    },
    '002': {
        'nome': 'Maria',
        'idade': 25,
        'cargo': 'Analista',
        'salario': 3500.00
    },
    '003': {
        'nome': 'Pedro',
        'idade': 28,
        'cargo': 'Desenvolvedor',
        'salario': 4000.00
    }
}
```

CSV:
O resultado será o seguinte:
```
001,João,30,Gerente,5000.00 002,Maria,25,Analista,3500.00 003,Pedro,28,Desenvolvedor,4000.00
```

Conseguimos obter os dados no formato desejado com o prompt escrito acima. Aqui temos apenas um exemplo, utilizando código, mas fique à vontade para explorar diferentes formatos.

## Verificação ortográfica/verificação gramatical

Carol precisa escrever um artigo para uma demanda do trabalho e quer ter certeza de que seu texto está livre de erros ortográficos e gramaticais antes de entregá-lo. Então, ela decide usar o ChatGPT para verificação ortográfica e gramatical. Como ela poderia escrever um prompt para essa tarefa? Que tal usar o seguinte prompt?

Revise e corrija o texto abaixo delimitado por “””. Reescreva a versão corrigida.

Texto: “”” Quando uma historia esta sendo contada ocorre a ativação de partes do cerebro que permitem que quem esteja ouvindo consiga transformar a historia em suas próprias ideias e experiências. No artigo “Speaker–listener neural coupling underlies successful communication” de 2010, publicado na revista PNAS, temos uma estudo de como isso acontece. Na imagem abaixo, retirada do artigo, nós temos a atividade neural de um par de pessoas, sendo uma delas a falante e outra a ouvinte durante uma narrativa. Em A temos a captura da gravaçao da narrativa e em B está o acoplamento neural falante-ouvinte, que foi avaliado através do uso de um modelo linear geral, no qual as séries temporais no cerebro da pessoa que estava falando são usadas para prever a atividade no cérebro da pessoa ouvinte. Esse estudo mostrou que a atividade da pessoa falante é espacial e temporalmente acoplada à atividade da ouvinte. Por conta disso esse acoplamento desaparece quando os participantes não conseguem se comunicar. “””

O resultado da revisão e correção é o seguinte:

    "Quando uma história está sendo contada, ocorre a ativação de partes do cérebro que permitem que quem esteja ouvindo consiga transformar a história em suas próprias ideias e experiências.

    No artigo "Speaker-Listener Neural Coupling Underlies Successful Communication", publicado em 2010 na revista PNAS, temos um estudo sobre como isso acontece. Na imagem abaixo, retirada do artigo, temos a atividade neural de um par de pessoas, sendo uma delas a falante e a outra a ouvinte durante uma narrativa. Em A, temos a captura da gravação da narrativa, e em B está o acoplamento neural falante-ouvinte, que foi avaliado por meio do uso de um modelo linear geral. Nesse modelo, as séries temporais no cérebro da pessoa que estava falando são utilizadas para prever a atividade no cérebro da pessoa ouvinte.

    Esse estudo mostrou que a atividade da pessoa falante é espacial e temporalmente acoplada à atividade da ouvinte. Por conta disso, esse acoplamento desaparece quando os participantes não conseguem se comunicar."

Com isso, podemos concluir que o ChatGPT conseguiu analisar o texto e entender quais palavras estavam com possíveis erros ortográficos. Ele também conseguiu checar a pontuação inadequada e fez correções.

## Criando respostas automáticas para e-mails
Uma empresa de comércio eletrônico recebe centenas de e-mails por dia dos clientes com perguntas sobre pedidos, informações de produtos, políticas de devolução, entre outros. Devido ao grande volume de emails, a equipe de atendimento ao cliente está sobrecarregada e leva muito tempo para responder a todas as perguntas.

Além disso, a falta de padronização nas respostas resulta em inconsistências e erros de comunicação. Nesse sentido, o uso de respostas automáticas economiza tempo e esforço ao evitar a necessidade de escrever respostas individuais para cada email recebido. Isso é particularmente útil em situações em que muitos e-mails precisam ser respondidos rapidamente.

Abaixo temos o exemplo de um prompt, criado para responder um e-mail sobre a resenha de um produto. Podemos começar pedindo para o ChatGPT agir como um assistente de atendimento ao cliente e ir passando quais tarefas ele terá que executar. Note que nós estamos utilizando as boas práticas:

1) dividindo a grande tarefa em tarefas menores e;

2) utilizando delimitadores para separar a resenha de todas as instruções. Também pedimos para que ele analise o sentimento da resenha e dê a resposta de acordo com o sentimento da pessoa.

Além disso, o tom de voz foi especificado, deixando com um tom conciso e profissional:

```
Você é um assistente de IA de atendimento ao cliente. Sua tarefa é enviar uma resposta por e-mail a um(a) cliente. Dado o e-mail do(a) cliente delimitado por """", gere uma resposta para agradecer ao cliente por sua avaliação. Se o sentimento for positivo ou neutro, agradeça por sua revisão. Se o sentimento for negativo, peça desculpas e sugira que eles entrem em contato com o atendimento ao cliente. Certifique-se de usar detalhes específicos da resenha. Escreva em um tom conciso e profissional. Assine o e-mail como Atendimento ao cliente.

Resenha: """Entrega: rápida e muito eficiente, amei aprovado. Estética liquidificador: linda, não tem o que falar, visualmente é lindo. Potência: ótima, bate bem as coisas, mas se for fazer algo como massa e triturar algo não bate muito bem, são apenas 4 lâminas e elas não pegam bem no final, acaba dando mais trabalho, já tive liquidificador de 6 lâminas e amei a experiência, mas se o seu caso não for esse, é ótimo. Copo: ele é lindo, mas frágil, parece que a qualquer momento pode cair e quebrar do nada, como muito frágil e arranha muito fácil, mas a tampa veda bem e tem medidor em todo o copo e isso é ótimo, fácil também de limpar. Contexto geral: o liquidificador é bom, única coisa de ponto negativo é o quesito das lâminas e que o encaixe do copo com o morto não é bem travado, não tem trava de segurança, e ele fica a todo tempo querendo sair do motor e isso é ruim, deveriam prestar mais atenção a isso, pois é um fator de risco para os consumidores em geral. """

Sentimento da resenha:
```

Ao executar o prompt, a resposta do ChatGPT foi a seguinte:

O sentimento geral da resenha é uma combinação de sentimentos positivos e negativos. Alguns aspectos do produto foram apreciados, enquanto outros apresentaram problemas ou preocupações. Para responder ao cliente, você pode usar a seguinte resposta:

```
Caro(a) cliente,

Agradecemos sinceramente por compartilhar sua avaliação detalhada do nosso liquidificador. A opinião dos nossos clientes é extremamente importante para nós.

Ficamos contentes em saber que a entrega foi rápida e eficiente, e que você apreciou a estética do liquidificador. Também estamos felizes em saber que a potência do produto atende às suas necessidades na maioria das tarefas.

Pedimos desculpas pelos problemas que você encontrou com as lâminas e o encaixe do copo. Levaremos suas observações em consideração para aprimorar esses aspectos em futuras versões do produto. Sua preocupação em relação à segurança é válida, e faremos o possível para melhorar o design do liquidificador. Para resolver as questões específicas que você mencionou, gostaríamos de encorajá-lo(a) a entrar em contato com nosso atendimento ao cliente. Nossa equipe estará à disposição para fornecer assistência adicional e encontrar uma solução que atenda às suas necessidades.

Agradecemos novamente por sua revisão e por compartilhar sua experiência conosco. Sua opinião é valorizada e nos ajuda a aprimorar continuamente nossos produtos e serviços.

Atenciosamente,

Atendimento ao cliente
```
Conseguimos criar uma resposta com base no sentimento da pessoa! Incrível, né?!

Esses foram apenas alguns exemplos de como podemos criar prompts utilizando todas as boas práticas que aprendemos no decorrer do curso. Existem muitas outras maneiras de aplicar esses conceitos e a chave é encontrar maneiras de tornar a sua vida mais eficiente e produtiva com a ajuda dos prompts.
