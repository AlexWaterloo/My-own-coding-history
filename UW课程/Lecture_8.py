def build_str(los):
    if los==[]:
        return ''
    else:
        return los[0]+build_str(los[1:])
print(build_str(['i','hate','spaces']))

print(str.join(' ',['i','hate','spaces']))
print( 'sdsadfsaf'.upper())

def count_stuff(L):
    if L==[]:
        return 0
    else:
        return(len(L[0]))+count_stuff(L[1:])
print(count_stuff(['a','abc','','d']))
print(3 in [4,3,6,7])
print('mom'in 'mommy')
print('mom'in['mommy'])
print('mom'in['mom'])
print(2in[2])
print(2in[4,[2],3])
print(sum([4,1,6]))
print([1]*5)
print([1,4]*5)


def weird_sum(M):
    if M==[]:
        return 0
    elif M[0]%2==0:
        return (sum(M))+weird_sum(M[1:])
    else:
        return weird_sum(M[1:])
print(weird_sum([5,4,3,2,1]))



print([3,4]+['bb',':'])

a=['world',2,4,5]