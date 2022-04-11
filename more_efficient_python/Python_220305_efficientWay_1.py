import time
import numpy as np
from collections import OrderedDict
import statistics


# 타이머 생성
def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        check_func = func(*args, **kwargs)
        total_time = time.time() - start
        print(f'이 함수 {func.__name__} 를 실행하는데 {total_time}초가 걸렸습니다.')
        return total_time
    return wrapper


# 포문 비교
@check_time
def for_inside_constant(constant: int):
    empty = []
    for i in range(10000000):
        a = 3
        empty.append(a*3)
    print(empty[:5])


@check_time
def for_outside_constant(constant: int):
    empty = []
    a = 3
    for i in range(10000000):
        empty.append(a*3)
    print(empty[:5])


for_inside_constant(3)
for_outside_constant(3)


# 딕트 비교
# dict 생성
sample_data = np.random.randint(100000, size=(2, 1000000))


@check_time
def sort_dict1(dict_array: dict):

    dict_origin = {}
    for i, j in zip(dict_array[0], dict_array[1]):
        dict_origin[i] = j

    sort_keys = sorted(dict_origin, key=dict_origin.get)

    dict_with_sort = {}

    for key in sort_keys:
        dict_with_sort[key] = dict_origin[key]

    return dict_with_sort


@check_time
def sort_dict2(dict_array: dict):
    ordered_dict = OrderedDict()
    for i, j in zip(dict_array[0], dict_array[1]):
        ordered_dict[i] = j

    return ordered_dict


sort_dict1(sample_data)
sort_dict2(sample_data)


# 포문 생성 비교
@check_time
def for_list_comprehension(num: int):
    return [i for i in range(num)]


@check_time
def for_just_loop(num: int):
    temp_list = []
    for i in range(num):
        temp_list.append(i)
    return temp_list


for_list_comprehension(1000000)
for_just_loop(1000000)


# 빌트인 함수 비교
@check_time
def max_built(num_list):
    print(max(num_list))
    return max(num_list)


@check_time
def max_made(num_list):
    print(sorted(num_list)[-1])
    return sorted(num_list)[-1]


max_built(range(10000000, 0, -1))
max_made(range(10000000, 0, -1))


# numpy 비교
@check_time
def list_calculation(num_list):
    empty_list = []
    for i in num_list:
        empty_list.append(i*3)
    return empty_list


@check_time
def numpy_calculation(num_list):
    return np.array(num_list) * 3


list_calculation(range(100000000))
numpy_calculation(range(100000000))

print(3)
