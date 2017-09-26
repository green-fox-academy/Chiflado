class Aircraft(object):

    def __init__(self, aircraft_type):
        self.aircraft_type = aircraft_type
        self.ammo = 0
        if aircraft_type == 'F18':
            self.max_ammo = 8
            self.base_damage = 30
        elif aircraft_type == 'F35':
            self.max_ammo = 12
            self.base_damage = 50