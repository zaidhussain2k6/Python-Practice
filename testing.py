import numpy as np

# ==========================================
# 1. LISTS
# ==========================================

# Family members with their heights
fam = [
    ["Zaid", 5.11],
    ["John", 6.0],
    ["Jane", 5.5]
]

# List of heights
fam1 = [2.34, 5.61, 7.13, 8.45, 9.22, 9.22]


# ==========================================
# 2. VARIABLES
# ==========================================

height = 5.11
weight = 65
age = 21

person = [
    "Height", height,
    "Weight", weight,
    "Age", age
]


# ==========================================
# 3. LIST MANIPULATION
# ==========================================

# Modify list elements using slicing
person[0:3] = ["Max-Height", 6.1, "Min-Weight"]

# Delete elements using slicing
del person[1:3]


# ==========================================
# 4. FUNCTIONS
# ==========================================

def my_function():
    """Calculate the sum of two user-provided numbers."""

    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))

    total = a + b

    print("Sum of two values is:", total)


# Call the function
my_function()


# ==========================================
# 5. BUILT-IN FUNCTIONS
# ==========================================

# Find the smallest and largest values
print("Minimum:", min(fam1))

highest_height = max(fam1)

print("Maximum:", highest_height)

# Count occurrences of a value
print("9.22 appears:", fam1.count(9.22), "times")

# Round a number
print(round(1.987, 3))

# Get documentation of a function
# help(round)


# ==========================================
# 6. SORTING AND SEARCHING LISTS
# ==========================================

names = ["zaid", "john", "jane", "max", "zander"]

# Sort names alphabetically
names = sorted(names)

print("Sorted names:", names)

# Find the index of a name
name_index = names.index("zaid")

print("Zaid's index:", name_index)


# ==========================================
# 7. STRING MANIPULATION
# ==========================================

name = "zander"

# Replace characters
name = name.replace("er", "ar")

# Capitalize first character
name = name.capitalize()

print("Modified name:", name)

# string to experiment with: place
place = "poolhouse"


# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))


# ==========================================
# 8. NUMPY ARRAYS
# ==========================================

height = [5.11, 6.0, 5.5 , 5.9, 6.2]
weight = [65, 70, 55, 80, 90]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print(bmi) 
print(bmi[1]) 
print(bmi > 1)

print(type(np_height))

np_2d = np.array(
    [
        [5.11, 6.0, 5.5] ,
        [65, 70, 55]
    ]
)

print(np_2d.shape)
print(np_2d)