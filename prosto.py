num = int(input('Введите год '))
print("YES" if not(num % 100 == 0) and num % 4 == 0 or num % 400 == 0 else "NO")