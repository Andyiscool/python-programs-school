int(123.456)
int('123')
len('this is a test string')
creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragom', 'troll']
print(len(creature_list))
favorite_games = ['Sim City', 'Pokemon Go', 'Extreme Car Simulator', 'Fly Bush Pilot']
print(len(favorite_games))
enemies_map = {'Batman' : 'Joker', 'Superman' : 'Lex Luthor', 'Spiderman' : 'Green Goblin'}
print(len(enemies_map))
school_map = {'Upstairs' : 'classrooms', 'Production Lab' : 'Tech lab Textile Space Wood shop', 'Downstairs' : 'Commons'}
print(len(school_map))
fruit = ['apple', 'banana',' clementine', 'dragon fruit']
lenth = len(fruit)
for x in range(0, lenth):
    print('the fruit at index %s is %s' % (x, fruit[x]))
school_subject = ['math', 'reading', 'science', 'history', 'language arts', 'physics', 'social studies', 'life science', 'earth and space science', 'chemestry', 'biology', 'algebra', 'geometry'
, 'tech smart', 'PE', 'health', 'orchestra', 'band', 'choir', 'foreign language', 'cooking']
lenth = len(school_subject)
for x in range(0, lenth):
    print('school subjects at index %s is %s' % (x, school_subject[x]))
numbers = [5, 4, 10, 30, 22]
print(max(numbers))
numbers = [9, 100, 2000040, 99395959, 49996978685839, 120768775653434434]
print(max(numbers))
strings = 's,t,r,i,n,g,S,T,I,N,G'
print(max(strings))
letters = 's,d,g,t,u,e,y,x,z,S,D,G,T,U,E,Y,X,Z'
print(max(letters))
print(max(10, 300, 450, 50, 90))
print(max(10, 15, 100, 10000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
numbers = [5, 4, 10, 30, 22]
print(min(numbers))
numbers = [3,4,5,6,7,8,9,100,1000,9000000]
print(min(numbers))
letters = 'A,N,D,Y,a,n,d,y'
print(min(letters))
guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
        print('Boom! You all lose')
else:
        print('You win')
guess_the_number = 77
guesses = [15, 22, 30, 42, 55, 80, 45]
if max(guesses) > guess_the_number:
        print('You lose')
else:
        print('You win!')
for x in range(0, 5):
    print(x)
for i in range(0, 20):
    print(i)
print(list(range(0, 5)))
print(list(range(0, 199)))
count_by_twos = list(range(0, 30, 2))
print(count_by_twos)
count_by_threes = list(range(0, 80, 3))
print(count_by_threes)
count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)
count_down_by_threes = list(range(80, 0, -3))
print(count_down_by_threes)
my_list_of_numbers = list(range(0, 500, 50))
print(my_list_of_numbers)
print(sum(my_list_of_numbers))
my_list = list(range(0, 5000, 50))
print(my_list)
print(sum(my_list))
test_file = open('D:\\Python Programs\\Hello World.py')
text = test_file.read()
print(text)
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)
dir(['a', 'long', 'list'])
s = "this if is you not are a reading very this good then way you to have hide done a lit message wrong"
dir(s)
s = "this if is you not are a reading very this good then way you to have hide done a lit message wrong"
words = s.split()
for x in range(0, len(words), 2):
    print(words[x])
    
f = open('Hello World.py')
n = f.read()
f.close
f = open('output.txt', 'w')
f.write(n)
f.close()
import shutil
shutil.copy('Hello World.py', 'output.txt')
n = open('draw.py')
r = n.read()
n.close
n = open('output.txt', 'w')
n.write(r)
n.close()

import shutil
shutil.copy('draw.py', 'output.txt')

