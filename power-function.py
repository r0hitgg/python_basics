from functools import reduce


power = map(lambda x: x**3, [1,2,3,4,5])

print(list(power))

def square(num):
    return num**2

power = map(square, [1,2,3,4,5])
print(list(power))

filtered_data = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])

print(list(filtered_data))

reduced_data = reduce(lambda x, y : x - y, [10, 5, 3])

print(reduced_data)