#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs

"""	The input file should have quotes (") as text qualifiers and commas (,) as field delimiters. """

f = codecs.open("russian.txt", "r")#input file
f2 = codecs.open("English-Russian.txt", "w")#output file
doc = f.read().split("\n")
#enter the PartsOfSpeech in this list AND in the check down below.
PartsOfSpeech = ['нареч.', 'pref.', 'мест.', 'прил.', 'межд.', 'предл.', 'г.', 'с.', 'art.']

"""format(): uses regular expressions to create standards for easier formatting
	then takes definitions and prints out one per line with the part of speech at the end of the line"""

def format():
	for i,line in enumerate(doc):
		#change the brackets / curly braces to parenthesis #and ; to , #and " to  '
		line = re.sub('\[|\{', '(', line)
		line = re.sub('\]|\}', ')', line)
		line = re.sub('\;', ',', line)
		line = re.sub('\"', '\'', line)
		line = line.rstrip('\'').rstrip()
		engword = line.split("\',\'")[0].replace("\'", "").split(' (')[0]
		#change all parenthesis to commas #perhaps there is a better way...
		line = re.sub('(?<!\,)(\ \()|(\)\ )((?!\,)(?!\'))', ', ', line)
		line = re.sub('[()]', '', line)
		entry = line.split("\',\'")[1].rstrip("\'")
		#enter the parts of speech in the lookaheads ***make sure that the period is an escape character***
		#this line checks for Parts of speech in the middle of the definition
		entry = re.split('(\ )((?=нареч\.)|(?=pref\.)|(?=мест\.)|(?=прил\.)|(?=межд\.)|(?=предл\.)|(?=г\.)|(?=с\.)|(?=art\.))', entry)
		entry = [i.rstrip().rstrip(",").rstrip(")") for i in entry]
		entry = filter(bool, entry)
		#checks for unecessary part of speech at the end of definition
		last = entry[len(entry) - 1]
		if last in PartsOfSpeech:
			entry.pop()
		#prints one definition per line
		for item in entry:
			defs = item.split(', ')
			defs = filter(bool, defs)
			pos = item.split()[0]
			if pos in PartsOfSpeech:
				temp = defs[0].split('. ')[1]
				defs.pop(0)
				defs = [temp] + defs
				for i in defs:
					definition = '\"%s\",\"%s\",\"%s\"\n' % (engword, i, pos)
					f2.write(definition)
			else:
				for i in defs:
					definition = '\"%s\",\"%s\",' % (engword, i)
		if engword == 'A-bomb':
			print 'appples are cool'
	
format()
f.close()
f2.close()