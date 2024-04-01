import json, os
from .unit import Unit
from .base import Base
from .capital_ship import Capital_Ship

class Cards():

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def create_cards(self, folder_path):
        cards = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.json'):
                file_path = os.path.join(folder_path, filename)
                json_data = self.load_json(file_path)

                # Now, you can process the JSON data as needed
                # print(f"Processing {filename}:")
                # skip outer rim pilots
                if json_data['card_type'] == 'unit':
                    for i in range(0, json_data['quantity']):
                        cards.append(Unit(
                            name = json_data['name'],
                            faction = json_data['faction'],
                            unique = json_data['unique'],
                            cost = json_data['cost'],
                            attack = json_data['attack'],
                            resources = json_data['resources'],
                            force = json_data['force'],
                            target_value = json_data['target_value'],
                            reward = json_data['reward'],
                            trait = json_data['trait'],
                            ability = json_data['ability'],
                            description = json_data['description'],
                        ))
                elif json_data['card_type'] == 'capital_ship':
                    for i in range(0, json_data['quantity']):
                        cards.append(Capital_Ship(
                            name = json_data['name'],
                            faction = json_data['faction'],
                            unique = json_data['unique'],
                            cost = json_data['cost'],
                            attack = json_data['attack'],
                            resources = json_data['resources'],
                            hp = json_data['hp'],
                            ability = json_data['ability'],
                            description = json_data['description']
                        ))
                elif json_data['card_type'] == 'base':
                    cards.append(Base(
                        name = json_data['name'],
                        faction = json_data['faction'],
                        hp = json_data['hp'],
                        ability = json_data['ability'],
                        description = json_data['description'],
                    ))

        return cards