def count_words(text):
    text_split = text.split()
    print(f"{len(text_split)} words found in the document")

def count_chars(text):
    # each char in string -> add to dict and add counter
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sorted_on(items):
    return items["num"]

def sorted_list_dicts(dict):
    list_of_dicts = []
    for char in dict:
        init_dict = {}
        init_dict["char"] = char
        init_dict["num"] = dict.get(char)
        list_of_dicts.append(init_dict)
    list_of_dicts.sort(reverse=True, key=sorted_on)
    return list_of_dicts