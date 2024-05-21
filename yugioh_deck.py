import random

class YuGiOhDeck:
    def __init__(self):
        # Directly define the card list as a dictionary
        self.deck = {
            'Tenpai Dragon Chundra': 3,
            'Tenpai Dragon Paidra': 3,
            'Tenpai Dragon Fadra': 2,
            'Sangen Summoning': 3,
            'Terraforming': 1,
            'Sangen Kaimen': 3,
            'Ash Blossom': 3,
            'Ghost Ogre': 3,
            'Effect Veiler': 3,
            'Infinite Impermanence': 3,
            'Ghost Belle': 2,
            'Bystial Magnamut': 1,
            'Kashtira Fenrir': 2,
            'Pot of Prosperity': 3,
            'Forbidden Droplets': 3,
            'Feather Duster': 1,
            'Lightning Storm': 2
        }
        self.deck_size = sum(self.deck.values())


    def shuffle(self):
        self.shuffled_deck = []
        for card, count in self.deck.items():
            self.shuffled_deck.extend([card] * count)
        random.shuffle(self.shuffled_deck)

    def draw_hand(self, num_cards):
        hand = []
        for _ in range(num_cards):
            if len(self.shuffled_deck) > 0:
                card = self.shuffled_deck.pop(0)
                hand.append(card)
            else:
                print("Deck is empty!")
                break
        return hand


