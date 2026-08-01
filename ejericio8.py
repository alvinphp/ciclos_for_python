n = int(input("dame el numero divisor"))
for i in range(1,101):
    if i % n == 0:
        print(i,"es divisor")
    else:
        print(i,"no es divisor")
        