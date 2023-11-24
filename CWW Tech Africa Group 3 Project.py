#!/usr/bin/env python
# coding: utf-8

# #                                                     Tuples
# 

# In[1]:


##Create a tuple of the number one to ten and print it 
Tuple =tuple(range(1,11))
print(Tuple)


# In[2]:


##Check if number 3 is in tuple
if 3 in Tuple:
    print("number 3 is in tuple")
else:
    print("number 3 is not in tuple")
          


# In[ ]:


##Add a number to the tuple
## Tuples are immutable so their elements cannot be changed or modified once they are created


# # Dictionaries
# 

# In[3]:


##create a dictionary with name,age,country and assign appropriate values
Dict = {"Name":"Folaranmi Olaniyi","age":20, "Country":"Nigeria"}

##Print the value assigned to key age
print(Dict["age"])

##Update the value of the key country and make it another country and print it
Dict["Country"]= "Ghana"
print(Dict)

##Add a new key value
Dict["favorite_musician"] = "Michael Jackson"
print(Dict)

##Remove a key value
del Dict["age"]
print(Dict)


# # Mathematical Operation

# In[5]:


## Create two variable a and b and assign them any numerical value
a = 1
b = 2

## Add them together and print the result
c = a + b
print(c)

## Multiply them together and print the ressult
d = a * b
print(d)

##add, subtract and divide any two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_of_2 = num1 + num2
print(sum_of_2)

difference_of_2 = num1 - num2
print(difference_of_2)

division_of_2 = num1 / num2
print(division_of_2)

##Find the remainder of the division
remainder = num1 % num2
print(remainder)

##Raise a number to a power
raise_number_power = num1 ** 2
print(raise_number_power)

##Find square root of a number
Square_root=num1 ** 0.5
print(Square_root)


# # Casting

# In[4]:


##Create a string called 5
num_str= "5"

##Convert string to integer and print
num_int = int(num_str)
print(num_int)

##Convert string to float and print
num_float = float(num_str)
print(num_float)

