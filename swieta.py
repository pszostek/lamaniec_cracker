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

words=[u"The North Face Flux Power Stretch Pant Lady NE", 
u"Rękawiczki The North Face Pamir Windstopper II Glove", u"Nosidełko Deuter Daszek Sun Roof Rain Cover"]

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

pw=[u'jezus',
 u'aniołek',
 u'barszcz',
 u'choinka',
 u'ciasto',
 u'czerwony',
 u'dania',
 u'duch',
 u'folklor',
 u'grzybowa',
 u'gwiazdka',
 u'igliwie',
 u'kapusta',
 u'karp',
 u'kartka',
 u'kluski',
 u'kolędy',
 u'kolęda',
 u'kompot',
 u'królowie',
 u'kutia',
 u'lampki',
 u'mikołaj',
 u'narodziny',
 u'nerwy',
 u'noc',
 u'opłatek',
 u'ozdoby',
 u'pasterka',
 u'pasterka',
 u'pasterze',
 u'piernik',
 u'pierniki',
 u'pieróg',
 u'pierogi',
 u'porządki',
 u'post',
 u'potrawy',
 u'prezenty',
 u'renifer',
 u'sanki',
 u'sianko',
 u'siano',
 u'świeca',
 u'święto',
 u'stroik',
 u'sweter',
 u'szopka',
 u'tradycja',
 u'uszka',
 u'rodzina',
 u'wiara',
 u'wieczerza',
 u'wigilia',
 u'wspólnota',
 u'zabawki',
 u'zakupy',
 u'zielony',
 u'łańcuch',
 u'śnieg']


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

fw = create_feasible_list(pw, letters.keys())

import random
from copy import copy

max_string = []
iter_counter = 0
while True:
    words = []
    seq = range(0, len(fw))
    random.shuffle(seq)
    this_iter_letters = copy(letters)
    for i in seq:
        word = fw[i]
        reduced_word_dict = reduce_word(word)
        if is_doable(reduced_word_dict, this_iter_letters):
            remove(reduced_word_dict, this_iter_letters)
            words.append(word)
    if len(words) > len(max_string):
        words.sort()
        print("")
        print(iter_counter)
        print(str(len(words)) + ": " + str(words))
        print(str(this_iter_letters))
        max_string = words
    iter_counter += 1