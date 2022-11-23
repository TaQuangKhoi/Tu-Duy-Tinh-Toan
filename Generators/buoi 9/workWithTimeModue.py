import time

time.process_time()

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

def do_my_sum2(xs):
    # sum 1
    sum1 = 0
    for v in xs:
        sum1 += v
    # sum 2
    sum2 = 0
    for v in xs:
        sum2 += v
    return sum

sz = 10000000
testdata = range(sz)


t0 = time.process_time()
my_result = do_my_sum(testdata)
t1 = time.process_time()
print("my_result = {0} (time taken =  {1:.4f} seconds )"
    .format(my_result,t1-t0))


t4 = time.process_time()
my_result = do_my_sum2(sz)
t5 = time.process_time()
print("my_result = {0} (time taken =  {1:.4f} seconds )"
    .format(my_result,t5-t4))

t2 = time.process_time()
their_result = sum(testdata)

t3 = time.process_time()
print("their_result = {0} (time taken = {1:.4f} seconds)"
        .format(their_result,t3-t2))