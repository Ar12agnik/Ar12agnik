'''l=[[11,-2,3],
   [5,6,7],
   [8,9,10],
   [5,-6,-2]
   ]
   1) print the ∑ of all elements
   2)print the ∑ of rowwise
   3)print the ∑ of collumwise'''
#1)
l=[[11,-2,3],
   [5,6,7],
   [8,9,10],
   [5,-6,-2]
]
sum=0
for i in l:
    for j in i:
        sum+=j
print(f"The sum of the numbers is {sum}")
#2)
l=[[11,-2,3],
   [5,6,7],
   [8,9,10],
   [5,-6,-2]
]
counter=0
for q in l:
    row_wise=0
    for w in q:
        row_wise+=w
    counter+=1
    print(f"The sum of the row {counter} is {row_wise}")
#3)
l=[[11,-2,3],
   [5,6,7],
   [8,9,10],
   [5,-6,-2]
   ]
for x in range(3):
    sum=0
    for y in range(4):
        sum+=l[y][x]
    print(f"The sum of collumn {x+1} is {sum}")