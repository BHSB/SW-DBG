class Force_Tracker():

    def __init__(self):
        self.force = 7

    def check_force(self):
        if self.force > 4:
            return 'light'
        elif self.force == 4:
            return 'neutral'
        elif self.force < 4:
            return 'dark'

    def add_force(self, faction, force):
        if faction == 'rebel':
            self.force += force
        else:
            self.force -= force

        if self.force > 7:
            self.force = 7
        elif self.force < 1:
            self.force = 1

    def get_resource(self, faction):
        if (faction == 'rebel' and self.force == 7) or \
            (faction == 'empire' and self.force == 1):
            return True
        else:
            return False
