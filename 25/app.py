def break_words(stuff):
  """this function will break up words for us"""
  words = stuff.split(' ')
  return words

def sort_words(words):
  """sorts the words."""
  return sorted(words)

def print_first_word(words):
  word = words.pop(0)
  print word

def print_last_word(words):
  word = words.pop(-1)
  print word

def sort_sentence(sentence):
  """takes a full sentence and returns the sorted words."""
  return sort_words(words)

def print_first_and_last(sentence):
  """prints the first and last words of the sentence."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)
