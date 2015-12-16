from random import randint


class Treasure:

    @staticmethod
    def generate_random_index(limit):
        rand_index = randint(0, limit)
        return rand_index

    @staticmethod
    def return_generated_treasure(max_mana, max_health):
        # generate num from 0-3
        rand_gen_num = Treasure.generate_random_index(3)
        options = {
            0: Treasure.generate_spell,
            1: Treasure.generate_weapon,
            2: Treasure.generate_mana_pot,
            3: Treasure.generate_health_pot
        }
        # give arguments for mana and health potion functions only (for now)
        if rand_gen_num == 2:
            options[rand_gen_num](max_mana)
        elif rand_gen_num == 3:
            options[rand_gen_num](max_health)

    @staticmethod
    def generate_spell():
        with open('spell_names.txt', 'r') as f:
            database_spell_names = f.read().replace('\n', '').split(',')

        lst_len = len(database_spell_names) - 1
        # generate number in range 0 - <spell names length>
        rand_gen_num = Treasure.generate_random_index(lst_len)

        spell_name = database_spell_names[rand_gen_num]
        spell_mana_cost = randint(5, 35)
        spell_damage = randint(5, 40)
        cast_range = randint(1, 3)

        # return Spell()

        print database_spell_names

    @staticmethod
    def generate_weapon():

        with open('weapon_names.txt', 'r') as f:
            database_weapon_names = f.read().replace('\n', '').split(',')

        lst_len = len(database_weapon_names) - 1
        rand_gen_num = Treasure.generate_random_index(lst_len)

        weapon_name = database_weapon_names[rand_gen_num]
        weapon_damage = randint(5, 40)

        # return Wep
    @staticmethod
    def generate_mana_pot(max_mana):
        max_possible_mana_limit = max_mana * 1/2
        mana_portion = randint(0, max_possible_mana_limit)


    @staticmethod
    def generate_health_pot(max_health):
        max_possible_health_limit = max_health * 1/3
        health_portion = randint(0, max_possible_health_limit)

def main():
    print (Treasure.return_generated_treasure(100,100))

if __name__ == '__main__':
    main()
