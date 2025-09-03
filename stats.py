def get_num_words(text):
    num_words = 0
    for word in text.split():
        num_words+=1
    return num_words

def count_characters(text):
    character_count = {}
    for word in text.lower().split():
        for char in word:
            if char in character_count:
                c = character_count[char]
                c +=1
                character_count[char] = c
            else:
                character_count[char] = 1
    return character_count 


def sort_dictionarys(d):
    dict_list = []
    def sort_on(items):
        return items["num"]
    for k,v in d.items():
        empty_dict = {}
        empty_dict["char"] = k
        empty_dict["num"] = v
        dict_list.append(empty_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

