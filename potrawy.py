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

words=[u'Travellunch Śniadanie Obiad wegetariański',u'Travellunch Deser Baton energetyczny', u'Travellunch Zupa liofilizowany']

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
w=u"kisiel,grzyby,flaki,pierogi,karp,figi,szynka,daktyle, wino, zupa, ryba, kutia, groch, kapusta, grzyby, piróg, gołąbki, ciasto, kulebiak, pierogi, miakowiec, mak, piernik, kluski, bakalie, orzechy, rodzynki, migdały, barszcz, sałatka, chałka, sernik, strudel, śledź. chrzan, pstrąg, sos, łosoś, dorsz, panga, halibut, tuńczyk, ziemniak, kompot, susz, chleb, tort, keks,uszka, ciastka, masa, ciasto, krem, groch, paszteciki, kapuśniaczek/ czki, rolada, krokiety, chrzan, gęś, wołowina, cielęcina, kaczka, indyk, kura, kurczak, schab, szynka, pieczeń, pasztet, sum, flądra, gicz, kasza, pszenica"
pw=sorted(list(set(w.split(","))))
pw=[w.strip() for w in pw]

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

        #if hash(tuple(seq)) in max_seq_hashes:
        #    continue

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
            
            max_hashes.clear() 
            max_hashes.add(hash(tuple(words)))
          #  max_seq_hashes.clear() 
          #  max_seq_hashes.add(hash(tuple(seq)))
        elif len(words) == len(max_string):
            words.sort()
            if hash(tuple(words)) not in max_hashes:
                max_hashes.add(hash(tuple(words)))
             #   max_seq_hashes.add(hash(tuple(seq)))
                print_sequence(iter_counter, words, this_iter_letters)
        iter_counter += 1
except KeyboardInterrupt:
    print iter_counter