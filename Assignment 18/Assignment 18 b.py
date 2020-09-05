'''
1) Create two dictionary of friends , then combine using chain map then do above mentioned operation
'''

# Creating and printing both the dictionaries
import  collections
my_fri_dict={'neighborhood friend':'Aditya','school friend':'Mani'}
fri_fri_dict={'neighborhood friend':'Mina','college friend':'Priya'}
print('My friend dictionanry: ',my_fri_dict,'',sep='\n')
print('My friend\'s friend dictionanry: ',fri_fri_dict,'',sep='\n')

# Creating the chainmap
chainmap = collections.ChainMap(my_fri_dict, fri_fri_dict)
print('The chainmap: ',chainmap.maps,'',sep='\n')

# Printing the keys of the chainmap
print('The keys in the chainmap: ',list(chainmap.keys()),'',sep='\n')

# Printing the values of the chainmap
print('The values in the chainmap: ',list(chainmap.values()),'',sep='\n')