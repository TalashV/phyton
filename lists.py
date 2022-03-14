#list is a kind of collection frinds = ['joseph', ' Glen', 'Sally']

# range() function returns the list of numbers
print (range(4))
#[0,1,2,3]
frinends = ['a',"b",'c']
print(len(friends))
#3
print (range(len(friends)))
#[0,1,2]

#8.2 - Manipulating Lists
#list methods
stuff = list()
staff.append('book')
stuff.append('99')
print(stuff)
#['book',99]

#in method in the Lists
some = [1, 9, 21, 10, 16]
9 in some
#true
15 in some
#False
20 not in some
#true

#sort method (alphabet sort - ABC)
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
#['Glenn','Joseph','Sally']
print (frineds[1])
#joseph

#built-in functions in the List
#len - number of items in the List
#max - maximum number in the list
#min - minimum number in the list
#sum - summary

#average for numbers promted from user

numlist = list()
while True :
    inp = input ('Enter the number: ')
    if inp == 'done' : break
    value = float (inp)
    numlist.appdend(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)


#connecting lists and strings together
#split method
abc = 'With three words'
stuff = abc.split()
print(stuff)
#['With','trhee', 'words']

#abc.split(';') - will split the words that are divided with ;
