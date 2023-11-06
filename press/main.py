from random import randint
import sys

def getOccurrences(fpath):
  totals = {}
  occurences = {}
    
  with open(fpath, 'r') as fin:
    for l in fin:
      parts = l.strip().split(sep = ' ')
      for i in range(len(parts)-1):
        prev, nxt = parts[i], parts[i+1]

        foo = occurences.get(prev, {})
        foo[nxt] = foo.get(nxt, 0) + 1
        occurences[prev] = foo
        totals[prev] = totals.get(prev, 0) + 1

  return totals, occurences

def getOdds(totals, occurences):
  odds = {w: {} for w in totals.keys()}
  for prev, nxts in occurences.items():
    for nxt in nxts:
      odds[prev][nxt] = occurences[prev][nxt] / totals[prev]
  
  return odds

def getSeed(totals):
  T = sum([x for _, x in totals.items()])
  r = randint(1, T)
  for word, x in totals.items():
    r -= x
    if r <= 0:
      return word

def chooseWord(totals, occurences, prev):
  if prev in totals:
    r = randint(1, totals[prev])
    for word, occs in occurences[prev].items():
      r -= occs
      if r <= 0:
        return word

def createSentence(totals, occurences, start, maxLen = 50):
  sentence = [start]
  for i in range(maxLen):
    word = chooseWord(totals, occurences, sentence[-1])
    if word is None:
      break
    sentence.append(word)

  return ' '.join(sentence)

if __name__ == '__main__':
  fpath = sys.argv[1] # Archivo de oraciones, una oración por linea.

  totals, occurences = getOccurrences(fpath)
  # print(getOdds(totals, occurences))
  print(createSentence(totals, occurences, getSeed(totals)))
