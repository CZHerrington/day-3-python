"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    def alive(self):
        return (self.health > 0)

    def attack(self, target):
        target.health -= self.power

class Hero(Character):
    def health_check(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Goblin(Character):
    def health_check(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))

class Zombie(Character):
    def alive(self):
        return True

    def health_check(self):
        print("The %s has unlimited health and %d power." % (self.name, self.power))

def main():
    hero = Hero(10, 5, "hero")
    goblin = Zombie(6, 2, 'zombie')

    while hero.alive() and goblin.alive():
        print()
        hero.health_check()
        goblin.health_check()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end='')
        user_input = input()
        if user_input == "1":
            # Hero powers goblin
            hero.attack(goblin)
            print("You do %d damage to the %s." % (hero.power, goblin.name))
            if not goblin.alive():
                print("The %s is dead." % goblin.name)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            print("The %s does %d damage to you." % (goblin.name, goblin.power))
            if not hero.alive():
                print("You are dead.")

main()
