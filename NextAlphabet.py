a,b=input("Enter a string:"),""
for i in a:
    if i.isalpha():
        if i=='Z'or i=='z': #错误： i=='Z'or 'z'
            i=chr(ord(i)-25)
        else:
            i=chr(ord(i)+1)
    b+=i
print(b)
