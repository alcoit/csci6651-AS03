# import os woudn't work in REPL.IT!!!
import os
import re
# dates are easily constructed and formatted
#from datetime import date
from datetime import datetime
now = datetime.today()
counter=0
lettersDict = {}
wordsDict = {}


outfilename=now.strftime('%Y%m%d-%H%M%S') #set the output file name to include the date/time so it's always unique

handleout = open(outfilename, 'a') #create and open the new file as append

infilename1 = 'text3.txt' #set a variable which points to the input file
handlein1 = open(infilename1, 'r') #opens file as read-only
linecount=0 #set the line counter to zero

for line in handlein1:
# regex.sub https://docs.python.org/3/library/re.html
# reference for the regex filter
# https://regex101.com/r/AJygLR/2/
	newline=re.sub(r"([^A-Z|a-z|0-9|'|\s])", ' ', line) #line cleaner-upper
	current=0 				#counter is the position counter in the line
	linelength=len(newline)	#calculate line length
	while current < (linelength): #loop continuously until the condition is satisfied; like a for loop
#		newline.lower()	
		character=newline[current]
#		character.lower()
#		print(character)
		if character.isalpha(): #check if the item is a letter
			character=character.lower()
			if character in lettersDict:
				lettersDict[character]+=1 #increment the item count
			else:
				lettersDict[character]=1
#             lettersDict[character]+=1 #increment the item count
		current+=1 #increment the index (line position counter) #go to the next character
	linelength+=1
	handleout.write(newline) #write cleaned new to output file


	
handlein1.close() #close the input file
handleout.close() #close the output file

outfilename=now.strftime('%Y%m%d-%H%M%S')
infilename2 = outfilename #set a variable which points to the input file
# infilename2 = 'text2.txt' #set a variable which points to the input file
handlein2 = open(infilename2, 'r') #opens file as read-only
linecount=0 #set the line counter to zero

for line in handlein2:
	splitline=line.split(sep=None)
	splitlength=len(splitline)
	current=0
#	print(line, end="")
#	print(splitline)
#	print(splitlength)	
	while current < (splitlength):
		word=splitline[current]
		word=word.lower()
#		print(word)
		if word in wordsDict:
			wordsDict[word]+=1 #increment the item count
		else:
			wordsDict[word]=1
#		print(sorted(wordsDict.items())) #print list of item tuples
		current+=1 #increment the index (line position counter) #go to the next character
linecount+=1

handlein2.close() #close the input file
	
#print(sorted(lettersDict.keys()))
#print(sorted(lettersDict.values())) #print list of values
#print(sorted(lettersDict.items())) #print list of item tuples

print(sorted(wordsDict.keys()))
print(sorted(wordsDict.values())) #print list of values
print(sorted(wordsDict.items())) #print list of item tuples

