list1 = ['rich', 'richiest', 'orichalcum', 'cheers', 'richies']
list2 = ['Disablement', 'Able', 'Mable', 'Disable', 'Bagel']

def single_root_words (root_word, *other_words):
    same_words = []
    for word in other_words:
        root_word_lower = root_word.lower()
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words

result1 = (single_root_words('rich', *list1))
result2 = (single_root_words('Disablement', *list2))
print(result1)
print(result2)

print(single_root_words('ябл', "ябл", "яблоко", "груша", "яблочный"))

