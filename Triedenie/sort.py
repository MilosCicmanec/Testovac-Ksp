def najviac_zavazi(n, zavazia):
    # Početnosť hmotností
    frekvencie = [0] * 1001  # Rozsah hmotností od 1 do 1000
    for zavazie in zavazia:
        frekvencie[zavazie] += 1
    
    # Hľadanie najväčšej početnosti a príslušnej hmotnosti
    max_pocet = 0
    min_hmotnost = 1001
    for hmotnost, pocet in enumerate(frekvencie):
        if pocet > max_pocet or (pocet == max_pocet and hmotnost < min_hmotnost):
            max_pocet = pocet
            min_hmotnost = hmotnost
    
    return min_hmotnost, max_pocet

# Vstup
n = int(input())
zavazia = list(map(int, input().split()))

# Výpočet a výstup
hmotnost, pocet = najviac_zavazi(n, zavazia)
print(hmotnost, pocet)
