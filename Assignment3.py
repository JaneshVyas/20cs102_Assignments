def Areamax(series, length):
    area=0
    for i in range(length):
        for j in range(i+1, length):
            area=max(area,min(series[j],series[i])*(j-i))
    return area

a=[int(n) for n in input("Enter sequence-").split()]
alen=len(a)
print(Areamax(a,alen))
