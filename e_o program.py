num = int(input("Enter a number: "))
if num<0:
    print("Negative")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")