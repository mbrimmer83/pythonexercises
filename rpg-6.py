import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            enemy.coins += self.coins
            self.coins -= self.coins
            print "%s recieved %s coins from %s" % (enemy.name, self.coins, self.name)
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        double_damage = random.random() > 0.8
        if double_damage:
            print "%s Is doing double damagewith %s during attack" % (self.name, enemy.name)
            hero_power = self.power
            self.power = self.power * 2
        super(Hero, self).attack(enemy)
        if double_damage:
            self.power = hero_power

    def receive_damage(self, points):
        points -= self.armor
        evade_chance = 1 - (enemy.evade / 40)
        aviod_attack = random.random() > evade_chance
        if aviod_attack:
            print "Attack wa evaded"
        else:
            super(Hero, self).receive_damage(points)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 10

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 11
        self.power = 2
        self.heal = 2
        self.coins = 15

    def attack(self, enemy):
        heal_self = random.random() > 0.8
        if heal_self:
            self.health += self.heal
            print "%s has healed himself %s health" % (self.name, self.heal)
            super(Medic, self).attack(enemy)
        else:
            super(Medic, self).attack(enemy)

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 2
        self.coins = 5

    def receive_damage(self, points):
        damage_chance = random.random() > 0.9
        if damage_chance:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
        else:
            print "%s has avoided the attack" % self.name

        if self.health <= 0:
            print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = "zombie"
        self.health = 0
        self.power = 2
        self.coins = 10

    def alive(self):
        return True

class Dragon(Character):
    def __init__(self):
        self.name = "dragon"
        self.health = 20
        self.power = 2
        self.coins = 20

    def attack(self, enemy):
        breath_fire = random.random() > 0.8
        if breath_fire:
            self.power = enemy.health
            print "%s breaths fire on %s so dead" % (self.name, enemy.name)
            super(Dragon, self).attack(enemy)
        else:
            super(Dragon, self).attack(enemy)

class Knight(Character):
    def __init__(self):
        self.name = "knight"
        self.health = 2
        self.power = 5
        self.coins = 15

    def attack(self, enemy):
        falls_off_horse = random.random() > 0.8
        knight_power = self.power
        if falls_off_horse:
            self.power = 2
            print "%s falls of his horse" % self.name
            super(Knight, self).attack(enemy)
            self.power = knight_power
        else:
            super(Knight, self).attack(enemy)

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 10

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class SuperTonic(object):
    cost = 25
    name = "supertonic"
    def apply(self, character):
        character.health += 10
        print "%s health restored to %s." % (character.name, character.health)

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Armor(object):
    cost = 50
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "Armor has been added to %s" % hero.name

class Evade(object):
    cost = 20
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        print "Evade has been added to %s" % hero.name

class Shopping(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Shopping.items => [Tonic, Sword]
    items = [SuperTonic, Tonic, Sword, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Knight(), Wizard(), Dragon(), Knight(), Zombie(), Goblin(), Medic(), Shadow()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
