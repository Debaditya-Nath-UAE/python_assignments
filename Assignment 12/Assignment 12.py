'''
Problem Steps: Create a list of friends do following operation

1) Get friends whose name end with 'e'
2) Convert all your friends name with capital letter
3) Get Sum overall count of your friends
4) Get friends name is even length with even length
5) Concat all the friends name in one variable and print
6) Find particular friends name in list
'''

#Create friends list
fri_list=['Ravi','Parthe','Mani','Arune','Vishnu']

#Get friends whose name end with 'e'
print('1) Get friends whoes name end with \'e\':')
print('All names that end with \'e\' are: ',list(filter(lambda x: (x[len(x)-1]=='e'), fri_list)))
print()

#Convert all your friends name with capital letter
print('2)Convert all your friends name with capital letter:')
print('All the names in capital letters:',list(map(lambda x: x.upper(), fri_list)))
print()

#Get Sum overall count of your friends
sec=[]
for i in fri_list:
    sec.append(len(i))
print('3)Get Sum overall count of your friends:')
print('The length of all the names of my friends: ',list(map(lambda x: len(x), fri_list)))
print('The sum of the length of all my friends names: ',sum(sec))
print()

#Get friends name is even length with even length
sec=list(map(lambda x: len(x), fri_list))
print('4)Get friends name is even length with even length')
print('The friends with the length of 4 are/is:',list(filter(lambda x: len(x)==4, fri_list)))
print('The friends with the length of 5 are/is:',list(filter(lambda x: len(x)==5, fri_list)))
print('The friends with the length of 6 are/is:',list(filter(lambda x: len(x)==6, fri_list)))
print()

#Concat all the friends name in one variable and print
var=' '
for i in fri_list:
    var=var+' '+i
print('5)Concat all the friends name in one variable and print:')
print('The varible where all my friend\'s name is there is:',var)
print()

#Find particular friends name in list
print('6)Find particular friends name in list:')
username=input('Enter a name or letter you wan\'t to find from the list: ')
print('The name in the list is: ',list(filter(lambda x: x==username or username in x, fri_list)))