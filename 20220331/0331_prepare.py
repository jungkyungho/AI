from numpy import kaiser


t1 = '네이스123'
t2 = '123123'
t3 = '!@#$'
t4 = '!@#1234'
t5 = 'wtf'
t6 = 'wtf1212'
t7 = '한글'
t8 = '한글!'
print(t1.isalnum())
print(t2.isalnum())
print(t3.isalnum())
print(t4.isalnum())
print(t5.isalnum())
print(t6.isalnum())
print(t7.isalnum())
print(t8.isalnum())


t = '!@@####%%^^&%%$%$%$네2232233#*이&^&{}스{{a'
t1 = '네이스'
t2 = '123123'
t3 = '!@#$'
check = ''
print(t.isalpha())
print(t1.isalpha())
print(t2.isalpha())
print(t3.isalpha())
for i in t:
    if i.isalpha():
        check += i
print(check)


a = 'BlockDMask'
b = '1234Blog'
c = '1231231'
d = '-234'
e = '1.23'
f = '2^2'
g = '%'
h = '2/3'
i = '0'
print(f"str.isdigit('{a}') : {str.isdigit(a)}")
print(f"str.isdigit('{b}') : {str.isdigit(b)}")
print(f"str.isdigit('{c}') : {str.isdigit(c)}")
print(f"str.isdigit('{d}') : {str.isdigit(d)}")
print(f"str.isdigit('{e}') : {str.isdigit(e)}")
print(f"str.isdigit('{f}') : {str.isdigit(f)}")
print(f"str.isdigit('{g}') : {str.isdigit(g)}")
print(f"str.isdigit('{h}') : {str.isdigit(h)}")
print(f"str.isdigit('{i}') : {str.isdigit(i)}")


a = '12343234'
print(a.isdigit())
print(a.isdecimal())
print(a.isnumeric())


a = 'I love Python'
print(a.islower())
print(a.isupper())
print(a.upper())
print(a.lower())


str = 'THIS is string example....wow!!!'
print(str.islower())
print(str.isupper())
str = 'this is string example...wow!!!'
print(str.islower())
str = 'this is string example...wow!!'
print(str.swapcase())
str = 'THIS IS STRING EXAMPLE...WOW!!'
print(str.swapcase())


str = 'THIS IS STRING EXAMPLE...WOW!!'
print(str.istitle())
str = 'this is string example...wow!!'
print(str.istitle())
print(str.title())


print('hello world!'.capitalize())


a = '        test!   '
b = '~~.test.~~'
c = '~test!'
print(a.lstrip())
print(a.rstrip())
print(a.rstrip(), end='.')
print(a.strip())
print(a.lstrip('t'))
print(b.lstrip('t'))
print(c.lstrip('t'))
print(a.rstrip('~'))
print(b.rstrip('~'))
print(c.rstrip('~'))
text = '000000000Water boils at 100 degrees 000'
print(text.lstrip('0'))
print(text.rstrip('0'))
print(text.strip('0'))
text = ',,,,,,,,123........water....pp'
print(text.lstrip('123.p'))
print(text.rstrip(',123.p'))
print(text.strip(',123.p'))


txt = '    Hz    '
x = txt.isspace()
print(x)


sentence = input('문자열을 입력하시오: ')
table = {"알파벳" : 0, '숫자' : 0, '빈칸' : 0}
for i in sentence:
    if(i.isalpha()):
        table['알파벳'] += 1
    elif(i.isdigit()):
        table['숫자'] += 1
    elif(i.isspace()):
        table['빈칸'] += 1
print(table)


s = '가나다라'
n = 7
answer = ''
for i in range(n-len(s)):
    answer += ''
answer += s
print(answer)

print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))


s = 'a b c d e f g'
print(f's        : {s}')
r = s.split()
print(f's.split( : {r}')


s = 'aa.bb.cc.dd.ee.ff.gg'
print(f's                       :{s}')
r0 = s.split()
r1 = s.split(':')
r2 = s.split(sep='.')
print(f"s.split()           : {r0}")
print(f"s.split('.')        : {r1}")
print(f"s.split(sep='.')    : {r2}")


s = 'aa.bb.cc.dd.BlockDMask.ee.ff.gg.python.example'
print(f'{s}')
r0 = s.split()
r1 = s.split('.', 3)
r2 = s.split(sep='.', maxsplit=4)
r3 = s.split('.',maxsplit=3)
print(f'\ns.split()\n{r0}')
print(f"\ns.split('.',3)\n{r1}")
print(f"\ns.split(sep='.',maxsplit=3)\n{r2}")
print(f"\ns.split('.',maxsplit=3)\n{r3}")


text = '123,456,789,999'
replaceALL = text.replace(",", "")
replace_t1 = text.replace(",", "", 1)
replace_t2 = text.replace(",", "", 2)
replace_t3 = text.replace(",", "", 3)
print('결과 : ')
print(replaceALL)
print(replace_t1)
print(replace_t2)
print(replace_t3)


txt = "홈짱닷컴\nHomezzang.com"
x = txt.splitlines()
print(x)
g = 'Milk\nChicken\r\nBread\rButter'
print(g.splitlines())
print(g.splitlines(True))
g = 'Milk Chicken Bread Butter'
print(g.splitlines())


a = ['a', 'b', 'c', 'd', '1', '2', '3']
print(a)
print()
result1 = ''.join(a)
print(result1)
result2 = ''
for v in a:
    result2 += v
print(result2)

print('3'.zfill(3))
print('s'.zfill(4))
x = 0
for x in range(3):
    print(str(x).zfill(4))


a = 'abc'
print(a.rjust(10))
print(a.rjust(10,'#'))
print(a.ljust(10))
print(a.ljust(10,'*'))


b = 'def'
print(b.ljust(15))
print(b.ljust(15,'k'))