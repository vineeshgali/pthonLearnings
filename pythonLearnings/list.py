#list is a data structure which can store any type of data and also it's mutable
list = ['nenu',1,2.3,True]
print(list[:])

#how to add elements in list(using append)
list.append("apple")
print(list[:])

#list is mutable
list[0] = 'nuvu'
print(list[:])

#insert method will append the element at particular position
'''
takes two params 1.index where to insert and 2.the value to be inserted
'''
list.insert(1,'vineesh')
print(list[:])

#extend a list
list1=['nenu','malli','vachina']
print(list.extend(list1))
print(list[:])

#range
# print(list(range(10)))

#shallow copy
a = list1
print(a[:])
a[0] = 'nuvu'
print(list1)

#deep copy
b = list1.copy()
b[0]='nenu'
print(b)
print(list1)

#sorting in list
sort = [2,3,4,1,4,5,8,7,6]
print(sorted(sort))

#length of list
print('length',len(sort))

#count() gives you the  
print(list.count("nenu"))

#index gives the first occuring index of the passed element
print(sort.index(4))

#clear method deletes all the elements in the 
list1.clear()
print(list1)

#remove is used to remove particular element
list.remove('nenu')
print(list)