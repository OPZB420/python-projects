## Select integers from a string

s = input()
l = len(s)

i = 0
while i < l:
    num = ''
    symbol = s[i]
    while symbol.isdigit():
        num += symbol
        i += 1
        if i < l:
            symbol = s[i]
        else:
            break
    if num != '':
        print(num)
    i += 1