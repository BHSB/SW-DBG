import random

class Player():

    def __init__(self, faction, deck, bases):
        self.faction = faction
        self.bases = bases
        self.active_base = [base for base in bases if base.ability == 'starter'][0]
        self.enemy_bases = []
        self.active_capital_ships = []
        self.resource_pool = 0
        self.draw_deck = self.shuffle(deck)
        self.hand = []
        self.draw_hand()
        self.discard_deck = []

    def shuffle(self, cards):
        random.shuffle(cards)
        return cards

    def draw_deck_empty(self):
        if len(self.draw_deck) == 0:
            self.deck = self.shuffle(self.discard)

    def draw(self, amount=1):
        for i in range(0, amount):
            self.draw_deck_empty()
            self.hand.append(self.draw_deck.pop())

    def draw_hand(self):
        self.draw(5)

    def show_cards(self, options, deck, selection=False):
        if bool(options):
            print(f"{deck} is empty.")
        else:
            print(f'{self.faction.capitalize()} {deck}:\n')
            for i, card in enumerate(self.hand):
                print(f"{i + 1}: {card.name}")

        if selection:
            while True:
                try:
                    selection = int(input(f"Select card (1-{len(options)}): ") - 1)
                    return options[selection]
                except (ValueError, IndexError):
                    print(f"Select a number between 1 and {len(options)}.")

    def discard(self, card):
        self.discard_deck.append(card)

    def discard_hand(self):
        for card in range(0, len(self.hand)):
            self.discard(self.hand.pop())

    def reset_turn(self):
        self.resource_pool = 0
        self.discard_hand()
        self.draw_hand()

    def select_new_base(self):
        for i, base in enumerate(self.bases):
            print(f'{i + 1}: {base.name}, {base.ability}')

        while True:
            try:
                selection = int(input('Select new base: ') - 1)
                self.active_base = self.bases[selection]
                print(f'New base, {base.active_base.name}, selected')
                break
            except ValueError:
                print(f'Select a value between 1 and {len(self.bases)}')

