#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_feasible(word, letters):
    for letter in word:
        if letter not in letters:
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

words=[u'rakieta śnieżna Salewa Tacul Donna Lady',u"Buty wysokogórskie Zamberlan Pelmo Plus GT RR", u"Materac Therm a Rest Trail Lite Lady NE"]

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
pw=[u'auto',
 u'balia',
 u'blacha',
 u'brzuch',
 u'buty',
 u'deska',
 u'drewno',
 u'dykta',
 u'dętka',
 u'drzwi',
 u'dupa',
 u'dywan',
 u'folia',
 u'gar',
 u'gazeta',
 u'habit',
 u'jabłuszko',
 u'karton',
 u'klapki',
 u'koc',
 u'lada',
 u'leżak',
# u'leże',
 u'lina',
 u'listwa',
 u'maska',
 u'mata',
 u'materac',
 u'metal',
 u'misa',
 u'monoski',
# u'narta',
 u'narty',
 u'narzuta',
 u'nogi',
 u'opona',
 u'opona',
 u'paka',
 u'pas',
 u'patelnia',
 u'plastik',
 u'plecak',
 u'plecy',
 u'pokrywa',
 u'ponton',
 u'pupa',
 u'rakieta',
 u'rama',
 u'roleta',
 u'rower',
 u'rura',
 u'samochód',
 u'sanie',
 u'sanki',
 u'siano',
 u'siatka',
 u'skibob',
 u'skitury',
 u'snowboard',
 u'splitboard',
 u'spodnie',
 u'stuptut',
 u'szmata',
 u'talerz',
 u'taca',
 u'teczka',
 u'torba',
 u'tyłek',
 u'wanna',
 u'waliza',
 u'worek',
 u'wór',
 u'zad',
 u'zlew',
 u'zderzak']


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
      
def reduce_word(word):
    ret = {}
    for letter in word:
        try:
            ret[letter] += 1
        except:
            ret[letter] = 1
    return ret

def print_sequence(counter, words):
    print("")
    print(counter)
    print(str(len(words))+ ": " + ', '.join(words))

fw = create_feasible_list(pw, letters.keys())

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
            print_sequence(iter_counter, words)
            max_string = words
            
            max_hashes.clear() 
            max_hashes.add(hash(tuple(words)))
            max_seq_hashes.clear() 
            max_seq_hashes.add(hash(tuple(seq)))
        elif len(words) == len(max_string):
            words.sort()
            if hash(tuple(words)) not in max_hashes:
                max_hashes.add(hash(tuple(words)))
                max_seq_hashes.add(hash(tuple(seq)))
                print_sequence(iter_counter, words)
        iter_counter += 1
except:
    print iter_counter