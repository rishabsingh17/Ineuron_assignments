#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1]Write a Python program to print Hello Python
n = "Hello Python"
print('Hello Python')


# In[17]:


#2] e a Python program to do arithmetical operations addition and division.?
n= int(input("Enter the number 1:  "))
m=  int(input("Enter the number 2:  "))
sum = int(m+n) 
Division = int(n/m)
print(sum)
print(Division)


# In[18]:


#3]3. Write a Python program to find the area of a triangle?
def areatriangle(b,h):
    return 0.5*b*h

b= int(input("enter the base"))
h= int(input('Enter the height'))
a =areatriangle(b,h)
print(a)


# In[ ]:


#4]Write a Python program to swap two variables?
a= int(input("enter the base"))
b= int(input('Enter the height'))
temp = a
a = b
b = temp
print(a)
print(b)


# In[20]:


#5]5. Write a Python program to generate a random number?
import random
random.randint(1,3)


# In[ ]:




