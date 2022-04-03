R1=int(input("Enter R1 speed:"))
R2=int(input("Enter R2 speed:"))
R3=int(input("Enter R3 speed:"))
R4=int(input("Enter R4 speed:"))
R5=int(input("Enter R5 speed:"))
avg=(R1+R2+R3+R4+R5)//5
if R1>=avg:
    print("R1 is qualified")
if R2>=avg:
    print("R2 is qualified")
if R3>=avg:
    print("R3 is qualified")
if R4>=avg:
    print("R4 is qualified")
if R5>=avg:
    print("R5 is qualified")
