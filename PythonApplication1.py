from random import *
nimed=["Mati", "Meelis", "Kati", "Mati"]
while True:
    print("****************")
    v=input("N-näitada andmeid\nl-lisada andmeid\n")
    if v=="N":
        v=input("Kas juhuslik(j) nimi või terve loetelu(t)?")
        if v=="t":
            print(nimed)
        elif v=="j":
            print(choice(nimed)) 
    elif v=="L":
        v=input("Kas nimekirja lõppu(l) või positsioonile(p)")
        if v=="l":
            nimi=input("Siseta nimi: ")
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Siseta nimi: ")
            ind=int(input("Mille kohale: "))
            nimed.insert(ind-1, nimi)
    elif v=="i":
        v=input("Kas nimi järgi(n) või indeksi järgi(i) või kõik nimed(k)")
        if v=="i":
            ind=int(input("Siseta indeks: ")) 
            nimed.pop(ind-1)
        elif v=="k":
        elif v=="n":
            nimi=input("Siseta nimi:  ")
            mitu=nimed.count(nimi)
            if mitu>0:
                pass
            else:
                print(f"{nimi} ei ole loetelus")

        v=input("Kas nimi järgi(n) või indeksi järgi(i) või kõik nimed(k)")
        if v.lower() == "i":
            ind = int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
            print(spc,nimed, end=spc)
        elif v.lower() == "n":
            nimi = input("Sisesta nimi: ")
            mitu = nimed.count(nimi)
            if mitu > 1:
                ind = -1
                indlist = []
                for e in nimed:
                    ind += 1
                    if e == nimi:
                        indlist.append(ind)
                print(indlist)
                v = int(input("Mis indeks?"))
                nimed.pop(v)
            else:
                nimed.remove(nimi)
        else:
            print(f*{nimi})




                nimed.sort(reverse=True) 




