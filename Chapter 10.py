class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
harry = Animal('hippogriff', 6, 'pink')
import copy
harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)
print(harry.species)
print(harry.species)

class Schools:
    pass

class Schools:
    def __init__(self, school, number_of_subjects, population):
        self.school = school
        self.number_of_subjects = number_of_subjects
        self.population = population
Gibson_Ek = Schools('Gibson Ek', 6, '108')
import copy
Gibson_Ek = Schools('Gibson Ek', 6, '108')
Skyline = copy.copy(Gibson_Ek)
print(Gibson_Ek.school)
print(Gibson_Ek.school)
Gibson_Ek = Schools('Gibson Ek', 6, '108')
Skyline = Schools('skyline', 6, '2240')
Issaquah = Schools('Issaquah', 6, '2240')
Schools = [Gibson_Ek, Issaquah, Skyline]
more_schools = copy.copy(Schools)
print(more_schools[0].school)
print(more_schools[1].school)
print(more_schools[2].school)

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)

sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))
more_anials = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'
print(my_animals[0].species)
print(more_animals[0].species)
class Schools:
    pass

class Schools:
    def __init__(self, school, number_of_subjects, population):
        self.school = school
        self.number_of_subjects = number_of_subjects
        self.population = population
Gibson_Ek = Schools('Gibson Ek', 6, '108')
import copy
Gibson_Ek = Schools('Gibson Ek', 6, '108')
Skyline = copy.copy(Gibson_Ek)
print(Gibson_Ek.school)
print(Skyline.school)
Gibson_Ek = Schools('Gibson Ek', 6, '108')
Skyline = Schools('skyline', 6, '2240')
Issaquah = Schools('Issaquah', 6, '2240')
Best_Schools = [Gibson_Ek, Issaquah, Skyline]
more_schools = copy.copy(Best_Schools)
print(more_schools[0].school)
print(more_schools[1].school)
print(more_schools[2].school)
Best_Schools[0].school = 'Liberty'
print(Best_Schools[0].school)
print(more_schools[0].school)
Pine_Lake = Schools('school', 6, '900')
Best_Schools.append(Pine_Lake)
print(len(Best_Schools))
print(len(more_schools))
Beaver_Lake = Schools('school', 6, '900')
Best_Schools.append(Beaver_Lake)
print(len(Best_Schools))
print(len(more_schools))
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozward'))
print(keyword.kwlist)
import random
print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))
import random
num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i ==num:
           print('you guessed right')
           break
    elif i < num:
            print('Try higher')
    elif i > num:
            print('Try lower')
import random
h = random.randint(1, 290)
while True:
    print('Guess a number between 1 and 290')
    guess = input()
    i = int(guess)
    if i == num:
            print('You guessed right')
            break
    elif i < h:
            print('Try higher')
    elif i > h:
            print('Try lower')
            
            

