#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs

f = codecs.open("resources/English-Chinese(T).txt", "r", encoding='utf-8')#input file
f2 = codecs.open("resources/Traditional_Test.txt", "w", encoding='utf-8')#output file

doc = f.read().split('\n')

def addTraditional():
	for index, line in enumerate(doc):
		line = line.strip().rstrip('\"') + u', Traditional\"'
		f2.write(line + '\n')

addTraditional()
f.close()
f2.close()