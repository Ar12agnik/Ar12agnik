s=input("Enter a date in mm/dd/yyyy format: ")
l=s.split('/')
date_str=''
j=['january','febuary','march','april','may','june','july','august','spetember','october','november','december']
date_str=date_str+j[int(l[0])-1]
date_str=date_str+' '+l[1]+','+l[2]
print(date_str)
