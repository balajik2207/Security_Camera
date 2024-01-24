#To basic python programming
'''
a,b,c,_ = 1,2,4,5
print(a,b,c,_)
'''
#x = y = [7, 8, 9]
#x = [13, 8, 9]
#print(x, y)

'''
x = [1,2, [1,2,3],7,8]

print(x[2])

print(x[2][2])


def my_function():
    a = 2
    return a
print(my_function())
'''

a , b=10, 20
if a > b: print(a)
else: print(b)

def will_be_implemented_later():
    pass

a = reversed('hello')
'''
a = (1,2,3)
b = ('a',1,'python',[1,2])
b[2] = 'something else'
print(b)
print(a,b)
'''
#Output was not printed tuple is not mutable

a = [1,2,3]
b = [1,'a','Python',(1,2),[1,2,3]]
b[2] = 'something else'
print(b) #Not hashable: List is mutable

