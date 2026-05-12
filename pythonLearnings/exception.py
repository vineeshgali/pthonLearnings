'''arr = ['mango', 'banana', 'grapes']
try:
    for i in range(4):
        print(arr[i])
except:
    print("An error occurred")
print("The program continues...")'''

#raise an exception
'''n = 1
try:
    if(n<2):
        raise Exception("number is negative")   
except:
    raise Exception('positive number')'''

'''def cube(x):
    assert (x>0),"pass a positive number"
    return x**3
print(cube(4))
try:
    vsl = cube(-8)
    print(vsl)
except:
    print("this is an exception provide positive number")'''

list = [1,1,1,2,2,3,3,3,3]
tup = set(list)
print(list)
print(tup)

