import random

# Card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Create a deck of cards
def create_deck():
    deck = []
    for card in card_values:
        for _ in range(4):  # 4 suits
            deck.append(card)
    random.shuffle(deck)
    return deck

# Calculate hand value, treating aces as 1 or 11
def calculate_hand_value(hand):
    value = sum(card_values[card] for card in hand)
    # Adjust for Aces
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Print hand and value
def print_hand(name, hand):
    print(f"{name}'s hand: {', '.join(hand)} (value: {calculate_hand_value(hand)})")

# Game logic
def blackjack():
    deck = create_deck()
    
    # Initial deal
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Show hands
    print_hand('Player', player_hand)
    print(f"Dealer's hand: {dealer_hand[0]}, ?")
    
    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        move = input("Do you want to [h]it or [s]tand? ").lower()
        if move == 'h':
            player_hand.append(deal_card(deck))
            print_hand('Player', player_hand)
        elif move == 's':
            break
        else:
            print("Invalid choice. Please choose [h]it or [s]tand.")
    
    player_value = calculate_hand_value(player_hand)
    
    if player_value > 21:
        print("Player busts! Dealer wins.")
        return
    
    # Dealer's turn
    print_hand('Dealer', dealer_hand)
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        print_hand('Dealer', dealer_hand)
    
    dealer_value = calculate_hand_value(dealer_hand)
    
    # Determine winner
    if dealer_value > 21:
        print("Dealer busts! Player wins.")
    elif dealer_value > player_value:
        print("Dealer wins.")
    elif dealer_value < player_value:
        print("Player wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    blackjack()
