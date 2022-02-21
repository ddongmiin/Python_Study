"""
https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-multi-processing-in-python/
A beginners guide to Multi-Processing in Python
"""
import time
import multiprocessing


# before multiprocessing
def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')


tic = time.time()
sleepy_man()
sleepy_man()
toc = time.time()

print(f'Done in {toc-tic:.4f} seconds')


# after multiprocessing
def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')


tic = time.time()
p1 = multiprocessing.Process(target=sleepy_man)
p2 = multiprocessing.Process(target=sleepy_man)
p1.start()
p2.start()
toc = time.time()

print('Done in {:.4f} seconds'.format(toc-tic))

# 10 different multi-processing instances using a for loop
tic = time.time()

process_list = []
for i in range(10):
    p = multiprocessing.Process(target=sleepy_man)
    p.start()
    process_list.append(p)

for process in process_list:
    process.join()

toc = time.time()
print('Done in {:.4f} seconds'.format(toc-tic))

# using args
tic = time.time()

process_list = []
for i in range(10):
    p = multiprocessing.Process(target=sleepy_man, args=[2])
    p.start()
    process_list.append(p)

for process in process_list:
    process.join()

toc = time.time()
print('Done in {:.4f} seconds'.format(toc-tic))


# Multi-Processing using Pool class
def sleepy_man(sec):
    print('Starting to sleep for {} seconds'.format(sec))
    time.sleep(sec)
    print('Done sleeping for {} seconds'.format(sec))


tic = time.time()

pool = multiprocessing.Pool(5)
pool.map(sleepy_man, range(1, 11))
pool.close()

toc = time.time()

print('Done in {:.4f} seconds'.format(toc-tic))