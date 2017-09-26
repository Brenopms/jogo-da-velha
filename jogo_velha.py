#from __future__ import print_function

def print_board (board):
    print('O quadro atual: \n ')
    print ('', board[1], '|', board[2], '|', board [3], '\n', board[4], '|', board[5], '|', board[6], '\n', board[7], '|', board[8],'|', board[9])
    
def modelo_board ():
    print (' \n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n') 

    
def escolha_sinal():
    jogador1 = input('Escolha se voce quer usar X ou O: ')
    jogador1 = jogador1.upper()
    if jogador1 == 'X':
        jogador2 = 'O'
    else:
        jogador2 = 'X'
    return [jogador1, jogador2]
        
def input_user (board, jogador):
    modelo_board()
    x = True
    while(x == True):
        temp = int(input('Escolha uma posicao: '))
        if temp>9 or temp<1 or board[temp] != ' ':
            x = True
            print('Digite  uma posicao valida ')
        else:
            board[temp] = jogador
            x = False
    print_board(board)

def init_board():
    board  = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
    return board

def check_win (board):
    if check_linha(board) or check_coluna(board) or check_diagonal(board) == True:
        return True
    else:
        return False
    
def check_linha(board):
    if (board[1] == board[2] == board[3] != ' ' or board[4] == board[5] == board[6] != ' ' or board[7] == board[8] == board[9] != ' '):
        return True
    else:
        return False
    
def check_coluna(board):
    if (board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' ' or board[3] == board[6] == board[9] != ' ' ):
        return True
    else:
        return False
    
def check_diagonal(board):
    if (board[1] == board[5] == board[9] != ' ' or board[3] == board[5] == board[7] != ' ' ):
        return True
    else:
        return False

def check_tie(board):
    if ' ' in board[1:]:
        return False
    else:
        return True
    
def rodada(board, player):
    input_user(board,player)
    if (check_win(board)== True):
        print ( ' Parabens por ganhar')
        return False

    if (check_tie(board) == True):
        print ( 'Jogo empatado')
        return False
    else:
        return True
    
# --------- Main Program Start ---------                       
fim = False
while not (fim):    
    board = init_board()
    jogador1 = ' '
    jogador2 = ' '
    jogador1, jogador2 = escolha_sinal()
    play = True
    player = 1
    jogando = True
    while(jogando):
        while(play):
            player+=1
            if (player%2 == 0):
                play = rodada(board,jogador1)
            elif(play):
                play = rodada (board,jogador2)

        continuar = input('deseja continuar? S ou N ')
        continuar = continuar.upper()
        if continuar == 'N':
            jogando = False
            fim = True
        else:
            jogando = False
            play = False
            fim = False

        
        



        




    
    
    
    
