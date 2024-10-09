#We start classes with a keyword class and we name them using PascalCase.
class Animal:
    #We start with the constructor (defines all the attributes of the object being created)
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
    #Methods are functions inside of the class!
    def fight(self, other):
        if len(self.name)> len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name)< len(other.name):
            self.losses += 1
            return other.name
        else:
            self.losses += 1
            other.losses += 1
            return "Tie"
        
    #Makes a more readable string when printed

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nAge: {self.age}\nGender: {self.gender}\nRarity: {self.rarity}"
    
#We generally store object in variables (individually or in a list) so we can use it!    
cat = Animal("Tom", "cat", 21, "male", "Common")
frog = Animal("Jarrod", "Poison Dart Frog", 500, "Female", "Rare")

#To call a method, you put the name of the object, then you use your dot operator (.name of the method, and any arguments needed)
cat.losses = 0
frog.losses = 0
print(cat.fight(frog))
cat.name = "Thomas"
print(cat.losses)
print(cat.fight(frog))
print(cat.losses)
print(frog.losses)

cat = None
print()