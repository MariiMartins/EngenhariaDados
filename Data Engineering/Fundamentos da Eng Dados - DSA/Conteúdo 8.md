# 8. DevOps para Engenheiros de Dados

## 1. [PDF] O que é DevOps?

DevOps é uma cultura e conjunto de práticas que tem como objetivo integrar as equipes de  desenvolvimento  de  software  e  operações  de  TI  (tecnologia  da  informação)  para  criar  e entregar software de forma mais eficiente e com maior qualidade.

A cultura DevOps enfatiza a colaboração e a comunicação contínua entre as equipes de desenvolvimento  e  operações,  incentivando  uma  mentalidade  de  responsabilidade compartilhada pelo sucesso da entrega de software.

As práticas DevOps incluem automação de processos de infraestrutura e deployment (implantação) de software, monitoramento e análise de métricas de performance e estabilidade, testes  automatizados  e  contínuos,  e  implementação  de  feedbacks  contínuos  e  iterações  no processo de desenvolvimento.

O objetivo final de DevOps é criar uma cultura e um processo de entrega de software eficiente, ágil e confiável, permitindo às organizações responder rapidamente às necessidades de seus usuários e do mercado

## 2. [PDF] Prática de DevOps na Engenharia de Dados

As práticas de DevOps na Engenharia de Dados têm como objetivo criar um processo eficiente  e  automatizado  de  coleta,  armazenamento,  processamento  e  análise  de  dados.
Algumas práticas comuns de DevOps na Engenharia de Dados incluem:

- **Automação de infraestrutura:** A infraestrutura de dados pode ser gerenciada por código, permitindo  a  criação  de  ambientes  de  desenvolvimento,  teste  e  produção  de  maneira consistente e previsível.
- **Controle de versão:** Todo o código e artefatos de dados podem ser armazenados em um sistema de controle de versão, permitindo o controle de mudanças e a colaboração entre as equipes de desenvolvimento e operações.
- **Integração contínua:** O código pode ser integrado e testado continuamente, permitindo a identificação precoce de erros e problemas de compatibilidade.
- **Entrega  contínua:**  As mudanças  no  código  e  na  infraestrutura podem ser  entregues rapidamente e com segurança para a produção, usando pipelines automatizados de deploy.
- **Monitoramento:**  Os dados  e  os  sistemas  de  infraestrutura podem ser  monitorados constantemente para garantir a qualidade, a estabilidade e a performance. A análise de métricas e logs pode ser usada para identificar problemas e oportunidades de melhoria.
- **Automação  de  processamento  de  dados:**  O processamento  de  dados pode ser automatizado, permitindo que novos dados sejam processados assim que estiverem disponíveis, minimizando o tempo de latência.
- **Testes automatizados:** Testes automatizados podem ser usados para garantir a qualidade dos dados e do código, permitindo a identificação precoce de erros e problemas.
Essas práticas de DevOps na Engenharia de Dados podem ajudar as equipes a trabalharem de  forma  mais  eficiente  e  colaborativa,  permitindo  a  entrega  de  soluções  de  dados  mais confiáveis e escaláveis

## 3. [PDF] O que é IaC (Infraestrutura como código)?

Infraestrutura como código (IaC) é uma prática de DevOps que consiste em gerenciar a infraestrutura de TI usando código. Em  vez  de  configurar  manualmente  servidores,  redes,  bancos  de  dados,  e  outros componentes de infraestrutura, a IaC permite que esses recursos sejam criados, configurados e gerenciados automaticamente através de código.A  IaC  é  geralmente  implementada  usando  linguagens  de  programação  ou  ferramentas específicas que permitem descrever a infraestrutura como código.

Esses códigos podem então ser   armazenados   em   sistemas   de   controle   de   versão,   permitindo   que   as   alterações   na infraestrutura sejam gerenciadas como mudanças no código.

Algumas das principais vantagens da IaC incluem:

- **Consistência:** A infraestrutura pode ser criada e configurada de maneira consistente em todos os ambientes, incluindo desenvolvimento, teste e produção.
- **Eficiência:**  A  IaC  permite  que  a  infraestrutura  seja  gerenciada  de  forma  mais  rápida  e eficiente,  reduzindo  o  tempo  e  o  esforço  necessários  para  configurar  servidores  e  outros componentes de infraestrutura.
- **Flexibilidade:**  As  configurações  de  infraestrutura  podem  ser  facilmente  alteradas  e atualizadas com base nas necessidades do aplicativo ou serviço.
- **Controle de versão:** Todas as alterações na infraestrutura são controladas e gerenciadas como mudanças no código,o que permite o controle de versão, o rastreamento e a colaboração de equipe.
A  IaC  é  frequentemente  usada  em  conjunto  com  outras  práticas  de  DevOps,  como integração contínua, entrega contínua e automação de testes, permitindo a criação de processos automatizados e consistentes para o desenvolvimento e a implantação de aplicativos e serviços.

## 4. [PDF] Como IaC é usada na Engenharia de Dados?

A Infraestrutura como código (IaC) é uma prática comum na Engenharia de Dados, pois pode ser usada para gerenciar e automatizar a criação e configuração de toda a infraestrutura necessária para processar, armazenar e analisar grandes volumes de dados.

Algumas das maneiras como a IaC é usada na Engenharia de Dados incluem:

- **Criação de ambientes de infraestrutura:** A IaC pode ser usada para criar ambientes de infraestrutura  de  dados,  incluindo  clusters  de  processamento  distribuído,  bancos  de  dados, armazenamento em nuvem, entre outros. Esses ambientes podem ser criados rapidamente e de forma consistente, garantindo que todos os ambientes estejam configurados de maneira idêntica e evitando problemas de configuração manual.
- **Configuração  de  serviços  de  processamento  de  dados:**  A  IaC  pode  ser  usada  para configurar  serviços  de  processamento  de  dados,  como  o  Apache  Spark  ou  Apache  Flink.  As configurações  desses  serviços  podem  ser  mantidas  em  código  e  versionadas,  permitindo  a colaboração e a rastreabilidade.
- **Gerenciamento de fluxos de dados:** A IaC pode ser usada para configurar e gerenciar fluxos de dados que movem dados de um ambiente para outro. Os códigos de infraestrutura podem ser usados para automatizar a criação e configuração de pipelines de dados, bem como para atualizar e modificar esses pipelines à medida que as necessidades de dados mudam.
- **Configuração  de  monitoramento  e  alertas:**  A  IaC  pode  ser  usada  para  configurar  o monitoramento de métricas de dados e infraestrutura, como uso de CPU, uso de disco, latência de rede, entre outros. Os alertas podem ser configurados para notificar automaticamente as equipes de operações quando as métricas se desviam dos valores desejados.
A IaC está se tornando uma prática essencial na Engenharia de Dados, pois permite que a infraestrutura de dados seja gerenciada como código, reduzindo o tempo e o esforço necessários para configurar e gerenciar infraestrutura complexa e permitindo que as equipes se concentrem na análise e processamento de dados em si

## 5. [PDF] CI/CD (Integração Contínua/Entrega Contínua)

Integração Contínua (CI–Continuous Integration) e Entrega Contínua (CD–Continuous Delivery)  são  práticas  de  DevOps  que  visam  automatizar  e  acelerar  o  processo  de desenvolvimento e entrega de software.

A  Integração  Contínua  é  a  prática  de  integrar  o  código  desenvolvido  por  vários desenvolvedores em um repositório central de código várias vezes ao dia. Isso significa que, sempre que um desenvolvedor faz uma alteração no código, essa alteração é integrada com o restante do código e testada automaticamente para garantir que não haja conflitos ou erros de integração.  Isso  permite  que  os  desenvolvedores  detectem  e  corrijam  rapidamente  erros  e problemas  de  compatibilidade,  reduzindo  o  tempo  e  o  esforço  necessários  para  solucionar problemas no final do ciclo de desenvolvimento.

A  Entrega  Contínua  é  a  prática  de  automatizar  o  processo  de  entrega  de  software, garantindo que o software possa ser entregue a qualquer momento com segurança e rapidez. Isso é feito através da automação de todo o processo de build, testes, empacotamento e deploy, permitindo que o software seja entregue com um clique. A Entrega Contínua também inclui a execução de testes automatizados, para garantir que o software entregue seja de alta qualidade e atenda aos requisitos de negócios e de usuários.

Juntas, a Integração Contínua e a Entrega Contínua formam a prática conhecida como CI/CD, que é uma abordagem ágil para o desenvolvimento e entrega de software. Ao adotar a CI/CD, as equipes de desenvolvimento podem trabalhar de maneira mais colaborativa, detectar e corrigir erros mais rapidamente, reduzir o tempo e o custo de entrega de software e melhorar a qualidade do software entregue.E qual a relação disso com Engenharia de Dados?

## 6. [PDF] Como aplicar CI/CD em Engenharia de Dados?

Aqui estão algumas maneiras de aplicar CI/CD na Engenharia de Dados:

- **Gerenciamento de código fonte:** É importante usar um sistema de controle de versão, como  o  Git,  para  gerenciar  o  código-fonte  do  projeto  de  dados.  Isso  permite  que  vários Engenheiros e Arquitetos de Dados trabalhem no mesmo projeto, e o versionamento de código ajuda a evitar conflitos e problemas de integração.
- **Teste automatizado:** Automação de testes para garantir que as alterações no código não interrompam  o  funcionamento  de  soluções  de  dados  já  existentes.  Isso  pode  incluir  testes unitários, testes de integração e testes de carga para verificar a escalabilidade da solução de dados.
- **Pipeline  de  dados:** Automação do  processo  de  desenvolvimento  e  implantação  de soluções de dados criando um pipeline de dados. Isso inclui o processamento, armazenamento e entrega de dados. Cada etapa do pipeline deve ser testada e validada antes de ser implementada em produção.
- **Configuração de infraestrutura como código:** Usando ferramentas como Terraform ou CloudFormation,  você  pode  automatizar  a  configuração  da  infraestrutura  necessária  para implementar uma solução de dados. Isso permite que você configure rapidamente um ambiente de teste e produção para implementar e testar soluções de dados.
- **Monitoramento e alertas:** Configuração de um sistema de monitoramento e alertas para os pipelines de dados. Isso ajudará a identificar problemas de desempenho ou erros no pipeline e permitirá que a equipe de operações de dados responda rapidamente.
- **Entrega  contínua:** Configuração de um  processo  de  entrega  contínua  que  permita  a implantação automatizada da solução de dados em um ambiente de produção. Isso ajudará a garantir que a solução de dados seja entregue rapidamente e com segurança.

Ao implementar essas práticas de CI/CD na Engenharia de Dados, você pode acelerar o tempo de entrega de soluções de dados, garantir a qualidade e a estabilidade das soluções e facilitar a colaboração entre as equipes de dados.

## 7. [PDF] Containers e Orquestração de Containers

Containers são uma tecnologia de virtualização que permite empacotar uma aplicação e suas dependências em um ambiente isolado e portável. Em outras palavras, os containers permitem que as aplicações sejam executadas de forma isolada  do  sistema  operacional  e  de  outras  aplicações,  enquanto  mantém  todas  as  suas dependências e bibliotecas necessárias em um único pacote portátil.A orquestração de containers é uma técnica usada para gerenciar e escalonar aplicativos em containers.

Ela permite que as aplicações sejam implantadas e gerenciadas em vários hosts, criando uma rede virtual que permite que os containers se comuniquem entre si. Além disso, a orquestração  permite  que  a  escalabilidade  e  a  resiliência  das  aplicações  sejam  gerenciadas  de forma automática. Usamos containers e orquestração de containers na Formação Arquiteto de Dados e Formação Engenheiro de Dados aqui na DSA.

As ferramentas de orquestração de containers mais populares são o Kubernetes, o Docker Swarm   e   o   Apache   Mesos.   Essas   ferramentas   permitem   a   criação,   gerenciamento   e escalonamento de aplicativos em containers de maneira fácil e eficiente.

Algumas  das  principais  vantagens  do  uso  de  containers  e  orquestração  de  containers incluem:

- **Portabilidade:**   Os   containers   podem   ser facilmente   movidos   entre   ambientes   de desenvolvimento, teste e produção, permitindo que as aplicações sejam implantadas de forma rápida e consistente em diferentes ambientes.
- **Escalabilidade:** A orquestração de containers permite que as aplicações sejam escaladas rapidamente para atender às demandas de tráfego.
- **Resiliência:** Os containers podem ser reiniciados automaticamente em caso de falha ou erro, garantindo que as aplicações estejam sempre disponíveis.
- **Eficiência:**  A  utilização  de  containers  permite  que os  recursos  de  hardware  sejam compartilhados  entre  várias  aplicações,  reduzindo  o  desperdício  de  recursos  e  aumentando  a eficiência.
- **Flexibilidade:**  Os  containers  permitem  que  as  aplicações  sejam  empacotadas  de  forma modular, o que facilita a manutenção e atualização de diferentes componentes do aplicativo

## 8. [PDF] Como usar containers em Engenharia de Dados?

Os containers são uma tecnologia de virtualização que pode ser usada em Engenharia de Dados  para  ajudar  a  criar,  gerenciar  e  implantar  aplicativos  de  dados. Aqui  estão alguns exemplos:

- **Desenvolvimento e teste de soluções de dados:** Os containers podem ser usados para criar ambientes de desenvolvimento e teste para soluções de dados. Isso pode incluir a criação de clusters de bancos de dados, ambientes de processamento de dados e outras infraestruturas de  dados.  Os containers  podem  ser  criados  rapidamente  e  facilmente,  o  que  permite  aos Engenheiros de Dados criar e testar soluções de dados de maneira mais eficiente, exatamente como ensinamos na Formação Engenheiro de Dados.
- **Implantação  de  soluções  de  dados:**  Os  containers  podem  ser  usados  para  implantar soluções de dados em ambientes de produção. Os containers permitem que as soluções de dados sejam empacotadas e implantadas de forma consistente em diferentes ambientes, incluindo ambientes de nuvem e on-premises(local).
- **Orquestração  de  clusters  de  bancos  de  dados:** Os containers podem ser usados para orquestrar  clusters  de  bancos  de  dados,  permitindo  que  os  bancos  de  dados  sejam dimensionados rapidamente e gerenciados de maneira eficiente. Ferramentas de orquestração de containers, como o Kubernetes, podem ser usadas para gerenciar clusters de bancos de dados e permitir que eles sejam dimensionados horizontalmente em resposta a aumentos de demanda.
- **Processamento  de  dados  distribuídos:**  Os  containers  podem  ser  usados  para  criar ambientes de processamento de dados distribuídos. Isso pode incluir a implantação de clusters Apache  Hadoop  ou  Apache  Spark  em  containers.  Isso  permite  que  os  processos  de processamento  de  dados  sejam  escalados  horizontalmente  e  gerenciados  de  maneira mais eficiente.
- **Automação de processos de dados:** Os containers podem ser usados para automatizar processos de dados. Isso pode incluir a criação de pipelines de dados em contêineres, permitindo que  os  dados  sejam  processados  de  maneira  eficiente  e  consistente.

## 9. [PDF] Cloud Computing x Solução Local para Engenharia de Dados

A decisão de usar Cloud Computing ou uma solução local para a Engenharia de Dados dependerá dos requisitos específicos do projeto, das necessidades da empresa e do orçamento disponível. Cada abordagem tem suas vantagens e desvantagens.
Cloud  Computing  é  uma  abordagem  que  permite  que  os  recursos  de  computação, armazenamento e rede sejam alugados sob demanda em provedores de nuvem, como Amazon Web Services (AWS), Microsoft Azure ou Google Cloud Platform.

Essa abordagem oferece várias vantagens para a Engenharia de Dados:

- **Escalabilidade:** A nuvem permite escalar recursos de computação e armazenamento com base nas necessidades do projeto, permitindo que os recursos sejam aumentados ou diminuídos conforme necessário.
- **Redução de custos:** A nuvem permite que as empresas paguem apenas pelos recursos que usam, sem a necessidade de investir em infraestrutura local. Isso pode ser especialmente vantajoso para projetos que exigem recursos de computação e armazenamento intensivos.
- **Facilidade  de  acesso:**  A  nuvem  permite  que  as  equipes  acessem  os  recursos  de Engenharia de Dados de qualquer lugar, desde que tenham acesso à Internet.
- **Manutenção  simplificada:**  Os  provedores  de  nuvem  geralmente  gerenciam  a manutenção e atualização dos recursos de infraestrutura, liberando as equipes de TI para se concentrarem em outras áreas de trabalho.

Por outro lado, uma solução local de Engenharia de Dados oferece outras vantagens, incluindo:

- **Controle  total:**  Uma  solução  local  oferece  às  empresas  controle  total sobre  sua infraestrutura de dados, incluindo segurança, privacidade e conformidade.
- **Latência de rede:** Em alguns casos, a latência de rede pode ser um problema para projetos de Engenharia de Dados em nuvem, especialmente para projetos que exigem grandes volumes de dados e latências baixas.
- **Investimento inicial:** O uso de uma solução local de Engenharia de Dados pode exigir um grande  investimento  inicial  em  hardware,  software  e  licenças, mas  que  pode  ser  usado  por diversos anos em muitos diferentes projetos.

A decisão  de  usar  Cloud  Computing  ou  uma  solução  local  de Engenharia  de Dados dependerá dos requisitos específicos do projeto, das necessidades da empresa e do orçamento disponível. Cada abordagem tem suas vantagens e desvantagens, e cabe às empresas avaliar os prós e contras de cada opção antes de tomar uma decisão.

## 10. [PDF] Principais Soluções de IaC para Engenharia de Dados

Existem várias soluções de IaC (Infraestrutura como Código) disponíveis no mercado. Aqui estão algumas das principais soluções de IaC:

- **Terraform:**  Terraform  é  uma  ferramenta  de  IaC  de  código  aberto  desenvolvida  pela HashiCorp. Ele permite que os usuários definam, gerenciem e provisionam a infraestrutura em vários provedores de nuvem, incluindo AWS, Microsoft Azure e Google Cloud Platform, além de provedores on-premises.
- **Ansible:** Ansible é uma plataforma de automação de TI que inclui recursos de IaC. Ele permite que os usuários gerenciem a configuração de servidores e outras máquinas remotas de forma automatizada, usando arquivos YAML que descrevem o estado desejado da infraestrutura.
- **Puppet:** Puppet é uma plataforma de gerenciamento de configuração que permite que os usuários gerenciem a configuração de servidores e outras máquinas remotas. Ele permite que os usuários definam a configuração da infraestrutura usando uma linguagem de programação de código aberto.
- **Chef:** Chef é uma plataforma de gerenciamento de configuração que permite que os usuários  gerenciem  a  configuração  de  servidores  e  outras  máquinas  remotas.  Ele  usa  uma linguagem de programação própria para definir a configuração da infraestrutura.
- **CloudFormation:** CloudFormation é uma solução de IaC da Amazon Web Services (AWS) que permite que os usuários definam e provisionam recursos da AWS em um arquivo de modelo. Ele usa um formato JSON ou YAML para definir a infraestrutura e os recursos necessários para executar os aplicativos em uma nuvem da AWS.

Essas  são  apenas  algumas  das  principais  soluções  de  IaC  disponíveis  atualmente.  A escolha  da  solução  certa  dependerá  das  necessidades  específicas  de  cada  empresa,  dos provedores de nuvem em uso e da equipe de TI disponível para gerenciar a infraestrutura.É importante avaliar as soluções de IaC disponíveis no mercado e escolher aquela que melhor atende às necessidades de cada projeto.

## 11. [PDF] Plataforma Databricks

Databricks é uma plataforma de análise e inteligência artificial baseada em nuvem que pode  ser  usada  em Engenharia  de Dados  para  ajudar  a  criar,  gerenciar  e  analisar  grandes conjuntos de dados.

Aqui estão algumas maneiras de usar a plataforma Databricks em Engenharia de Dados:

- **Processamento de dados em larga escala:** A plataforma Databricks é construída sobre o Apache Spark, um framework de processamento de dados em larga escala. Isso permite que a plataforma seja usada para processar grandes conjuntos de dados de maneira eficiente, escalável e distribuída.
- **Implantação  de  soluções  de  dados:**  A  plataforma  Databricks  pode  ser  usada  para implantar soluções de dados em nuvem. A plataforma permite que os usuários criem ambientes de desenvolvimento e teste de maneira fácil e rápida, além de implantar soluções de dados em produção em um ambiente de nuvem seguro e escalável.
- **Análise  de  dados:**  A  plataforma  Databricks  oferece  recursos  de  análise  de  dados avançados, permitindo que os usuários executem análises complexas em grandes conjuntos de dados.  A  plataforma  também  oferece  recursos  de  visualização  de  dados,  permitindo  que  os usuários criem gráficos e dashboards para visualizar os resultados das análises.
- **Aprendizado  de  máquina:** A plataforma Databricks Inclui recursos de aprendizado de máquina(Machine Learning), permitindo que os usuários treinem modelos de aprendizado de máquina em grandes conjuntos de dados. A plataforma oferece recursos de automação de fluxo de trabalho, permitindo que os usuários criem fluxos de trabalho de aprendizado de máquina complexos e escaláveis.
- **Colaboração:**  A  plataforma  Databricks  é  projetada  para  facilitar  a  colaboração  entre equipes de Engenharia de Dados e Cientistas de Dados. A plataforma permite que os usuários compartilhem código, dados e notebooks, além de colaborar em tempo real em projetos de dados.

Databricks é uma plataforma poderosa para Engenharia de Dados, oferecendo recursos de processamento de dados em larga escala, implantação de soluções de dados em nuvem, análise de dados, aprendizado de máquina e colaboração. Ao usar a plataforma Databricks, as empresas podem processar grandes conjuntos de dados de maneira eficiente, criar soluções de dados escaláveis e seguras, executar análises avançadas e treinar modelos de aprendizado de máquina.

Visite o site oficial da plataforma: <https://www.databricks.com>

## 12. [PDF] Modern Data Stack

Modern Data Stack, ou simplesmente MDS, é uma abordagem moderna e integrada para gerenciamento  de  dados,  que  envolve  a  combinação  de  várias  ferramentas,  serviços  e tecnologias em uma única plataforma.A  abordagem  MDS  busca  resolver  alguns  dos  desafios  comuns  enfrentados  pelas empresas na gestão de dados, como a necessidade de integrar dados de várias fontes, manter dados  limpos  e  consistentes,  realizar  análises  avançadas  e  fornecer  insights  acionáveis  aos usuários finais.

O Modern Data Stack combina diferentes tecnologias e ferramentas, incluindo:

- **Armazenamento de dados:** Bancos de dados como Amazon Redshift, Google BigQuery, Snowflake e Microsoft Azure Synapse Analytics são frequentemente usados para armazenar e gerenciar grandes volumes de dados em nuvem.
- **Integração de dados:** Plataformas como Fivetran, Stitch e Talend ajudam a integrar dados de várias fontes e transformá-los em um formato compatível para análise.
- **Ferramentas  de  análise:**  Plataformas  de  análise,  como  Tableau,  Looker  e  Power  BI, permitem que os usuários criem visualizações e dashboards para análise de dados.
- **Processamento de dados:** Plataformas de processamento de dados em tempo real, como Apache Kafka e Apache Flink, permitem o processamento em tempo real e a análise de dados em streaming.
- **Automação de fluxo de trabalho:** Plataformas de automação, como Airflow e Prefect, permitem a automação de fluxos de trabalho de dados.
- **Infraestrutura em nuvem:** Serviços de nuvem, como Amazon Web Services, Microsoft Azure  Google  Cloud  Platform,  fornecem  infraestrutura  em  nuvem  escalável  e  segura  para executar as ferramentas de Modern Data Stack.

Ao  combinar  essas  tecnologias  e  ferramentas,  o  Modern  Data  Stack  permite  que  as empresas gerenciem seus dados de forma mais eficiente e eficaz. A abordagem MDS também permite  que  as  empresas  aproveitem  as  vantagens  da  nuvem,  incluindo  escalabilidade, flexibilidade e redução de custos

## [13. Quiz](https://github.com/MariiMartins/EngenhariaDados/blob/e0586d7a13df852874632d8b74c1b79e9a748b39/Fundamentos%20da%20Eng%20Dados%20-%20DSA/QUIZ/8.13%20-%20Quiz.md)
