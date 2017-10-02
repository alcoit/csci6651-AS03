wordsDict = {}
lettersDict = {}

def cleanupLine(line):
  """this function will remove characters that are not needed from the line-string. Unwanted characters are all characters except a-z, A-Z, 0-9 and ' and should be replaced with a space
      long-term -> long term
      It's amazing, isn't it? -> It's amazing  isn't it
      Note, if you are familiar with regex, you can use that, otherwise a loop is fine"""
  stripped_line = ""
  return stripped_line


def countWords(line):
  """For a stripped line, this function counts the words and updates
      the global variable wordsDict{}.
      Note, we convert upper case words to lower case words"""
  global wordsDict
  return wordsDict


def countLetters(line):
    """For a stripped line, this function counts the letters and updates
        the globla variable lettersDict{}.
        Note, we convert upper case letters to lower case
        Note2, numbers and ' should be ignored"""
    global lettersDict
    return lettersDict


def readFile(filename):
    handle = open(filename, 'r')
    for line in handle:
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)
        
def results():
  return [0,0,0,0,0,0]

readfile("text1.txt")
print(lettersDict['e'])
