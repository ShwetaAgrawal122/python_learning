for x in range (2,5):
    print(x)

16*5
print(16*5)

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therfore, x/y is", x/y)

elif x < y :
    print("x is smaller")
elif x > y :
    print("x is greater")
print("Thanks")


num = int(input("Enter a number..."))
if num % 2 == 0:
    print("Number is equal")
else:
    print("Number is Odd")

n = input("You are in the Lost Forest\n*******"
          "**\n*********\n*********\n:)\n*********\n*********\nGo "
          "left or right?")

while n == "right" or n == "Right":
    n = input("You are in the lost Forest\n****\n :(\n****\
               \nGo left or right? ")

print("\n You got out of the Lost forest!")

for n in range(5):
    print(n)

mysum = 0
for i in range(10):
    mysum += i
print(mysum)

mysum = 0
for i in range(7,10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i

    if mysum == 5:
        mysum += 1
print(mysum)

ans = 0
neg_flag = False
x = int(input("Enter an float: "))
if x < 0:
    neg_flag = True

while ans**2 < x:
    ans=ans+1
if ans**2 == x:
    print("square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("just checking... did you mean", -x, "?")




