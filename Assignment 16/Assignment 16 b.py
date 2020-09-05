'''
1) Using list comprehension generate number till 1000
2) Above using generators
'''
# To create the generator
num=1
def generate(max=1):
    n=0
    while n<max:
        yield n+1
        n+=1
c=-20
li=list(generate(1000))

# To print the numbers
try:
    for x in range(80):
        c+=20
        for i in range(c,20+c):
            print(li[i],end='  ')
        print()
except:
    print()