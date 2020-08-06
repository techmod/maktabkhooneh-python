wins = 0
total = 0
mosavi=0
for i in range(30):
    num = int(input())
    if num == 3:
       wins += 1
       total += num
    elif num == 1:
        mosavi += 1
        total += num
print(total, wins)
