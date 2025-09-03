from stats import get_num_words, count_characters, sort_dictionarys
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path):
    book_text = get_book_text(path)
    dict_list = sort_dictionarys(count_characters(book_text))
    def dict_to_report(dct_list):
        lines = []
        for i in dct_list:
            if i["char"].isalpha():
                lines.append(f"{i["char"]}: {i["num"]}")
        return "\n".join(lines)

                              
    report = f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {get_num_words(book_text)} total words
--------- Character Count -------
{dict_to_report(dict_list)}
============= END ===============
    """
    return report


def main(path):
    return print(print_report(path))

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])


