row=int(input("Enter the amount of rows you want: "))
number=1
print("Floyd's Triangle")
for i in range(1, row+1):
    for j in range(1, i+1):
        print(number, end = ' ')
        number=number+1
    print()