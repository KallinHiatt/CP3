class Pokemon:
    def __init__(self, name, hp, type, level):
        self.name = name
        self.hp = hp
        self.type = type
        self.level = level
    
    def combat(self, other):
        self.other = other
        if self.level > other.level:
            return f"{self.name} won!"
        elif other.level > self.level:
            return f"{other.name} has beaten you!"
        else:
            return f"{other.name} and {self.name} are too tired to fight each other any longer."
    
    def __str__(self):
        return f"""
        Name: {self.name},
        Type: {self.type}
        Level: {self.level}
        HP: {self.hp}
        """
#these can't change the instance variable
#CLASS METHODS @classmethod used to keep method from changing object instances
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp * 1.5)

    @classmethod
    def pikachu(self):
        return Pokemon(input("Give me a name: "), 50, "Electric", 1)
#Static methods do not require self. or class., so they are methods that we write inside of the class that operate like a normal method.
    @staticmethod
    def hp_update(poke_hp):
        return pika.hp - 5






eevee = Pokemon("JayRod", 37, "normal", 2)
print(eevee)
steve = Pokemon("Steven", 65, "normal", 2)
print(steve)
charzard = Pokemon("Bob", 1, "fire", 36)
print(charzard)
print()
print(eevee.combat(charzard))
print()
pika = Pokemon.pikachu()
pika.hp = Pokemon.hp_update(pika)
print(pika)
