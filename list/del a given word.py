a=input("enter a sentence: ")
a=a.split(' ')
l=''
del_element=input("enter a word to delete: ")
a.remove(del_element)
for x in a:
    l=l+x+' '
print("Modified Sentence: ",l)
