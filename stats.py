def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c.isalpha():
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
    return chars

def sort_characters_by_frequency(char_dict):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)