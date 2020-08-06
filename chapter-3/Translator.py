my_input=int(input())
tedad=0
class_list = dict()
while tedad != my_input:
 data = input()
 tedad +=1
 temp = data.split(' ')
 class_list[temp[0]] = (temp[1])


jomle = input()
lst = jomle.split()
j = ''

for i in lst:
 if i in class_list:
  j = j + class_list.get(i) + ' '
 else:
  j = j + i + ' '

print(j)