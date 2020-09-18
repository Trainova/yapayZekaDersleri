# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


'istediginiz seyleri yazabilirsiniz'

sayi = 1+2

print("Sayiniz: " + str(sayi))

liste = [1,2,3,4,5,6]

print(liste)

for degisken in liste:
    print(degisken)
    
for degisken in liste:
    if degisken == 1:
        print(degisken)
        
#%% yeni bir hucre olusuturuyor
print("merhaba dunya")


#%% music yapalim

import musicalbeeps


player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

# Examples:

# To play an A on default octave n°4 for 0.2 seconds
player.play_note("A", 0.2)

# To play a G flat on octave n°3 for 2.5 seconds
player.play_note("G3b", 2.5)

# To play a F sharp on octave n°5 for the default duration of 0.5 seconds
player.play_note("F5#")

# To pause the player for 3.5 seconds
player.play_note("pause", 3.5)


#%% music calma
import musicalbeeps
player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

Twinkle_List = ['c4','c4','g4','g4','a4','a4','g4',\
				'f4','f4','e4','e4','d4','d4','c4',\
				'g5','g5','f4','f4','e4','e4','d4',\
				'g5','g5','f4','f4','e4','e4','d4',\
				'c4','c4','g4','g4','a4','a4','g4',\
				'f4','f4','e4','e4','d4','d4','c4',\
				]

for i in range(0,len(Twinkle_List),1):
    player.play_note("pause", 0.5)
    player.play_note(Twinkle_List[i],0.5)
    
    
#%% 
    
from random import randrange
import musicalbeeps

import datetime


player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

rastgeleSayi = randrange(0,6)  

print()

notaIsimleri = ["A","B","C","D","E","F","G"]
octavListesi = [0,1,2,3,4,5,6,7,8]
duzVeyaTiz = ['#','b']
sure=[0.3,0.6,0.9,1.2,1.5]            
               
notaRastSayi = randrange(0,6)
octavRastSayi = randrange(0,8)
dVTSayi = randrange(0,1)
sureSayi = randrange(0,4)

yeniNota = str(notaIsimleri[notaRastSayi]+str(octavListesi[octavRastSayi])+duzVeyaTiz[dVTSayi])

player.play_note(yeniNota, sure[sureSayi])


def NotaYap():
    notaIsimleri = ["A","B","C","D","E","F","G"]
    octavListesi = [0,1,2,3,4,5,6,7,8]
    duzVeyaTiz = ['#','b']
    sure=[0.3,0.6,0.9,1.2,1.5]
    
    notaRastSayi = randrange(0,6)
    octavRastSayi = randrange(0,8)
    dVTSayi = randrange(0,1)
    sureSayi = randrange(0,4)
    yeniNota = str(notaIsimleri[notaRastSayi]+str(octavListesi[octavRastSayi])+duzVeyaTiz[dVTSayi])
    yeniSure = sure[sureSayi]
    return yeniNota, yeniSure
    
yeniNota, yeniSure = NotaYap()


def muzikYap():
    muzikListesi = []
    for i in range(0,10,1):
        yeniNota, yeniSure = NotaYap()
        muzikListesi.append(yeniNota+str(yeniSure))
        player.play_note(yeniNota, yeniSure)
        tarihVeZaman = datetime.datetime.now()
    with open("muzikListesi_"+tarihVeZaman.strftime("%Y-%m-%d_%H-%M-%S")+".txt","w") as dosya:
        for notalar in muzikListesi:
            dosya.write("%s\n" %notalar)
        
muzikYap() 


import schedule
import time

def job():
    print("Çok çalışıyorum...")
    muzikYap()

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
  
