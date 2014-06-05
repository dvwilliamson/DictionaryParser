#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs
import os

f = codecs.open('resources/English-Japanese.txt', 'r', 'utf-8')
f2 = codecs.open('resources/full_dictionary_POS.txt' ,'w+', 'utf-8')

doc = f.read().split('\n')
definitions = []
pos = []
for line in doc:
	definitions.append(line.split("\",\"")[1])
for line in definitions:
	pos.append(line.split(')')[0])
	if not not pos[len(pos)-1].find('('):
		pos.pop()
	else:
		pos[len(pos)-1] = pos[len(pos)-1].strip('(')

pos = set(pos)
for e in pos:
	if len(e) is 1:
		f2.write(e + '\n')

f.close()
f2.close()