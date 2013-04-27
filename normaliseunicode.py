# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE ; Annette von STOCKHAUSEN
# GPL 3
# https://www.gnu.org/licenses/gpl-3.0.html
#
# Ce script se contente de transformer les caractères unicodes en caractères unicode combiné.
# Ex :U+03B1 U+0345 => U+1FB3
# Version 1.0
import unicodedata
import os

def normaliser_fichier(fichier):
	'''Normalise un fichier'''
	import codecs
	finale = ''
	debut_phrase = True
	file = codecs.open(fichier,encoding='utf-8')
	for ligne in file:
		ligne  = ligne.strip()
		if ligne!='':
			finale = finale + normalise_ligne(ligne)+'\n'
	file.close()
	if os.path.dirname(fichier)=="":
	    destination = "normal_" + os.path.basename(fichier)
	else:
	    destination = os.path.dirname(fichier) + os.sep + "normal_" + os.path.basename(fichier)
	file = codecs.open(destination,encoding='utf-8',mode='w')
	file.write(finale)
	file.close()

def normalise_ligne(ligne):
	'''On normalise ligne par ligne'''
		
	return unicodedata.normalize("NFC",ligne)

def __main__():
	import sys
	import getopt
	option = getopt.getopt(sys.argv[1:],'')[1]
	if option == ['test']:
		test()
		sys.exit()
	else:
		for fichier in option:
			try:
			    normaliser_fichier(fichier)
			    print (fichier + " normalisé")
			except:
			    print ("Impossible de normaliser "+ fichier)
		sys.exit()
	

__main__()