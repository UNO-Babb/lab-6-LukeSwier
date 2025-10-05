#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  linecount = 0
  wordcount = 0
  charactercount = 0
  for line in textFile:
    linecount = linecount + 1
    words = line.split()
    for w in words:
      wordcount = wordcount + 1
    characters = list(line)
    for c in characters:
      charactercount = charactercount + 1
  print("Lines: ",linecount)  
  print("Words: ",wordcount)
  print("Characters: ",charactercount)
if __name__ == '__main__':
  main()
