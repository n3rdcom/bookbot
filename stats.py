def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1

    return counts

def get_count(entry):
    return entry["num"]

def sort_characters(counts):
    sorted_chars = [{"char": char, "num": count} for char, count in counts.items()]
    sorted_chars.sort(key=get_count, reverse=True)
    return sorted_chars
