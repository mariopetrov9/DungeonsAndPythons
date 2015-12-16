class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_mana_cost(self):
        return self._mana_cost

    def get_cast_range(self):
        return self._cast_range
