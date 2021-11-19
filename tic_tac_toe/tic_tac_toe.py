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
    for row in self.board:
      print(row)
  
  def choose_random_player(self):
    return random.randint(0,1)
    
  def is_board_filled(self):
    for row in self.board:
      for item in row:
        if item == '_':
          return False
    return True

  def clear_board(self):
    le = len(self.board)
    for row in range(le):
      for col in range(le):
        self.board[row][col] = '_'

class TicTacToe(Board):
  def __init__(self,col = 3,row = 3):
    self.board = [['_' for i in range(col)]for i in range(row)
    ]

  def assign_player(self):
    self.player = self.choose_random_player() 
    self.player = 'x'
  
  def next_player(self):
    if self.player.strip() =='x':
      self.player = 'o'
    else:
      self.player = 'x'


  def select_spot(self):
    try:
      row,col =  [int(x) - 1 for x in input( f'{self.player} turn! Type the row number followed by a space and then column number to move.  ').split() ]
    except ValueError:
      print('Please enter your spot with a space seperating the row and column, example(1 1) is row 1 column 1.')
      self.select_spot()
    else:
    
      if self.board [row][col] == 'x' and self.player == 'o' or self.board [row][col] == 'o' and self.player == 'x' :
        print('That spot is already taken, please choose another.')
        self.select_spot()
      else:  
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
      self.next_player()
    rematch = input('Do you want to play again? \nEnter Yes or No \n')
    if rematch.strip().lower() == 'yes':
      self.clear_board()
      return self.start()
    else: 
      return exit()

      

TicTacToe().start()
