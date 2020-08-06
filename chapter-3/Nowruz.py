adad=input()
adad=adad.split()
for i in range(len(adad)):
    adad[i]=float(adad[i])
print(int(max(adad)-min(adad)))

