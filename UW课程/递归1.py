# 递归

def add_nums(s):
    if s=='':
        return 0
    elif s[0].isnumeric():
        return int(s[0])+add_nums(s[1:])
    else:
        return add_nums(s[1:])
print(add_nums('2srewq334fa'))

def print_three_times(s):
    print(s)
    print(s)
    print(s)
print_three_times('fuck')

def print_again(s,n):
    if n>=0:
        print(s)
        print_again(s,n-1)
print_again('a',2)

def make_it_odd(n):
#  returns the amount of divisions by 2 necessary to make n an odd number and prints
# each value along the
# effects: prints a line at each stage stating whether the current number is odd or not
    if n%2==1:
        print(str(n)+" is odd")
        return 0
    else:
        print("not odd,"+str(n))
        return 1+ make_it_odd(int(n/2))
make_it_odd(32)





