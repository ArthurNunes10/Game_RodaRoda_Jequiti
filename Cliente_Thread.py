from threading import Thread
import socket
from RodaRodaJequiti import RodaRodaJequiti

class Th(Thread):

    def __init__(self, conectionSocket, address):
        Thread.__init__(self)
        self.conectionSocket = conectionSocket
        self.address = address

    def run(self):
        game = RodaRodaJequiti(self.conectionSocket)
        theme = game.mode_game()
        game.select_player()
        game.rand_word(theme)

        while not game.game_over():
            score = game.roda_roda()
            # Dois send consecutivos
            status = game.print_game_status(theme)
            sentense = ' digite uma letra valendo R$' + str(score) + ' :'
            self.conectionSocket.send(str(status + '\n>> ' + game.player_current.nome + sentense).encode())
            user_input = self.conectionSocket.recv(1024).decode().strip().upper()
            game.guess(user_input, score)
        
        self.conectionSocket.send(str(game.print_game_status(theme) + '\n>> Digite  OK para ver o ganhador: ').encode())
        user_input = self.conectionSocket.recv(1024).decode().strip().upper()
        while(user_input != 'OK'):
            self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
            user_input = self.conectionSocket.recv(1024).decode().strip().upper()

        if game.game_won():
            winner = game.winner_player()
            mensage = str('\nParabéns!' + str(winner.nome) + ' ganhou a partida com R$' + str(winner.score))
            correct_word = str('\n>> A palavra era: ' + game.word)
            self.conectionSocket.send(str(mensage + correct_word + '\n>> Conexão Finalizada...').encode())