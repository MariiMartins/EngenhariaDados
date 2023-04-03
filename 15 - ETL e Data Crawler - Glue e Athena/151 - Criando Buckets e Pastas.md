151. Criando Buckets e Pastas
Bom, agora nós vamos para o S3 e nós vamos criar um bucket onde a gente vai ter algumas passas que vão ser utilizadas para o nosso processo de ETL.
Então eu vou buscar aqui em serviços S3. Primeiramente, então vou criar aqui um bucket. Vou escolher um nome. A gente não precisa mexer em nenhuma, nenhuma outra propriedade.

E agora que a gente vai criar algumas pastas, a primeira pasta que eu vou criar vai se chamar Data Lake mesmo, que é onde vão ficar os dados transformados. A outra pasta vai ser uma pasta Temp que vão ser gerados, vão ser colocados dados temporários do processamento do Glue, uma pasta log que também para o log, uma pasta scripts onde ele vai salvar o script criado no processo de ETL. eEuma pasta source, ou melhor, vamos chamar de source data, que é onde vão estar os dados de origem.

Os dados que o processo de ETL vai importar para fazer transformação, para criar a tabela que vai para o nosso Data Lake, Vai ser então DataLake, que é a pasta principal do nosso bucket. Vamos criar aqui mais uma pasta que vai ser temp para os dados temporários. Vamos criar aqui mais uma pasta para Logs, e vamos criar uma pasta scripts.

Queremos mais uma pasta e, por fim, a pasta Sources Data com os dados de origem.
Bom, o que a gente pode fazer agora ainda? A gente pode então carregar estes arquivos. Então, lembrando que esses arquivos estão no material do curso, você deve pegar especificamente os arquivos que estão no diretório desta seção. Em outras seções existem arquivos com nomes parecidos, mas não são os mesmos arquivos.
Então você precisa pegar os que estão nessa seção. Então os arquivos a gente vai carregar para essa pasta source data e aqui, então a gente vai clicar em carregar.