#!/usr/bin/python
# -*- coding: utf-8 -*-

from string import Template


lista_ich_slow = u"The north face super bót parbat"
#lista slow oddzielonych /,\b*/
lista_moich_slow = u"pieróg, barszcz, karp"
###
lista_ich_slow = [w.strip().lower() for w in lista_ich_slow.split(" ") if w.strip()]
#podzielmy to na cześci i wywalmy spacje
lista_moich_slow = [w.strip().lower() for w in lista_moich_slow.split(",")]
#usuńmy duplikaty
lista_moich_slow = list(set(lista_moich_slow))

litery_prawdziwe = u"aąbcćdeęfghijklłmnńoóprsśtuvwxyzżź"
litery_prawdziwe = list(litery_prawdziwe)

litery_ampl = ['a','aa','b','c','cc','d','e','ee','f','g','h','i','j','k','l','ll','m','n','nn','o','oo','p','r','s','ss','t','u','v','w','x','y','z','zz','zzz']

#zmapujmy litery prawdziwe na litery amplowe
mapa_real_ampl = dict(zip(litery_prawdziwe, litery_ampl))

ampl_string = """data;

set LITERY := a aa b c cc d e ee f g h i j k l ll m n nn o oo p r s ss t u v w x y z zz zzz;
param N := ${ilosc_slow};

param litery_w_slowach: a aa b c cc d e ee f g h i j k l ll m n nn o oo p r s ss t u v w x y z zz zzz :=
${string_id_litery}

param: litery_dane :=
${string_litera_ilosc}
"""
ampl_template = Template(ampl_string)

def redukuj_slowo(slowo):
    """zwraca slownik {litera_ampl:wartosc, ...}"""
    licznik = {}
    for litera in slowo:
        try:
            licznik[mapa_real_ampl[litera]] += 1
        except: #jeszcze nie było tej wartości w słowniku
            licznik[mapa_real_ampl[litera]] = 1
    return licznik

#w tej liscie kazdy element to bedzie slownik {litera_amplowa : ilosc, ..}, kazdy wyraz bedzie mial swoj slownik
litery_w_slowach = [] 

for slowo in lista_moich_slow:  
    zredukowane = redukuj_slowo(slowo)
    litery_w_slowach.append(zredukowane)
    
#to bedzie slownik {litera_amplowa: wartosc, ...} policzony jako suma dla wszystkich wyrazow
litery_dane = dict(zip(litery_ampl, [0 for x in range(0, len(litery_ampl))]))

for slowo in lista_ich_slow:
    zredukowane = redukuj_slowo(slowo)
    for litera, liczba in zredukowane.items():
        litery_dane[litera] += liczba
        
licznik = 1
string_id_litery = ""
for litery_w_slowie in litery_w_slowach:
    string_id_litery += str(licznik) + "   "
    for litera in litery_ampl:
        if litera in litery_w_slowie:
            string_id_litery += str(litery_w_slowie[litera]) + " "
        else:
            string_id_litery += "0 "
    string_id_litery += "\n"
    licznik += 1
    
string_litera_ilosc = ""
for litera in litery_ampl:
    string_litera_ilosc += litera + "\t" + str(litery_dane[litera]) + "\n"
    
print(ampl_template.safe_substitute(ilosc_slow=len(lista_moich_slow), string_id_litery=string_id_litery, string_litera_ilosc=string_litera_ilosc))
