import sys
from stats import get_num_words, character_count, sorted_list




def get_book_text(path):
        with open(path) as f:
                file_content = f.read()
        return file_content



def main():

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book = sys.argv[1]
	with open(book) as f:
		text = f.read()
	words = get_num_words(text)
	letters = character_count(text)
	sorted_letters = sorted_list(letters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print("----------- Word Count ----------")
	print("Found",words,"total words")
	for word in sorted_letters:
		if word["char"].isalpha() == True:
			print(f"{word['char']}: {word['num']}")
	print("============= END ===============")





main()



