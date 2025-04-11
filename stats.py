def number_of_words(a):
    word_count = len(a.split())
    return word_count

def character_count(b):
    b = b.lower()
    characters = {}
    for char in b:
        if char in characters:
            characters[char] +=1
        else:
            characters[char] = 1
    return characters

def sorted_characters(c):
    sorted = []
    for char, count in c.items():
        sorted.append({"char": char, "count": count})
    def sort_on(d):
        return d["count"]
    sorted.sort(reverse=True, key=sort_on)
    return sorted



