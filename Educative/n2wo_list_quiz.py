def foo(value, lst):
    value = 1
    lst[0] = 44
 
v = 3
lst = [1, 2, 3]
foo(v, lst)
print(v, lst[0])

#IMP: NEED TO WORK ON SCOPE / pass by reference
def f(i, values = []):
    values.append(i)
    print (values)
    #return values
f(1)
f(2)
f(3)