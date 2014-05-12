#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs

f = codecs.open('russian.txt', 'r', 'utf-8')
f2 = codecs.open('Rando.txt' ,'w', 'utf-8')

doc = f.read().split('\n')
for line in doc:
	line = line.split("\",\"")[1]
	array = re.findall('(?<=\ )|(?<=^)(\S*?\.)', line)
	array = set(array)
	array = filter(bool, array)
	for item in array:
		f2.write(item + '\n')

f.close()
f2.close()

Pos = codecs.open("Pos.txt", 'w', 'utf-8')
with codecs.open("Rando.txt", "r", "utf-8") as f:
	doc = f.read().split('\n')
	doc = set(doc)
	doc = filter(bool, doc)
	for x in doc:
		Pos.write(x)
		if x is not doc[len(doc) - 1]:
			Pos.write('\n')
	Pos.close()