import sys
import decimal

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
d1 = decimal.Decimal(sys.argv[1])
d2 = decimal.Decimal(sys.argv[2])

print('# 不使用 decimal')
print(f'{n1} + {n2} = {n1 + n2}')
print(f'{n1} - {n2} = {n1 - n2}')
print(f'{n1} * {n2} = {n1 * n2}')
print(f'{n1} / {n2} = {n1 / n2}')

print()  # 換行

print(f'{d1} + {d2} = {d1 + d2}')
print(f'{d1} - {d2} = {d1 - d2}')
print(f'{d1} * {d2} = {d1 * d2}')
print(f'{d1} / {d2} = {d1 / d2}')
