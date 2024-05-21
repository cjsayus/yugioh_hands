from yugioh_deck import YuGiOhDeck

def simulate_draws(num_simulations, num_cards):
    hand_traps = [
        'Ash Blossom',
        'Ghost Ogre',
        'Effect Veiler',
        'Infinite Impermanence',
        'Ghost Belle',
        'Bystial Magnamut',
    ]

    fenrir = ['Kashtira Fenrir']

    starters = ['Tenpai Dragon Chundra',
                'Tenpai Dragon Paidra',
                'Tenpai Dragon Fadra',
                'Sangen Summoning',
                'Terraforming',
                'Sangen Kaimen']

    count_hands_with_hand_traps = 0
    count_hands_with_two_or_more_hand_traps = 0
    count_hands_with_fenrir = 0
    count_hands_with_starters = 0

    # Initialize the deck once to get the counts
    deck = YuGiOhDeck()
    total_hand_traps_in_deck = sum(deck.deck[card] for card in hand_traps if card in deck.deck)
    total_fenrir_in_deck = sum(deck.deck[card] for card in fenrir if card in deck.deck)
    total_starters_in_deck = sum(deck.deck[card] for card in starters if card in deck.deck)
    total_ghost_ogre_in_deck = deck.deck.get('Ghost Ogre', 0)
    total_cards_in_deck = sum(deck.deck.values())

    for _ in range(num_simulations):
        deck.shuffle()
        hand = deck.draw_hand(num_cards)

        # Count the number of hand traps in the hand
        num_hand_traps_in_hand = sum(card in hand_traps for card in hand)

        # Check if the hand contains any hand traps
        if num_hand_traps_in_hand > 0:
            count_hands_with_hand_traps += 1

        # Check if the hand contains two or more hand traps
        if num_hand_traps_in_hand >= 2:
            count_hands_with_two_or_more_hand_traps += 1

        # Check if the hand contains any cards from fenrir
        if any(card in fenrir for card in hand):
            count_hands_with_fenrir += 1

        # Check if the hand contains any cards from starters
        if any(card in starters for card in hand):
            count_hands_with_starters += 1

    return count_hands_with_hand_traps, count_hands_with_two_or_more_hand_traps, count_hands_with_fenrir, count_hands_with_starters, total_hand_traps_in_deck, total_fenrir_in_deck, total_starters_in_deck, total_ghost_ogre_in_deck, total_cards_in_deck

def main():
    num_simulations = 100000
    num_cards = 5
    (count_hands_with_hand_traps,
    count_hands_with_two_or_more_hand_traps,
    count_hands_with_fenrir,
    count_hands_with_starters,
    total_hand_traps_in_deck,
    total_fenrir_in_deck,
    total_starters_in_deck,
    total_ghost_ogre_in_deck,
    total_cards_in_deck) = simulate_draws(num_simulations, num_cards)

    print(f"Out of {num_simulations} hands, {count_hands_with_hand_traps} contained at least one hand trap.")
    print(f"Out of {num_simulations} hands, {count_hands_with_two_or_more_hand_traps} contained two or more hand traps.")
    print(f"Out of {num_simulations} hands, {count_hands_with_fenrir} contained at least one card from fenrir.")
    print(f"Out of {num_simulations} hands, {count_hands_with_starters} contained at least one card from starters.")
    print(f"Total number of hand traps in the deck: {total_hand_traps_in_deck}")
    print(f"Total number of fenrir in the deck: {total_fenrir_in_deck}")
    print(f"Total number of starters in the deck: {total_starters_in_deck}")
    print(f"Total number of Ghost Ogre in the deck: {total_ghost_ogre_in_deck}")
    print(f"Total number of cards in the deck: {total_cards_in_deck}")

if __name__ == "__main__":
    main()
