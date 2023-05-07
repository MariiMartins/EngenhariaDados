<!-- Como iniciamos um projeto de
pipeline de dados?
opção (a) iniciamos pelas ferramentas Pois existe uma curva de aprendizado e quanto antes começar
melhor 
opção (b) iniciamos pelos dados já
que eles são novo petróleo o novo ouro
um ativo corporativo e devem ser
prioridade 
opção (C) iniciamos pela compreensão dos requisitos de negócio e o que se espera do uso de dados no dia a
dia.

 se você respondeu letra C então ótimo você
já tem uma boa visão do que é realmente
trabalhar com dados.

O profissional que quer trabalhar
com tecnologia tem que estar disposto a
aprender e reaprender o tempo inteiro.
Engenheiro de dados Qual é o seu trabalho? 
 seu trabalho é ajudar na empresa alcançar os requisitos de negócio na que a empresa possa se manter no mercado de maneira competitiva aumentando lucro reduzindo custo.
-->

# 3. Arquitetura e Pipelines de Dados

<details><summary>3.1 A importância da Arquitetura de Pipelines de Dados </summary>

A importância da arquitetura de pipelines de dados.

Os pipelines de dados não são peças isoladas criadas pela área de TI (ou pelo menos não deveriam ser), os pipelines de dados são parte da arquitetura de dados de uma empresa que por sua vez é parte da plataforma de dados da empresa.

Veja que nessa frase eu tenho três definições diferentes. Então usando uma
hierarquia, topo da hierarquia é a
plataforma de dados, logo abaixo eu tenho arquitetura Geral de dados da empresa ou seja como os componentes vão secomportar dentro da plataforma de dados.
E aí mais abaixo ainda eu tenho os
pipelines de dados, que são exatamente os componentes responsáveis por movimentar os dados, transformar os dados, levar os dados de uma fonte para um destino fazendo as modificações necessárias no meio do caminho.

Logo cada pipeline de dados deve ter um propósito e deve fazer parte de uma arquitetura de dados que atenda os requisitos de negócio da empresa, com o menor custo possível, com segurança e que seja flexível as mudanças ao longo do tempo pois as únicas certezas que temos é que os requerimentos de hoje não serão os mesmos de amanhã, e uma boa estratégia é criar uma poc uma prova de conceito, uma espécie de laboratório que simula cenários, válida requisitos de negócio, testa ferramentas e ajuda a prever os custos.
</details>

<details><summary> 3.2 e 3.3 Pipeline de Dados x Pipeline ETL x Pipeline de Machine Learning </summary>
    - ETL: Extração, Limpeza e Transformação;
    - Dados: Extração de Dados, Limpeza e Transformação, Processamento dos Dados e Fluxo de Dados
</details>

<details><summary> 3.4 e 3.5 Comece a Arquitetura de Pipelines de Dados por estas Perguntas </summary>

    -> Quais são os requisitos de negócio?
    -> Quais resultados finais são necessarios?
    -> Os dados estão disponiveis? Quais as fontes?
    -> Quais tipos de formato(s) de dados estão disponíveis?
    -> Qual o crescimento esperado do volume de dados?
    -> Quanto de armazenamento será necessário?
    -> Quanto de capacidade computacional será necessário?
    -> Usaremos dados em batch, em streaming ou ambos?
    -> Ja temos tecnologia que permita criar os pipelines?
    -> Quais tecnologias devem ser consideradas?
    -> Quais sao os Acordos de Nível de Serviço (SLA's)?
    -> Qual o custo de implementar e manter os pipelines?
    -> Qual será o destino do pipeline?
    -> Como será monitorado?
    -> Usaremos diversos pipelines encadeados?
    -> Vamos criar os pipelines locais, na nuvem ou ambos?
</details>

<details><summary> 3.6 [PDF] Estudo de Caso 1 - Design de Arquitetura Moderna de Pipeline de Dados para empresa da área de Manufatura </summary></details>

<details><summary> 3.7 Estudo de Caso 1 - Visão Geral </summary></details>

<details><summary> 3.8 Estudo de Caso 1 - Compreensao dos Requisitos de Negócio</summary>

    -> Compreender o problema
        - empresa de manufatura
        - medio porte
        - fabrica utensilhos domesticos
        - adquiriu novas máquinas que conectam a rede
    -> Compreender o que deve ser entregue
    -> Pesquisar as fontes de dados
        - máquinas em formato TXT
    - Interficar a infraestrutura atual e o que será necessário
    -> Desenhar o esboço da solução
</details>

<details><summary>3.9 Estudo de Caso 1 - Esboço do Pipeline de Dados </summary></details>

<details><summary>3.10 Estudo de Caso 1 - Batch, Streaming ou Ambos?</summary>
    Batch (dados em Lotes), são dados assincronos na empresa.
</details>

<details><summary> 3.11 Estudo de Caso 1 - Volume de Dados e Armazenamento </summary>
    -> 10 máquinas, cada uma gerando 1 arquivo a cada 1h e cada arquivo tem aproximadamente 1MB.
    -> Logo são 10MH/h
    -> Empresa funciona 12h/dia (5 dias por semana)- 120MB/dia, 600MB/semana, 2.4GB/mes e 30GB/ano.
        -> mais 5 máquinas irão chegar no próximo semestre, logo esperamos crescimento de cerca de 50% no volume de dados.
    -> Vamos considerar que precisamos armazener os dados extraidos e também após o processo de limpeza e transformação. Sendo assim cerca de 100GB/ano.
</details>

<details><summary>3.12 Estudo de Caso 1 - Repositório de Dados</summary>
    -> Podemos usar o AWS Data Lake para Armazenamento.
    -> AWS Glue para criar um catalogo de Dados.
    -> Amazon Cloud Watch para o monitoramento da infraestrutura.
</details>

<details><summary> 3.13 Estudo de Caso 1 - Extração e Processamento de Dados</summary>
    -> Podemos usar o Kafka (Apache Kafka) para extrair os dados e enviar-los para o ambiente em nuvem.
    -> Na nuvem o Spark (Apache Spark) poderia fazer o processamento, assim evitariamos a necessidade de um armazenamento intermediário.
 - Ou seja, ao invés de armazenar dados em um data lake para processa-los depois, já processariamos os dados no momento em que são extraídos, aplicando as transformações necessárias e reduzindo o espaço total de armazenamento dos dados.
 Então o resultado do processamento seria gravado em um ?DataLake para então ser usado em Machine Learning.
 E enviariamos as atualizações necessárias para o sistema de estoque da empresa, atendendo assim os 2 requisitos de entrega do pipeline, com o menor custo possível e com todo o processamento sendo feito na nuvem.
</details>

<details><summary>3.14 Estudo de Caso 1 - Containers e Orquestração de Containers como Parte da solução</summary></details>

<details><summary>3.15 Estudo de Caso 1 - IaC (Infraestrutura como código) e CI/CD</summary>
    -> O Conceito de IaC é gerenciar a infraestrutura de forma simples, permitindo mudanças rápidas e implementando as boas práticas de CI/CD (Integração Contínua/ Entrega Contínua), essencialmente estamos implementando DataOps.
</details>

<details><summary>3.16 Estudo de Caso 1 - Custo do Pipeline de Dados</summary>
    -> Para o custo do pipeline devemos considerar:
        -> Custo do AWS Data Lake
        -> Custo de implementação do Apache Kafka/Apache Spark
        -> Custo do Amazon ECS, EKS e Fargate
        -> Custo de construção dos modelos de ML.
        -> Custo da automação com IaC e boas práticas de CI/CD.
        -> Custo de Monitoramento
</details>

<details><summary>3.17 Estudo de Caso 1 - Arquitetura Final do Pipeline e Considerações Finais </summary></details>

[3.18 Quiz]()
