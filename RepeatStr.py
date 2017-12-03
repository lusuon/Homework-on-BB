a=''
b=''
while len(a)<1 or len(a)>10000 or len(b)<1 or len(b)>10000:
    a=input('Enter a string that you want to repeat;')
    b=input('Enter a string you want to make it a substring: ')
Max =(len(b)//len(a))+1
for i in range(Max+1):
    if b in a*i:
        print(i)
        break
if b not in a*i:
    print('-1')
