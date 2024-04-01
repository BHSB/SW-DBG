from .card import Card

class Capital_Ship(Card):

    def __init__(self, name, faction, unique, cost, attack, resources,
        hp, ability=None, description=None):
        super().__init__(name, description)
        self.faction = faction
        self.unique = unique
        self.card_type = 'capital_ship'
        self.cost = cost
        self.attack = attack
        self.resources = resources
        self.hp = hp
        self.ability = ability # same as unit abilities

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def take_damage(self, damage):
        self.hp = self.hp - damage


    def repair(self, hp):
        self.hp = self.hp + hp