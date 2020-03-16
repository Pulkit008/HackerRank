def mutate_string(string, position, character):
    t=[x for x in string]
    t[position]=character
    return ''.join(t)
