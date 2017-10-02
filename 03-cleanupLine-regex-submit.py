import re
# dates are easily constructed and formatted
#from datetime import date
from datetime import datetime
now = datetime.today()
# print (now)
# print(now.strftime("%Y%m%d-%H%M%S"))

outfilename=now.strftime('%Y%m%d-%H%M%S') #set the output file name to include the date/time so it's always unique

handleout = open(outfilename, 'a') #create and open the new file as append

infilename = 'text3.txt' #set a variable which points to the input file
handlein = open(infilename, 'r') #opens file as read-only
linecount=0 #set the line counter to zero

for line in handlein:
# regex.sub https://docs.python.org/3/library/re.html
# reference for the regex filter
# https://regex101.com/r/AJygLR/2/
	newline=re.sub(r"([^A-Z|a-z|0-9|'|\s])", ' ', line) #line cleaner-upper
	handleout.write(newline) #write cleaned new to output file
#	print(newline, end="")
	
handlein.close() #close the input file
handleout.close() #close the output file
	
# print('line is {}'.format(type(line)))
# print('newline is {}'.format(type(newline)))
# print('outfilename is {}'.format(type(outfilename)))