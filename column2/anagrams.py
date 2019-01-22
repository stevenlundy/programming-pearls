DICTIONARY_FILE = "/usr/share/dict/words"

def get_signature(word):
    letters = sorted(word.lower())
    return "".join(letters)

def find_anagrams(dictionary_file, max_length=8):
    with open(dictionary_file) as d:
        words_with_signature = [(word, get_signature(word)) for word in d if len(word) <= max_length]
    words_with_signature.sort(key=lambda t: t[1])  # sort by signature
    current_signature = None
    anagram_sets = []
    for word, signature in words_with_signature:
        if signature == current_signature:
            anagram_sets[-1].append(word)
        else:
            anagram_sets.append([word])
            current_signature = signature
    anagram_sets = [anagrams for anagrams in anagram_sets if len(anagrams) > 1]
    return anagram_sets

print find_anagrams(DICTIONARY_FILE)
