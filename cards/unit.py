from .card import Card

class Unit(Card):

    def __init__(self, name, faction, unique, cost, attack, resources, force,
        target_value, reward, trait, ability=None, description=None):
        super().__init__(name, description)
        self.faction = faction
        self.unique = unique
        self.card_type = 'unit'
        self.cost = cost
        self.attack = attack
        self.resources = resources
        self.force = force
        self.target_value = target_value
        self.reward = reward
        self.trait = trait
        self.ability = ability # import from an abilities class that unpacks different types of abilities