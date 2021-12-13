s = str.lower(input())
pangram = "abcdefghijklmnopqrstuvwxyz "

for item in range(27):
    print(item)
    if pangram[item] in s:
        output = True
    
    else:
        output = False
        print("not pangram")
        break
        
if output==True:
    print("pangram")