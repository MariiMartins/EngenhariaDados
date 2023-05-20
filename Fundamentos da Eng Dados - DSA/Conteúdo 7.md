# 7. Data Quality, Data Lineage e Data Observability.
<!--
1) O que é qualidade dos Dados (Data Quality)?
Data Quality é a medida da qualidade dos dados, ou seja, de quanto os dados são confiáveis.
É importante para garantir que os dados sejam precisos, consistentes e úteis para suportar as decisões de negócios.
Qualidade dos Dados é a medida da condição dos dados com base em fatores como precisão, integridade, consistencia, confiabilidade e se estão atualizados.

2) Como medir qualidade dos Dados (Data Quality)?
A medida da qualidade de dados pode ser feita usando uma combinação de técnicas estatísticas e metodologias de avaliação. Alguns dos indicadores comuns incluem a precisão, a completude, a consistencia, a integridade e a atualização dos dados.
Também pode ser necessário avaliar a relevância dos dados para o negócio e a facilidade de uso dos dados para os destinatários.
Existem vários fatores e métricas que podem ser usados para medir a qualidade dos dados. Os mais comuns são:
    - precisão
    - exatidão
    - constistencia
    - relevancia
    - cobertura
    - atualidade

3) Principais medidas de qualidade dos Dados - Precisão
A precisão mede o quanto os dados são confiáveis, pu seja, a confiabilidade dos dados. O objetivo é garantir que os dados e informações contidos nos sistemas são completos, corretos, consitentes e seguros. Por exemplo:
 A idade dos clientes cadastrados é confiável?

4) Principais medidas de qualidade dos Dados - Exatidão
A exatidão é a medida de quão bem os dados correspondem à realidade. É necessário assegurar que os dados estão exatos e refletem a realidade da melhor forma possível. Poe exemplo:
 totais de vendas apresentam exatidao?

5) Principais medidas de qualidade dos Dados - Consistencia
A consistencia é um indicador de como os dados são uniformes. É importante garantir que os dados sejam consistentes e que não estejam sujeitos a mudanças muito fortes ou erros. A consistencia também reflete a integridade dos dados. Por exemplo:
 Os dados apresentam problemas de valores ausentes?

6) Principais medidas de qualidade dos Dados - Relevancia
A relevancia mede a quantidade de informações relevantes que se tem sobre um determiando assunto. É importante assegurar que os dados sejam relevantes e úteis ao se fazer análises. Por exemplo:
 Dados da cor dos olhos dos clientes cadastradis é relevante para análise?

7) Principais medidas de qualidade dos Dados - Cobertura
A cobertura mede a quantidade de dados disponiveis para serem usados. É importante ter uma base de dados completa e fornecer informações suficientes para obter resultados confiáveis. Por exemplo:
 Daos sobre vendas estão disponiveis em todos os pontos de venda?

8) Principais medidas de qualidade dos Dados - Atualidade
A atualidade é a medida de quão recentes sao os dados. É importante garantie que os dados sejam atualizados e que reflitam o comportamento do evento que está sendo analisado. Por exemplo:
 Dados demograficos após o ano de 2010 fazem mais sentido do que dados demográficos da decada de 1950?

9) O Valor da qualidade dos Dados
Avaliar o valor da qualidade dos dados é importante para garantir que os dados sejam precisos e úteis para a realização de analises. Existem várias tecnicas para determinar o valor da qualidade dos dados, como:
 Avaliacao da qualidade dos dados oir erris potenciais. Esta abordagem envolve a verificação de ddos em busca de erros, como erros de digitação, dados ausentes ou incorretos, erros de formatação, etc.
 Análise estatistica e de mineração de dados. Esta tecnica envolve a analise estatistica dos dados e o uso de técnicas de analise de dados para identificar padrões e anomalias.
 Teste de qualidade. testar a qualidade dos dados é uma das melhores maneiras de avaliar a qualidade dos dados. O teste de qualidade permite verificar se os dados estão corretos e se a conformidade dos dados ás especificações é adequada.
 Avaliação de dominio. Esta tecnica envolve a verificação dos dados em relação ao dominio dos dados. Por exemplo, se estivermos analisando dados de um banco de dados de vendas, seria necessário verificar se os preços das vendas estão dentro dos limites esperados.

10) Correções Típicas nos Dados
Algumas correções tipicas nos dados apra garantir a qualidade incluem:
    - Limpeza: remover dados duplicados, incompletos, inconsistentes ou irrelevantes.
    - Padronização: converter dados para um formato comum, como a padronização de datas, endereços, nomes e códigos ou colocar os dados na mesma escala.
    - Tratar Valores ausentes: usar tecnicas de interpolação para preencher valores ausentes ou eliminar registros com valores ausentes em uma ou mais colunas.
    - Correção de Erros: verificar e corrigir erros de digitação, remover caracteres especiais ou espaços desnecessários, corrigir erros de sobreposição de colunas, etc..
    - Normalização: transformar dados para um formato normalizado, como por exemplo transformar uma variável para reduzir assimetria.
    - Validação: validar os dados com regras de negócios ou restrições para garantir a precisçao e integridade dos dados.

11) O que é Linhagem de Dados (Data Lineage)?
Linhagem dos Dados é a trajetoria de dados ao longo do tempo, incluindo suas origens, transformações, aplicações e destinos finais.
É uma representação visual ou lógica da evolução dos dados em um sistema, o que permite entender a integridade e a qualidade dos dados.
A Linhagem dos Dados é importante para várias aplicações, como auditoria de dados, gerenciamento de governança de dados e análise de impacto.
Linhagem de dados é o processo de rastreamento e documentação do fluxo de dados ao longo do tempo, desde a origem até o destino final, incluindo todas as transformações e operações realizadas nos dados.
Este conceito é importante para garantir a qualidade dos dados e fornecer uma visão clara de como os dados foram gerados e utilizados em diferentes sistemas e processos.

12) A importância da Linhagem de Dados (Data Lineage)
A Linhagem de Dados é importante porque:
 - Ajuda a garantir a qualidade dos dados: rastreando o fluxo de dados, é possivel identificar e corrigir erros ou inconsistencias em diferentes pontos do processo.
 - Fornece trasnparencia e confiança nos dados: a linhagem de dados permite aos usuários compreender a origem e evolução dos dados, o que aumenta a confiança nos resultados e decisões baseadas neles.
 - Facilita a auditoria e conformidade regulatória: a linhagem de dados fornece uma visão completa e documentada dos processos de dados, o que é importante para atender a regulamentos e exigencias de auditoria.
 - Melhora a eficiência de negócios: ao entender o fluxo de dados, é possível identificar oportunidades de otimização e automação de processos de negócios.

13) Definindo o Conceito de Observabilidade dos Dados (Data Observability)
A Qualidade dos Dados está relacionada com os dados em si, enquanto a Observalidade dos Dados está relacionada com o sistema que fornece esses dados.

**Observabilidade dos Dados > Linham dos Dados > Qualidade dos Dados**

Observabilidade dos Dados é a capacidade de visualizar e entender o estado e o comportamneto dos dados a fim de identificar problemas, corrigir erros e tomar decisçoes informadas.
A Observabilidade dos Dados inclui a capacidade de monitorar, rastrear e auditar o fluxo de dados, bem como a disponibilidade de matadados e informações sobre as transformações e operações realizadas nos dados.
Um aspecto fundamental da Observabilidade dos Dados é a capacidade de acessar e analisar dados de todas as partes do sistema.
Isso inclui dados de aplicações, da infraestrutura e dos usuários do sistema.
Para utilizar efetivamente a Observabilidade de Dados, é importante ter as ferramentas e os processos corretos em vigor.
Isso inclui coleta de dados e infraestrutura de armazenamento, bem como ferramentas de análise e visualização.
Também é importante ter uma compreensão clara das métricas que são mais importantes para rastrear e a maneira apropriada de analisar os dados.
Outro aspecto importante da Observabilidade de Dados é a capacidade de identificar e solucionar problemas em tempo real.
Ao monitorar constantemente os dados, é possivel detectar e resolver problemas antes que eles se tornem críticos. 
Isso pode ser especialmente importante em sistemas com requisitos de alta disponibilidaed, pois o tempo de inatividade pode ter consequencias significativas.

14) Os 5 pilares da Observabilidade dos Dados (Data Observability)
A Observabilidade dos Dados se baseia no conceito de Qualidade dos Dados para abranger a integridade geral dos sistemas de dados de uma organização.
Com a Observabilidade dos Dados, uma organização pode identificar melhor seus conjuntos de dados mais críticos, usuários desses dados e problemas decorrentes desses dados.
 - Freshness: Descreve se os dados são atualis e com que frequencia os dados são atualizados.
 - Distribution: Descreve se os d=valores dos dados estão dentro de um intervalo aceitável. Os dados fora desse intervalo podem não ser confiaveis.
 - Volume: Mede se os dados estão completos. Volume de dados inconsistente indica problemas com fontes de dados.
 - Schema: Rastreia mudanças na organização, quem faz quais mudanças nos dados e quando.
 - Lineage: Restringe e documenta todo o fluxo de dados desde as fontes iniciais até o consumo final.

15) [PDF] Exemplos de Ferramentas de Observabilidade dos Dados (Data Observability)

16) [PDF] Tendências em Engenharia de Dados - Contrato de Dados

17) Demonstração Prática 3 - Visão Geral

18) Demonstração Prática 3 - Conhecendo o SQLFlow para Linhagem de Dados - P1
19) Demonstração Prática 3 - Conhecendo o SQLFlow para Linhagem de Dados - P2

20) Demonstração Prática 3 - Linhagem de Dados de Data Warehouse - P1
21) Demonstração Prática 3 - Linhagem de Dados de Data Warehouse - P2
22) Demonstração Prática 3 - Linhagem de Dados de Data Warehouse - P3
23) Demonstração Prática 3 - Linhagem de Dados de Data Warehouse - P4
24) Demonstração Prática 3 - Linhagem de Dados de Data Warehouse - P5

25) Quiz
-->