# 7. Data Quality, Data Lineage e Data Observability
<!--

## 1. O que é qualidade dos Dados (Data Quality)?

Data Quality é a medida da qualidade dos dados, ou seja, de quanto os dados são confiáveis.
É importante para garantir que os dados sejam precisos, consistentes e úteis para suportar as decisões de negócios.
Qualidade dos Dados é a medida da condição dos dados com base em fatores como precisão, integridade, consistência, confiabilidade e se estão atualizados.

## 2. Como medir qualidade dos Dados (Data Quality)?

A medida da qualidade de dados pode ser feita usando uma combinação de técnicas estatísticas e metodologias de avaliação. Alguns dos indicadores comuns incluem a precisão, a completude, a consistência, a integridade e a atualização dos dados.
Também pode ser necessário avaliar a relevância dos dados para o negócio e a facilidade de uso dos dados para os destinatários.
Existem vários fatores e métricas que podem ser usados para medir a qualidade dos dados. Os mais comuns são:
    - precisão
    - exatidão
    - consistência
    - relevância
    - cobertura
    - atualidade

## 3. Principais medidas de qualidade dos Dados - Precisão

A precisão mede o quanto os dados são confiáveis, ou seja, a confiabilidade dos dados. O objetivo é garantir que os dados e informações contidos nos sistemas são completos, corretos, consistentes e seguros. Por exemplo:
 A idade dos clientes cadastrados é confiável?

## 4. Principais medidas de qualidade dos Dados - Exatidão

A exatidão é a medida de quão bem os dados correspondem à realidade. É necessário assegurar que os dados estão exatos e refletem a realidade da melhor forma possível. Por exemplo:
 totais de vendas apresentam exatidão?

## 5 Principais medidas de qualidade dos Dados - Consistência

A consistência é um indicador de como os dados são uniformes. É importante garantir que os dados sejam consistentes e que não estejam sujeitos a mudanças muito fortes ou erros. A consistência também reflete a integridade dos dados. Por exemplo:
 Os dados apresentam problemas de valores ausentes?

## 6. Principais medidas de qualidade dos Dados - Relevância

A relevância mede a quantidade de informações relevantes que se tem sobre um determinado assunto. É importante assegurar que os dados sejam relevantes e úteis ao se fazer análises. Por exemplo:
 Dados da cor dos olhos dos clientes cadastrados é relevante para análise?

## 7. Principais medidas de qualidade dos Dados - Cobertura

A cobertura mede a quantidade de dados disponíveis para serem usados. É importante ter uma base de dados completa e fornecer informações suficientes para obter resultados confiáveis. Por exemplo:
 Dados sobre vendas estão disponíveis em todos os pontos de venda?

## 8. Principais medidas de qualidade dos Dados - Atualidade

A atualidade é a medida de quão recentes são os dados. É importante garantir que os dados sejam atualizados e que reflitam o comportamento do evento que está sendo analisado. Por exemplo:
 Dados demográficos após o ano de 2010 fazem mais sentido do que dados demográficos da década de 1950?

## 9. O Valor da qualidade dos Dados

Avaliar o valor da qualidade dos dados é importante para garantir que os dados sejam precisos e úteis para a realização de análises. Existem várias técnicas para determinar o valor da qualidade dos dados, como:
 Avaliação da qualidade dos dados por erros potenciais. Esta abordagem envolve a verificação de dados em busca de erros, como erros de digitação, dados ausentes ou incorretos, erros de formatação, etc.
 Análise estatística e de mineração de dados. Esta técnica envolve a análise estatística dos dados e o uso de técnicas de análise de dados para identificar padrões e anomalias.
 Teste de qualidade: testar a qualidade dos dados é uma das melhores maneiras de avaliar a qualidade dos dados. O teste de qualidade permite verificar se os dados estão corretos e se a conformidade dos dados às especificações é adequada.
 Avaliação de domínio. Esta técnica envolve a verificação dos dados em relação ao domínio dos dados. Por exemplo, se estivermos analisando dados de um banco de dados de vendas, seria necessário verificar se os preços das vendas estão dentro dos limites esperados.

## 10. Correções Típicas nos Dados

Algumas correções típicas nos dados para garantir a qualidade incluem:

- Limpeza: remover dados duplicados, incompletos, inconsistentes ou irrelevantes.
- Padronização: converter dados para um formato comum, como a padronização de datas, endereços, nomes e códigos ou colocar os dados na mesma escala.
- Tratar Valores ausentes: usar técnicas de interpolação para preencher valores ausentes ou eliminar registros com valores ausentes em uma ou mais colunas.
- Correção de Erros: verificar e corrigir erros de digitação, remover caracteres especiais ou espaços desnecessários, corrigir erros de sobreposição de colunas, etc..
- Normalização: transformar dados para um formato normalizado, como por exemplo transformar uma variável para reduzir assimetria.
- Validação: validar os dados com regras de negócios ou restrições para garantir a precisão e integridade dos dados.

## 11. O que é Linhagem de Dados (Data Lineage)?

Linhagem dos Dados é a trajetória de dados ao longo do tempo, incluindo suas origens, transformações, aplicações e destinos finais.
É uma representação visual ou lógica da evolução dos dados em um sistema, o que permite entender a integridade e a qualidade dos dados.
A Linhagem dos Dados é importante para várias aplicações, como auditoria de dados, gerenciamento de governança de dados e análise de impacto.
Linhagem de dados é o processo de rastreamento e documentação do fluxo de dados ao longo do tempo, desde a origem até o destino final, incluindo todas as transformações e operações realizadas nos dados.
Este conceito é importante para garantir a qualidade dos dados e fornecer uma visão clara de como os dados foram gerados e utilizados em diferentes sistemas e processos.

## 12. A importância da Linhagem de Dados (Data Lineage)

A Linhagem de Dados é importante porque:

- Ajuda a garantir a qualidade dos dados: rastreando o fluxo de dados, é possível identificar e corrigir erros ou inconsistências em diferentes pontos do processo.
- Fornece transparência e confiança nos dados: a linhagem de dados permite aos usuários compreender a origem e evolução dos dados, o que aumenta a confiança nos resultados e decisões baseadas neles.
- Facilita a auditoria e conformidade regulatória: a linhagem de dados fornece uma visão completa e documentada dos processos de dados, o que é importante para atender a regulamentos e exigências de auditoria.
- Melhora a eficiência de negócios: ao entender o fluxo de dados, é possível identificar oportunidades de otimização e automação de processos de negócios.

## 13. Definindo o Conceito de Observabilidade dos Dados (Data Observability)

A Qualidade dos Dados está relacionada com os dados em si, enquanto a Observalidade dos Dados está relacionada com o sistema que fornece esses dados.

**Observabilidade dos Dados > Linhagem dos Dados > Qualidade dos Dados**

Observabilidade dos Dados é a capacidade de visualizar e entender o estado e o comportamento dos dados a fim de identificar problemas, corrigir erros e tomar decisões informadas.
A Observabilidade dos Dados inclui a capacidade de monitorar, rastrear e auditar o fluxo de dados, bem como a disponibilidade de metadados e informações sobre as transformações e operações realizadas nos dados.
Um aspecto fundamental da Observabilidade dos Dados é a capacidade de acessar e analisar dados de todas as partes do sistema.
Isso inclui dados de aplicações, da infraestrutura e dos usuários do sistema.
Para utilizar efetivamente a Observabilidade de Dados, é importante ter as ferramentas e os processos corretos em vigor.
Isso inclui coleta de dados e infraestrutura de armazenamento, bem como ferramentas de análise e visualização.
Também é importante ter uma compreensão clara das métricas que são mais importantes para rastrear e a maneira apropriada de analisar os dados.
Outro aspecto importante da Observabilidade de Dados é a capacidade de identificar e solucionar problemas em tempo real.
Ao monitorar constantemente os dados, é possível detectar e resolver problemas antes que eles se tornem críticos.
Isso pode ser especialmente importante em sistemas com requisitos de alta disponibilidade, pois o tempo de inatividade pode ter consequências significativas.

## 14. Os 5 pilares da Observabilidade dos Dados (Data Observability)

A Observabilidade dos Dados se baseia no conceito de Qualidade dos Dados para abranger a integridade geral dos sistemas de dados de uma organização.
Com a Observabilidade dos Dados, uma organização pode identificar melhor seus conjuntos de dados mais críticos, usuários desses dados e problemas decorrentes desses dados.

- Freshness: Descreve se os dados são atuais e com que frequência os dados são atualizados.
- Distribuition: Descreve se os valores dos dados estão dentro de um intervalo aceitável. Os dados fora desse intervalo podem não ser confiáveis.
- Volume: Mede se os dados estão completos. Volume de dados inconsistente indica problemas com fontes de dados.
- Schema: Rastreia mudanças na organização, quem faz quais mudanças nos dados e quando.
- Lineage: Restringe e documenta todo o fluxo de dados desde as fontes iniciais até o consumo final.

## 15. [PDF] Exemplos de Ferramentas de Observabilidade dos Dados (Data Observability)

- Monte Carlo
- DataBuck
- Databand
- Honeycomb
- AccelData
- Datafold

## 16. [PDF] Tendências em Engenharia de Dados - Contrato de Dados

 O  Contrato  de  Dados  em  engenharia  de  dados  é  um  acordo  formal  que  estabelece  as expectativas,  responsabilidades  e  obrigações  entre  as  partes  envolvidas  na  gestão  e  uso  de dados.
 Ele define como  os dados serão  coletados, armazenados, protegidos e  compartilhados, bem  como  quais  são  as  restrições  e  condições  de  uso  dos  dados.  O  objetivo  é  garantir  a privacidade,  a  segurança  e  a  integridade  dos  dados,  além  de  assegurar  o  cumprimento  de regulamentos e leis relacionados à proteção de dados.
 O Contrato de Dados é um acordo entre produtores e consumidores dos dados e é uma tendência na área de Engenharia de Dados.O Contrato de Dados estabelece regras claras para garantir que os dados sejam usados de maneira ética e correta, incluindo quais dados podem ser coletados, como podem ser usados e por quanto tempo, e como os dados serão protegidos e excluídos quando não mais necessários. O Contrato de Dados é importante para garantir a  confiança e a transparência nas práticas de Engenharia de Dados.
 O Contrato de Dados ainda é uma ideia relativamente nova. Eles são uma tentativa inicial de melhorar a manutenção dos pipelines de dados e os problemas decorrentes da quebra de um monólito,  portanto,  provavelmente  veremos  mais  iterações  e  outras  abordagens  surgindo  no futuro

## 17. Demonstração Prática 3 - Visão Geral

## 18 e 19. Demonstração Prática 3 - Conhecendo o SQLFlow para Linhagem de Dados

## 20. O que é um DataOps?

 DataOps é uma abordagem para a gestão de pipelines de dados, baseada em práticas de DevOps, que se concentra na agilidade, qualidade e confiabilidade na entrega de dados.

É uma forma de otimizar os fluxos de trabalho dos pipelines de dados, do desenvolvimento à entrega, com o objetivo de torná-los mais rápidos, confiáveis e escaláveis. Isso é alcançado através da automação de tarefas repetitivas, monitoramento contínuo e colaboração estreita entre equipes de desenvolvimento de software e de dados.

DataOps é o resultado da aplicação dos princípios do DevOps ao ciclo de vida dos dados. A ideia básica em DataOps é: “se você construir um sistema em torno dos dados – que automatize muito do monitoramento, implantação e colaboração – sua produtividade aumenta, seus clientes ficam muito mais felizes e você acaba fazendo um trabalho melhor”.

DataOps se concentra em três processos:

1- Redução de Erros, o que melhora a confiança nos dados.
2- Ciclo de Vida de Desenvolvimento, que envolve a rapidez com que você pode obter novos modelos, novos conjuntos de dados e novas visualizações, da concepção do problema até a produção. Este aspecto envolve tanto velocidade quanto risco.
3- Aumento da Produtividade da Equipe, com redução do número de reuniões e aumento da colaboração.

Todos os processos definidos anteriormente são mensuráveis. Por exemplo, você deve analisar métricas que respondam às seguintes perguntas:

Quanto trabalho sua equipe está fazendo?
Com que frequência as coisas estão “quebrando”?
Quão rápido você está colocando coisas novas em produção?
Como Implementar DataOps
A implementação de DataOps envolve vários passos, incluindo:

Definição de Processos: Defina os processos e fluxos de trabalho para os pipelines de dados, incluindo a integração, validação, teste e implantação.

Automatização: Automatize tarefas repetitivas para melhorar a eficiência e a precisão. Isso inclui a automação de testes, implantações e atualizações.

Colaboração: Crie uma equipe cross-funcional de desenvolvimento de software e de dados para trabalhar juntos na criação, manutenção e monitoramento dos pipelines de dados.

Monitoramento: Monitore o desempenho de cada pipeline de dados para identificar problemas e oportunidades de melhoria.

Feedback: Implemente um sistema de feedback para permitir que as equipes de desenvolvimento de software e de dados possam compartilhar informações e soluções em tempo real.

Cultura: Fomente uma cultura de experimentação, inovação e melhoria contínua para garantir que todos estejam sempre procurando formas de tornar cada pipeline de dados mais eficiente e eficaz.

A implementação de DataOps é um processo contínuo e pode levar algum tempo. No entanto, a implementação correta pode melhorar significativamente a qualidade, confiabilidade e agilidade na entrega de dados.

### **DataOps x MLOps**
DataOps é uma abordagem de gerenciamento de dados que tem como objetivo aumentar a velocidade, qualidade e eficiência do ciclo de vida dos dados. O DataOps se concentra em automatizar e otimizar processos de coleta, armazenamento, processamento e distribuição de dados.

Já MLOps é uma extensão do DataOps que se concentra especificamente no gerenciamento do ciclo de vida dos modelos de aprendizado de máquina (Machine Learning). Isso inclui tarefas como o treinamento, o teste e o monitoramento de modelos, bem como a implementação e o gerenciamento de modelos em produção.

Enquanto DataOps pode ser responsabilidade de um Engenheiro de Dados ou de um Engenheiro DataOps, MLOps é responsabilidade do Engenheiro de Machine Learning.

**Ferramentas de DataOps**
Algumas das principais ferramentas de DataOps incluem:

- Apache Airflow: um sistema de orquestração de pipelines de dados baseado em tarefas.
- AWS Glue: um serviço de ETL da Amazon que permite a criação, execução e gerenciamento de pipelines de dados.
- Talend: uma plataforma de integração de dados que oferece ferramentas para coletar, integrar e distribuir dados.
- Apache Nifi: um sistema de fluxo de dados de código aberto para automatizar a movimentação e o tratamento de dados.
- StreamSets: uma plataforma de gerenciamento de dados que permite a criação, execução e monitoramento de pipelines de dados.
- DataKitchen: uma plataforma de automação em DataOps.

***Caso de Uso***
E aqui está um exemplo de caso de uso para implementar DataOps na prática:

**Identificação das necessidades de dados:** A primeira etapa é compreender as necessidades de dados da empresa. Isso pode incluir a definição de KPIs, o entendimento do fluxo de dados e a identificação dos dados críticos para o negócio.

**Criação de pipelines de dados:** Uma vez que as necessidades de dados são conhecidas, é hora de criar pipelines de dados para coletar, processar e distribuir os dados. Isso pode ser feito usando uma ferramenta de integração de dados, como Apache Airflow ou Talend.

**Automatização de processos:** A próxima etapa é automatizar processos como a validação de dados, a geração de relatórios e a distribuição de dados. Isso pode ser feito usando scripts ou ferramentas de automação, como o Apache Nifi.

**Monitoramento e otimização de pipelines de dados:** É importante monitorar continuamente o desempenho dos pipelines de dados para identificar problemas e oportunidades de otimização. Isso pode ser feito usando ferramentas de monitoramento, como Amazon CloudWatch.

**Colaboração e documentação:** Por fim, é importante promover a colaboração entre equipes e documentar processos para garantir a transparência e a escalabilidade. Isso pode ser feito usando ferramentas de colaboração, como Confluence, e a criação de documentação detalhada dos processos de dados.

Este é apenas um exemplo geral de como implementar DataOps na prática. O processo pode variar de acordo com a complexidade dos dados e as necessidades específicas da empresa.

**Conclusão**
DataOps pode ser uma abordagem poderosa para qualquer empresa e vale a pena dedicar um tempo para entender a estrutura e seus benefícios.

Mas a coisa mais importante a lembrar é que esta prática é sobre colaboração.

Trata-se de construir uma cultura em que os profissionais de dados trabalhem em conjunto com as partes interessadas para produzir resultados orientados por dados com mais rapidez e eficiência.

## 21, 22, 23, 24 e 25. Demonstração Prática 3 - Linhagem de Dados de Data Warehouse

## [26. Quiz](link)
