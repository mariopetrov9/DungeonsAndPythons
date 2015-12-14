class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self._health = health
        self._mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self._max_health = health
        self._max_mana = mana

        # classes
        self._weapon = self.get
        self._spell

    def known_as(self):
        return '{} the {}'.format(self.name, self.title)

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        return self._health > 0

    def can_cast(self, given_magic):
        return given_magic >= self._mana

    def take_damage(self, damage_points):
        self._health -= damage_points
        if self._health < 0:
            self._health = 0

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            self._health += healing_points
            if self._health > self._max_health:
                self._health = self._max_health
            return True

    def take_mana(self, mana_points):
        # if not self.is_alive():
        #     return False
        self._mana += mana_points
        if self._mana > self._max_mana:
            self._mana = self._max_mana

    # call it when the hero is moved
    def _auto_regenerate_mana(self):
        self._mana += self.mana_regeneration_rate

    def equip(self, weapon):
        pass

    def learn(self, spell):
        pass

    def attack(self):
        pass

    

