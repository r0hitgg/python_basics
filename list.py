data = [1,2,3,4,5,6,7,8,9]

print(data[::-1])
# [star: end: step]
print(data[1:8:2])

data.append(10)
print(data) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data.extend([11,12,13,14,15])
print(data) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

data.pop(8) # Remove At Index 8
print(data) # [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]

data.insert(8, 9) # Insert 9 At Index 8
print(data) # [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]

del data[0:5]
print(data) # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
