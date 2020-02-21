#!/usr/bin/env python
# coding: utf-8

# In[6]:


# function to calculate the value of

def totient_function(prime_factors):
    multiplication = 1
    for factor in set(prime_factors):
        multiplication *= (1.0 - 1.0/factor)
    return 1.0/multiplication

# function to generate prime factors of numbers

def prime_factors_generator(n):
    prime_factors = [[i] for i in range(n+1)]
    composite = [False]*(n+1)

    for i in range(3, int(n**0.5)+1, 2):
        if not composite[i]:
            for j in range(i, n//i+1, 2):
                mul = i*j
                prime_factors[mul] = [i] + prime_factors[j]
                composite[mul] = True

    for j in range(2, n//2+1):
        mul = 2*j
        prime_factors[mul] = [2] + prime_factors[j]
        composite[mul] = True
    return prime_factors


# In[12]:


# generate prime factors upto 1000000
p_f = prime_factors_generator(1000000)

# remove 0, 1 from the list and find the
# value of n/phi(n)
p_f_nums = list(map(totient_function, p_f[2:]))


# find the index of the maximum of p_h_nums
# add 2 to compensate the removal of 0, 1
print("Solution Problem 69 is: ")
print(p_f_nums.index(max(p_f_nums))+2)

