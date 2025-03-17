20. Riscos Parte III

A qualidade dos dados é um problema crônico e global, e os sistemas de onde se originam os dados em geral, no melhor caso, são pensados e manter a operação. A gente já falou sobre isso. Os sistemas de processamento de transações.

O dado é coletado, processado, produz uma saída de sua vida útil nesse sistema praticamente acabou.
No pior caso, são usados mecanismos de entradas de dados arcaicos, que sequer dispõem de recursos para minimizar problemas de qualidade. Ou seja, o usuário entra qualquer tipo de informação.
O resultado disso às vezes são décadas de dados que por muitas vezes são inúteis ou economicamente inviáveis de serem aproveitados em qualquer tipo de processo analítico. Ou seja, esses sistemas ficaram por décadas recebendo entrada de dados com qualidade, que se você pensar, por exemplo, em um DataWarehouse, não servem para nada.

Existem, claro, muitas e excelentes ferramentas de qualidade de dados que minimizam problemas de entrada de dados inválidos, sujos, com problemas, mas claro que não é um milagre. Em alguns casos, apenas uma intervenção manual registro a registro agregaria valor aos dados, o que pode, obviamente, tornar o projeto inviável do ponto de vista de tempo, do ponto de vista financeiro. Então, a qualidade dos dados é um fator que pode, em muitos casos e bastante comum, inviabilizar o projeto. Então, a equipe do projeto tem que estar de olho neste requisito, nessa questão, já no início do projeto.

Existe um plano. Independente da questão de se avaliar a qualidade dos dados. Existe um plano de limpeza e tratamento de dados.

Então, o que é um plano de limpeza de dados?
A gente está falando de ferramentas de limpeza, de dados e está falando de um processo de limpeza e tratamento de dados, e a gente está falando de um orçamento e isso vai ter algum custo para o projeto.

Outra questão importante todas as fontes de dados do projeto foram identificadas? Quer dizer, às vezes acontece de lá, no meio do projeto, você saber que uma determinada informação, que é vital para o tipo de análise que se está, que se está buscando, buscando desenvolver, ela não existe ou ela não é acessível. Então, é preciso identificar todas as fontes do projeto, as fontes de dados, certo?
Uma questão importante é o chamado sistema sombra. O que são sistemas sombra?

Bom, toda empresa tem alguns sistemas. Geralmente, alguns grandes sistemas departamentais que mantêm as operações. Porém, toda empresa, sem exceção, também tem diversos sistemas paralelos. Pode ser pequeno software que resolve algum problema.Como pode ser planilhas, e o que acontece às vezes. 
Os requisitos do projeto obrigatoriamente passam pela coleta de dados de sistemas sombras e você vai ter que identificar esses sistemas. E quando esses sistemas são em planilhas que não estão sequer em uma pasta compartilhada, estão em uma pasta privada, em um computador de algum usuário. E quando você coloca essa planilha no seu processo de gestão de dados e o usuário simplesmente vai lá e muda a planilha, muda a estrutura da planilha. Então, são questões que têm que ser consideradas já no projeto.

E outra questão. Todas as fontes de dados do projeto são acessíveis? Bom, você identificou todas as fontes do projeto, mas elas são acessíveis.

O que quer dizer isso?
Quer dizer que existem fontes de dados de sistemas antigos, por exemplo, que são dados a arquivos proprietários, que não se consegue ler esses arquivos nem com um ODBC.

O que você vai fazer se lá no meio do projeto você descobre que determinado dado que você precisa é um desses tipos de fontes de dados?

Outra coisa existem sistemas que criptografam alguns dados. Eles armazenam esses dados de forma criptografada.
Como que você vai ler essas informações? Elas são criptografadas pelo próprio software, a chave privada da criptografia está no software ela não é pública. Como você vai fazer?

Às vezes, é inviável você obter certos tipos de dados e as fontes de dados possuem documentação apropriada. Então, é comum hoje você encontrar sistemas que têm centenas ou até milhares de tabelas. E é comum também você encontrar, por exemplo, sistemas cujas tabelas foram geradas por um gerador de aplicação que as tabelas o nome das tabelas foram criadas de forma sequencial. A mesma coisa as colunas. Então, por exemplo, se você precisa de uma tabela de faturamento, por exemplo, como que você vai encontrar qualquer tabela de faturamento? Se as tabelas foram geradas de forma sequencial ou foram abreviados com cinco dígitos e não existe um único documento com relação a esta estrutura de dados? 
Talvez você possa resolver isso com uma ferramenta de sniffer que fica lá monitorando as consultas enquanto se usa o sistema. Só que, mesmo assim, quanto tempo isso vai demandar a mais do projeto até você identificar todas as fontes de dados que você precisa?

A latência entre a produção da informação e a carga é suficiente viável para produção de valor? Então, imagine, por exemplo, que você é que você precisa desenvolver o sistema que vai criar um modelo preditivo de streaming em tempo real para prevenção de fraude. Só que os dados de transação eles estão na nuvem, você vai processar isso no seu ambiente On Prairie, mas os dados estão na nuvem. E se o volume, o tempo entre a extração dos dados, a carga e a aplicação sobre o modelo não for suficiente, quer dizer, a latência for maior do que é possível e admissível pelo modelo de negócio. Ou seja, você só vai identificar se a transação é fraudulenta ou não num tempo em que isso não serve mais para nada.

O sistema, por exemplo ele não podia mais esperar o retorno do resultado dessa avaliação. Então, você precisa sempre avaliar se, dentro da arquitetura que está proposta, se é possível desenvolver esta funcionalidade e entregar este valor com a arquitetura da forma que ela se apresenta, com as ferramentas que foram propostas. Obviamente que em alguns casos você pode achar soluções alternativas.