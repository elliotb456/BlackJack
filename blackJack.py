# Importing Required Modules 

import sys # For handling system operations 
import random # For shuffling and dealing cards 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont 
from PyQt5.QtCore import Qt



# This Project consists of two main classes | Card & Game 


# Card class | Handles the cards > face, value, suit
class Card:

    # Represents a single playing card | Storing its Face, Value  and Suit
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



    # This method provides a clean, structured, and interactive GUI for the Blackjack game.
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



    # This method ensures that every new game begins with a randomly shuffled deck of 52 cards
    def init_deck(self):
        suits = ['♠', '♥', '♦', '♣'] # 4 suits in a deck of cards: Spades, Hearts, Diamonds, Clubs 

        # Cards 2-10 retain their numeric value
        # Face cards (J, Q, K) are assigned a value of 10.
        # The Ace (A) is given an initial value of 11, but its value will be adjusted later if needed
        faces = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        
        # Use a list comprehension to generate all 52 cards, combining each suit with all face values
        # Each card is an instance of the Card class, which stores its face, value, and suit
        deck = [Card(face, value, suit) for suit in suits for face, value in faces.items()]

        # The Deck is randomly shuffled and then returned
        random.shuffle(deck)
        return deck



    # This method ensures that every time a new round starts, the game resets completely, allowing for a new playthrough
    def restart(self):
        self.deck = self.init_deck() # Calls init_deck() to create and shuffle a fresh deck of cards 

        # Resets the players and dealers hands to be empty 
        self.player_cards = []
        self.dealer_cards = []

        # Resets the players and dealers score to zero
        self.player_score = 0 
        self.dealer_score = 0

        # Ensures the game is active by setting game_over to false
        self.game_over = False 

        # Resets the UI to remove te previous cards 
        self.clear_layout(self.dealer_box)
        self.clear_layout(self.player_box)

        # Deal initial cards
        # Each the player and dealer both receive two starting cards using the deal_card method 
        for _ in range(2):
            self.player_cards.append(self.deal_card())
            self.dealer_cards.append(self.deal_card())

        # Calles update_display() ro reflect the new hands on the screen 
        self.update_display()

        # Re-enables the 'hit' and 'stand' buttons so the player can interact with the game
        self.hit_btn.setDisabled(False)
        self.stand_btn.setDisabled(False)

        # Updates the result label to display 'Game in Progress' 
        self.result_label.setText('Game in Progress')



    # The deal_card() method handles drawing a card from the deck
    # Retrieves (pop()) the top card from the deck
    # Since the deck is shuffled at the start (init_deck()), this ensures randomness
    # The returned Card object contains the face, value, and suit
    def deal_card(self):
        return self.deck.pop()



    # Computes the score for both the player and dealer while enforcing Blackjack rules and determining winners 
    # Uses list comprehension to sum up the values of all cards in the given hand
    # Since face cards (J, Q, K) have a value of 10, and Aces (A) initially have 11, they are already accounted for in the Card class
    def calculate_score(self, cards):
        score = sum(card.value for card in cards)
        aces = sum(1 for card in cards if card.face == 'A')

        # If the total score exceeds 21, we check for Aces ('A')
        # Since Aces can be either 11 or 1, we subtract 10 from the score for each Ace until the score is 21 or lower
        # This ensures the best possible score without busting
        while score > 21 and aces: 
            score -= 10
            aces -= 1
        return score



    # The update_display() method updates the UI by rendering the current state of the game, displaying the cards, scores, and handling game-over scenarios
    # Ensures that the game UI updates dynamically
    # Controls how cards are displayed and hidden
    # Implements Blackjack rules like hiding the dealer’s first card
    # Handles busting conditions efficiently
    def update_display(self):

        # Calls clear_layoutto remove previously displayed cards
        self.clear_layout(self.dealer_box)
        self.clear_layout(self.player_box)

        # Dealers cards
        for i, card in enumerate(self.dealer_cards): 
            color = 'red' if card.suit in ['♥', '♦'] else 'black' # Hearts and diamons are red, other suites are black
            if i == 0 and not self.game_over:
                color = 'blue' # If the game is not over hides the dealers first card with the colour blue to differentiate 
                label_text = '🂠'
            else:
                label_text = f'{card.face}{card.suit}' # If the game is over displayes all of the dealers cards

            # Font, style, and alignment for the dealers label
            label = QLabel(label_text)
            label.setFont(QFont('Arial', 16, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(f'border: 2px solid black; padding: 10px; background: white; color: {color}; min-width: 60px; min-height: 100px;')
            self.dealer_box.addWidget(label)

        # Players cards | Always visible
        for card in self.player_cards:
            color = 'red' if card.suit in ['♥', '♦'] else 'black' # Hearts and diamons are red, other suites are black

            # Font, style, and alignment for the players cards 
            label = QLabel(f'{card.face}{card.suit}')
            label.setFont(QFont('Arial', 16, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(f'border: 2px solid black; padding: 10px; background: white; color: {color}; min-width: 60px; min-height: 100px;')
            self.player_box.addWidget(label)

        # Calls calculate_score() to update the players and dealers score
        self.player_score = self.calculate_score(self.player_cards)
        self.dealer_score = self.calculate_score(self.dealer_cards)

        # Players score always displayed | Dealers score hiddne (?) until the game ends
        self.player_score_label.setText(f'Player Score: {self.player_score}')
        self.dealer_score_label.setText(f'Dealer Score: {self.dealer_score if self.game_over else '?'}')

        # If the players score exceeds 21, they go bust
        if self.player_score > 21:
            self.result_label.setText('Player Busts! Dealer Wins!') # Updates the results label

            # Disables the playing buttons
            self.hit_btn.setDisabled(True)
            self.stand_btn.setDisabled(True)

            # Marks game_over as true
            self.game_over = True



    # The clear_layout() method ensures the UI updates properly by removing previous elements 
    # Loops through all widgets inside a given layout
    # Uses .takeAt(0) to remove items one by one
    # If the item is a widget, it is deleted (deleteLater()) to clear the UI properly
    # This is important for refreshing the dealer's and player's hands before updating the display
    def clear_layout(self, layout): 
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()



    # The below two methods hit() & stand() complete the game logic, allowing smooth and interactive gameplay

    # Handles the players 'Hit' action
    def hit(self):
        if not self.game_over: # Checks first to mamke sure the game is still running
            self.player_cards.append(self.deal_card()) # Deals a new card to the player
            self.player_score = self.calculate_score(self.player_cards) # Recalculates the score based on the new card
            self.update_display() # Calls update_display() to refresh the UI based on the new score

            # If the players score exceeds 21, the game declares a bust
            # Updates the labels and disables the buttons, marks the game as 'over'
            if self.player_score > 21:
                self.result_label.setText('Player Busts! Dealer Wins!')
                self.hit_btn.setDisabled(True)
                self.stand_btn.setDisabled(True)
                self.game_over = True
                self.update_display()



    # Handles the players 'Stand' action, and lets the dealer play
    def stand(self):
        # Disables the 'Hit' and 'Stand' buttons to prevent further player interaction
        self.hit_btn.setDisabled(True)
        self.stand_btn.setDisabled(True)

        # While loop ensures the dealer keeps drawing cards until their score reaches at least 17 | As per Blackjack rules
        while self.dealer_score < 17:
            self.dealer_cards.append(self.deal_card()) # Draws card
            self.dealer_score = self.calculate_score(self.dealer_cards) # Updates score based on drawn card above

        # Once the dealer stops drawing cards, the game is marked as 'over' and the display is updated
        self.game_over = True
        self.update_display()

        # Determines the final game result
        # If dealer busts (>21) -> Player wins
        if self.dealer_score > 21:
            self.result_label.setText('Dealer Busts! Player Wins!')
        # If dealer has a higher score than the player -> Dealer wins
        elif self.dealer_score > self.player_score:
            self.result_label.setText('Dealer Wins!')
        # If dealer has a lower score than the player -> Player wins
        elif self.dealer_score < self.player_score:
            self.result_label.setText('Player Wins!')
        # If scores are equal -> it's a tie
        else:
            self.result_label.setText("It's a Tie!")

        # Ensures that the UI updates smoothly
        QApplication.processEvents()





# Runs the PyQt5 application and intializes the game window, starting the event loop 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BlackjackGame()
    window.show()
    sys.exit(app.exec_())