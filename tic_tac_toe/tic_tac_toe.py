from operator import length_hint
import random
# create board
# pick player/ one player is x, the other o
#player picks spot
#check if board is full
#check who wins
class Board:

  
  def __init__(self,col,row):

    self.board = [['_' for i in range(col)]for i in range(row)
    ]
  
  def draw_board(self):
    print(self.board)
     
      
  
  def choose_random_player(self):
    return random.randint(0,1)
    
  def is_board_filled(self):
    for row in self.board:
      for item in row:
        if item == '_':
          return False
    return True



class TicTacToe(Board):
  def __init__(self,col = 3,row = 3):
    self.board = [['_' for i in range(col)]for i in range(row)
    ]

  def assign_player(self):
    if self.choose_random_player() == 1:
      self.player = 'x'
    elif self.choose_random_player() == 0:
      self.player = 'o'
  
  def next_player(self):
    if self.player == 'x':
      self.player = 'o'
    if self.player == 'o':
      self.player = 'x'

  def select_spot(self):
    row = int(input('Please choose your next move, row number 1, 2, or 3:  \n')) - 1
    col = int(input('Please choose your next move, column number 1, 2, or 3:  \n')) - 1
    self.board[row][col] = self.player

  def winner(self):
    win = None 
    le = len(self.board)

    #check row
    for row in range(le):
      win = True
      for col in range(le):
        if self.board[row][col] != self.player:
          win = False
          break
    if win == True:
      return True

    #check col
    for row in range(le):
      win = True
      for col in range(le):
        if self.board[col][row] != self.player:
          win = False
          break
    if win == True:
      return True

    #check diagnol
    if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player or self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player):
      win = True
    else: 
      win = False
    if win == True:
      return True

  
  def start(self):
    self.choose_random_player()
    self.assign_player()
    
    self.draw_board()

    while True:
      self.select_spot()
      self. draw_board()

      self.winner()
      self.is_board_filled()
      

      if self.winner() == True:
        print(f'Player {self.player} Wins!!')
        break
      elif self.is_board_filled() == True:
        print('DRAW!')
        break
    rematch = input('Do you want to play again? \nEnter Yes or No \n')
    if rematch.strip().lower() == 'yes':
      return self.start()
    else: 
      return exit()
   
      

TicTacToe().start()
