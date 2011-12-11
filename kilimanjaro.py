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

words=[u'UprzążBlack Diamond Momentum SA SpodenkiLafuma Lady Explorer Shorts TshirtThe North Face Watercolour Tee SS Lady']

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

w=u'namiot, mat, spiwór, but, sandał, klapki, polar, puchówka, kurtki, kurtka, czołówka, świec, gaz, gar, woda, żel, map, szal, sól, szczot, past, kij, skarpet, bielizny, majtki, koszul, bluz, zegar, telefon, zapałki, lek, bandaż, opaska, nóż, kurtka, okulary, rak, maść, stuptut, butla, kartusz, hamak, ciuch, wór, worek, spinka, sznur, bilet, aparat, kamer, waty, lornetki, igła, tonik, moskitier, kapelusz, krem, łyżka, kart, kości, gry, gra, baton, kasz, rep, hak, mis, pas, flet, termos, talerz, szkła, płyn, mić, nitka, baterie, koc, kaw, fig, daktyl, orzech, morel, kask, lin, kubek, sos, lamp, filtr, szampan, bidon, rac,lep, lup, sok, soi, ser, tub, win,wiz,gum,czap,drut,zup,płacht, etui, kompas,piw,mydło,gąbek,plastry, skalpel, agrafka, taśm, noży, poncho, rondel, pet, samca, mufa, hel, dar'
#safari, sawann
pw=sorted(list(set([x.strip() for x in w.split(",") if x.strip()])))

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
print fw
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
30887
23: dar, drut, etui, flet, hak, hel, lep, lin, mat, mufa, noży, poncho, rep, rondel, samca, ser, soi, sok, sos, talerz, termos, tub, waty
acddhmrxą


38522
23: but, dar, drut, etui, flet, hamak, hel, lep, lin, mat, mufa, noży, orzech, pet, polar, rondel, samca, ser, soi, sok, sos, termos, waty
cddhnrxą

25049
23: but, dar, drut, flet, hak, hel, koc, lep, lin, mat, mufa, namiot, pet, rep, rondel, samca, ser, soi, sos, sznur, termos, waty, żel
acddhhoorxyą

31437
23: but, ciuch, dar, drut, flet, hak, hel, koc, lin, map, mat, morel, mufa, noży, pet, rep, rondel, ser, soi, sos, talerz, termos, waty
aaddhnossxą


"""