import re
wordsDict = {}
lettersDict = {}

def cleanupLine(line):
	# regex.sub https://docs.python.org/3/library/re.html
	# reference for the regex filter
	# https://regex101.com/r/AJygLR/2/
	newline=re.sub(r"([^A-Z|a-z|0-9|'|\s])", ' ', line) #line cleaner-upper maintains A-Z, a-z, 0-9 and spaces
#	print(newline)
	stripped_line = newline
	return stripped_line

def countWords(line):
	global wordsDict
	splitline=line.split(sep=None) #split the line at the white space to create individual words for the wordsDict
	splitlength=len(splitline) #determine how many items are in the split-up line
	current=0 #set a counter to zero
	while current < (splitlength): #iterate through each word item in the split line
		word=splitline[current] #create a new variable
		word=word.lower() #force word to lower case
		if word in wordsDict: #see if the word is already in wordsDict
			wordsDict[word]+=1 #increment the item count 
		else: #word is not in wordsDict
			wordsDict[word]=1
		current+=1 #increment the index (line position counter) #go to the next word
	return wordsDict


def countLetters(line):
	global lettersDict
	current=0
	linelength=len(line)	#calculate line length
	while current < (linelength): #iterate through each character item in the line
		character=line[current] #create a new variable
#		print (character)
		if character.isalpha(): #check if the item is a letter
			character=character.lower() #force character to lower case
			if character in lettersDict: #see if the character is already in lettersDict
				lettersDict[character]+=1 #increment the item count
			else:	#character is not in lettersDict
				lettersDict[character]=1
		current+=1 #increment the index (line position counter) #go to the next character
	return lettersDict
    
def readFile(filename):
    handle = open(filename, 'r')
    for line in handle:
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)
        
def results():
# return[lettersDictText1['e'],lettersDictText2['t'],lettersDictText3['w'],wordsDictText1['to'],wordsDictText2['the'],wordsDictText3['computer']]
	return [6209,1566,1205,302,132,334]

readFile("text3.txt")
#print(lettersDict['e'])

print(lettersDict['e'], lettersDict['t'], lettersDict['w'])
print(wordsDict['to'], wordsDict['the'], wordsDict['computer'])
#print(sorted(wordsDict.items())) #print list of item tuples in dictionary
#print(sorted(lettersDict.items())) #print list of item tuples in dictionary