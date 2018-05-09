# CHUONG I: BAI TAP MO DAU

# Bai 1

print('CHAO MUNG BAN DEN VOI MON HOC PYTHON')

# Bai 2

a = int(input('Ban hay nhap do dai canh: '))
for i in range(a):
    for j in range(a):
        print('*', end=' ')
    print('\n')

# Bai 3

from math import pi
from math import sqrt

r = float(input('Nhap ban kinh hinh tron: '))
print('Dien tich cua hinh tron:', pi*r*r)
print('Chu vi cua hinh tron: ', 2*pi*r)

S = float(input('Nhap dien tich hinh tron '))
print('Ban kinh hinh tron:', sqrt(S/pi))

# Bai 4

DayLon = float(input('Nhap day lon: '))
DayNho = float(input('Nhap day nho: '))
ChieuCao = float(input('Nhap chieu cao: '))

print('Dien tich hinh thang:', (DayLon+DayNho)*ChieuCao/2)

# Bai 5

import math

t = float(input('Moi ban nhap 1 so thuc t: '))
y = 3*math.exp(math.cos(t+1))
print('Gia tri cua bieu thuc can tinh la:', y)

# Bai 6

print('Ban hay nhap 2 so nguyen: ')
a = int(input('a = '))
b = int(input('b = '))
print('Tong cua 2 so vua nhap la:', a + b)
print('Hieu cua 2 so vua nhap la:', a - b)
print('Tich cua 2 so vua nhap la:', a * b)
if b != 0:
    print('Thuong cua 2 so vua nhap la:', a/b)

# Bai 7

MaSV = input('Nhap ma so sinh vien: ')
HoTen = input('Nhap ho ten sinh vien: ')
QueQuan = input('Nhap que quan: ')
NamSinh = input('Nhap nam sinh: ')
DiemTrungBinhCacNamHoc = input('Diem trung binh cac nam hoc: ')

print('Ma so sinh vien:', MaSV)
print('Ho ten:', HoTen)
print('Que quan:', QueQuan)
print('Nam sinh:', NamSinh)
print('Diem trung binh cac nam:', DiemTrungBinhCacNamHoc)

# Bai 8

from math import sqrt

print('Nhap do dai 3 canh cua 1 tam giac')
a = float(input('Nhap canh a: '))
b = float(input('Nhap canh b: '))
c = float(input('Nhap canh c: '))
p = (a+b+c)/2 # nua chu vi
print('Dien tich cua tam giac:', sqrt(p*(p-a)*(p-b)*(p-c)))

# Bai 9

print('Nhap toa do diem A:')
xa = float(input('Nhap xA: '))
ya = float(input('Nhap yA: '))
print('Nhap toa do diem B: ')
xb = float(input('Nhap xB: '))
yb = float(input('Nhap yB: '))
print('Toa do trung diem: (' + str((xa+xb)/2) + ', ' + str((ya+yb)/2) + ')')

# Bai 10

print('Nhap toa do diem A:')
xa = float(input('Nhap xA: '))
ya = float(input('Nhap yA: '))
print('Nhap toa do diem B: ')
xb = float(input('Nhap xB: '))
yb = float(input('Nhap yB: '))
print('Nhap toa do diem C: ')
xc = float(input('Nhap xC: '))
yc = float(input('Nhap yC: '))
print('Toa do trung diem: (' + str((xa+xb+xc)/3) + ', ' + str((ya+yb+yc)/3) + ')')

# Bai 11

a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
c = float(input('Nhap c: '))
x = float(input('Nhap x: '))
print('f=', a*x**2+b*x+c)

# Bai 12

# Bai tap nay khong the thuc hien bang Python

# CHUONG II: CAU TRUC DIEU KHIEN-CAU TRUC LAP

# Bai 13

N = int(input('Nhap N: '))
if N % 2 == 0:
    print('So chan')
else:
    print('So le')

# Bai 14

a = float(input('Nhap a: '))
b = float(input('Nhap b: '))

if a > b:
    print('Gia tri lon nhat:', a)
elif b > a:
    print('Gia tri lon nhat:', b)
else:
    print('Hai gia tri ban nhap vao bang nhau')

# Bai 15

A = input('Nguoi choi A ra: ')
B = input('Nguoi choi B ra: ')

if A == B:
    print('2 nguoi choi hoa nhau')
elif A == 'B' and B == 'O':
    print('B thang')
elif B == 'B' and A == 'O':
    print('A thang')
elif A == 'B' and B == 'K':
    print('A thang')
elif B == 'B' and A == 'K':
    print('B thang')
elif A == 'K' and B == 'O':
    print('A thang')
elif B == 'K' and A == 'O':
    print('B thang')

# Bai 16

luongcb = 650
tnct = float(input('Nhap tham nien cong tac: '))
heso = 0
if tnct < 12:
    heso = 1.92
elif tnct < 36:
    heso = 2.34
elif tnct < 60:
    heso = 3
else:
    heso = 4.5
luong = luongcb * heso
print('Luong:', luong)

# Bai 17

giobd = 7
giokt = 25
tien = 0
while giobd < 8 or giokt > 24 or (giobd >= giokt):
    giobd = int(input('Nhap gio bat dau: '))
    giokt = int(input('Nhap gio ket thuc: '))

thoigian = giokt - giobd
if thoigian > 3:
    tien = 3 * 30000 + (thoigian - 3) * 30000 * 0.7
else:
    tien = thoigian * 30000
if giokt <= 17:
    tien *= 0.9

print('Tien phai tra:', tien)

# Bai 18

day = int(input('Nhap ngay: '))
month = int(input('Nhap thang: '))
hople = False
if month > 12 or day > 31 or month < 1 or day < 1:
    print('Gia tri ban nhap khong hop le')
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print('Gia tri ban nhap hop le')
        print('Thang ban nhap co 31 ngay')
        hople = True
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 31:
            print('Gia tri ban nhap khong hop le')
        else:
            print('Gia tri ban nhap hop le')
            print('Thang ban nhap co 30 ngay')
            hople = True
    else: # month == 2
        if day <= 29:
            print('Gia tri ban nhap hop le')
            print('Thang ban nhap co 28 hoac 29 ngay')
            hople = True
        else:
            print('Gia tri ban nhap khong hop le')
if hople:
    if month < 4:
        print('Thang', month, 'thuoc quy 1')
    elif month < 7:
        print('Thang', month, 'thuoc quy 2')
    elif month < 10:
        print('Thang', month, 'thuoc quy 3')
    else:
        print('Thang', month, 'thuoc quy 4')

# Bai 19

a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
c = float(input('Nhap c: '))
minval = maxval = a
if b < minval:
    minval = b
elif b > maxval:
    maxval = b
if c < minval:
    minval = c
elif c > maxval:
    maxval = c
print('Gia tri lon nhat:', maxval)
print('Gia tri nho nhat:', minval)

# Bai 20

MyList = []
MyList.append(float(input('Nhap a: ')))
MyList.append(float(input('Nhap b: ')))
MyList.append(float(input('Nhap c: ')))
MyList.append(float(input('Nhap d: ')))
minval = maxval = MyList[0]

for i in range(1, MyList.__len__()):
    if MyList[i] < minval:
        minval = MyList[i]
    elif MyList[i] > maxval:
        maxval = MyList[i]
print('Gia tri lon nhat:', maxval)
print('Gia tri nho nhat:', minval)
