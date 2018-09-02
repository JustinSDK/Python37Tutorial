number = int(input('輸入數字：'))
half = number // 2
for num in range(2, half + 1):
    if number % num == 0:
        print(f'{number} 不是質數')
        break
else:
    print(f'{number} 是質數')