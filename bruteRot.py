#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================
# Author	--> DevMen
# Date created	--> 07/04/2021
# Last modified	--> 08/04/2021
# Version	--> Python 3.8.5
# =============================
'''
 este programa fue echo para aplicar
 encriptacion ROT/caesar cipher
'''
# =============================
# Imports
import argparse
# =============================
# For example, ROT 13 would be:
# Index		0|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
# English	a|b |c |d |e |f |g |h |i |j |k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z
# ROT+13	n|o |p |q |r |s |t |u |v |w |x |y |z |a |b |c |d |e |f |g |h |i |j |k |l |m

ALPHABET = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

def banner():
	return """
    __               __       ____        __ 
   / /_  _______  __/ /____  / __ \____  / /_
  / __ \/ ___/ / / / __/ _ \/ /_/ / __ \/ __/
 / /_/ / /  / /_/ / /_/  __/ _, _/ /_/ / /_  
/_.___/_/   \__,_/\__/\___/_/ |_|\____/\__/  
=======================> by ☆ developmentMen☆
"""

def generateKey(rotNum):
        key={}
        for i, ch in enumerate(ALPHABET):
            if (i + int(rotNum)) < len(ALPHABET):
                key[ch] = ALPHABET[i + int(rotNum)]
            else:
                key[ch] = ALPHABET[(i + int(rotNum)) % len(ALPHABET)]
        return(key)

def encrypt(normalStr, key):
        encryptedText = ''
        for word in normalStr.split(' '):
            encryptedText += ' '
            for ch in word:
                if ch in key:
                    encryptedText += key[ch]
                elif ch.lower() in key:
                    encryptedText += key[ch.lower()].upper()
                else:
                    encryptedText += ch
        return(encryptedText)

def main(s, n):
	for num in range(1,n+1):
		k = generateKey(num)
		print('========= Rotation {} =========='.format(num))
		print(encrypt(s, k))



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="bruteforce for ROT cipher")
	parser.add_argument('-nb', '--noBanner', action='store_true', help='no print banner')
	parser.add_argument('-v', '--verbose', action='store_true', help="more details")
	parser.add_argument('-s', '--string', type=str, metavar='', help='string to encode/decode')
	parser.add_argument('-n', '--number', type=int, default=13, metavar='', help='numbers of rotations')

	args = parser.parse_args()

	if not args.noBanner: print(banner())
	try:
		main(args.string, args.number)
	except Exception as a:
		print("============ ERROR ============")
		if args.verbose:
			print("\n======== {} ======== \n\n\tpls select the string tho encrypt whit -s or --string\n".format(a))
		else:
			print("\n\tpls select the string tho encrypt whit -s or --string\n")

