#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number: "))
if(num1>num2):
    print("{} is greatest".format(num1))
elif(num2>num1):
    print("{} is greatest".format(num2))
else:
    print("{} and {} are equal".format(num1,num2))
    


# In[11]:


print ("Enter marks")
marks = int(input())
if marks<25:
  print ("F")
elif marks>=25 and marks<45:
  print ("E")
elif marks>=45 and marks<50:
  print ("D")
elif marks>=50 and marks<60:
  print ("C")
elif marks>=60 and marks<80:
  print ("B")
else:
  print ("A")


# In[12]:


age1 = int(input("Enter age Person 1: "))
age2 = int(input("Enter age Person 2: "))
age3 = int(input("Enter age Person 3: "))
print()
if (age1 > age2) & (age1 > age3):
    print('Person 1 is the oldest')
    if age2 < age3:
        print('Person 2 is the youngest')
    else:
        print('Person 3 is the youngest')
elif (age2 > age1) & (age2 > age3):
    print('Person 2 is the oldest')
    if age1 < age3:
        print('Person 1 is the youngest')
    else:
        print('Person 3 is the youngest')
else:
     print('Person 3 is the oldest')
     if age1 < age2:
         print('Person 1 is the youngest')
     else:
         print('Person 2 is the youngest')


# In[ ]:




