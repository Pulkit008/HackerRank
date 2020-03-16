def count_substring(string, sub_string):
    c = 0
    length = len(string)
    index = 0
    while index < length:
        x = string.find(sub_string, index)
        if x == -1:
            return c
        c+=1
        index = x + 1
    return c
