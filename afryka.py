#!/usr/bin/python
# -*- coding: utf-8 -*-

def reduce_word(word):
    ret = {}
    for letter in word:
        try:
            ret[letter] += 1
        except:
            ret[letter] = 1
    return ret

def is_feasible(word, letters):
    word_letters = reduce_word(word)
    for letter, value in word_letters.items():
        if letter not in letters:
            return False
        if letters[letter] < value:
            return False
    return True

def create_feasible_list(words, letters):
    ret = []
    for word in words:
        if is_feasible(word, letters):
            ret.append(word)
        else:
            continue
    return ret

words=[u'Uprząż Singing Rock Profi Worker Standard Sandały The North Face Hedgehog Sandal Tshirt The North Face Watercolour Tee SS Lady']

letters = {}
for word in words:
	for letter in word:
		if letter in " \n":
			continue
		letter = letter.lower()
		try:
			letters[letter] += 1
		except:
			letters[letter] = 1

w=u'ar,stres,lat,honor,żar,harem,taniec,chat,żądeł,het,hen,dal,sen,tors,hord,rap,plag,rowy,dech,kanał,łowy,syk,muł,broni,kolec,dal,ogni,wojen,klimat,dar,ul,koral,zew,zje,zło,zoo,kat,kolor,bieda,pot,brud,kres,lot,komar,rajd,szok,oaz,pij,susz,mord,rasizm, bocian, gry,jad,jar,byk, giez,mat,mat,bat,boy,garb,miraż,dur,jądro,ląd, lud, rytm, czar, piach, upał, gnu, krew, pustyni, równik, woda, syf, ból, malaria, ras, czarny, burza, słoń, lew, las, bieg, atak, rzeź, walk, wróg, wrogi, rogi, kieł, kły, kość, skór, tamtam, deszcz,palm, fig, łup, wąż, boli, brąz, kot,kij, wioska, wiosek, chat, glin, barw, kanał, tarcz, dzid, rud, ropa, busz,film,raf,czerwony,opad,delt,małp,tropiki,ptak,zielony,fynbos,papug,tęcz,hien,fauna,slums'
#safari, sawann
pw=sorted(list(set([x.strip() for x in w.split(",") if x.strip()])))
print pw
exit
def is_doable(dict_word, dict_all):
    for letter, count in dict_word.items():
        if letter not in dict_all:
            return False
        if count > dict_all[letter]:
            return False
    return True

def remove(reduced_word, letters):
    for letter, number in reduced_word.items():
        letters[letter] -= number
      


def print_sequence(counter, words, letters):
    print("")
    print(counter)
    print(str(len(words))+": "+", ".join(words))
    print("".join(sorted([l*v for l,v in letters.items()])))

fw = create_feasible_list(pw, letters)

import random
from copy import copy

random.seed()
max_string = []
max_hashes = set() 
max_seq_hashes = set()
iter_counter = 0

try:
    while True:
        words = []
        seq = range(0, len(fw))
        random.shuffle(seq)

        if hash(tuple(seq)) in max_seq_hashes:
            continue

        this_iter_letters = copy(letters)
        for i in seq:
            word = fw[i]
            reduced_word_dict = reduce_word(word)
            if is_doable(reduced_word_dict, this_iter_letters):
                remove(reduced_word_dict, this_iter_letters)
                words.append(word)
        if len(words) > len(max_string):
            words.sort()
            print_sequence(iter_counter, words, this_iter_letters)
            max_string = words
	    print("\a")
            
            max_hashes.clear() 
            max_hashes.add(hash(tuple(words)))
            max_seq_hashes.clear() 
            max_seq_hashes.add(hash(tuple(seq)))
        elif len(words) == len(max_string):
            words.sort()
            if hash(tuple(words)) not in max_hashes:
                max_hashes.add(hash(tuple(words)))
                max_seq_hashes.add(hash(tuple(seq)))
                print_sequence(iter_counter, words, this_iter_letters)
        iter_counter += 1
except KeyboardInterrupt:
    print iter_counter

"""
1531422
24: chat, chord, dar, dech, delt, gry, hien, kat, kres, las, lot, ogni, pot, raf, ras, rogi, rud, safari, sawann, syf, tors, wąż, zoo, łup
cdeeeeeeghhhnnnrttt

1548970
24: atak, chat, chord, dal, dar, dech, delt, dur, fig, gry, hien, kres, ogni, pot, raf, ras, rogi, ropa, sawann, syf, tors, ul, wąż, zło
ceeeeeehhhnnnorsstttt

1552372
24: atak, chat, chord, dal, dar, dech, dur, fig, glin, gry, hien, kres, lot, pot, raf, ras, rogi, ropa, rud, sawann, syf, tors, wąż, zło

105479
27: atak, chat, chord, dar, dech, delt, dur, fig, gry, hen, het, hien, kres, lot, pot, raf, rap, ras, rogi, sawann, sen, syf, tors, ul, wrogi, zoo, żądeł
aceehnnstt
805
27: KOT, chat, chord, dal, dar, dech, delt, dur, fig, gnu, gry, hen, het, hien, kres, las, pot, raf, rap, ras, rogi, sawann, sen, syf, taniec, tors, wąż, zło
eehoortt

"""