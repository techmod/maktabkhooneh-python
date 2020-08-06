#def divisor is from:
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php


def divisor(n):
    for i in range(n):
        x = len([i for i in range(1, n+1) if not n % i])
    return x


nums = []
i = 0
while i < 20:
    preNum = int(input())
    if(preNum > 0):
        nums.append([divisor(preNum), preNum])
        i += 1
    

nums.sort()

f=nums[len(nums)-1]
x=f.copy()
y = (x[::-1])
print(*y, sep=" ")

