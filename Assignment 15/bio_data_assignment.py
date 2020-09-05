"""
 Design a class to take bio data:

Consists of following Information

a) Your name
b) Your age
c) Your school name
d) Your Father name and occupation
e) Your Mother name and occupation
f) Your Hobbies
g) Your Friends Name
h) Your ambition

Following Operation need to be done

1) Print the instance it should provide the your details
2) Create a instance method to_json() it should return dictionary of key and    values
3) Create a class method from_json() dictionary and return the object of the bio data

if any of the key is missing then you throw custom exception stating message following keys are mission with key names

Step 1: Welcome the user
Step 2: Ask the user how many people's information will be entered
Step 3: Ask the user the name for person 1
Step 4: Ask the user the age for person 1
Step 5: Ask the user the location for person 1
Step 6: Repeat the same for all the other people
Step 7: Print the dictionary
Step 8: Thank the user
"""
# Design a class to take bio data
Data = []
a = 0
b = 0
inp = 0

# to enter the data
class person_data:

    # This is to take the user input for the bio data
    def input_user(name=0, age=0, loc=0):
        '''
        
        '''
        user = int(input('How many people: '))
        for i in range(user):
            name = input('Enter the name for person: ')
            age = int(input('Enter the age: '))
            loc = input('Enter the location: ')
            print()
            Data.append({
                'name': name,
                'age': age,
                'location': loc,
            })

    # This will print the dictionary created
    def to_json(Data):
        for i in range(len(Data)):
            print('person',i+1,': ',Data[i],sep='')

    # This will run the main code
    def main_app(Data):
        # 1 : To welcome the user
        print('Welcome to the bio data app! Hope you enjoy it!')
        # 2 : To call the input user function
        person_data.input_user()
        # 3 : To call the to json function
        person_data.to_json(Data)
        # 4 : To thank the user
        print('Thank you for trying the app!')

if __name__=='__main__':
    person_data.main_app(Data)