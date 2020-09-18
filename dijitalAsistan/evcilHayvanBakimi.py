# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:21:44 2020

@author: 132415621
"""

# Critter Caretaker
# A virtual pet to care for


class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "mutlu"
        elif 5 <= unhappiness <= 10:
            mood = "normal"
        elif 11 <= unhappiness <= 15:
            mood = "üzgün"
        else:
            mood = "kızgın"
        return mood

    mood = property(__get_mood)
    
    def talk(self):
        print ("Ben", self.name, "ve cok", self.mood, "şimdi.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print ("Hummmm. Teşekkürler.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print ("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Evcil hayvanınızın ismi ne olsun?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print (
        """
        Evcil Hayvan Bakımı
    
        0 - Çıkış
        1 - Dinle
        2 - Besle
        3 - Oyna
        """)
    
        choice = input("Seçenek: ")
        print

        # exit
        if choice == "0":
            print ("Güle güle.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            crit.eat()
            food = int(input('Ne kadar yemek vermek ister siniz?(1-4):'))
            crit.eat(food)
            

         
        # play with your critter
        elif choice == "3":
            crit.play()
            fun = int(input('Ne kadar oynamak istersiniz?(1-4):'))
            crit.play(fun)

        # some unknown choice
        else:
            print ("\nKusura bakmayın, fakat"+choice+"geçerli bir seçenek değil.")

main()
("\n\nHerhangi bir tuşa basın.") 
