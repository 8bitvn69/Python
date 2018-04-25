# Bai 1
for i in range(1, 101):
    print(str(i), end = "")
    if(i % 10 == 0):
        print(end = "\n")
        
# Bai 2
for i in range(1, 201):
    if i % 2 == 0:
        print("{:>3}".format(str(i)), end = " ")
        if(i % 20 == 0):
            print("")
            
# Bai 3
import math  
def KiemTraSoNguyenTo(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
        
    return True

print("Nhap so cua ban:", end = " ")
n = int(input())
b = KiemTraSoNguyenTo(n)
if b:
    print(str(n) + " la so nguyen to.")
else:
    print(str(n) + " khong la so nguyen to.")
    
# Bai 4
import math  
def KiemTraSoNguyenTo(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
        
    return True

def MyFunction():
    for i in range(1, 1001):
        if KiemTraSoNguyenTo(i):
            print("{:>4}".format(i))
            
MyFunction()
    
# Bai 5
def ConvertFromCtoF(n):
    return n * 1.8 + 32

print("Nhap gia tri do F:", end = " ")
F = input()
print(F, "F = ", ConvertFromCtoF(float(F)), "C")

# Bai 6
def ConvertFromFtoC(n):
    return (n - 32) / 1.8

print("Nhap gia tri do F:", end = " ")
C = input()
print(C, "C = ", ConvertFromCtoF(float(C)), "F")

# Bai 7
def ConvertKmToM(n):
    for i in range(0, len(n)):
        n[i] = 1000 * n[i]
        
MyList = [1, 2, 3, 4, 5, 6]
print(MyList)
ConvertKmToM(MyList)
print(MyList)

# Bai 8
def Factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * Factorial(n - 1)
    
print("Nhap so cua ban:", end = " ")
n = input()
print("Giai thua cua ", n, " la: ", Factorial(int(n)))
