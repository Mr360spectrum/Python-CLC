def mathFun(x, y):
    if x.isdigit() and y.isdigit():
        num1 = x
        num2 = y
        total = int(num1) * int(num2)
        return total
    else:
        print("That is not a number.")

num1 = input("Enter a number")
num2 = input("Enter another number")

answer = mathFun(num1, num2)
print(num1)
print(num2)
print(answer)


