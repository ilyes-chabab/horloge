import time

heure = 4, 30 , 00
heure_initiale = (int(heure[0]), int(heure[1]), int(heure[2]))
def afficher_heure(heure):
    print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

def demarrer_horloge(heure_initiale):
    hh, mm, ss = heure_initiale
    while True:
        print("\033[H\033[J")# ça efface l'ecran a chaque tour de boucle 
        afficher_heure((hh, mm, ss))
        ss += 1
        if ss == 60:
            ss = 0
            mm += 1
        if mm == 60:
            mm = 0
            hh += 1
        if hh == 24:
            hh = 0
        time.sleep(1)
demarrer_horloge(heure_initiale)        



