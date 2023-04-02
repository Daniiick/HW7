s = input('Hello! ')

s = s.lower()
if s in['hello']:
    print('$0')
elif s.startswith('h'):
    print('$20')
else:
    print('$100')


