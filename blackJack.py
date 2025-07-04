# Importing Required Modules 
import sys # For handling system operations 
import random # For shuffling and dealing cards 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont 
from PyQt5.QtCore import Qt


# This Project consists of two main classes | Card & Game 

# Card class | Handles the cards > face, value, suit
class Card:

    # Represents a single playing card | Storing its Face, Value, and Suit
    def __init__(self, face, value, suit):
        self.face = face
        self.value = value 
        self.suit = suit 


# Game class | Handles the game logic and GUI
class BlackjackGame(QWidget):

    # Initializes the game window and calls initUI()
    def __init__(self):
        super().__init__()
        self.initUI()

    # Sets up the graphical innterfactes (buttons, labels, layouts)
    def initUI(self):
        pass

    # Creates and shuffles a full deck of cards 
    def init_deck(self):
        pass

    # Resets the game face for a new round 
    def restart(self):
        pass

    # Draws a card from the deck
    def deal_card(self):
        pass

    # Computes the score for both the player and dealer
    def calculate_score(self, cards):
        pass

    # Updates the UI with the latest game info
    def update_display(self):
        pass

    # Clears old UI elements before updating the display 
    def clear_layout(self, layout): 
        pass

    # Handles the players 'Hit' action
    def hit(self):
        pass

    # Handles the players 'Stand' action, and lets the dealer play
    def stand(self):
        pass

# Runs the PyQt5 application and intializes the game window, starting the event loop 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BlackjackGame()
    window.show()
    sys.exit(app.exec_())
