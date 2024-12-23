# When we have a variable let's say num1 = 11, and we create another variable num2 = num1, num2 is a pointer to num1.
# How is that possible?
num1 = 11
num2 = num1

print("Before num2 value is updated")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# When we update num2, what happens to num1?
num2 = 22

print("Before num2 value is updated")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

print("\n\n")
# Let's do an experimentation with dictionaries
dict1 = {
    "value": 11
}

dict2 = dict1

print("Before dict2 value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2["value"] = 22

print("\nAfter dict2 value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
