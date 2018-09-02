def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

print('輸入兩個數字...')

m = int(input('數字 1: '))
n = int(input('數字 2: '))

r = gcd(m, n)
if r == 1:
    print('互質')
else:
    print(f'最大公因數：{r}')