number = int(input("Enter a number to see its multiplication table: "))
for n in range(1,11):
    result = n * number
    print(f"{number} * {n} = {result}")