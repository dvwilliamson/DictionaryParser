#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

f = open('russian.txt', 'r')
f2 = open('Parts.txt' ,'w')

def remove_dups(a):
	b = []
	for everything in a:
		if everything not in b and everything is not '':
			b.append(everything)
	return b

doc = f.read().split('\n')
for line in doc:
	line = line.split("\",\"")[1]
	array = re.findall('(?<=\ )|(?<=^)(\S*?\.)', line)
	
	array = remove_dups(array)

	for item in array:
		if item is not '':
			f2.write(item + '\n')

f.close()
f2.close()