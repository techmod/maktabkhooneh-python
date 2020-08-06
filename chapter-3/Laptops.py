num=input()
num2=int(num)
lst=[]
for i in range(num2):
    lap = list(map(int, input().split()))
    lst.append(lap)

minimumesh = (min(lst))
maximumesh = (max(lst))
if minimumesh[-1] >= maximumesh[-1]:
    print('happy irsa')
else:
    print('poor irsa')

