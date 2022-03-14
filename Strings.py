fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)

#len function

fruit = 'banana'
x = len(fruit)
print(x)

#for in structure

fruit = 'banana'
for letter in fruit:
    print (letter)


word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print (count)

#slicing strings

s = 'monty python'
print(s[0:4])
#mont
print(s[6:7])
#p
print(s[:2])
#mo
print([:])
#monty python

fruit = 'banana'
'n' in fruit
#true
'm' in fruit
#false
if 'a' in fruit
    print("found it!")
#found it!

#string comparasion
if word == "banana" :
    print ("all right banana")

if word < "banana" :
    print ('your word,' + word + ', comes before banana.')
elif word > 'banana' :
    print ('your word,' + word + ', comes after banana.')
else:
    print ('all right , bananas.')

# string library .lower() method

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
#hello bob
print(greet)
#Hello Bob
print('Hi There'.lower())
#hi there

#dir - show methods of the clas
stuff = "hello world"
type(stuff)
#<class 'str'>
dir(stuff)
......

#find method
fruit = 'banana'
pos = fruit.find('na')
print (pos)
#2
aa = fruit.find('z')
print(aa)
#-1 - of the substring is not found, find() returns -1


#search and replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print (nstr)
#Hello Jane

#whitespace. strip() function removes both beginning and ending whitespace
greet = '   Hello bob   '
greet.lstrip()
#'Hello Bob '
greet.strip()
#'Hello bob'

#prefixes
line = 'Please bla bla bla'
line.startswith('Please')
#true
line.startswith('p')
#False

#parsing and extracting

data = 'From askdjklsjd sakdjl sj@sakdjlk.sd.s djlkajsd'
atpos = data.find('@')
print (atpos)
#21
sppos = data.find(' ',atpos) #poisk s pozicii #21 a ne s #0
print (sppos)
#31
host = data[atpos+1 : sppos]
print(host)
#sakdjlk.sd.s
