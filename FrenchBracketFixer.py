#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs

f = codecs.open("English-French.txt", 'r')
document = []
doc = f.read().split('\n')
for l in doc:
	line = l.rstrip('\"').rstrip(']').rstrip().rstrip('&').rstrip() + '\"'
	document.append(line)
f.close()
f = codecs.open("English-French.txt", 'w')
for item in document:
	f.write(item)
	if item is not document[len(document) - 1]:
		f.write('\n')
f.close()