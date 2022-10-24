n = int(input('Nhap n = '))

# a)
print(('*'*n + '\n')*n)

# b)
for i in range(1, n+1):
    print('*'*i)

# c)
for i in range(1, n + 1):
    print(' '*(n-i) + '*' * i)

# d)
for i in range(1, n+1, 2):
    print(('*'*i).center(n))
