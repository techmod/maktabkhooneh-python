name=(str(input()).lower())
for i in range(0,len(name)):
    e=(i,name[i])
name2=name[::-1] 
for j in range(0,len(name2)):
    g=(j,name2[j])
if g==e:
    print('palindrome')
else:
    print('not palindrome')