#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs
import os

f = codecs.open('resources//English-Japanese.txt', 'r', 'utf-8')
f2 = codecs.open('resources//full_dictionary_POS_JP.txt' ,'w', 'utf-8')

doc = f.readlines()
POS = []
for line in doc:
	line = line.split("\",\"",)
	if len(line) <= 2:
		continue
	else: 
		linie = line[2]
	array = re.split(',|/', linie)
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