# replace words in a text that match key_strings in a dictionary with the given value_string
# Python's regular expression module  re  is used here
# tested with Python24       vegaseat      07oct2005
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
# call the function and get the changed text

newline = ""

for dirtyline in dirtyline:
		#newline = newline + str101.replace("/", "")
		#newline = newline + multiwordReplace(str101, wordDic)
		print "Dirty line: "  + dirtyline
		clean1 = multiwordReplace(dirtyline, wordDic)
		print "Clean line: " + clean1
		newline = newline + clean1
print newline