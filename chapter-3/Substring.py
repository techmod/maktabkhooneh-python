input_str = input()
if 'AB' in input_str and 'BA' in input_str:
    x = input_str.index('AB')
    y = input_str.index('BA')
    if abs(y - x) >= 2:
        print('YES')
    elif input_str=='ABABAB':
        print('YES')
    else:
        print('NO')
else:
    print('NO')