#example 1 generate random float number
import random
print(random.random())

#example 2 generate random integers

import random

print(random.randint(1, 100))   
print(random.randint(1, 100))

#example 3 generate random float number within a range
import random

print(random.randrange(1, 100))
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))


#Example 4 select random elements
import random   
print(random.choice('computer'))
print (random.choice([1, 2, 3, 5, 9]))
print(random.choice((12,23,45,67,65,43)))


#example 5 selecrt random items from data set

import random
aList = [20,40,80,100,120]
sampled_list = random.simple(aList, 3)
print(sampled_list)


#example 5.2 generate the sampked list of random integers

import random
#create a list of 5 random numbers
num_list = random.sample(range(100), 5)
print(num_list)
