def calculations(No1, No2):
   Add = No1 + No2
   Sub = No1 - No2
   return Add, Sub

print("Enter First Number : ")
A = int(input())

print("Enter Second Number : ")
B = int(input())

Result1, Result2 = calculations(A,B)

print("Addition is : ",Result1)
print("Substraction is : ",Result2)


