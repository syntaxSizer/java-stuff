#Strings & escap sequence 

'this is isn\'t flying, its falling with style'

# String methods
len()
lower()
upper()
str()

#String formatting
# Example 
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#String Formatting with twoo parts

''' raw_input() used to capture user input 
'''
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

#datetime library
# getting the current date and time 

from datetime import datetime

now=datetime.now()
print now


#extracting informations (date and time)

from datetime import datetime
now=datetime.now()
print now
current_year=now.year
current_month=now.month
current_day=now.day
print current_year
print current_month
print current_day

# yy/mm/dd format
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.year, now.month, now.day)

#HH/MM/SS format

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)

# conditinals
# a simle dimonstration of how to use cionditional statements
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
clinic()

# boolean oparators 

and #checks if both sides are true
or # checks if at least one side of the statement is true 
not # gives the opposite of the statement


# pigLatin game 

pyg = 'ay'
#getting user input
original = raw_input('Enter a word:')
#checking if the user entered a valide word 
if len(original)>0 and original.isalpha():
	word=original.lower()
	first=word[0]
	new_word=word+first+pyg
	#sliceing the word
	new_word=new_word[1: ]
 	print new_word
else:
    print 'empty'


    
#function calling function 

def one_good_turn(n):
	return n+1


def deserves_another(n):
	return one_good_turn(n)+2



#built in function 
max()
min()
abs()
type()


#python lists and dictionaries 
#lists are datatypes that used to store a collection of data 
# example
l=[1,2,3,'a','b','c']

#sliceing
l[2:]
l[:2]
#adding items to the list
l.append(23)
#inserting an item in a specific index
l.insert(6,'d')

#removing element based on value
l.remove(3)

# return last element , modifying the list
lasr_element=l.pop()
lasr_element =

thired_element = pop(2)
thired_element = l[2]

#index() return position of the value in the list just like indexOf() in java
l.index('a')

#l.count('a') return number of occurrences 
l.count('a')

#concatenates a list on to the existing lis
l.extend([1,2])
#sort list
l.sort()
# remove duplicate in list
ll=list(set(l))
#reverse list
l.reverse()

#List Comprehensions,
l = [1,2,3]
l_new=[i**2 for i in l]
l_new=[1,4,9]

'''
-set oparations
Union
Intersection
Difference
Symmetric Difference
'''
# Union
set1=set([1,2,3])
set2=set([3,4,5])
>>> set1 | set2 
>>>set([1,2,3,4,5])
#intersection
set1 & set2
set([3])
#difference
set1 - set2
set([1,2])
#Symmetric difference
set1^set2
set([1,2,4,5])

# Set Comprehensions
vowels = ['a','e','i','o','u']
# oparition withen the context of the set in relation the the passed value 
{x for x in 'maintenance' if x not in vowels}
# not vowels
set(['c', 'm', 't', 'n'])