import random
from unidecode import unidecode
from Player import Player

class RodaRodaJequiti():
    # Método Construtor
    def __init__(self, conectionSocket):
        self.word = None
        self.wrong_words = []
        self.correct_words = []
        self.player_list = []
        self.player_current = None
        self.conectionSocket = conectionSocket
        self.roleta = [100, 150, 200, 'passa',250, 300,
                      'passa',350, 400, 450, 500, 'passa',
                       550, 600, 'perdeu',650, 700, 750,
                       'passa', 800, 850, 900, 950, 1000, 'passa']
    
    # Método para adivinhar a leta
    def guess(self, letter, score):
        while letter in self.correct_words or letter in self.wrong_words:
            self.conectionSocket.send(str('>> Letra inválida, digite novamente: ').encode())
            letter = self.conectionSocket.recv(1024).decode().strip().upper()
        if letter in ['A','E', 'I', 'O', 'U']:
            if(letter in unidecode(self.word) and (letter not in self.correct_words)):
                self.conectionSocket.send(str('>> Acertou !!!\n>> Digite OK para continuar...').encode())
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                self.correct_words.append(letter)
                self.player_current.score += score
            elif (letter not in unidecode(self.word)) and (letter not in self.wrong_words):
                self.conectionSocket.send(str('>> Errou !!!\n>> Digite OK para continuar...').encode())
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                self.player_current = self.passTurn()
                self.wrong_words.append(letter)
        elif letter not in ['A','E', 'I', 'O', 'U']:
            if (letter in self.word) and (letter not in self.correct_words):
                self.conectionSocket.send(str('>> Acertou !!!\n>> Digite OK para continuar...').encode())
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                self.correct_words.append(letter)
                self.player_current.score += score
            elif (letter not in self.word) and (letter not in self.wrong_words):
                self.conectionSocket.send(str('>> Errou !!!\n>> Digite OK para continuar...').encode())
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                self.player_current = self.passTurn()
                self.wrong_words.append(letter)
        else:
            return False
        return True
    
    # Troca jogador
    def passTurn(self):
        current_player = self.player_current
        current_index = self.player_list.index(current_player)
        next_player = (current_index + 1) % len(self.player_list)
        return self.player_list[next_player]
    
    # Verifica se o jogo terminou
    def game_over(self):
        if self.game_won():
            return True
        return False
    
    # Verifica se o jogador venceu
    def game_won(self):
        if '_' not in self.hide_word():
            return True
        else:
            return False
    
    # Oculta as letras no board
    def hide_word(self):
        occultWord = ''
        for letter in self.word:
            if letter == ' ':
                occultWord += ' - '
                continue
            if unidecode(letter) in ['A','E', 'I', 'O', 'U']:
                if unidecode(letter) not in self.correct_words:
                    occultWord += '_ '
                else:
                    occultWord += letter
            elif letter not in self.correct_words:
                occultWord += '_ '
            else:
                occultWord += letter
        return occultWord
    
    def countWord(self):
        if ' ' in self.word: 
            return len(self.word) - 1
        else:
            return len(self.word)
    
    # Imprime placar
    def score_board(self):
        score = []
        header = '\n>> JOGADORES/PONTUAÇÃO:\n'
        for player in self.player_list:
            score.append('--> ' + str(player.nome) + ' = ' + str(player.score))
        #self.conectionSocket.send(str('>> JOGADORES/PONTUAÇÃO: ').encode())
        score = "  ".join(score)
        score = header + score
        return str(score)
        #self.conectionSocket.send(str(score).encode())
    
    # Imprime status do game e o board na tela
    def print_game_status(self, theme):
        status_game = []
        status_game.append('\nPalavra: (' +str(self.countWord())+' letras): '+ self.hide_word())
        status_game.append('Dica: '+ str(theme))
        status_game.append('Letas Erradas: '+ str(self.wrong_words))
        status_game.append('Letas Corretas: '+ str(self.correct_words))
        status_game = '\n'.join(status_game)
        score_board = self.score_board()
        return str(status_game + '\n' + score_board)
        #self.conectionSocket.send(str(status_game + '\n' + score_board).encode())

    # Sorteia palavra aleatória
    def rand_word(self, theme):
        if (theme == "ANIMAIS")or(theme == '1'):
            base_words = ['andorinha','baleia','cachorro','camaleão','elefante','golfinho', 'macaco','urso']
        elif (theme == "PAÍSES") or (theme == "PAISES") or (theme == '2'):
            base_words = ['Brasil','Angola', 'República Dominicana', 'Argentina','Estados Unidos','Chile','Bolívia','Espanha']
        elif (theme == "FRUTAS") or (theme == '3'):
            base_words = ['Abacate','Acerola','Caju','Carambola','Melão','Pêra','Tomate','Morango']
        self.word = base_words[random.randint(0, len(base_words) - 1)].strip().upper()

    def mode_game(self):
        menu = ['>>>>>>>>>> RODA A RODA <<<<<<<<<<']
        menu.append('Escolha um tema:')
        menu.append('==> Países')
        menu.append('==> Frutas')
        menu.append('==> Animais')
        menu.append('>> Opção: ')
        menu = '\n'.join(menu)

        opcoes = ['FRUTAS','PAÍSES','PAISES','ANIMAIS']

        self.conectionSocket.send(menu.encode())
        opcao = self.conectionSocket.recv(1024).decode().strip().upper()

        while opcao not in opcoes:
            self.conectionSocket.send(str('Opção inválida, digite novamente: ').encode())
            opcao = self.conectionSocket.recv(1024).decode().strip().upper()
        return opcao

    def select_player(self):
        self.conectionSocket.send(str('\n>> Digite o número de jogadores: ').encode())
        while True:
            try:
                number_player = self.conectionSocket.recv(1024).decode().rstrip()
                for player in range(int(number_player)):
                    self.conectionSocket.send(str('>> Digite o nome do jogador '+ str(player + 1)).encode())
                    name_player = self.conectionSocket.recv(1024).decode()
                    self.player_list.append(Player(name_player))
                    self.player_current = self.player_list[0]
                break
            except:
                self.conectionSocket.send(str('\n>> Entrada inválida, digite somente números: ').encode())
    
    def winner_player(self):
        winner = self.player_list[0]
        for player in self.player_list:
            if player.score > winner.score:
                winner = player 
        return winner

    def roda_roda(self):
        while True:
            self.conectionSocket.send(str('\n>>'+ self.player_current.nome + ' digite RodaRoda para continuar....').encode())
            user_input = self.conectionSocket.recv(1024).decode().rstrip().upper()
            while(user_input != 'RODARODA'):
                self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
            
            score = random.choice(self.roleta)

            if score == 'passa':
                result = ['\n>> Sorteio realizado ...']
                result.append('>> ' + self.player_current.nome + ' passa a vez !!')
                result.append('\n>>Digite OK para continuar!!')
                result = '\n'.join(result)
                self.conectionSocket.send(str(result).encode())

                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()

                self.player_current = self.passTurn()
                continue
            elif score == 'perdeu':
                result = ['\n>> Sorteio realizado ...']
                result.append('>> ' + self.player_current.nome + ' perdeu tudo !!')
                result.append('\n>>Digite OK para continuar!!')
                result = '\n'.join(result)
                self.conectionSocket.send(str(result).encode())
                
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()

                self.player_current.score = 0
                self.player_current = self.passTurn()
                continue
            else:
                result = ['\n>> Sorteio realizado ...']
                result.append('>>Digite OK para continuar!!')
                result = '\n'.join(result)
                self.conectionSocket.send(str(result).encode())
                
                user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                while(user_input != 'OK'):
                    self.conectionSocket.send(str('>> Comando inválido, digite novamente: ').encode())
                    user_input = self.conectionSocket.recv(1024).decode().strip().upper()
                return score
                
