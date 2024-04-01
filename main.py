from cards.unit import Unit
from cards.base import Base
from cards.capital_ship import Capital_Ship
from cards.cards import Cards
from cards.player import Player
from cards.force_tracker import Force_Tracker
from game import Game

def main():
    print("SW-DBG")
    cards = Cards()
    galaxy_deck = []
    galaxy_discard = []
    galaxy_deck = galaxy_deck + cards.create_cards('cards/units')
    outerrim = cards.create_cards('cards/starter/outerrim')
    bases = cards.create_cards('cards/bases')
    rebel_bases = [base for base in bases if base.faction == 'rebel']
    empire_bases = [base for base in bases if base.faction == 'empire']
    force_tracker = Force_Tracker()
    rebel_player = Player('rebel', cards.create_cards('cards/starter/rebel'), rebel_bases)
    empire_player = Player('empire', cards.create_cards('cards/starter/empire'), empire_bases)

    game = Game()
    print(rebel_player.resource_pool)
    game.start_turn(rebel_player, force_tracker)
    print(rebel_player.resource_pool)
    rebel_player.reset_turn()
    print(rebel_player.resource_pool)






    # for card in galaxy_deck:
    #     print(card.name, card.cost)







if __name__ == '__main__':
    main()