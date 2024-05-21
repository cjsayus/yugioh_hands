import random

class YuGiOhDeck:
    def __init__(self):
        self.cards = ['Tenpai Dragon Chundra','Tenpai Dragon Chundra','Tenpai Dragon Chundra',
                      'Tenpai Dragon Paidra','Tenpai Dragon Paidra','Tenpai Dragon Paidra',
                      'Tenpai Dragon Fadra','Tenpai Dragon Fadra',
                      'Sangen Summoning','Sangen Summoning','Sangen Summoning', 'Terraforming',
                      'Sangen Kaimen', 'Sangen Kaimen','Sangen Kaimen',
                      'Ash Blossom', 'Ash Blossom', 'Ash Blossom',
                      'Ghost Ogre','Ghost Ogre','Ghost Ogre',
                      'Effect Veiler','Effect Veiler','Effect Veiler',
                      'Infinite Impermanence','Infinite Impermanence','Infinite Impermanence',
                      'Ghost Belle', 'Ghost Belle',
                      'Bystial Magnamut', 'Kashtira Fenrir', 'Kashtira Fenrir',
                       'Pot of Prosperity', 'Pot of Prosperity', 'Pot of Prosperity',
                      'Forbidden Droplets', 'Forbidden Droplets','Forbidden Droplets',
                      'Feather Duster', 'Ligntning Storm', 'Ligntning Storm',]  # Sample cards, you can add more
        self.deck_size = len(self.cards)
        print(f"Deck size: {self.deck_size}")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_hand(self, num_cards):
        hand = []
        for _ in range(num_cards):
            if len(self.cards) > 0:
                card = self.cards.pop(0)
                hand.append(card)
            else:
                print("Deck is empty!")
                break
        return hand

def main():
    deck = YuGiOhDeck()
    deck.shuffle()
    hand = deck.draw_hand(5)  # Drawing 5 cards
    print("Your hand:")
    for card in hand:
        print(card)

    # List of cards to check for in the hand
    hand_traps = ['Ash Blossom',
                      'Ghost Ogre',
                      'Effect Veiler',
                      'Infinite Impermanence',
                      'Ghost Belle',
                      'Bystial Magnamut',]

    # Counter for hands containing at least one card from cards_to_check
    count = 0
    for card in hand:
        if card in hand_traps:
            count += 1

    if count > 0:
        print("This hand contains at least one of the following cards:")
        for card in hand_traps:
            if card in hand:
                print(card)
        print(f"Number of hands with at least one hand trap: {count}")

    if count == 0:
        print("There were no hand traps in this hand")

if __name__ == "__main__":
    main()

