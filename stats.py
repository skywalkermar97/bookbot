def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  words = file_contents.split()
  charCount = sorted_char_count(char_count(file_contents))
  return len(words), charCount

def char_count(chars):
  countDict = {}
  for char in chars:
    if char.lower() in countDict:
      countDict[char.lower()] = countDict[char.lower()] + 1
    else:
      countDict[char.lower()] = 1
  return countDict



def sort_on(items):
  return items["num"]


def sorted_char_count(char_count):
  listOfCounts = []
  for count in char_count:
    listOfCounts.append({"char": count, "num": char_count[count]})
  listOfCounts.sort(reverse=True, key=sort_on)
  return listOfCounts