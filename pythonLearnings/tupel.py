#====================================================================
'''
tuple is same as list but you can not change any thing in the tuple . Heance the are immutable
->diff from list syntax is that you use () insted of []
'''
tup = (0,1,2,3,4,5,6)
print()

#access elements based on index
print("element at index : ",tup[0])

#slicing works in tuple as well nothing diff from string or list refer strings.py for more slicing examples
print("revese the tuple : ",tup[::-1])

#you can get min and max form tuple
print("min : ",min(tup),"max : ",max(tup))

#concatination works here as well
tup1 = (3,4,5,6,8)
print(tup+tup1)