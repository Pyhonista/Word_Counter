def word_counter(file_name, search_words):
  word_counts = {}
  with open(file_name, 'r') as file:
      for line in file:
          word = line.strip()
          if word in search_words:
              if word in word_counts:
                  word_counts[word] += 1
              else:
                  word_counts[word] = 1
  for word in search_words:
      if word in word_counts:
          print(f"{word} -> {word_counts[word]}")
      else:
          print(f"{word} -> 0")

search_words = ["Python", "C", "OOP", "Hello", "Java"]
word_counter("input.txt", search_words)
