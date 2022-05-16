import math

n=int(input("How many students?: "))
corse=[]

for i in range(n):
    a=float(input("Enter grade: "))
    corse.append(a)

x=sum(corse)
ave=x/n
print("Average is: ", ave)

maximom= max(corse)
print("Max is: ", maximom)

minimom= min(corse)
print("Min is: ", minimom)
