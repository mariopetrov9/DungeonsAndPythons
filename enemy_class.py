import spell_class


class Enemy:

    def __init__(self, health, mana, damage):
        self._health = health
        self._mana = mana
        self._damage = damage
        self._max_health = health

    def is_alive(self):
        if self._health > 0:
            return True
        return False

    def can_cast(self, spell):
        if self._mana >= spell.get_mana_cost():
            return True
        return False

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            self._health += healing_points
            if self._health > self._max_health:
                self._health = self._max_health
            return True

    def take_mana(self, mana_points):
        self._mana += mana_points

    def attack(self):
        return self._damage
        # not completed !

    def take_damage(self, damage_points):
        self._health -= damage_points
