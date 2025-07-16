import os

def clean_screen():
   os.system('cls' if os.name == 'nt' else 'clear')


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    


    
    def choose_name(self):
        while True:
            name = input("please Enter your name\n")
            if(name.isalpha()):
                self.name = name
                break
            else:
                print("please use letters only\n")


    def choose_symbol(self):
        symbol = input(f"{self.name}, please Enter your symbol, (a single letter)\n")
        while True:
            if(symbol.isalpha()) and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("please use letters only and (a single letter)\n")
        
class Menu:

    def displey_start_menu(self):
        menu_text = """
        welcome to my X-O game
        pelase choose
        ----------------------------------------
        1. Start Game 
        2. Quit Game """
        print(menu_text)
        return self.validate_choice()
    
    def display_end_game(self):
        menu_text = """
        Game over!
        1. Restart Game
        2. Quit Game """
        print(menu_text)
        return self.validate_choice()
    
    def validate_choice(self):
        while True:
            Choice = input("        Enter your choice 1 or 2\n ")
            if(Choice == "1" or Choice == "2"):
                return int(Choice.strip())
            else:
                print("Please choose 1 or 2\n")

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]   
 
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            print("-"*6)

    def update_board(self, choice, symbol):
        if self.is_valide_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valide_move(self, choice):
        return self.board[choice-1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]   

class Game:
    def __init__(self):
        self.Players = [Player(), Player()]
        self.Board = Board()
        self.Menu = Menu()
        self.current_player = 0
    
    def Start_Game(self):
        choice = self.Menu.displey_start_menu()
        if choice == 1:
            clean_screen()
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def setup_players(self):
        for i, player in enumerate(self.Players, start = 1):
            print(f"Player {i} : please enter your details")
            player.choose_name()
            player.choose_symbol()
            clean_screen()

    def play_game(self):
        while True:
            self.player_turn()
            if(self.chack_win() or self.chack_draw()):
                print("*"*20)
                print(f"{self.player.name} is winner")
                print("*"*20)
                choice = self.Menu.display_end_game()
                if choice == 1:
                    self.restart_game()
                    clean_screen()

                else:
                    self.quit_game()
                    break

    def player_turn(self):
        clean_screen()
        self.player = self.Players[self.current_player]
        self.Board.display_board()
        print(f"{self.player.name}'s turn, {self.player.symbol}")
        cell_choice = int(input("choice a cell (1-9)"))
        while True:
            try:
                if(1<= cell_choice <=9 and self.Board.update_board(cell_choice,self.player.symbol)):
                    break
                else:
                    print("-"*15)
                    print("invalid move")
                    print("-"*15)
                    self.player_turn()
            except ValueError:
                print("please enter a number between 1 and 9")
        self.switch_player()

    def switch_player(self):
        self.current_player = 1 - self.current_player
 
    def chack_win(self):
        win_combinations = [
            [0, 1, 2],  
            [3, 4, 5], 
            [6, 7, 8], 

            [0, 3, 6], 
            [1, 4, 7], 
            [2, 5, 8], 

            [0, 4, 8],  
            [2, 4, 6]   
        ]
        for i in win_combinations:
            if(self.Board.board[i[0]] == self.Board.board[i[1]] == self.Board.board[i[2]]):
                return True
            return False
  

    def chack_draw(self):
        return all(not cell.isdigit() for cell in self.Board.board)

    def restart_game(self):
        self.Board.reset_board()
        self.current_player = 0
        self.play_game() 


    def quit_game(self):
        print("Thanks for playing! Goodbye.")
        exit()



game = Game()
game.Start_Game()