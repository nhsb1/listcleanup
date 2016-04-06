#!/usr/bin/env python
import re
from argparse import ArgumentParser
import stringcase


def get_args():
	parser = ArgumentParser(description = 'Get Arguments')
	parser.add_argument("-f", "--file", required=True, dest="filename", help="file name to parse", metavar="FILE")
	args = parser.parse_args()
	filename = args.filename
	return filename

def openandreadfile():
	global filename
	bigstring = open(filename)
	stringline = bigstring.readlines()
	bigstring.close()
	return stringline

def multiwordReplace(text, wordDic):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)

filename = get_args()
dirtyline = openandreadfile()


# the dictionary has target_word : replacement_word pairs
wordDic = {
'P.E.': '',
'/': '',
'CM': '',
'"': '',}

newline = ""

for dirtyline in dirtyline:
		clean1 = multiwordReplace(dirtyline, wordDic)
		namematch = re.findall(r'([a-zA-Z]\w+)', clean1)

		if namematch: #I'm using the first 2 elements of my list as first and last name; this works if there's a middle initial (e.g. bob p. smith, but not if there's a full middle name "Bob Pick Smith" )
				fname = namematch[0]
				lname = namematch[1]
				fname = stringcase.lowercase(fname)
				fname = stringcase.capitalcase(fname)
				lname = stringcase.lowercase(lname)
				lname = stringcase.capitalcase(lname)

				emailmatch = re.search(r'[\w.]+@[\w.-]+', clean1) #
				if emailmatch:
					fullname = fname + " " + lname + ","
					#newline = fullname, emailmatch.group()
					print fullname, emailmatch.group()
				else:
					print "**********2"
		else:
			print "*********1"

				


