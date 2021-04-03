from Linear_probing import refresh


def Hashing(keyvalue, size):  # 1 + 2*n + 1 = O(n)
    sum = 0
    for i in keyvalue:
        sum += ord(i)
    return sum % size


def Hashing1(keyvalue, size):
    sum = 0
    prime = size // 2+1
    for i in keyvalue:
        sum += ord(i)
    return (prime - (sum % prime))


class SeprateChaining:
    _size = 0
    _hashTable = []

    def __init__(self, size) -> None:
        self._size = size
        self._hashTable = [[] for _ in range(self._size)]

    def insert(self, value):  # O(n)
        if value == '':
            return
        hash_key = Hashing(value, self._size)
        self._hashTable[hash_key].append(value)

    def display(self):
        for i in range(len(self._hashTable)):
            print(i, end=" ")
            if len(self._hashTable[i]) == 0:
                print("->", end=" ")
                print("NULL", end=" ")
            else:
                for j in self._hashTable[i]:
                    print("->", end=" '")
                    print(j, end="' ")
            print()

    def refresh(self):
        self._hashTable = [[] for _ in range(self._size)]


class HashTable:
    _size = 0
    _hashTable = []

    def __init__(self, size) -> None:
        self._size = size
        self._hashTable = [None]*self._size

    def _isFull(self):
        currSize = 0
        for i in range(self._size):
            if self._hashTable[i] != None:
                currSize += 1
        if currSize >= self._size - 1:
            return True
        return False

    def insert(self, value):
        pass

    def display(self):
        for i in range(len(self._hashTable)):
            if self._hashTable[i] != None:
                print(i, "'" + self._hashTable[i] + "'")
            else:
                print(i, ' NULL')

    def refresh(self):
        self._hashTable = [None]*self._size


class LinearProbing(HashTable):
    def insert(self, value):
        if value == '':
            return
        if self._isFull():
            return False
        hash_key = Hashing(value, self._size)
        step = 0
        while self._hashTable[hash_key] != None:
            step += 1
            hash_key = (hash_key + step) % self._size
        self._hashTable[hash_key] = value
        return True


class QuadraticProbing(HashTable):
    def insert(self, value):
        if value == '':
            return
        if self._isFull():
            return False
        hash_key = base = Hashing(value, self._size)
        step = 0
        while self._hashTable[hash_key] != None:
            step += 1
            hash_key = (base + step ** 2) % self._size
        self._hashTable[hash_key] = value
        return True


class DoubleHashing(HashTable):
    def insert(self, value):
        if value == '':
            return
        if self._isFull():
            return False
        hash_key = Hashing1(value, self._size)
        if self._hashTable[hash_key] != None:
            hash_key1 = Hashing1(value, self._size)
            step = 0
            while True:
                step += 1
                hash_key = (hash_key + step * hash_key1) % self._size
                if self._hashTable[hash_key] == None:
                    self._hashTable[hash_key] = value
                    break
        else:
            self._hashTable[hash_key] = value
