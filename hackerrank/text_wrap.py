import textwrap

def wrap(string, max_width):
    ans = ''
    c = 0
    for s in string:
        ans += s
        c += 1
        
        if c % max_width == 0:
            ans+='\n'
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
