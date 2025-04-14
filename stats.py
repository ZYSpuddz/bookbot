def get_book_words(path) :
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = 0
        for word in words :
            num_words += 1
    return num_words

def get_book_letters(path) :
    letters = {}
    with open(path) as f :
        file_contents = f.read()
        for char in file_contents :
            lowercase_char = char.lower()
            if lowercase_char in letters :
                letters[lowercase_char] +=1
            else:
                letters[lowercase_char] = 1
        return letters

def sort(char_dict) :
    char_list = []
    for char, count in char_dict.items() :
        char_list.append({"char": char, "count": count})
    def sort_on(dict) :
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)

    return char_list