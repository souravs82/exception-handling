try:
    n = int(input("enter num: "))
    if n % 2 == 0:
        print("even number")
    else:
        print("odd number: ")
except ValueError:
    raise ValueError("please enter integer only!!!")
finally:
    print("thank you")


