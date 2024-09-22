a = 13
b = 18
c = b-a
d = a+c
e = b-c

print(f"b-a={c}")
print(f'a+c={d}')
print(f'b-c={e}')
print(f'a > b:{a>b}')
print(f'd < b:{d<b}')
print(f'd == e:{d==e}')

a = 5
b = 2
c = b*a
d = a*a
e = b*b

print("b*a= ",c)
print(f'd*b != e*a={(d*b)!=(e*a)}')
print(f'{d*b}')
print(e*a)

x = 64
while x > 2:
    print(x)
    x = int(x/2)