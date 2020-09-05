'''
Take input from the user and using the result of mulitplication table using list comprehension
'''

# To take the input from the user
num=int(input('For what number do you want the tables for: '))
ite=int(input('Till what number do you want the tables for: '))

# To create the list with all 6the values
li=list(num*i for i in range(1,ite+1))

# To print the list
for i in li:
    print(i)