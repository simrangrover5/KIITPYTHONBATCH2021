"""This file is used to find the numbers divisible by other numbers"""
start = int(input("\n Enter any number : "))
end = int(input("\n Enter second number : "))
n1 = int(input("\n Enter number 1 : "))
n2 = int(input("\n Enter number 2 : "))
op = input("\n Enter operation and/or : ").strip().lower()
if op == "and":
    while start<=end:
        if start%n1==0 and start%n2==0:
            print(start)
        start += 1
elif op == "or":
    while start<=end:
        if start%n1==0 or start%n2==0:
            print(start)
        start += 1
else:
    print("\n INCORRECT OPTION")
