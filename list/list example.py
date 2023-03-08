#list
thislist=['apple','bnana','cherry']
print(thislist)
#output:-['apple', 'bnana', 'cherry']
##list are used to store multiple items in a single variable
##lists are created with [] brackets
# Properties:-
# ordered changable and allow dublicate entries
# ordered -have a definite order if you add somthing to a list it will be placed at the end of the list
# changable-list items can be changed whenever needed
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#output: ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(thislist[1])
#output: banana (scince banana is placed at 1st index of the list)
#changing The items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"#changes the 1th index element to blackcurrant
print(thislist)
# output: ['apple', 'blackcurrant', 'cherry']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]#deletes the index 1,2 and replaces it with "blackcurrant", "watermelon"
print(thislist)
# output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
thislist[1:4] = ["blackcurrant", "watermelon"]#deletes the index 1,2,3 and replaces it with "blackcurrant", "watermelon"
print(thislist)
# output: ['apple', 'blackcurrant', 'watermelon', 'kiwi', 'mango']
#incerting to a list
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")#incerts watermelon to indes position 2
print(thislist)
#output: ['apple', 'banana', 'watermelon', 'cherry']
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")#appends Orange to the end of the list
print(thislist)
# output: ['apple', 'banana', 'cherry', 'orange']
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)#appends tropical to this list
#append() only adds one whereas extend adds multiple elements
print(thislist)
# output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")#creates a tupple
thislist.extend(thistuple)#appends thistupple to thislist
print(thislist)
# output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")#removes Banana from thislist
print(thislist)
# output: ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist #delets the list
# print(thislist)
# output(if print statement is not commented out): NameError: name 'thislist' is not defined
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):#run loop till len(thislist) (len(thislist) gives the legnth of the list as an output)
  print(thislist[i])#prints thislist[i]
'''output : apple
            banana
            cherry
'''

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])#prints thislist[i]
  i = i + 1#increases the value of i by 1
'''output : apple
            banana
            cherry
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
"does the same thing as the above 2"
'''output : apple
            banana
            cherry
'''



