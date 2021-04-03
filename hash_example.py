import math


def hash1(key, m):
    sum = 0
    for i in key:
        sum += ord(i)
    return sum % m


def hash2(key, m):
    sum = 0
    for i in key:
        sum += ord(i)
    A = math.sqrt(5)-1
    return int(m*(sum*A % 1))


def sFolding(key, m):
    sum = 0
    mul = 1
    for i in key:
        mul = 1 if (key.index(i) % 4 == 0) else mul*256
        sum += ord(i) * mul
    return sum % m
# https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/HashFuncExamp.html


def main():
    m = 11
    a = hash1("1235", m)
    print(a)
    a = hash2("1235", m)
    print(a)
    b = sFolding("1235", m)
    print(b)


if __name__ == '__main__':
    main()
