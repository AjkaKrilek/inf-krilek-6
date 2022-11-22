def nakup(zoznam1):
    cena=0
    for i in range(len(zoznam1)):
        if i%2!=0:
            cena+=zoznam1[i]*zoznam1[i-1]
    return cena
zoznam=[6, 8.5, 3, 4.5, 6, 1.59]
print(nakup(zoznam))