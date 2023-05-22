# 6. Introdução à Modelagem de Dados

<!--
## 1. Definição de Dados

Dados são valores, observações ou resultados de medição armazenados em um sistema ou base de dados.
Eles podem ser estruturados, como os dados armazenados em tabelas de banco de dados relacional, ou não estruturados, como texto não formatado, imagens ou áudio.
Quando transformados ou processados os dados se tornam informações que suportam a tomada de decisões.
Dados podem representar qualquer tipo de informação, como texto, números, imagens, som, vídeo, entre outros.
Dados são usados para descrever eventos, tendências, relações e outras características de interesse.
Eles são coletados, armazenados e processados para fornecer informações úteis para a tomada de decisão, a pesquisa e outros fins.
Esses dados precisam ser modelados para que possamos armazená-los e processá-los de forma eficiente.

## 2. O que é Modelagem de Dados?

Modelagem de dados é o processo de projetar e criar modelos ou estruturas lógicas que representam como os dados são armazenados, relacionados e usados.
Isso inclui a definição de tabelas, campos e relacionamentos em um banco de dados, bem como a criação de diagramas e especificações que descrevem como os dados serão usados em aplicativos e sistemas.
A modelagem de dados é uma etapa importante na construção de sistemas de informação eficientes e confiáveis.

## 3. Modelagem Relacional x Dimensional x Modelagem de Data Lakes

    - Modelagem Relacional é uma abordagem para projetar bancos de dados que se baseia nas relações entre as entidades, com tabelas e campos.
     Isso envolve a criação de tabelas que representam entidades, como clientes ou pedidos, e definição de relações entre essas tabelas, como "um cliente pode fazer vários pedidos".
     A modelagem relacional é amplamente utilizada em sistemas de gerenciamento de banco de dados relacional (SGBDs. e é uma abordagem estruturada e estável para armazenar e gerenciar dados em sistemas transacionais.

    - Modelagem Dimensional é uma técnica de modelagem de dados utilizada principalmente em sistemas de Business Intelligence (BI. e Data Warehousing(DW.. Ela consiste em modelar os dados de forma a facilitar a análise de dados multidimensionais.
     Os modelos dimensionais são construídos a partir de fatos (tabelas de medidas. e dimensões (tabelas de contexto., onde os fatos são medidas quantitativas, como vendas, e as dimensões são os contextos dessas medidas, como data, local, produto, entre outros. Essas dimensões são divididas em hierarquias, o que permite uma análise detalhada dos dados.
     A modelagem dimensional é muito utilizada em sistemas de BI e DW pois permite uma fácil agregação e análise dos dados, além de ser escalável e performático.
     Além disso, ela permite a criação de dashboards e relatórios para acompanhamento de indicadores de desempenho, e facilita a análise de dos históricos e a previsão de tendências futuras.
     A Modelagem Dimensional é de fato Modelagem Relacional, mas com foco na agregação dos dados e análise e algumas pequenas diferenças.

    Modelagem de Data Lakes, por outro lado, é uma abordagem para projetar sistemas de armazenamento de dados que são voltados para a análise de grandes volumes de dados não estruturados.
     Um DL é uma grande coleção de dados brutos, normalmente armazenada em sistemas de arquivos distribuídos, como o HDFS, que podem ser facilmente acessados e processados por ferramentas de análise de Big Data.
     A Modelagem de Data Lakes é menos estruturada e mais flexível do que a Modelagem Relacional e é projetada para lidar com grandes volumes de dados e permitir análises exploratórias dos dados.
     Com Data Lakes estamos preocupados primeiro em armazenar os dados no formato bruto, mas em algum momento os dados terão que ser organizados e estruturados e podem ser modelados e carregados em um DW, por exemplo.

## 4. O que é Esquema em Modelagem de Dados?

O esquema de dados é a estrutura lógica que descreve como os dados estão organizados e relacionados em um banco de dados.
Ele define as tabelas, campos e relacionamentos entre as tabelas, além de outras restrições e propriedades dos dados.
Em um banco transacional ou em um DW, o esquema é mandatório e deve ser definido antes da carga de dados.
Um mesmo SGBD pode ter diversos bancos de dados e cada banco de dados pode ter diversos esquemas (schemas).
No Data Lake normalmente não temos esquema pré-definido, mas alguma organização será requerida para o armazenamento.

## 5. O que são Constraints?

Constraints, ou restrições, são regras ou limitações que são aplicadas aos dados em um banco de dados para garantir a integridade dos dados. Essas restrições podem incluir regras de validação, como verificar se um valor é numérico ou se uma data está no formato correto, ou regras de integridade referencial, que garantem que os dados em diferentes tabelas sejam consistentes entre si.
    Alguns exemplos de constraints são: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK e DEFAULT.

## 6. Modelagem de Dados - Modelo conceitual

O Modelo Conceitual é uma das três camadas de modelagem de dados, juntamente com o modelo lógico e o modelo físico. É a camada mais abstrata da modelagem de dados e é projetado para representar os dados de uma organização de forma independente de qualquer sistema ou tecnologia específica.
O modelo Conceitual é projetado para capturar a estrutura de negócio dos dados, incluindo entidades, atributos e relacionamentos, e é usado para comunicar a estrutura de dados para os stakeholders de negócios.
Esse modelo é geralmente desenvolvido usando notações gráficas, como diagramas de entidade-relacionamento (ER), e é usado como base para a criação dos modelos lógico e físico.
O Modelo Conceitual é a primeira etapa de modelagem de dados e é importante para garantir que os dados sejam projetados de forma consistente e coerente com as necessidades de negócio da empresa. Embora às vezes seja negligenciado, esse modelo é fundamental para a compreensão sobre os dados.

## 7. Modelagem de Dados - Modelo Lógico

O Modelo Lógico é uma das três camadas de modelagem de dados, juntamente com o modelo conceitual e o modelo físico.
Ele é a representação lógica dos dados, independente da plataforma ou tecnologia de banco de dados específica que será usada na implementação física.
O modelo lógico é a representação dos dados como tabelas, campos e relacionamentos, e é usado para descrever a estrutura lógica dos dados.
Esse modelo é projetado para capturar a estrutura de negócio nos dados, incluindo entidades, atributos e relacionamentos, mas é adaptado para se adequar às necessidades de implementação do banco de dados, independente da tecnologia usada. Ele é geralmente desenvolvido usando notações gráficas, como diagramas de entidade-relacionamento (ER), e é usado como base para a criação do modelo físico.
O Modelo Lógico permite identificar eventuais problemas que poderão ocorrer na implementação física.

## 8. Modelagem de Dados - Modelo Físico

O Modelo Físico é a última camada de modelagem de dados. Ela é a representação física dos dados, incluindo a estrutura de armazenamento e as configurações de banco de dados específicas.
Ele descreve como os dados serão armazenados e como eles serão acessados em um sistema de gerenciamento de banco de dados específico.
O Modelo Físico deve conter todas as definições de constraints, índices e particionamento dos dados.
O Modelo Físico inclui detalhes como o nome das tabelas e campos, tipo de dados, tamanho, índices, chaves estrangeiras e outras configurações de banco de dados específicas.
Esse modelo normalmente é uma extensão do modelo lógico contendo os detalhes de implementação em um SGBD específico. Diversas ferramentas de modelagem permitem converter um modelo lógico para um modelo físico de acordo com o SGBD escolhido.
Ele é a etapa final da modelagem de dados e é importante para garantir a eficiência, desempenho e escalabilidade do banco de dados.

## 9. [PDF] Definindo a Granularidade do Modelo de Dados

    Granularidade é o nível de detalhe ou precisão com que os dados são representados em um modelo de dados.
    A  granularidade  dos  dados  pode  ser  alta,  quando  os  dados  são  divididos  em  muitas entidades e atributos pequenos, ou baixa, quando os dados são agregados em poucas entidades e atributos maiores.A granularidade é uma característica importante a ser considerada na modelagem de dados, pois afeta a capacidade de armazenar, recuperar e analisar dados.
    Uma granularidade alta permite uma maior flexibilidade e precisão na análise dos dados, mas pode exigir mais armazenamento e processamento. Por outro lado, uma granularidade baixa pode resultar em dados agregados e menos precisos, mas pode ser mais fácil de armazenar e processar. Portanto, é importante equilibrar a granularidade dos dados com as necessidades de negócio e técnicas para garantir uma boa modelagem de dados.
    Por exemplo: Considerando um DW, os relatórios devem permitir análise de vendas por dia ou por hora? A resposta a essa pergunta ajuda a definir o nível de granularidade necessário na modelagem.

## 10. [PDF] O que são Formas Normais?

As Formas Normais são um conjunto de regras e princípios que foram desenvolvidos para garantir a integridade dos dados e a eficiência do banco de dados. Elas são usadas na modelagem relacional para garantir que as tabelas e relacionamentos estejam corretamente projetados e para evitar problemas como a redundância de dados e a inconsistência. Existem várias formas normais, cada uma com seus próprios critérios e requisitos.

## 11. [PDF] Principais Formas Normais

As principais formas normais são:
    1ª Forma Normal (1NF): Todos os valores em uma tabela devem ser atômicos, ou seja, indivisíveis.
    2ª  Forma  Normal  (2NF):  Todos  os  atributos  não  chave  devem  ser  dependentes funcionalmente da chave primária.
    3ª Forma Normal (3NF): Não deve haver dependência transitiva de não chave para chave.
    4ª Forma Normal (4NF): Não deve haver relacionamentos multivalorados.
    5ª Forma Normal (5NF): Não deve haver relacionamentos com atributos dependentes.
Cada  forma  normal  é  uma  etapa  para  se  chegar  a  uma  tabela  estruturada  e  sem redundância e cada uma dessas formas normais é uma pré-condição para a seguinte, e aplicando-as em ordem, garante-se uma melhor estruturação do banco de dados.
A normalização (aplicação das formas normais) é feita ao final do processo de modelagem para ajustar o modelo e prepará-lo para o banco de dados.Vale ressaltar  que  a  normalização é  aplicada  em  modelos  de  bancos  de  dados transacionais.  Em  bancos  de  dados  multidimensionais,  como  o  DW, aplicamos  a desnormalização, pois os dados devem ser agregados para facilitar as análises.

## 12. [PDF] Projeto de Índices em Modelagem de Dados

Em  bancos  de  dados,  os  índices  são  estruturas  de  dados  que  permitem  acessar rapidamente  os  registros  em  uma  tabela.  Eles  funcionam  como  um  "mapa"  para  os  dados, permitindo que as consultas sejam executadas mais rapidamente, especialmente em tabelas grandes. Existem vários tipos diferentes de índices.O  projeto  de  índices  é  uma  parte  importante  da  modelagem  de  dados,  pois  afeta significativamente  o  desempenho  das  consultas.  
Para  definir  o  projeto  de  índices,  é recomendado seguir as seguintes etapas:
    - Identificar quais  colunas  são  frequentemente  usadas  em  consultas  de  seleção  e ordenação, pois essas colunas podem se beneficiar de um índice.- Escolher o tipo de índice adequado para o tipo de dados. Por exemplo, se a coluna contém dados numéricos, um índice numérico pode ser mais eficiente do que um índice de texto.
    - Criar índices  somente  em  tabelas  grandes,  pois  tabelas  pequenas  podem  ser facilmente lidas sem um índice.
    - Escolher a ordem das colunas no índice com base na frequência de uso. As colunas mais frequentemente usadas devem vir primeiro.
    - Avaliar a necessidade de índices compostos, que podem ser usados para melhorar o desempenho de consultas que usam várias colunas de busca.
    - Monitorar e otimizar o desempenho dos índices e otimizá-los regularmente. Isso inclui verificar a fragmentação do índice e reconstruí-lo se necessário.
    - Considerar o uso de índices não convencionais pois alguns bancos de dados oferecem tipos de índices não convencionais, como índices espaciais, índices full-text, entre outros. Esses tipos de índice podem ser úteis dependendo do tipo de dados e da natureza das consultas.
Lembre-se de que, embora os índices possam melhorar significativamente o desempenho das  consultas,  eles  também  podem  afetar  negativamente  o  desempenho  das  operações  de inserção,  atualização  e  exclusão,  portanto,  é  importante  equilibrar  as  necessidades  de desempenho de consulta e operação do banco de dados

## 13. [PDF] A importância do Particionamento em Modelagem de Dados

O particionamento é a técnica de dividir grandes tabelas ou índices em partes menores chamadas  partições.  Isso  é  importante  na  modelagem  de  dados  porque  permite  gerenciar grandes volumes de dados de forma mais eficiente e escalável.Algumas das vantagens do particionamento são:
    - Melhora o desempenho das consultas: Ao particionar grandes tabelas, as consultas podem  ser  direcionadas  para  uma  partição  específica,  o  que  pode  aumentar significativamente a velocidade de recuperação dos dados.
    - Facilita a manutenção e backup dos dados: As partições podem ser gerenciadas de forma independente, o que permite fazer backup, recuperação ou migração de uma partição sem afetar o restante dos dados.
    - Melhora a escalabilidade: Particionar as tabelas permite distribuir os dados em vários dispositivos  ou  servidores,  o  que  aumenta  a  capacidade  de  armazenamento  e  a capacidade de processamento.
Além disso, o particionamento também pode ser usado para organizar os dados por data, geolocalização, ou outras características, tornando mais fácil e rápido para os usuários encontrar e analisar os dados relevantes para as análises.

## 14. [PDF] O Engenheiro de Dados deve ser Responsável pela modelagem de dados?

O Engenheiro de Dados é responsável por construir e manter sistemas de gerenciamento de dados. Isso inclui a modelagem de dados. Ele  é  responsável  por  projetar  a  estrutura  de  dados,  incluindo  entidades,  atributos  e relacionamentos, e garantir que os dados sejam armazenados de forma consistente e coerente com as necessidades de negócios.
Além da modelagem de dados, o Engenheiro de Dados também é responsável por outras tarefas relacionadas a dados, como:
    - Garantir a qualidade dos dados, limpando, transformando e validando os dados antes de serem armazenados.
    - Otimizar o desempenho dos bancos de dados, incluindo o particionamento de tabelas e o projeto de índices.
    - Garantir  a  segurança  dos  dados,  incluindo  a criptografia  de  dados  sensíveis  e  a implementação de medidas de segurança.
    - Monitorar  e  gerenciar  os  sistemas  de  gerenciamento e  pipelines de  dados  para garantir a disponibilidade e desempenho.
Em  resumo,  o  Engenheiro  de  Dados  é  responsável  por  garantir que  os  dados  sejam armazenados de forma eficiente e estruturada,e que estejam disponíveis para análise e uso em toda a organização

## 15. [PDF] Qual o papel do Arquiteto de Dados na modelagem de dados?

O  Arquiteto  de  Dados  é  responsável  por  projetar e  garantir  a integridade,  qualidade  e segurança dos dados em uma organização. Ele é o responsável por garantir que os dados sejam coletados, armazenados, processados e exibidos de maneira consistente e eficiente.
O  Arquiteto  de  Dados  é  responsável  por  definir  a  estratégia  de  dados  da  empresa, incluindo a modelagem de dados, e garantir que a estratégia seja implementada e mantida. Ele trabalha  em  estreita  colaboração  com  outros  profissionais  de  dados,  como  Engenheiros  de Dados,  Cientistas  de Dados  e  Analistas  de Dados, para  garantir  que  os  dados  sejam  coletados, processados e armazenados a fim de gerar valor para a empresa.
Na modelagem de dados, o Arquiteto de Dados é responsável por projetar a estrutura de dados,  incluindo  entidades,  atributos  e  relacionamentos,  e  garantir  que  os  dados  estejam  de acordo com as necessidades das áreas de negócio.O Arquiteto de Dados planeja e projeta. O Engenheiro de Dados executa e mantém

## [16. Quiz](link)
