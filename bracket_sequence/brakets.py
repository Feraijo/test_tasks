## Write python code for verifying that brackets sequence is correct. E.g.: {[(}]) incorrect, {()[]} correct

def bracket_string_verify(s):    
    q = []
    dic = {
        '(': ')', 
        '{': '}', 
        '[': ']',
    }   
    for char in s:
        if char in dic:
            q.append(dic[char])
        elif char in dic.values():
            if not q or char != q.pop():
                # last opened bracket is not closing
                return 'incorrect'
    if q:
        # incomplete parentheses
        return 'incorrect'
    return 'correct'  

print(bracket_string_verify(input()))