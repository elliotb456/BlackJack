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
        self.setWindowTitle('Blackjack - PyQt5 GUI') # Sets the main window title
        self.setGeometry(200, 200, 600, 400) # Sets the window size to 600x400 pixels

        # Layouts
        # QVBoxLayout: Arranges elements vertically (dealer area, player area, and controls)
        # QHBoxLayout: Used for arranging dealer/player labels, scores, and controls horizontally
        self.vbox = QVBoxLayout()
        self.dealer_box = QHBoxLayout()
        self.player_box = QHBoxLayout()
        self.controls = QHBoxLayout()

        # Labels for the cards
        # Dealer and player labels (QLabel) display "Dealer's Cards:" and "Player's Cards:"
        # Result Label (QLabel) displays the game status (e.g., "Game in Progress")
        # Score labels show the dealer’s and player’s current score
        self.dealer_label = QLabel("Dealer's Cards:")
        self.player_label = QLabel("Player's Cards:")
        self.result_label = QLabel('Game in Progress')
        self.result_label.setAlignment(Qt.AlignCenter)
        self.dealer_score_label = QLabel('Dealer Score: 0')
        self.player_score_label = QLabel('Player Score: 0')

        # Align dealer/player labels and scores 
        self.dealer_layout = QHBoxLayout()
        self.dealer_layout.addWidget(self.dealer_label)
        self.dealer_layout.addStretch()
        self.dealer_layout.addWidget(self.dealer_score_label)

        self.player_layout = QHBoxLayout()
        self.player_layout.addWidget(self.player_label)
        self.player_layout.addStretch()
        self.player_layout.addWidget(self.player_score_label)

        # Buttons
        self.hit_btn = QPushButton('Hit') # Adds a card to the players hand
        self.stand_btn = QPushButton('Stand') # Ends the players turn and lets the dealer play
        self.restart_btn = QPushButton('Restart') # Resets the game

        # The above buttons are linked to their respective methods using .clicked.connect()
        self.hit_btn.clicked.connect(self.hit)
        self.stand_btn.clicked.connect(self.stand)
        self.restart_btn.clicked.connect(self.restart)

        # Add widgets to the layouts 
        # Dealer and player sections are grouped using horizontal layouts
        self.vbox.addLayout(self.dealer_layout)
        self.vbox.addLayout(self.dealer_box)
        self.vbox.addLayout(self.player_layout)
        self.vbox.addLayout(self.player_box)
        self.vbox.addWidget(self.result_label)

        # Buttons are aligned in a horizontal layout (controls)
        self.controls.addWidget(self.hit_btn)
        self.controls.addWidget(self.stand_btn)
        self.controls.addWidget(self.restart_btn)

        # The main layout (vbox) stacks everything neatly
        self.vbox.addLayout(self.controls)
        self.setLayout(self.vbox)

        # Calling restart when initializing the UI ensures the game starts in a fresh state when the window loads
        self.restart()


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
