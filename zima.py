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

words=[u'Bielizna termoaktywna SmartWool Lighweight Asymmetrical Zip lady Bluza The north face drew peak pullover hoodie rękawiczki the north face etip pamir windstopper glove lady']

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

w=u"śnieg puch biel czapka  szalik kurtka polar sweter kozak płaszcz koc ubaw miód choinka sanki nart grzaniec win pada zimno lody iskrzy lawin zjazd bitwa iglo sanie kul kulig sport prezent mikst pompon bombki deska kakao piernik gry drewno rakiet bigos raki czekan dziab futro kominek szopka noc burz sen zawieja rodzina lampki katar zabaw post rok elf kuc kry lamp dar sny sowa wilk chlap tlę bal zupa korki bęc krę razem dom kolęd ferie pierze gryp szkli tor czas cud watah piec moc panel gil duj ozime zasp"#wieczory walenty 
## bal, cud, dar, dom, elf, ferie, gry, gryp, iglo, kry, lamp, lawin, lody, moc, noc, pada, piec, pierze, polar, post, rakiet, razem, sanie, szkli, tlę, tor, ubaw, watah, wilk, win, zimno, waty
pw=sorted(list(set(w.split(" "))))
pw=[w.strip() for w in pw if w.strip()]

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
