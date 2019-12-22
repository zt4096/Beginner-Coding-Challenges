
# Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. 
# If so, return true, otherwise return false.

s = '?a?b1236???4'
q = '???'
if q in s:
    for i in s:
        ix = int(s[s.find(q) - 1])
        iy = int(s[s.find(q) + 3])
    if ix + iy == 10:
        print('True')
    else:
        print('False')
else:
    print('Question marks not found.')
