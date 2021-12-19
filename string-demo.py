str = "Hello.com.vn"
str1 = "world"
print(str[1])
print(str[0:5]) # substring in python
print(str + str1) # concatenation
print(str in str1) # check str in str1

splitted = str.split(".")
print(splitted)

str2 = " test string " # trim
print(str2.strip())
print(str2.lstrip())
print(str2.rstrip())
