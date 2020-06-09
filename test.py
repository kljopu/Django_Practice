
def reverse(x):
    s = str(x)
    result = ''
    if s.startswith('-'):
        s2 = s.replace('-', '')
        for v in s2:
            result = v + result
        result= '-'+result

        print(int(result))
    else:
        for v in s:
            result = v + result
        return int(result)
x =-1420
print(reverse(x))