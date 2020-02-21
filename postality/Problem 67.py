#!/usr/bin/env python
# coding: utf-8

# In[71]:


with open("C:\\Users\\\Lenovo\\p067_triangle.txt") as f:
    number = f.read()


# In[72]:


number = number.strip().split('\n')


# In[68]:


print(number)


# In[73]:


for i in range(1,len(number)):
 number[i] = number[i].strip().split(' ')
 number[i] = [int(x) for x in number[i]]


# In[74]:


number[0] = [59]
counter = 0
for i in range(len(number)-2,-1,-1):
 for j in range(len(number[i])):
  number[i][j] = number[i][j] + max(number[i+1][j], number[i+1][j+1])
  counter += 1
 number.pop()


# In[88]:


print("Solution Problem 67 is:")
print(number[0])

