from pathlib import Path
import sys

from stats import word_count, char_count, sort_dict

def get_book_text(path):
    
    path = Path(path)
    contents = path.read_text()

    return contents


def main():
    if len(sys.argv) < 2: 
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('===== BOOKBOT =====')
    text = get_book_text(sys.argv[1])
    print(f'Analyzing book found at {sys.argv[1]}...')
    
    word_total = word_count(text)
    print('---------- Word Count ----------')
    print(f'Found {word_total} total words')
    
    print('--------- Character Count ---------')
    char_chart = char_count(text)
    list_chart = sort_dict(char_chart)
    for item in list_chart:
        print(f'{item['char']}: {item['num']}')

main()
