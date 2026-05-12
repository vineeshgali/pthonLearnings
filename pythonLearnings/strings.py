#string is a collection of carecters so anything you write in "" is a string 
string = "this is example of a string"

#every char is a num which is represented in terms ASCII

char = "a"
print('the ascii of "a" is ',ord(char))

#you can access any char in a string see example bellow
print(string[0])

#can also access in reverse
print(string[-1])

#slicing in strings : this means you can chop the string use it or do what ever the point is you can get what ever part you want from a string
'''
few points to remember :
1.there will be three parts in a slicing bracket [0:9:2]
    1.1 the first part is stright forward which is you specify the starting part from where you want to slice
    1.2 the second part is where you specify till where you want to slice the catch is that the num is not inclusive so its (n-1)
    1.3 the last part is like a step you specify it to skip the in between based on the number(try using the example bellow)
'''
#this will give whole string
print(string[0:])
#this will give till (n-1)
print(string[0:4])
#this will skip the each 2 letter
print(string[0:8:2])
#by using -ve numbers you can access it from back(prints except last four chars)
print(string[:-4])
#prints last 4 chars
print(string[-4:])

#you can find length of string by len()
print(len(string))

#you can modify string using replace method
'''this to remember
1.you will create a new string not modify the old one 
2.so the old string will be same but new string will be created in memory
'''
print(string.replace("string","str"))
print(string)

'''
few more methods in strings
1.lower()
2.upper()
3.swapcase()
4.title()
5.capitalize()
'''

#ypu can use "in" to search or check something is present in string
print("to" in string)

#sotring a string this returns a list 
sort = "bcasd"
print(sorted(sort))

sorrt = ['abcd','acbd','abcd','bcad','bcda']
print(sorted(sorrt))

#strip will remove the leading and trailing spaces
stripExample = '    string.        '
print(stripExample.strip())

#split method is used to seperate the words based on a common delimeter
splitExample = 'this,is,a,split,example'
print(splitExample.split(','))