import time
print(time.time())
def lots_of_numbers(max):
    for x in range(0, max):
        print(x)
lots_of_numbers(1000)
def high_numbers(max):
    for x in range(0, max):
        print(x)
high_numbers(500)
def high_numbers(max):
    t1 = time.time()
    for x in range(0, max):
            print(x)
    t2 = time.time()
    print('it took %s seconds' % (t2-t1))
high_numbers(500)
def long_time(max):
    for x in range(0, max):
            print(x)
long_time(1000)
def long_time(max):
    r = time.time()
    for x in range(0, max):
            print(x)
    n = time.time()
    print('it took %s seconds' % (n-r))
long_time(1000)

