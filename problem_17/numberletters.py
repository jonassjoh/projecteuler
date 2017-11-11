def letters(n):
    # 999 = nine hundred ninety-nine
    pre = [['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
           ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],
           ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
           , 'hundred', 'thousand']

    n = str(n)

    if len(n) == 0:
        return ''

    if int(n[0]) == 0:
        return letters(n[1:])

    if len(n) == 1:
        return pre[0][int(n)-1]

    if len(n) == 2:
        if int(n[0]) == 1:
            return pre[1][int(n[1])]
        return pre[2][int(n[0])-2] + ('' + pre[0][int(n[1])-1] if int(n[1]) != 0 else '')

    suf = letters(n[1:])
    if suf != '':
        suf = 'and'+suf
    return pre[0][int(n[0])-1] + '' + pre[len(n)] + suf

s = 0
for i in range(1, 1001):
    s += len(letters(i))

print(s)
