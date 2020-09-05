'''
1) In friends list try to check the any friends name has length 10
2) In friends list try to check the any friends name has even length
'''

# To create the list
fri_list=['Durga','Gargi','Krishna','Tara','Kumari','Rama','Mitra','Priya','asdefcgrth','fdrvghtfdr']

# To filter the list
new_fri_list=list(filter(lambda x: len(x)==10, fri_list))

# To print the list
print(new_fri_list)