list1 = [4, 5, 7, 8]
list2 = list(range(4, 11))
print(list1, list2)

# Insert element at the end of the list
list1.append(6)
print(list1)

# Insert element in a position
list1.insert(0, 10)
print(list1)

# Removes an element from the list
list1.remove(8)
print(list1)

# Removes the last element from the list
list1.pop()
print(list1)

# Sorts the elements by ascending order
list1.sort()
print(list1)

# Sorts the elements by descending order
list1.reverse() # or list1.reverse()
print(list1)

# Gets the number of elements in the list
print(f"Number of elements: {len(list1)}")

for c, v in enumerate(list1):
    print(f"In position: {c} I found the value: {v}")

# A list accepts different data types
data = list()
data.append("Pedro")
data.append(25)
print(data)

# Lists of lists
data = [[1, 2, 3], [5, 7, 10]]
print(data[1][0])

# Sum of lists
x = [3, 4, 5]
y = [4, 9, 7]
print(x + y)