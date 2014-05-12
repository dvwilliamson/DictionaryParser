#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
bob = codecs.open("bob.txt", 'w', 'utf-8')
with codecs.open("Parts.txt", "r", "utf-8") as f:
	doc = f.read().split('\n')
	doc = set(doc)
	doc = filter(bool, doc)
	for x in doc:
		bob.write(x)
		if x is not doc[len(doc) - 1]:
			bob.write('\n')
	bob.close()