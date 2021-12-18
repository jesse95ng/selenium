values = [1, 2, "world", 4, 5]
print(values[0])

# access last element's value
print(values[-1])

print(values[1:3])

# insert element at index
values.insert(1, "hello")
print(values)

# insert element at the end of list
values.append("End")
print(values)

# update element
values[2] = "new"
print(values);

# delete element
del values[0]
print(values);


