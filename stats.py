def count_words(text):
    return len(text.split())


def count_characters(text):
    character_dict = {}

    words = text.split()

    for word in words:
        for c in word.lower():
            if c in character_dict:
                character_dict[c] += 1
            else:
                character_dict[c] = 1

    return character_dict


def sort_on(items):
    return items["num"]


def sort_characters(character_dict):
    list = []

    for ch in character_dict:
        if ch.isalpha():
            list.append({"char": ch, "num": character_dict[ch]})

    list.sort(reverse=True, key=sort_on)

    return list
