#Check if a Number is Even or Odd

a=int(input("enter your value: "))

if a % 2==0:
     print("Entered value is even")
else:
     print("entered value is odd")



#Task 2  Sum of Integers from 1 to 50 Using a Loop
  
a =int(input("enter your value: "))
total = 0
for i in range(1, a + 1):
    total += i

print("Your sum is:", total)
