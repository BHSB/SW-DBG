class Game():

    def start_turn(self, player, force_tracker):
        print(f"{player.faction.capitalize()}'s turn.")
        # Check if there is an active base, choose a new one if not
        if player.active_base == None:
            player.select_new_base()
        print(f"The force is with the {force_tracker.check_force()} side ({force_tracker.force}/7)")
        # Gain +1 resource if the force with max light/dark
        if force_tracker.get_resource(player.faction):
            print("The force is strong with you. Gain 1 resource")
            player.resource_pool += 1
        # Gain resources for all capital ships in play
        if bool(player.active_capital_ships):
            ship_resources = 0
            for ship in player.active_capital_ships:
                player.resource_pool += ship.resource
                ship_resources += ship.resource
            print(f"{ship_resources} resources gained from capital ships in play.")

    def select_action(self):
        print("*" * 20, '\nPlayer actions...\n')
        options = [
            'Play a card',
            'Purchase a card',
            'Use a card ability',
            'Commit to an attack',
            'Resolve an attack',
            'End your turn'
        ]

        for i, option in enumerate(options):
            print(f"{i + 1}: {option}")

        while True:
            try:
                selection = int(input("Select a turn action to perform: ") - 1)
                return options[selection]
            except (IndexError, ValueError):
                print(f"Select a number between the 1 and {len(options)}.")

    def take_action(self, player):
        player.show_cards(player.hand, 'hand')
        action = self.select_action()
        if action == 'Play a card':
            card = player.show_cards(player.hand, 'hand')
            self.play_card(card)
        elif action == 'Purchase a card':
            pass
        elif action == 'Use a card ability':
            pass
        elif action == 'Commit to an attack':
            pass
        elif action == 'Resolve an attack':
            pass
        elif action == 'End your turn':
            pass

    def play_card(self, player, force_tracker, card):
        # gain resource
        player.resource_pool += card.resources
        # gain force
        force_tracker.add_force(player.faction, card.force)
        # activate ability
        ## passive
        ## optional

        pass

