class Abilities():

    def select_ability(self, ability):
        if ability == 'select_raf_1':
            self.select_raf()

    def select_raf(self, amount=1):
        """
        Player choose either resource, attack, force or nothing.
        """
        options = ['Resource', 'Attack', 'Force', 'Do nothing']

        for i, option in enumerate(options):
            if option.startswith('Do'):
                print(f'{i + 1}.', f'{option}.')
            else:
                print(f'{i + 1}.', f'Gain {amount} {option}.')

        while True:
            try:
                selection = int(input('Select option: ') - 1)
                return (amount, option[selection.lower()])
            except ValueError:
                print(f'Enter a number between 1 and 4.')


a = Abilities()
a.select_raf()