# Test tốc độ max
import random
import time

def find_max(array):
    max = array[0]
    for i in range(1, len(array)):
        if max < array[i]:
            max = array[i]
    return max
            
def create_array(len):
    ran = random.Random()
    array = []
    for i in range(len):
        array.append(ran.random())
    return array

array = create_array(10000000)

# Find max of 1000 random numbers
t0 = time.process_time()
my_result = find_max(array)
t1 = time.process_time()

print("my_result = {0} (time taken =  {1:.4f} seconds )"
    .format(my_result, t1-t0))

t2 = time.process_time()
their_result = max(array)
t3 = time.process_time()

print("their_result = {0} (time taken = {1:.4f} seconds)"
    .format(their_result, t3-t2))