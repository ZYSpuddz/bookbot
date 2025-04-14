import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
print(f"Analyzing book: {book_path}")
def get_book_text(path) :
    with open(path) as f :
        file_contents = f.read()
    
        return file_contents

from stats import get_book_words

from stats import get_book_letters

from stats import sort

def main() :
    path = book_path
    text = get_book_text(path)
    num = get_book_words(path)
    charanum = get_book_letters(path)
    charalist = sort(charanum)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for char_dict in charalist:
        char = char_dict["char"]
        count = char_dict["count"]
    
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()