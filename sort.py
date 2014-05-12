#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open("russian.txt", 'r+')

doc = f.read().split('\n')

doc.sort(key=str.lower)
doc = filter(bool, doc)
f.close()
f = open("russian.txt", 'w')
for line in doc:
	f.write(line)
	if line is not doc[len(doc) - 1]:
		f.write('\n')
f.close()