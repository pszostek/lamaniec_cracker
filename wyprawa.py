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
    tricks = {u'ą':'a', u'ę':'e', u'ó':'o', u'ł':'l',u'ć':'c',u'ś':'s', u'ż':'z', u'ź':'z'}
    from copy import copy
    letters_copy = copy(letters)
    word_letters = reduce_word(word)
    for letter, value in word_letters.items():
        if letter not in letters_copy:
            if letter in tricks:
                if tricks[letter] not in letters_copy:
                    return False
                elif letters_copy[tricks[letter]] < value:
                    return False
                else:
                    letters_copy[tricks[letter]] -= value
            else:
                return False
        elif letters_copy[letter] < value:
            return False
        else:
             letters_copy[letter] -= value
    return True

def create_feasible_list(words, letters):
    ret = []
    for word in words:
        if is_feasible(reduce_word(word), letters):
            ret.append(word)
        else:
            continue
    return ret

def remove(reduced_word, letters):
    tricks = {u'ą':'a', u'ę':'e', u'ó':'o', u'ł':'l',u'ć':'c',u'ś':'s', u'ż':'z', u'ź':'z'}
    for letter, number in reduced_word.items():
        if letter in letters:
            letters[letter] -= number
        else:
            letters[tricks[letter]] -= number

def print_sequence(counter, words, letters):
    print("")
    print(counter)
    print(str(len(words))+": "+", ".join(words))
    print("".join(sorted([l*v for l,v in letters.items()])))


#import sys
#import codecs

#f = codecs.open( sys.argv[1], "r", "utf-8" )
#lines = [l.strip() for l in f.readlines()]

words=u'CzołówkaPetzl TacTikka CamouflageMarmot Snowdrift in Glove NE Plecak turystycznyBerghaus Twentyfourseven SE  Butelka GRATIS'
w=u'żupan,dzinsy,delia,anorak,melonik,masek,algierka,katanka,hacabaj,bolero,top, kask,kurtka,dres, kaptur, softshell, sweter, polar, puchówka, pas, bluz, koszul, golf, spodni, getr, rajstop, leginsy, kalesony, skarpet, but, kozak, opaska, chust, szal, nauszniki, rękawic, majtki, bielizna, futro, botki, skorup, łapawic, kominiarka, kombinezon, ponch, kapelusz, kamizelek, moher, beret, czapka, gaci, muf, bandan, szub, papach, trzewik, kamasz, kożuch, parka, peleryn, kardigan, pulower, blezer, galoty, stuptut, spódnic, uggi, ocieplacz, kołnierz, membran, piżam, palt, slipy, stringi'

letters = {}
for letter in words:
    if letter in " \n":
        continue
    letter = letter.lower()
    try:
        letters[letter] += 1
    except:
        letters[letter] = 1

pw=sorted(list(set([x.strip() for x in w.split(",") if x.strip()])))
fw = create_feasible_list(pw, letters)
print(u"Literki do wyrazów: " + words)
print(u"Twoje słowa: "+", ".join(pw))
print(u"Ukladalne słowa: "+", ".join(fw))
print("")
raw_input(u"Nacisnij enter albo ctrl+c")


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
            if is_feasible(reduced_word_dict, this_iter_letters):
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
            print this_iter_letters
        elif len(words) == len(max_string):
            words.sort()
            if hash(tuple(words)) not in max_hashes:
                max_hashes.add(hash(tuple(words)))
                max_seq_hashes.add(hash(tuple(seq)))
                print_sequence(iter_counter, words, this_iter_letters)
        iter_counter += 1
except KeyboardInterrupt:
    print iter_counter
    
#    3828
#18: anorak, bluz, but, chust, dres, futro, gaci, galoty, getr, golf, kamasz, masek, muf, palt, rękawic, sweter, szal, top
#cceeeeeiiknnnnnotttvvwyyyół

#24820
#18: anorak, bluz, dres, futro, gaci, getr, golf, kalesony, katanka, masek, muf, papach, rękawic, sweter, szal, szub, top, uggi
#cceeeeilmnnnottttttvvwyyyół
#32797
#18: beret, but, chust, dres, futro, gaci, galoty, getr, golf, kask, kozak, melonik, muf, palt, piżam, rękawic, sweter, szal
##aacceeennnnnostttuvvwyyyół


#39528
#18: blezer, but, chust, dres, futro, gaci, galoty, getr, kalesony, katanka, masek, melonik, muf, sweter, szal, top, trzewik, łapawic
#ccefgnnnottuvvyyó

