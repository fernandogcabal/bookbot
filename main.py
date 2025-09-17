from stats import count_words, count_characters, set_response
import sys

def get_book_text(Path):
    with open((Path)) as f:
        file_content = f.read()
    return file_content


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_path= sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    words = count_characters(book_text)
    sorted_list = set_response(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")

main()
