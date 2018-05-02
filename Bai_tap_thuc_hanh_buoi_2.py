# Bai 9
def Convert_Decimal_to_Binary(n):
    if n == 0:
        return
    else:
        Convert_Decimal_to_Binary(n // 2)
        print(str(n % 2), end = '')        

# Bai 10
def myMap(fn, C):
    newC = []
    for x in C:
        newC.append(fn(x))
    return newC

MyList = [1, 2, 3]
print(myMap(lambda x: x**2 + 3, MyList))

# Bai 11
def myReduce(fn, C):
    reduceVal = 0
    for x in C:
        reduceVal = fn(reduceVal, x)
    return reduceVal

MyList = [1, 2, 3]
print(myReduce(lambda x, y: x if x > y else y, MyList))

# Bai 12
def myFilter(fn, C):
    newsC = []
    for x in C:
        if fn(x):
            newsC.append(x)
    return newsC

Test = [1, 2, 3]
print(myFilter(lambda x: x % 2 == 0, Test))

# Bai 13
MyList1 = []
MyList2 = []
MyList3 = []
for item in range(1, 11):
    MyList1.append(item)
print(MyList1)

for item in range(1, 20, 2):
    MyList2.append(item)
print(MyList2)

for item in range(1, 47, 5):
    MyList3.append(item)
print(MyList3)

# Bai 14
MyList1 = [c for c in "QHONLINE"]
print(MyList1)

MyList2 = [i * j for i in ('x', 'y', 'z') for j in range(1, 5)]
print(MyList2)

MyList3 = [i * j for i in range(1, 5) for j in ('x', 'y', 'z')]
print(MyList3)

MyList4 = [[i + j] for i in range(0, 3) for j in [2, 3, 4]]
print(MyList4)

MyList5 = [[i + j for j in range(1, 5)] for i in range(1, 5)]
print(MyList5)

MyList6 = [(j, i) for i in range(1, 4) for j in range(1, 4)]
print(MyList6)

# Bai 15
def foo(*args):
    CurrentStr = ''
    for string in args:
        if len(string) > len(CurrentStr):
            CurrentStr = string
    return CurrentStr

print(foo('Hanoi University of Science and Technology', 'School of Applied Mathematics and Informatics', 'Phung Trong Hieu', 'Toan-tin 01 K60'))

# Bai 16
def foo2(MyStr):
    for c in MyStr:
        if str.isdigit(c):
            return True
    return False

print(foo2('So 1 Dai Co Viet'))

# Bai 17
def foo3(MyStr):
    MyDict = {}

    for c in MyStr:
        c = c.upper()
        if c not in MyDict:
            MyDict[c] = 1
        else:
            MyDict[c] += 1
    return MyDict

print(foo3('Hanoi University of Science and Technology'))