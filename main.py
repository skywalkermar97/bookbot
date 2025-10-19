import sys
from stats import get_book_text

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    length_of_words, char_count = get_book_text(sys.argv[1])
    print(f"Found {length_of_words} total words")
    for count in char_count:
      if count["char"].isalpha():
        print(f'{count["char"]}: {count["num"]}')

main()