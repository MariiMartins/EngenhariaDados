51. Instalando Postgres
Então agora vamos iniciar a nossa parte prática e primeira que vou deixar algumas observações. Você pode ver que eu já estou aqui com um shell conectado a uma máquina  virtual (Um Ubuntu Linux no EC2) ou seja, no AWS.
Eu explico passo a passo como fazer isso, como ter esse ambiente configurado e como você se conectar a ele na seção dois.
Bom, nesse primeiro tutorial a gente vai fazer a instalação do postgres. A gente vai instalar o postgres. No próximo tutorial a gente vai criar o banco de dados e a gente vai popular ele e depois nós vamos rodar as consultas interativas.
Então o que a gente vai fazer agora? Primeira coisa a gente vai instalar o programa, uzip, o programa uzip. A gente vai precisar dele para descompactar os scripts que nós vamos baixar da internet para dentro da nossa máquina virtual.
Então vamos lá.
Eu vou executar o sudo que é o superusuário, apt-get, que é o programa de gerenciamento de pacotes de aplicativos Zip, então, simples assim.
Sudo apt-get install unzip.Então a gente vai instalar aqui a instalação.Ela deve ser rápida.Ela não depende da sua internet nenhuma, na verdade, da conexão lá do servidor onde está rodando essa máquina virtual com o local onde está o arquivo?
Bom, agora existe uma série de etapas para instalar o post. Esses quatro, esses quatro procedimentos.
Eles são os procedimentos, os procedimentos que você encontra lá no site oficial do postgre. Então, o procedimento para você instalar a versão mais atual do post no Ubuntu, que é a máquina virtual que a gente tem aqui, é o que é o equipamento, o servidor que a gente tem rodando aqui.
Eu vou copiar e colar esses scripts, porque eu acho que a gente precisa de uma forma como uma forma de aprendizado. É importante você digitar o código, você escrever o código. Mas aqui, gente, está falando apenas de configuração, ok?
Então eu vou copiar e colar esses scripts. Você pode fazer o mesmo. Você encontra os scripts no material do curso. Se você preferir também você pode digitar. Então eu copiei. Aqui no Windows, botão direito e ele cola o script.
Então, primeiro ele vai criar uma pasta com um repositório de configuração.
A segunda aqui, do script que eu vou copiar, ele vai criar uma uma chave para fazer a instalação. O W-Get é um programa que baixa, que faz download da internet. Depois que o próximo comando, a gente vai atualizar a lista de pacotes do app-get, então esse comando pode demorar um pouquinho mais.
E pronto. Ele já fez atualização, e agora sim o quarto comando aqui que eu vou, que o copiei e vou colar aqui. E para fazer a instalação da versão mais atualizada do postgres.
O independente da versão que você instalar, que esse procedimento está lá. Os comandos que a gente vai executar depois eles vão ser exatamente os mesmos, não vai ter diferença nenhuma.
Então aqui você pode ver quem está fazendo a instalação do meu postgres e pronto, a gente tem o postgres instalado, então agora com o postgres instalado, a gente está pronto para logar no no post e para fazer os demais procedimentos.
Primeiro a gente vai fazer o download dos scripts e depois a gente vai logar no post e depois a gente vai rodar esses scripts. Então, a partir do próximo tutorial, a gente vai executar esse processo já com o postgres instalado.
