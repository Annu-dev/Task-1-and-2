#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.
#E.g. :
#a = 1,
#b = 2.01,
#c = 'string'

a,b,c=1,1.04,'string'
print(a,b,c)


# In[3]:


#Create a variable of type complex and swap it with another variable of type integer.

a,b=5+7j,6
a,b=b,a
print(a,b)


# In[5]:


#Swap two numbers using a third variable
  
x = input('Enter First Number: ')
y = input('Enter Second Number: ')
  
print("\nValue of x before swapping: ", x)
print("Value of y before swapping: ", y)

# Swapping of two variables using third variable
temp = x 
x = y 
y = temp 
 
print("\nValue of x after swapping: ", x)
print("Value of y after swapping: ", y)


# In[8]:


#Swap two numbers without using any third variable.
  
x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))

print("\nValue of x before swapping: ", x)
print("Value of y before swapping: ", y)

# Swapping of two variables using arithmetic operations 
x = x + y    
y = x - y   
x = x - y  
  
print("\nValue of x after swapping: ", x)
print("Value of y after swapping: ", y)


# In[9]:


# Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

# takes input from the user and prints it using Python 3.x Version

val = input("Enter your value: ") 
print(val)


# In[ ]:


# Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

# takes input from the user and prints it using Python 3.x Version
# raw_input():This function works in older version (like Python 2.x). This function takes exactly what is typed from the 
# keyboard, convert it to string and then return it to the variable in which we want to store.

g = raw_input("Enter your name : ") 
print g 


# In[11]:


# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 
# 30 to z and store the output in variable result and print result as the final output.

x=int(input("Enter a number between 1 to 10 : "))
y=int(input("Enter a number between 1 to 10 : "))
z=x+y
result=z+30
print(result)


# In[15]:


# to check the data type of the entered values.

x=10.4
print("The data type of the input value is : ", type(x))
y=[34, 57, 37]
print("The data type of the input value is : ", type(y))


# In[19]:


# Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

FirstVariableName = 1 #Upper CamelCase : Each word starts with a capital letter
secondVariableName = 2 #Lower CamelCase : Each word, except the first, starts with a capital letter
third_variable_name = 3 #SnakeCase : Each word is separated by an underscore character
FOURTHVARIABLENAME = 4 #UPPERCASE
print(FirstVariableName, secondVariableName, third_variable_name, FOURTHVARIABLENAME)


# In[22]:


# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it 
# change the value? If Yes then Why?

#A variable is a memory space that is used in programs to store values ad change them at run time. Yes. We can change its 
#value at run time.

a=4
print(a)
a=5.56
print(a)


# In[5]:


# Write a program in Python to perform the following operation:If a number is divisible by 3 it should print “Consultadd” as
# a string, If a number is divisible by 5 it should print “Python Training” as a string, If a number is divisible by both 3 
# and 5 it should print “Consultadd - Python Training” as a string.

x=int(input("Enter a number : "))
if x%3==0 and x%5==0:
    print("Consultadd - Python Training")
elif x%5==0:
    print("Python Training")
elif x%3==0:
    print("Consultadd")
else:
    print(x)


# In[29]:


#Write a program in Python to perform the following operator based task:Ask user to choose the following option first:
#If User Enter 1 - Addition,If User Enter 2 - Subtraction,If User Enter 3 - Division,If User Enter 4 - Multiplication,If User
#Enter 5 - Average,Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.Ask the user to enter two more numbers as first and second for calculating
#the average as soon as the user chooses an option 5. At the end if the answer of any operation is Negative print a statement
#saying “NEGATIVE”

option=int(input("Enter a number from 1 to 5 : "))
num1=int(input("Enter a number1 : "))
num2=int(input("Enter a number2 : "))
if option==1:
    result=num1+num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif option==2:
    result=num1-num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif option==3:
    result=num1*num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif option==4:
    result=num1/num2
    print(result)
    if result<0:
        print("NEGATIVE")
elif option==5:
    first=int(input("Enter a number3 : "))
    second=int(input("Enter a number4 : "))
    average=(num1+num2+first+second)/4
    print(average)
    if average<0:
        print("NEGATIVE")


# In[9]:


#program in Python to break and continue:If user enters a negative number just break the loop and print “It’s Over”,If user 
#enters a positive number just continue in the loop and print “Good Going”

for x in range(10):
    x=eval(input("Enter a number : "))
    if x<0:
        print("It's Over")
        break
    else:
        print("Good Going")
        continue


# In[9]:


#Program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

print("All numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 are : ")
for x in range(2000,3201):
    if x%7==0 and x%5!=0:
        print(x, end=' ')
    


# In[10]:


# Output of the following code examples?

x=123
for i in x:
    print(x)
    
#Output: ---------------------------------------------------------------------------

#TypeError                                 Traceback (most recent call last)
#<ipython-input-10-349be829c3bb> in <module>
#      1 x=123
#----> 2 for i in x:
#      3     print(x)

#TypeError: 'int' object is not iterable


# In[12]:


# Output of the following code examples?

i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print("error")

# Output:
#0
#error
#1
#error
#2


# In[15]:


# Output of the following code examples?

count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break

# Output:
#0
#1
#2
#3
#4


# In[28]:


#Prints all the numbers from 0 to 6 except 3 and 6.
#Expected output: 0 1 2 4 5 ,Note: Use ‘continue’ statement

for x in range(7):
    
    if x==3 or x==6:
        continue   
    print(x, end=' ')


# In[10]:


# Program that accepts a string as an input from the user and calculate the number of digits and letters. 
#Sample input: consul72
#Expected output: Letters 6 Digits 2

x=input("Enter a string : ")
digits=letters=0
for c in x:
    if c.isdigit():
        digits+=1
    elif c.isalpha():
        letters+=1
    else:
        pass
print("Letters", letters,"\nDigits",digits)


# In[2]:


for counter in range(5):
        number = input("Guess the " + str(counter + 1) + ". number ")
        if number != 5:
          print("Try again.")
        else:
          print("Good guess!")
          break


# In[7]:


counter = 1
hits = 0
while counter <= 5:
    number = input("Guess the " + str(counter) + ". number ")
    if number != 5:
      print("Try again.")
    else:
      print("Good guess!")
      hits = hits + 1
    counter = counter +1

if hits > 0:
    print("You guessed the number", hits, "times")
else:
    print("The number was not guessed at all")


# In[9]:


counter = 1
while counter <= 5:
  number = input("Guess the " + str(counter) + ". number ")
  if number != 5:
    print("Try again.")
  else:
    print("Good guess!")
    break
  counter = counter +1
else:
  print("Sorry but that was not very successful")


# In[11]:


counter = 1
while counter <= 5:
  number = input("Guess the " + str(counter) + ". number ")
  if number != 5:
    print("Try again.")
  else:
    print("Good guess!")
  counter = counter +1
else:
  print("Game over")


# In[14]:


number = -1
again = "yes"
while number != 5 and again != "no":
  number = input("Guess the lucky number: ")
  if number != 5:
    print("That is not the lucky number")
    again = input("Would you like to guess again? ")


# In[ ]:


number = input("Guess the lucky number ")
while number != 5:
  print("That is not the lucky number")
  number = input("Guess the lucky number ")


# In[ ]:




