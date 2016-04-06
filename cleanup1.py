#!/usr/bin/env python
import re
from argparse import ArgumentParser
import stringcase


def getArgs():
	parser = ArgumentParser(description = 'Get Arguments')
	parser.add_argument("-f", "--file", required=True, dest="filename", help="file name to parse", metavar="FILE")
	args = parser.parse_args()
	filename = args.filename
	return filename

def openReadFile():
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

def nameScrub(text1, text2):
	"""
	takes irregularly formatted first and last names (e.g. BOB sMiTH), converts them to lowercase, 
	and converts them again to capital case (e.g. Bob Smith) using the stringcase library returning 
	a clean full name (e.g. Bob Smith)

	"""
	fname = text1
	lname = text2
	fname = stringcase.lowercase(fname)
	fname = stringcase.capitalcase(fname)
	lname = stringcase.lowercase(lname)
	lname = stringcase.capitalcase(lname)
	fullname = fname + " " + lname + ","
	return fullname


filename = getArgs()
dirtyline = openReadFile()


# the dictionary has target_word : replacement_word pairs
wordDic = {
'P.E.': '',
'/': '',
'CM': '',
'"': '',}

newline = ""

for dirtyline in dirtyline:
		clean1 = multiwordReplace(dirtyline, wordDic)
		#namematch = re.findall(r'([a-zA-Z]\w+)', clean1)#Full name
		#namematch = re.findall(r'\w*[,]', clean1) finds the lastname which is infront of the ,
		fullname = clean1.split(",")[0]
		lastname = fullname.split(",")[0].split()[-1]
		firstname = re.findall(r'([a-zA-Z]\w+)', fullname)[0]

		if lastname: #I'm using the first 2 elements of my list as first and last name; this works if there's a middle initial (e.g. bob p. smith, but not if there's a full middle name "Bob Pick Smith" )
				fullname = nameScrub(firstname, lastname)
				emailmatch = re.search(r'[\w.]+@[\w.-]+', clean1) #
				if emailmatch:
					print fullname, emailmatch.group()
		# 		else:
		# 			#print ""
		# else:
		# 	#print ""

				


