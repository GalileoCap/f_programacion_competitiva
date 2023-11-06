from random import randint
import sys

def getOccurrences(fpath, *, level = 1):
  totals = {}
  occurences = {}
    
  with open(fpath, 'r') as fin:
    for l in fin:
      parts = l.strip().split(sep = ' ')
      for i in range(len(parts)-level):
        prev, nxt = tuple(parts[i:i + level]), parts[i + level]

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
  print(totals, prev)
  if prev in totals:
    r = randint(1, totals[prev])
    for word, occs in occurences[prev].items():
      r -= occs
      if r <= 0:
        return word

def createSentence(totals, occurences,  seed, *, maxLen = 50, level = 1):
  sentence = list(seed)
  for i in range(maxLen):
    word = chooseWord(totals, occurences, tuple(sentence[-level:]))
    if word is None:
      break
    sentence.append(word)

  return ' '.join(sentence)

if __name__ == '__main__':
  level = int(sys.argv[1]) # Cantidad de palabras como semilla
  fpath = sys.argv[2] # Archivo de oraciones, una oración por linea.

  totals, occurences = getOccurrences(fpath, level = level)
  # print(getOdds(totals, occurences))
  print(createSentence(totals, occurences, getSeed(totals), level = level))
