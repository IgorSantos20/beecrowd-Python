palavra1 = input().lower()
palavra2 = input().lower()
palavra3 = input().lower()

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if palavra3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if palavra3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")