#repeats symbol or string n times
def str_repeat(ch, n):
    i = 0
    result = ''
    while i < n:
        result += ch
        i += 1
    return result

#formats dictionary for readability NEEDS IMPROVEMENT!
def format_dict(dictionary, depth=0):
    result = '{\n'
    keys = dictionary.keys()
    for key in keys:
        result += str_repeat(' ', depth+1) + key + ': ' 
        value = dictionary.get(key)
        if isinstance(value, dict):
            new_value = format_dict(value, depth+1)
            result += '\n' + str_repeat(' ', depth+1) + new_value + ',\n'
        else:
            result += str(value) + ',\n'
    result +=  '\n' + str_repeat(' ', depth) + '}'
    return result
            
            
