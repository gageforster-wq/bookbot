

def character_count(text):

	characters = {}
	text_lower = text.lower()
	for c in text_lower:
		if c not in characters:
			characters[c] = 0
		characters[c] += 1
	return characters



def get_num_words(text):
	x = 0
	words = text.split()
	for w in words:
		x += 1
	return x


def sorter(items):
	return items["num"]

def sorted_list(char_count):
	sorted_char = []
	for letter in char_count:
		entry = {}
		char = char_count[letter]
		entry["char"] = letter
		entry["num"] = char
		sorted_char.append(entry)
	sorted_char.sort(reverse=True, key=sorter)
	return sorted_char
