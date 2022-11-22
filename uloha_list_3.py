def sucin(zoznam):
    vysledok=zoznam[0]
    for i in range(len(zoznam)):
        if i>0:
            vysledok=vysledok*zoznam[i]
    return vysledok

c = [2, 3, 5, 7, 11]
print(sucin(c))

print(sucin(list(range(1, 11))))

print(sucin([2] * 20))