#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs
import os

f = codecs.open('English-French.txt', 'r', 'utf-8')
f2 = codecs.open('full_dictionary_POS.txt' ,'w', 'utf-8')

doc = f.read().split('\n')
POS = []
for line in doc:
	line = line.split("\",\"",)
	if len(line) <= 2:
		continue
	else: 
		line = line[2]
	array = re.split(',|/', line)
	array = [i.rstrip().rstrip('\"') for i in array]
	array = filter(bool, array)
	for thing in array:
		POS.append(thing)
#print array
POS = set(POS)
for i in POS:
	f2.write(i + '\n')

f.close()
f2.close()