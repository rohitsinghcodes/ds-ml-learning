
# todo If statement in Python

i = 10

 # Checking if i is greater than 15
if (i > 15):
    print("10 is less than 15")
    
print("I am Not in if")



# todo If-Else statement in Python
i = 20

 # Checking if i is greater than 0
if (i > 0):
    print("i is positive")
else:
    print("i is 0 or Negative")
    

# todo If-Elif One line statement in Python
a = -2

# Ternary conditional to check if number is positive or negative
res = "Positive" if a >= 0 else "Negative"
print(res)


# todo Logical operator with if-else statement in Python
age = 25
exp = 10

# Using '>' operator & 'and' with if-else
if age > 23 and exp > 8:
    print("Eligible.")
else:
    print("Not eligible.")
    
    
# todo Nested If-Else statement in Python
i = 10
if (i == 10):
  
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
        
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
        
else:
  print("i is not equal to 10")