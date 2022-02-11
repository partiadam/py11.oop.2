'''
2. Feladat
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait (név, életkor, nem)! A nevét a felhasználó adja meg, az életkorát és a nemét véletlenszerűen határozza meg a program! Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!
'''

from random import choice, randint

nemek = ['fiu', 'lany']

class Kutyak:
    def __init__(self, nev):
        self.nev = nev
        kor = randint(0,15)
        nem = choice(nemek)
        print(f'A kutya neve:  {self.nev}, kora {kor}, neme: {nem}')

kutya1 = Kutyak('Bulldózer')