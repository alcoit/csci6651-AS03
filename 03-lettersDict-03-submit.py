# import os woudn't work in REPL.IT!!!
import os
import re
# dates are easily constructed and formatted
#from datetime import date
from datetime import datetime
now = datetime.today()
counter=0
lettersDict = {}

outfilename=now.strftime('%Y%m%d-%H%M%S') #set the output file name to include the date/time so it's always unique

handleout = open(outfilename, 'a') #create and open the new file as append

infilename = 'text2.txt' #set a variable which points to the input file
handlein = open(infilename, 'r') #opens file as read-only
linecount=0 #set the line counter to zero

for line in handlein:
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
		current+=1 #increment the index (line position counter) #go to the next character
	linelength+=1
	handleout.write(newline) #write cleaned new to output file

	
handlein.close() #close the input file
handleout.close() #close the output file
	
print(sorted(lettersDict.keys()))
print(sorted(lettersDict.values())) #print list of values
print(sorted(lettersDict.items())) #print list of item tuples
