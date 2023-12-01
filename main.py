import time
#initialisation des variable
ss=0
mm=0
hh=0
heure = 16,30,0 #l'heure de départ
heure_initiale = (int(heure[0]), int(heure[1]), int(heure[2]))
heure_alarme=16,30,3 #l'heure de l'alarme
heure_pause=16,30,10 #l'heure de pause
mode=str(input("que voulais vous entre le mode d'affichage 12h ou 24h ? : "))
#creation d'une fonction qui fait commencer l'horloge a l'heure mis dans la variable heure
def afficher_heure_24(heure):
    hh=heure[0]
    mm=heure[1]
    ss=heure[2]
    print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
def afficher_heure_12am(heure):
    hh=heure[0]
    mm=heure[1]
    ss=heure[2]
    print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d} AM")   
def afficher_heure_12pm(heure):
    hh=heure[0]
    mm=heure[1]
    ss=heure[2]
    print(f"{heure[0]-12:02d}:{heure[1]:02d}:{heure[2]:02d} PM")    

#creation de la fonction qui mettra une alarme
def alarme(alarme):
    if (hh , mm , ss) == alarme:
        print("l'alarme sonne !")
    return alarme
#creation de la fonction qui fera une pause de l'horloge
def pause(heure_pause):
    if mode == str("24h"):
        if (hh , mm , ss) == heure_pause:
            print("Pause !")
            while True:
                time.sleep(2)
    elif mode == str("12h"):
        if (hh , mm , ss) == heure_pause:
            print("Pause !")
            while True:
                time.sleep(2)
#creation de la boucle horloge qui rajoutera +1 a la variable des seconde , +1 a minute lorsque les seconde auront atteint 60
# et +1 a heure lorsque les minutes auront atteint 60. lorsque seconde et heure atteingnent 60 , ca se met a 0 
# et quand heure atteint 24 heure se remet a 0        
hh , mm ,ss =heure_initiale
if mode == str("24h"):
    while True:
        ss += 1
        if ss == 60:
            ss = 0
            mm += 1
        if mm == 60:
            mm = 0
            hh += 1
        if hh == 24:
            hh = 0    
        afficher_heure_24((hh,mm,ss))
        alarme(heure_alarme)
        pause(heure_pause)
        time.sleep(1)#commande qui sert a freeze une boucle pdt une seconde .
elif mode == str("12h"):   
    if hh < 13:
        while True:
            ss += 1
            if ss == 60:
                ss = 0
                mm += 1
            if mm == 60:
                mm = 0
                hh += 1
            if hh == 13:
                hh = 0    
            afficher_heure_12am((hh,mm,ss))
            alarme(heure_alarme)
            pause(heure_pause)
            time.sleep(1)  
    elif hh > 12:
        while True:
            ss += 1
            if ss == 60:
                ss = 0
                mm += 1
            if mm == 60:
                mm = 0
                hh += 1
            if hh == 12:
                hh = 0    
            afficher_heure_12pm((hh,mm,ss))
            alarme(heure_alarme)
            pause(heure_pause)
            time.sleep(1)   