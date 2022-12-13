from cont_bancar import ContBancar

cont1 = ContBancar('Alex Ionut', 'RO001')
cont2 = ContBancar('Miha Andrei', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.interogareSold()
cont2.interogareSold()

cont1.plataCard(500)
cont1.plataCard(300) # 0
cont2.plataCard(100)
cont2.plataCard(200) # 700

# tema
# clasa angajat
# nume, prenume, salariu, functie, vechime
# constructor : nume, prenume, salariu, functie, vechime
# metode
# descriere
# marire salariuin functie de vechime
# actualizare vechime (parametru noua vechime)
        # self,vechime = noua_vechime
# daca are vechime sub 5 ani marim cu 300
# daca are peste 5 ani marim cu 500