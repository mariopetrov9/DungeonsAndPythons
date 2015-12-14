class Weapon:

    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    def get_damage(self):
        return self._damage

    def get_name(self):
        return self._name
