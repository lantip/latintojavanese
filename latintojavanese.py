#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2019/04/02"
__description__ =   "Latin to Javanese Transliterator"
""" 

import sys

HURUF = {
    'h': 'ꦲ',
    'n': 'ꦤ',
    'c': 'ꦕ',
    'r': 'ꦫ',
    'k': 'ꦏ',
    'd': 'ꦢ',
    't': 'ꦠ',
    's': 'ꦱ',
    'w': 'ꦮ',
    'l': 'ꦭ',
    'p': 'ꦥ',
    'dh': 'ꦝ',
    'j': 'ꦗ',
    'y': 'ꦪ',
    'ny': 'ꦚ',
    'm': 'ꦩ',
    'g': 'ꦒ',
    'b': 'ꦧ',
    'th': 'ꦛ',
    'ng': 'ꦔ'
}

PASANGAN = {
    'h': '꧀ꦲ',
    'n': '꧀ꦤ',
    'c': '꧀ꦕ',
    'r': '꧀ꦫ',
    'k': '꧀ꦏ',
    'd': '꧀ꦢ',
    't': '꧀ꦠ',
    's': '꧀ꦱ',
    'w': '꧀ꦮ',
    'l': '꧀ꦭ',
    'p': '꧀ꦥ',
    'dh': '꧀ꦓ',
    'j': '꧀ꦗ',
    'y': '꧀ꦪ',
    'ny': '꧀ꦚ',
    'm': '꧀ꦩ',
    'g': '꧀ꦒ',
    'b': '꧀ꦧ',
    'th': '꧀ꦛ',
    'ng': '꧀ꦔ'
}

SANDHANGAN = {
    'wulu': 'ꦶ',
    'suku': 'ꦸ',
    'pepet': 'ꦼ',
    'taling': 'ꦺ',
    'taling-tarung': 'ꦺꦴ',
    'cecak': 'ꦁ',
    'wignyan': 'ꦃ',
    'layar': 'ꦂ',
    'cakra': 'ꦿ',
    'keret': 'ꦽ',
    'pengkal': 'ꦾ',
    'pangkon': '꧀'
}

def transliterate(hrf, isend, prv, nxt):
    ltr = ''
    dobel = ['th', 'dh', 'ny']
    iskeret = False
    if hrf.find('ng') == 0:
        if len(hrf) == 2:
            ltr += SANDHANGAN['cecak']
        else:
            ltr += HURUF['ng']
        if len(hrf) > 3:
            if hrf[2] == 'l':
                ltr += PASANGAN['l']
            elif hrf[2] == 'y':
                ltr += SANDHANGAN['pengkal']
            elif hrf[2] == 'r':
                if hrf[3] == 'e':
                    ltr += SANDHANGAN['keret']
                    iskeret = True
                else:
                    ltr += SANDHANGAN['cakra']
    elif hrf.find('ny') == 0:
        if prv:
            if len(prv) == 1:
                ltr += PASANGAN['ny']
            else:
                ltr += HURUF['ny']
        else:
            ltr += HURUF['ny']
        if len(hrf) > 3:
            if hrf[2] == 'l':
                ltr += PASANGAN['l']
            elif hrf[2] == 'y':
                ltr += SANDHANGAN['pengkal']
            elif hrf[2] == 'r':
                if hrf[3] == 'e':
                    ltr += SANDHANGAN['keret']
                    iskeret = True
                else:
                    ltr += SANDHANGAN['cakra']
    elif hrf.find('th') == 0:
        if prv:
            if len(prv) == 1:
                ltr += PASANGAN['th']
            else:
                ltr += HURUF['th']
        else:
            ltr += HURUF['th']
        if len(hrf) > 3:
            if hrf[2] == 'l':
                ltr += PASANGAN['l']
            elif hrf[2] == 'y':
                ltr += SANDHANGAN['pengkal']
            elif hrf[2] == 'r':
                if hrf[3] == 'e':
                    ltr += SANDHANGAN['keret']
                    iskeret = True
                else:
                    ltr += SANDHANGAN['cakra']
    elif hrf.find('dh') == 0:
        if prv:
            if len(prv) == 1:
                ltr += PASANGAN['dh']
            else:
                ltr += HURUF['dh']
        else:
            ltr += HURUF['dh']
        if len(hrf) > 3:
            if hrf[2] == 'l':
                ltr += PASANGAN['l']
            elif hrf[2] == 'y':
                ltr += SANDHANGAN['pengkal']
            elif hrf[2] == 'r':
                if hrf[4] == 'e':
                    ltr += SANDHANGAN['keret']
                    iskeret = True
                else:
                    ltr += SANDHANGAN['cakra']
    if len(hrf) == 2:
        if hrf == 'ng':
            ltr += SANDHANGAN['cecak']
        else:
            if prv:
                if len(prv) == 1:
                    if prv not in  ['h', 'r', 'y']:
                        ltr += PASANGAN[hrf[0]]
                    else:
                        ltr += HURUF[hrf[0]]
                else:
                    ltr += HURUF[hrf[0]]
            else:
                ltr += HURUF[hrf[0]]
    elif len(hrf) == 1:
        if hrf == 'r':
            ltr += SANDHANGAN['layar']
        elif hrf == 'h':
            ltr += SANDHANGAN['wignyan']
        else:
            if isend:
                ltr += HURUF[hrf[0]]
                ltr += SANDHANGAN['pangkon']
            else:
                ltr += HURUF[hrf[0]]

    elif len(hrf) > 2:
        if hrf[1] == 'l':
            ltr += HURUF[hrf[0]]
            ltr += PASANGAN['l']
        elif hrf[1] == 'y' and hrf[0] != 'n':
            ltr += HURUF[hrf[0]]
            ltr += SANDHANGAN['pengkal']
        elif hrf[1] == 'r':
            if prv:
                if len(prv) == 1:
                    ltr += PASANGAN[hrf[0]]
                    ltr += SANDHANGAN['cakra']
                else:
                    ltr += HURUF[hrf[0]]
                    ltr += SANDHANGAN['cakra']
            else:
                ltr += HURUF[hrf[0]]
                ltr += SANDHANGAN['cakra']
    if hrf.find('u') == (len(hrf) - 1):
        ltr += SANDHANGAN['suku']
    
    if 'é' in hrf or 'è' in hrf:
        if prv:
            ltr += SANDHANGAN['taling']
        else:
            ltr += SANDHANGAN['taling']
    if hrf.find('e') == (len(hrf) - 1):
        if not iskeret:
            ltr += SANDHANGAN['pepet']
    if hrf.find('i') == (len(hrf) - 1):
        ltr += SANDHANGAN['wulu']
    if 'o' in hrf:
        ltr += SANDHANGAN['taling-tarung']
    return ltr


def translate(word):
    ltr = []
    start = 0
    consonant = ['c','k','s','w','l','p','j','m','b']
    specials = ['t','d']
    dobel = ['th', 'dh', 'ny', 'ng']
    insrt = [ 'h','y','g','n']
    vowels = "AaEeÈèÉéIiOoUuÊêĚěĔĕṚṛXxôâāīūō"
    for dob in dobel:
        if word.find(dob) == 0:
            if len(word) >= 3:
                if word[2] in vowels:
                    ltr.append(dob+word[2])
                    start = 3
            elif len(word) >= 4:
                if word[2] == 'r':
                    if word[3] in vowels:
                        ltr.append(dob+'r'+word[3])
                        start = 4
    for ins in insrt:
        if word.find(ins) == 0:
            if len(word) >=2:
                if word[1] in vowels:
                    ltr.append(ins+word[1])
                    start = 2
                elif word[1] in ['l', 'r', 'y']:
                    if word[2] in vowels:
                        ltr.append(ins+word[1]+word[2])
                        start = 3
    if word[0] in vowels:
        ltr.append('h'+word[0])
        start = 1
    for i in range(start,len(word)):
        if word[i] in consonant:
            try:
                if len(word[i:]) > 1:
                    if word[i+1] in vowels and word[i] != 'l':
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
                    else:
                        if word[i+1] in ['l', 'r','y']:
                            if len(word[i:]) > 2:
                                if word[i+2] in vowels:
                                    ltr.append(word[i]+word[i+1]+word[i+2])
                                    i = i + 3
                                else:
                                    ltr.append(word[i]+word[i+1])
                                    i = i + 2
                            else:
                                if (i-2) >= 0:
                                    if len(word[i:]) > 1:
                                        if word[i] not in word[i-2]+word[i-1]:
                                            ltr.append(word[i]+word[i+1])
                                            i = i + 2
                        else:
                            if word[i] != 'l':
                                ltr.append(word[i])
                                i = i + 1
                            else:
                                if len(word[i:]) > 1:
                                    if word[i+1] in vowels:
                                        if len(ltr) > 0:
                                            if not word[i]+word[i+1] in ltr[len(ltr)-1]:
                                                ltr.append(word[i]+word[i+1])
                                                i = i + 2
                                        else:
                                            ltr.append(word[i]+word[i+1])
                                            i = i + 2
                else:
                    ltr.append(word[i])
                    i = i + 1
            except:
                ltr.append(word[i])
                i = i + 1
        elif word[i] in specials:
            try:
                if len(word[i:]) >=2:
                    if word[i+1] == 'h' and word[i+2] in vowels:
                        ltr.append(word[i]+word[i+1]+word[i+2])
                        i = i + 3
                    elif word[i+1] in ['l', 'r']:
                        if len(word[i:]) > 2:
                            if word[i+2] in vowels:
                                ltr.append(word[i]+word[i+1]+word[i+2])
                                i = i + 3
                            else:
                                ltr.append(word[i]+word[i+1])
                                i = i + 2
                        else:
                            ltr.append(word[i]+word[i+1])
                            i = i + 2
                    elif word[i+1] in vowels:
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
                elif len(word[i:]) == 1:
                    if word[i+1] == 'h':
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
                    elif word[i+1] in vowels:
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
            except:
                ltr.append(word[i])
                i = i + 1
        elif word[i] == 'n':
            if len(word[i:]) > 2:
                if word[i+1] in ['g','y'] and word[i+2] in vowels:
                    ltr.append(word[i]+word[i+1]+word[i+2])
                    i = i + 3
                elif word[i+1] in ['g','y'] and word[i+2] not in vowels:
                    ltr.append(word[i]+word[i+1])
                    i = i + 2
                else:
                    if word[i+1] in vowels:
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
            else:
                try:
                    nxt = word[i+1]
                except:
                    nxt = None
                if nxt:
                    if nxt in vowels:
                        ltr.append(word[i]+nxt)
                        i = i + 2
                    elif nxt == 'g':
                        ltr.append(word[i]+nxt)
                        i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
                else:
                    ltr.append(word[i])
                    i = i + 1
        elif word[i] in ['r','y']:
            if i == 0:
                if len(word[i:]) > 1:
                    if word[i+1] in vowels:
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
            else:
                if len(word[i:]) > 1:
                    if word[i+1] in vowels:
                        if word[i-1] not in vowels:
                            if (i-2) >=0:
                                if (word[i-2]+word[i-1]) in dobel:
                                    ltr.append(word[i-2]+word[i-1]+word[i]+word[i+1])
                                    i = i + 2
                                else:        
                                    if not (word[i]+word[i+1]) in ltr[len(ltr)-1]:
                                        ltr[len(ltr)-1] = ltr[len(ltr)-1] + word[i] + word[i+1]
                                        i = i + 1
                        else:
                            ltr.append(word[i]+word[i+1])
                            i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
                else:
                    ltr.append(word[i])
                    i = i + 1
        elif word[i] == 'g':
            if 'g' in ltr[len(ltr)-1] and len(ltr[len(ltr)-1]) > 2:
                pass
            else:
                if len(word[i:]) > 1:
                    if word[i+1] in vowels:
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
                    else:
                        if (i-2) > 0:
                            if (word[i-2]+word[i-1]) == 'ng':
                                pass
                        else:
                            if ltr[len(ltr) - 1] != 'ng':
                                ltr.append(word[i])
                                i = i + 1
                            else:
                                i = i + 1
                else:
                    if (i-2) > 0:
                        if (word[i-2] + word[i-1]) == 'ng':
                            pass
                    else:
                        ltr.append(word[i])
                        i = i + 1
        elif word[i] == 'h':
            if 'h' in ltr[len(ltr)-1] and len(ltr[len(ltr)-1]) > 2:
                pass
            else:
                if len(word[i:]) > 1:
                    if word[i+1] in vowels:
                        ltr.append(word[i]+word[i+1])
                        i = i + 2
                    else:
                        ltr.append(word[i])
                        i = i + 1
                else:
                    ltr.append(word[i])
                    i = i + 1
    return ltr


def dotranslate(word):
    trslt = []
    for wrds in word.split():
        for wrd in wrds.split('-'):
            trslt = trslt + translate(wrd.lower())
    return trslt


def dotransliterate(word):
    ltr = dotranslate(word)
    litr = ''
    isend = False
    for index, lt in enumerate(ltr):
        if index == len(ltr) - 1:
            isend = True
            nxt = None
        else:
            nxt = ltr[index+1]
        if (index - 1) >= 0:
            prv = ltr[index-1]
        else:
            prv = None

        litr += transliterate(lt, isend, prv, nxt)

    return litr

if __name__ == '__main__':
    question = input('> ')
    while (question != 'quit'):
        try:
            print (dotransliterate(question).lower())
            question = input('> ')
        except:
            sys.exit(1)