def swap_case(s):
    new_str = ''
    for c in s:
        if c.islower():
            new_str += c.upper()
        else:
            new_str += c.lower()
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
