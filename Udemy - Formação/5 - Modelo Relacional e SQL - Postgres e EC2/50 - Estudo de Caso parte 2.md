50. Estudo de Caso Parte II
Então agora a gente vai apresentar aqui uma preparação, um roteiro da nossa parte prática. A gente vai colocar a mão na massa.
Porém, primeiro eu vou aqui fazer uma breve recapitulação do que a gente estudou. Então a gente viu alguns conceitos, alguns tutoriais sobre bancos de dados relacionais.
Então no dia a dia de um engenheiro de dados, é muito provável que você vai interagir ou já interage com um ou mais bancos de dados relacionais, porque é o principal modelo de banco de dados que suporta transações. Então, foi explicado o conceito de transações, que é o suporte a operações que mantêm as empresas funcionando. Então tem características como integridade e controle de transações, que para algumas aplicações são fundamentais. Então, por isso a gente vai estudar que agora, na prática, um banco de dados relacional.
Então, o que a gente vai fazer?
A gente vai utilizar uma instância EC2  do AWS. Com Ubuntu, Linux. Então, esta seção pressupõe que você já aprendeu a criar, inicializar instância. Caso contrário, então você deve voltar à seção dois, onde eu explico que você deve criar uma conta no AWS e criá la no serviço EC2 uma instância de uma máquina virtual com o Ubuntu Linux.
Então é a partir dessa máquina virtual. A gente vai, então, criar o nosso postgres. Então, a parte prática ela já pressupõe que você já está com essa máquina virtual criada e que você já está conectado a ela no seu prompt de comando.
Dado esse pressuposto, qual vai ser o nosso roteiro? Qual vai ser o roteiro da nossa parte prática?
●	Primeiro a gente vai instalar o UnZip para descompactar os arquivos.
●	Depois a gente vai instalar o postgre que já mencionamos. É um banco de dados relacional gratuito, um dos mais populares.
●	A gente vai criar um diretório, uma pasta.
●	A gente vai baixar da internet diretamente para essa máquina virtual, um arquivo zip com os scripts.
●	A gente vai logar no PSQL, que é o aplicativo de linha de comando do Postgres.
●	A gente vai criar um banco de dados que vai se chamar ID.
●	A gente vai conectar nesse banco de dados.
●	Vamos conectar o PSL nesse banco de dados e a gente vai criar.
É popular esse banco de dados, então a gente vai criar objetos. Então ele vai criar todas as tabelas nesse banco de dados. A gente vai inserir dados nesse banco de dados.
Como a gente vai fazer isso?
Bom, aquele arquivo que eu falei lá que você vai baixar da internet. Ele tem alguns scripts prontos que, como já foi mencionado, não faz sentido a gente ficar digitando código para fazer inserção de registros. Então existe alguns scripts prontos que você vai baixar.
Diretamente da internet, usando um comando do Linux, o W Get, para sua máquina virtual. 
●	Então você vai ter um script para criar todas as tabelas.
●	
●	O script vai ser dos clientes
●	O script vai ser de produtos para serem vendedores, vendas e itens, venda.
●	E existe um script interativo. (Esse script você não vai rodar ele).  Esse script vai executar passo a passo. Analisando o resultado, que objetivo é a gente entender como que a linguagem SQL funciona.
Ok, então, a partir da próxima aula do próximo tutorial, a gente começa a nossa parte prática.
