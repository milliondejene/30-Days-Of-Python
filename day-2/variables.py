# Exercise 1: Level 1

# Day 2: 30 Days of python programming

# Declare a first name variable and assign a value to it
first_name = "John"

# Declare a last name variable and assign a value to it
last_name = "Doe"

# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name

# Declare a country variable and assign a value to it
country = "United States"

# Declare a city variable and assign a value to it
city = "New York"

# Declare an age variable and assign a value to it
age = 30

# Declare a year variable and assign a value to it
year = 1992

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = True

# Declare multiple variable on one line
multiple_variables_on_one_line = 10, 20, 30, "Python"

# Exercise 2: Level 2

# Check the data type of all your variables using type() built-in function
print("Data types:")
print("First name:", type(first_name))
print("Last name:", type(last_name))
print("Full name:", type(full_name))
print("Country:", type(country))
print("City:", type(city))
print("Age:", type(age))
print("Year:", type(year))
print("is_married:", type(is_married))
print("is_true:", type(is_true))
print("is_light_on:", type(is_light_on))
print("Multiple variables on one line:", type(multiple_variables_on_one_line))

# Using the len() built-in function, find the length of your first name
print("Length of first name:", len(first_name))

# Compare the length of your first name and your last name
first_name_length = len(first_name)
last_name_length = len(last_name)
print("Is the first name longer than the last name?", first_name_length > last_name_length)
