class Warrior:
    def attack_with_sword(self):
        print("The character attacks with a sword")


class Mage:
    def cast_spell(self):
        print("The character casts a spell")


class Paladin(Warrior, Mage):
    def use_special_ability(self):
        print("The paladin uses a holy ability")


paladin = Paladin()

paladin.attack_with_sword()
paladin.cast_spell()
paladin.use_special_ability()