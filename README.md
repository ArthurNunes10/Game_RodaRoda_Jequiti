# PROJETO DE REDES I
## Jogo Roda a Roda Jequiti
### Aluno
Arthur Nunes de Castro Oliveira
## Descrição
O projeto proposto trata-se de uma aplicação de redes usando sockets e threads, o qual foi implementado um jogo chamado Roda Roda Jequiti. Trata-se de um jogo baseado em recompensas, porém para recebê-las, é necessário acertar as perguntas, no caso tentar adivinhar as palavras ocultas, semelhante a um jogo da forca.
## Funcionalidades
O jogo começa solicitando o usuário a selecionar um tema para a partida, em  seguida é solicitado que seja informado a  quantidade de jogadores e seus respectivos nomes, então o jogo é iniciado com os participantes informados e com pontuação 
inicialmente zerada. 
O jogo acontece em turnos, para que cada jogador tenha o direito dizer uma letra, antes é necessário rodar a roleta, a qual contém diversas pontuações, como também 
algumas penalidades (passar a vez ou perder tudo), caso o jogador diga uma letra que não pertence a palavra, ele deixa de receber os pontos e passa a vez para o próximo participante, caso contrário, ele recebe os pontos e gira a roleta novamente, e assim sucessivamente, ganha o jogador que acumular mais pontos.
## Instruções de Execução
A aplicação foi desenvolvida em python 3 no ambiente Windows por meio da ferramenta Visual Studio Code. É necessário a instalação da biblioteca unidecode por meio do comando pip install unidecode. Após extrair o Zip para uma pasta, em seguida é necessário abrir dois terminais no diretório em que estão os arquivos. No primeiro terminal, execute o comando python Servidor.py para inicializar o servidor, em seguida 
no segundo terminal, execute o comando python Cliente.py para executar a classe cliente, caso queira executar mais de um cliente em paralelo, basta abrir novos terminais no diretório em questão, e executar a classe Cliente.py em cada um deles, lembrando que para que os clientes possam ser executados, é necessário que o servidor esteja ativo


