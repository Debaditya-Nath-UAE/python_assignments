'''
1) Create deque of friends and do all deque operation
'''
import collections

# Creating and printing the original deque
fri_deque=collections.deque(['Chandra','Lakshmi','Maya',])
print('The original deque: ',fri_deque,'',sep='\n')

# Extending elements at the end of the deque and printing it
fri_deque.extend(['Partha','Hari'])
print('The deque after extending at the end: ',fri_deque,'',sep='\n')

# Extending elements at the begining of the deque and printing it
fri_deque.extendleft(['Karna','Aniruddha'])
print('The deque after extending at the begining: ',fri_deque,'',sep='\n')

# Reversing the list and printing the deque
fri_deque.reverse()
print('The reversed deque: ',fri_deque,'',sep='\n')

# Rotating the list by 5 and printing it
fri_deque.rotate(5)
print('The rotated deque: ',fri_deque,'',sep='\n')