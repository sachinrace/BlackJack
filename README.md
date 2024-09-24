**Overview**
This is a simple Python implementation of the Blackjack card game. The game simulates a one-on-one match between a player and a dealer, following the basic rules of Blackjack. The player aims to get as close to 21 points without exceeding it, while also trying to beat the dealer’s hand.

**Features**
Deck of cards is automatically generated and shuffled.
Aces can be counted as either 1 or 11, depending on the situation.
Basic game logic for hitting or standing, as well as dealer actions.
Interactive input for the player to choose between "hit" or "stand".
Game determines a winner by comparing the player's hand with the dealer's hand.
**How to Play**
The player and dealer are each dealt two cards.
The player's hand value is displayed, and the player is prompted to either hit (draw another card) or stand (keep their current hand).
The dealer's hand is revealed, and the dealer must hit until their hand's value is 17 or higher.
The winner is determined based on the hand values, with possible outcomes including a player win, dealer win, tie, or bust (exceeding 21 points).
**Code Structure**
**create_deck()**
Creates a deck of cards consisting of four suits with values ranging from 2 to Ace. The deck is shuffled before the game begins.

**calculate_hand_value(hand)**
Calculates the value of a player's or dealer's hand. Aces are dynamically counted as 11 or 1 depending on the total hand value to prevent busting.

**deal_card(deck)**
Deals a card from the shuffled deck.

**print_hand(name, hand)**
Displays the player's or dealer's hand and its calculated value.

**blackjack()**
Main function that contains the game logic, including the player's and dealer's turn sequence.
