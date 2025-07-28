def get_word_count(file_contents):
    return len(file_contents.split())

def get_char_count(file_contents):
    char_count = dict()
    for char in file_contents:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

def sort_char_count(char_count: dict):
    sorted_char_count = list()
    for key, value in char_count.items():
        sorted_char_count.append({"name": key, "num": value})
    sorted_char_count.sort(reverse=True, key=lambda x: x["num"])
    return sorted_char_count
