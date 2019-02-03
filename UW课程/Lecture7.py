x=input('what do you want to say?:')
y=input('tell me your age:')

def repeat_str():
    st = input('enter something:')
    n = input("enter int")
    print(int(n) * st)
repeat_str()

def add_your_nums():
    x=input('pick a number:')
    y=input('pick a second number:')
    return int(x)+int(y)
a=add_your_nums()
print(a)
def f(x,y):
    z=input("how old are you:")
    return int(z*(x+y))
print(f(-3,5))

print('{0}{1},{1}{2}'.format((1,2),2,1))
age=6
print('i act like a ',age,' year old')
print('i act like a {0}{1} year old boy'.format(age,3))
print('roses are red,',end='')
print('violets are blue',end='ssss\n')
print('if i have',10000000,'dollars',sep='\n')
def super_print(s,n):
    if n>0:
        print(s,n,'before')
        super_print(s,n-1)
        print(s,n,'after')
super_print('x',3)


