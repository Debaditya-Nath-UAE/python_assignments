'''
1) Print n natural numbers unless users says to stop
    a) iterator
    b) generator
'''

# To take the number input from the user
x=int(input('Enter the number till what you want the numbers through generater and iterater : '))

# Iterator
class Iterator:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

# Generator
def generator():
    n=1
    for i in range(x):
        yield n
        n+=1

# To print the numbers using iterator
print('Through iterator:')
a = iter(Iterator())
for i in range(x):
    print(next(a))
print()

# To print the numbers using generator
a = generator()
print('Through generator:')
for i in range(x):
    print(next(a))