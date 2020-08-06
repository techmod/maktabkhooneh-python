tedad=int(input())
sherkat_karde= input()
sherkat_karde=sherkat_karde.split()
for i in range(len(sherkat_karde)):
    sherkat_karde[i]=int(sherkat_karde[i])
sherkat_karde=[i for i in sherkat_karde if i<=2]
sherkat_karde.sort()
sherkat_konande=sherkat_karde[:3]
ghabel_sherkat_kardan=int(len(sherkat_karde)/3)
print(ghabel_sherkat_kardan)

