#!/usr/bin/env python
# coding: utf-8

# 1 write a program to accept percentage from the user and display the grade according the following criteria
# 

# ![Web%20capture_9-2-2023_235352_.jpeg](attachment:Web%20capture_9-2-2023_235352_.jpeg)

# In[1]:


marks = int(input("Enter your marks:"))
if (marks > 90):
    print("You got grade A")
elif (marks > 80 and marks <=90):
    print("You got grade B")
elif (marks >= 60 and marks<=80):
    print("You got grade C")
else:
    print("You got grade D")


# ![3.jpg](attachment:3.jpg)

# In[11]:


Cost_Price = int(input("Enter the cost of the bike:"))
if (Cost_Price > 100000):
    tax = Cost_Price*0.15
elif (Cost_Price > 50000 and cost_price <=100000):
    tax = Cost_Price*0.10
else:
    tax = Cost_Price*0.05
print("The applicable road tax is Rs.",tax)


# In[ ]:





# 

# ![2.jpg](attachment:2.jpg)

# In[2]:


city = int(input("Select any of the given city to view the monument name\nPress 1 for Delhi\nPress 2 for Agra\nPress 3 for Jaipur"))
if city == 1:
    print("Red Fort is in Delhi")
elif city == 2:
    print("Taj Mahal is in Agra")
elif city == 3:
    print("Jai Mahal is in Jaipur")
else:
    print("You have slelected wrong option")


# # (4) Check how many times a given number can be divided by 3 before it is less than or equal to 10.

# In[3]:


num = int(input("Enter a number:"))
onum = num
count = int(0)
while (num > 10):
    num = num/3
    count += 1
print("The number", onum, "can be divided", count,"times by 3 before it's less than or equal to 10")


# # (5)   Why and When to Use while Loop in Python give a detailed description with example.
# While loop is used when we have to stop/start executing some codes only when some condition(s) is/are fultilled.
# e.g 'Count from 1 to 10' - Here the conditionn is to start from int 1 and keep executing untill the counter doesn't reach 10 or in other words keep executing from 1 to till the counter is less than 11.

# # (6)  Use nested while loop to print 3 different pattern.# 
# 
# 

# In[4]:


rows = int(input("Please Enter the Total Number of Rows  : "))

print("Right Angled Triangle Star Pattern")
i = 1
while(i <= rows):
    j = 1
    while(j <= i):
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()


# In[5]:


userInput = int(input("Please enter the amount of rows: "))

row = 0
while(row < userInput):
    row += 1
    spaces = userInput - row

    spaces_counter = 0
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()


# In[6]:


n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = n
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1


# # (7) Reverse a while loop to display numbers from 10 to 1.

# In[7]:


i = int(10)
while(i>0):
    print(i)
    i =i-1


# In[ ]:





# In[ ]:





# In[ ]:




