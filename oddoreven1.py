def odd(a):
    if a % 2 == 0:
        print("no. is even")
    else:
        print("no. is odd")
try:
    n=int(input("enter num: "))
    c=odd(n)
except ValueError:
    raise ValueError("Enter a valid integer!!!!")
finally:
    print("thanks come again ")

