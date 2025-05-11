def word_count(passage):
    text = passage.split()
    return len(text)

def char_count(passage):
    char_dict = {}
    for char in passage:
        if char.isalpha() == False:
            continue
        if char.lower() in char_dict.keys():
            char_dict[char.lower()] += 1

        else:
            char_dict[char.lower()] = 1

    return char_dict

def sort_on(dict):
    return dict['num']

def sort_dict(passage_dict):
    dict_lst = []
    for key, value in passage_dict.items():
        dict_lst.append({"char": key, "num": value})
    dict_lst.sort(reverse=True, key=sort_on)
    return dict_lst 
