"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object): # Make a class named character that inherits object
    def __init__(self): # Class Character has a dunder-init that takes self parameters
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self): # Class character has a method named alive that takes self parameter
        return self.health > 0

    def attack(self, enemy): # Class character has a method named attack that takes self and enemy parameter
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points): # Class character has a method named receive_damage that takes self and points parameter
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self): # Class character has a method named print_status that takes self parameter
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character): # Make a class named Hero that inherits character
    def __init__(self): # Class character has a dunder-init that takes self parameter
        self.name = 'hero' # From self get name attribute and set it to 'Hero'
        self.health = 10 # From self get health atribute and set it to 10
        self.power = 5 # From self get power attribute and set it to 5
        self.coins = 20 # From self get coins attribute and set it to 20

    def restore(self): # Class Hero has a method named restore that takes self parameter
        self.health = 10 # From self get the health attribute and set it to 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1) # From time get sleep method and call it with parameter self and 1

    def buy(self, item): # Class Hero has a method named buy that takes self and item parameters
        self.coins -= item.cost
        item.apply(hero) #From item get the apply method, and call it with self and hero parameters

class Goblin(Character): # Make a class named Goblin that inherits Character
    def __init__(self): # Class Goblin has a dunder-init that takes self and
        self.name = 'goblin' # From self get the name attribute and set it to 'goblin'
        self.health = 6 # From self get the health attribute and set it to 6
        self.power = 2 # From self get the power attribute and set it to 2

class Wizard(Character): # Make a class named Wizard that inherits Character
    def __init__(self): # Class Wizard has a dunder-init that takes self as a parameter
        self.name = 'wizard' # From self get the name attribute and set it to 'wizard'
        self.health = 8 # From self get the health attribute and set it to 8
        self.power = 1 # From self get the power attribute and set it to 1

    def attack(self, enemy): # Class Wizard has a method named attack that takes self and enemy parameters
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object): # Make a class name Battle that inherits object
    def do_battle(self, hero, enemy): #Class Battle has a method named do_Battle that takes self, hero, and enemy as parameters
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive(): # From hero get th alive method and call it with self parameters. From enemy get the alive method and call it with self parameter
            hero.print_status() # From hero get the print_status method and call it with self parameter
            enemy.print_status() # From enemy get the print_status method and call it with the self parameter
            time.sleep(1.5) # From time get the sleep method and call it with parameters self and 1.5
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy) # From hero get the  attack method and call it with self and enemy parameters
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero) # From enemy get the attack method and call it with the self and hero parameters
        if hero.alive(): # From hero get the alive methos and call it with the self parameter
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object): # Make a class named Tonic that inherits object
    cost = 5
    name = 'tonic'
    def apply(self, character): #Class Tonic has a method named apply that tkes self and charater parameters
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object): # Make a class named sword that inherits object
    cost = 10
    name = 'sword'
    def apply(self, character): # Class Sowrd has a method named apply that takes self and character parameters
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)

class Shopping(object): # Make a classnamed Shopping that inherits object
    items = [Tonic, Sword]
    def do_shopping(self, hero): # Class Shopping has am method that takes self and hero parameters
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

hero = Hero() # Set hero to an instance of class Hero
enemies = [Goblin(), Wizard()] # Set enemies to an instance of Class Goblin and Class Wizard
battle_engine = Battle() # Set battle_engine to an instance of Class Battle
shopping_engine = Shopping() # Set shopping_engine to an instance of Class Shopping

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy) 
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero) # From shopping_engine get the method do_shopping and call it with self and hero

print "YOU WIN!"
