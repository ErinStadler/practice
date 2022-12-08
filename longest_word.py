def get_longest_word(words):
  longest_word = words[0]
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word
  
print(get_longest_word(['boo', 'a', 'I','hi']))
print(get_longest_word(['one', 'two', 'superduper','dog']))
print(get_longest_word(['hello', 'world']))
