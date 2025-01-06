pattern = int(input("Enter the size of the pattern: "))
i = 0
while i < pattern:
    for e in range(1,pattern+1):
        print("*", end="")
    i=i+1
    print()
