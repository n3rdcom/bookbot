import sys
from stats import word_count, character_count, sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]


    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")

    # Read the file
    with open(book_path) as f:
        text = f.read()

    # Word count
    total_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")

    # Character count
    char_counts = character_count(text)
    sorted_chars = sort_characters(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

main()
