# Bai 2

a = int(input('Ban hay nhap do dai canh: '))
for i in range(a):
    for j in range(a):
        print('*', end=' ')
    print('\n')

# Bai 8

from math import sqrt

print('Nhap do dai 3 canh cua 1 tam giac')
a = float(input('Nhap canh a: '))
b = float(input('Nhap canh b: '))
c = float(input('Nhap canh c: '))
p = (a+b+c)/2 # nua chu vi
print('Dien tich cua tam giac:', sqrt(p*(p-a)*(p-b)*(p-c)))

# Bai 29
# Cach 1

n = int(input('Nhap n: '))

temp = 1
if n % 2 == 0:
    # n chan    
    for i in range(2, n + 1, 2):
        temp *= i
else: # n le
    for i in range(1, n + 1, 2):
        temp *= i

print(str(n) + '!!=', temp)

# Cach 2
def GiaiThuaCach(n):
    if n < 2:
        return 1
    else:        
        return n * GiaiThuaCach(n - 2)

n = int(input('Nhap n: '))
result = GiaiThuaCach(n)
print(str(n) + '!!=', result)

# Bai 44
from math import fabs
x = int(input('Nhap x: '))

result = 0
temp = x
n = 3
while fabs(temp) >= 0.00001:
    result += temp
    temp *= -(x**2)/((n-1)*n)
    n += 2

print('sin(' + str(x) + ')=', result)

# Bai 49

def Fn(n):
    # n >= 3
    F1 = 1
    F2 = 2
    Temp = F1
    for i in range(3, n+1):
        Temp = F1
        F1 = F2
        F2 = 5*F1 + 3*Temp
    return F2

n = int(input('Nhap n: '))
result = Fn(n)
print('Phan tu thu', n, 'la', result)

# Bai 53

import numpy as np

# n = int(input('Nhap n: '))
def KhoiTaoMang(n):
    # Khoi tao mang
    MyArray = np.zeros(n)
    for i in range(n):
        MyArray[i] = np.random.randint(-100, 100)
    return MyArray
def InRaManHinh(MyArray):
    # Xuat mang ra man hinh
    print('Cac phan tu cua mang:')
    for item in MyArray:
        print(item, end=' ')
def FindMaxAndMin(MyArray):
    # Tim phan tu lon nhat va phan tu nho nhat cua mang
    MinVal = np.min(MyArray)
    MaxVal = np.max(MyArray)
    print('\nPhan tu lon nhat cua mang:', MaxVal)
    print('Phan tu nho nhat cua mang:', MinVal)
def FindItem(MyArray):
    # Tim va in ra phan tu am dau tien tan cung bang 6    
    for item in MyArray:        
        if (item < 0) and (item % 10 == 4):            
            return item
# Test = KhoiTaoMang(n)
# InRaManHinh(Test)
# FindMaxAndMin(Test)
# MyItem = FindItem(Test)
# print(MyItem)

def FindPosition(MyArray):
    # Tim va in ra vi tri phan tu duong nho nhat    
    MinVal = None
    Pos = None
    i = 0
    for item in MyArray:
        if item > 0:
            if MinVal == None:
                MinVal = item
                Pos = i
            elif item < MinVal:
                MinVal = item
                Pos = i
        i += 1
    return Pos

# MinVal = FindPosition(Test)
# print(MinVal)

def TongCuaMang(MyArray):
    # Tinh tong cua mang
    return np.sum(MyArray)

# print(TongCuaMang(Test))

def TrungBinhCong(MyArray):
    # Tinh trung binh cong cua mang
    return np.mean(MyArray)

# print(TrungBinhCong(Test))

def TimKiem(MyArray):
    # Nhap x
    x = int(input('Nhap x:'))

    # Tim kiem phan tu x cho truoc (x nhap tu ban phim)
    for i in range(len(MyArray)):
        if MyArray[i] == x:
            return i

# print(TimKiem(Test))

def SapXepTangDan(MyArray):
    # Sap xep mang theo thu tu tang dan
    temp = np.array(MyArray, copy=True)
    temp.sort()
    return temp

def SapXepGiamDan(MyArray):
    # Sap xep mang theo thu tu giam dan
    temp = np.array(MyArray, copy=True)
    temp[::-1].sort()
    return temp

# print(SapXepTangDan(Test))
# print(Test)
# print(SapXepGiamDan(Test))
# print(Test)

def XuatDayDaoNguoc(MyArray):
    # Xuat day dao nguoc cua day ban dau
    print(MyArray[::-1])

# XuatDayDaoNguoc(Test)
# print(Test)

def BoSung(MyArray):
    # Them mot phan tu x vao vi tri k (x, k nhap tu ban phim)
    x = float(input('\nNhap x: '))
    k = int(input('\nNhap k: '))
    Prefix = np.array(MyArray[:k], copy=True)
    Suffix = np.array(MyArray[k:], copy=True)
    result = np.append(Prefix, x)
    result = np.append(result, Suffix)
    return result

# print(BoSung(Test))

def LoaiBo(MyArray):
    # Huy mot phan tu o vi tri thu k
    k = int(input('\nNhap k: '))
    Prefix = np.array(MyArray[:k], copy=True)
    Suffix = np.array(MyArray[k+1:], copy=True)
    result = np.append(Prefix, Suffix)
    return result

# print(LoaiBo(Test))

def DemSoPhanTuDuongVaInTong(MyArray):
    # Dem so phan tu duong va in ra tong cac phan tu duong cua mang
    Tong = 0
    Dem = 0
    for item in MyArray:
        if item > 0:
            Tong += item
            Dem += 1
    print('\nSo phan tu duong:', Dem, '\nTong cac phan tu duong cua mang:', Tong)

# DemSoPhanTuDuongVaInTong(Test)

def KiemTraDoiXung(MyArray):
    # Kiem tra mang co doi xung hay khong
    KichThuocMang = len(MyArray)
    for i in range(KichThuocMang//2):
        if MyArray[i] != MyArray[KichThuocMang - i - 1]:
            return False
    return True

# if KiemTraDoiXung(Test):
#     print('\nMang doi xung')
# else:
#     print('\nMang khong doi xung')

def KiemTraTangDan(MyArray):
    # Kiem tra mang co sap xep theo thu tu tang hay khong
    temp = MyArray[0]
    KichThuocMang = len(MyArray)
    for i in range(1, KichThuocMang):
        if temp > MyArray[i]:
            return False
        temp = MyArray[i]
    return True

# if KiemTraTangDan(Test):
#     print('\nMang duoc sap xep theo thu tu tang')
# else:
#     print('\nMang khong duoc sap xep theo thu tu tang')

# Bai 60

from math import fabs
from math import sqrt

class DIEM:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TAMGIAC:
    def __init__(self):
        self.A = DIEM(0, 0)
        self.B = DIEM(0, 0)
        self.C = DIEM(0, 0)

    def Nhap(self, x1, y1, x2, y2, x3, y3):
        self.A = DIEM(x1, y1)
        self.B = DIEM(x2, y2)
        self.C = DIEM(x3, y3)
    
    def Xuat(self):
        pass

    def TinhDienTich(self):
        DienTich = (1/2)*fabs((self.B.x - self.A.x)*(self.C.y - self.A.y) - (self.C.x - self.A.x)*(self.B.y - self.A.y))
        return DienTich
    def TinhChuVi(self):
        DoDaiCanhAB = sqrt((self.A.x - self.B.x)**2 + (self.A.y - self.B.y)**2)
        DoDaiCanhAC = sqrt((self.A.x - self.C.x)**2 + (self.A.y - self.C.y)**2)
        DoDaiCanhBC = sqrt((self.B.x - self.C.x)**2 + (self.B.y - self.C.y)**2)
        return DoDaiCanhAB + DoDaiCanhAC + DoDaiCanhBC

    def TimTrongTam(self):
        return DIEM((self.A.x + self.B.x + self.C.x)/3, (self.A.y + self.B.y + self.C.y)/3)

print('Nhap toa do diem A:')
x1 = float(input('Nhap toa do x1: '))
y1 = float(input('Nhap toa do y1: '))
print('Nhap toa do diem B:')
x2 = float(input('Nhap toa do x2: '))
y2 = float(input('Nhap toa do y2: '))
print('Nhap toa do diem C:')
x3 = float(input('Nhap toa do x3: '))
y3 = float(input('Nhap toa do y3: '))

_TamGiac = TAMGIAC()
_TamGiac.Nhap(x1, y1, x2, y2, x3, y3)
DienTichTamGiac = _TamGiac.TinhDienTich()
print('Dien tich tam giac la:', DienTichTamGiac)
ChuViTamGiac = _TamGiac.TinhChuVi()
print('Chu vi tam giac la:', ChuViTamGiac)
ToaDoTrongTam = _TamGiac.TimTrongTam()
print('Toa do trong tam: G({0}, {1})'.format(ToaDoTrongTam.x, ToaDoTrongTam.y))

# Bai 61

class SoPhuc:
    def __init__(self, PhanThuc, PhanAo):
        self.PhanThuc = PhanThuc
        self.PhanAo = PhanAo
    def Nhap(self, PhanThuc, PhanAo):
        self.PhanThuc = PhanThuc
        self.PhanAo = PhanAo
    def Xuat(self):
        print('Gia tri cua so phuc: {0} + {1}i'.format(self.PhanThuc, self.PhanAo))

def Tong(x : SoPhuc, y : SoPhuc):
    return SoPhuc(x.PhanThuc + y.PhanThuc, x.PhanAo + y.PhanAo)
def Hieu(x : SoPhuc, y : SoPhuc):
    return SoPhuc(x.PhanThuc - y.PhanThuc, x.PhanAo - y.PhanAo)
def Tich(x : SoPhuc, y : SoPhuc):
    return SoPhuc(x.PhanThuc * y.PhanThuc - x.PhanAo * y.PhanAo, x.PhanThuc * y.PhanAo + y.PhanThuc * x.PhanAo)
def Thuong(x : SoPhuc, y : SoPhuc):
    PhanThuc = (x.PhanThuc * y.PhanThuc + x.PhanAo * y.PhanAo) / (y.PhanThuc ** 2 + y.PhanAo ** 2)
    PhanAo = (y.PhanThuc * x.PhanAo - x.PhanThuc * y.PhanAo) / (y.PhanThuc ** 2 + y.PhanAo ** 2)
    return SoPhuc(PhanThuc, PhanAo)
def LuyThua(x : SoPhuc, n):
    result = SoPhuc(1, 0)
    for i in range(n):
        result = Tich(result, x)
    return result

print('Nhap so phuc x:')
xPhanThuc = float(input('Nhap phan thuc: '))
xPhanAo = float(input('Nhap phan ao: '))
print('Nhap so phuc y:')
yPhanThuc = float(input('Nhap phan thuc: '))
yPhanAo = float(input('Nhap phan ao: '))
x = SoPhuc(xPhanThuc, xPhanAo)
y = SoPhuc(yPhanThuc, yPhanAo)
TongXvaY = Tong(x, y)
HieuXvaY = Hieu(x, y)
TichXvaY = Tich(x, y)
ThuongXvaY = Thuong(x, y)
n = int(input('Nhap n: '))
LuyThuaXvaN = LuyThua(x, n)
print('Tong x va y: {0} + {1}i'.format(TongXvaY.PhanThuc, TongXvaY.PhanAo))
print('Hieu x va y: {0} + {1}i'.format(HieuXvaY.PhanThuc, HieuXvaY.PhanAo))
print('Tich x va y: {0} + {1}i'.format(TichXvaY.PhanThuc, TichXvaY.PhanAo))
print('Thuong x va y: {0} + {1}i'.format(ThuongXvaY.PhanThuc, ThuongXvaY.PhanAo))
print('Luy thua x va n: {0} + {1}i'.format(LuyThuaXvaN.PhanThuc, LuyThuaXvaN.PhanAo))

# Bai 68

def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k) + C(n-1, k-1)

n = int(input('Nhap n: '))
k = int(input('Nhap k: '))

print('C(' + str(n) + ', ' + str(k) + ')=', C(n, k))

# Bai 71

MyFile = open(r'INPUT.txt', 'r')
MyTable = MyFile.readlines()
MyFile.close()
temp = MyTable[0].split()
n = int(temp[0])
print(n)
MyMat = []
for i in range(1, len(MyTable)):
    MyMat.append([])
    temp = MyTable[i].split()
    for item in temp:
        if str.isdigit(item):
            MyMat[-1].append(int(item))
MyNewMat = np.array(MyMat)
try:
    if MyNewMat.shape[0] == n and MyNewMat.shape[1] == n:
        print('Du lieu hop le')
    else:
        print('Du lieu khong hop le')
except:
    print('Du lieu khong hop le')

def KiemTraTong(MyMat, n):
    CacTongHang = []
    CacTongCot = []

    for i in range(n):
        temp = MyMat[i, :]
        CacTongHang.append(np.sum(temp))
        temp = MyMat[:, i]
        CacTongCot.append(np.sum(temp))
    
    Tong = CacTongHang[0]
    for i in range(n):
        if (CacTongHang[i] != Tong) or (CacTongCot[i] != Tong):
            return False

    return True

# if KiemTraTong(MyNewMat, n):
#     print('Tong cac phan tu tren tung hang va tren tung cot bang nhau')
# else:
#     print('Tong cac phan tu tren tung hang va tren tung cot khong bang nhau')