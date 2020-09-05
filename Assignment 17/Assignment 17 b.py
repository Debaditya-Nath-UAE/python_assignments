# Taking input from user
n=int(input('Enter the number for which you wan\'t the table: '))
i=int(input('Enter the number till the tale will comtinue: '))

# Creating the list
li=list(n*l for l in range(1,i+1))

# Printing the list
for i in li:
    print(i)