import time
print(time.asctime())
import time
t = (2007, 5, 27, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))
import time
print(time.localtime())
t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)
n = (2016, 10, 25, 9, 55, 55, 1, 0, 0)
print(time.asctime(n))
import time
print(time.localtime())
n = time.localtime()
year = n[0]
month = n[1]
print(year)
print(month)
for x in range(1, 61):
    print(x)
for x in range(1, 61):
    print(x)
    time.sleep(0.00000000000000001)
for x in range(1, 200):
    print(x)
for x in range(1, 14):
    print(x)
    time.sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
game_data = {'player-position' : 'N23 E45', 'pockets' : ['key', 'pocket knife', 'polished stone'],
'backpack' : ['rope', 'hammer', 'apple'], 'money' : 158.50}
import pickle
game_data = {'player-position' : 'N23 E45', 'pockets' : ['key', 'pocket knife', 'polished stone'],
'backpack' : ['rope', 'hammer', 'apple'], 'money' : 158.50}
save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()
load_file = open('save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close
print(loaded_game_data)
import copy
class Car:
    pass

car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)
favorites = {'flight simulator', 'driving games', 'cross country', 'programming Python'}
import pickle
favorites = {'flight simulator', 'driving games', 'cross country', 'programming Python'}
save_file = open('favorites.dat', 'wb')
pickle.dump(favorites, save_file)
save_file.close()
open_file = open('favorites.dat', 'rb')
open_favorites = pickle.load(open_file)
open_file.close()
print(open_favorites)
             
