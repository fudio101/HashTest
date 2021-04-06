hashTableSize = 11
prime = 7


def display_hash(hashTable):
    for i in range(len(hashTable)):
        if hashTable[i] != None:
            print(i, ' ', hashTable[i])
        else:
            print(i, ' None!!!')


def isFull(hashTable):  # 1 + n + 2 + O(n)
    currSize = 0
    for i in range(hashTableSize):
        if hashTable[i] != None:
            currSize += 1
    if currSize >= hashTableSize - 1:
        return True
    return False


def Hashing(keyvalue):  # 1 + 2*n + 1 = O(n)
    _sum = 0
    for i in keyvalue:
        _sum += ord(i)
    return _sum % hashTableSize


def Hashing1(keyvalue):
    sum = 0
    for i in keyvalue:
        sum += ord(i)
    return (prime - (sum % prime))


def insert(hashTable, value):
    if isFull(hashTable):
        return
    hash_key = Hashing(value)
    if hashTable[hash_key] != None:
        hash_key2 = Hashing1(value)
        step = 0
        while True:
            step += 1
            hash_key = (hash_key + step * hash_key2) % hashTableSize
            if hashTable[hash_key] == None:
                hashTable[hash_key] = value
                break
    else:
        hashTable[hash_key] = value


def main():
    hashTable = [None] * hashTableSize
    insert(hashTable, 'Mia')
    insert(hashTable, 'Tim')
    insert(hashTable, 'Bea')
    insert(hashTable, 'Zoe')
    insert(hashTable, 'Allahabad')
    insert(hashTable, 'Mathura')
    insert(hashTable, 'Leo')
    insert(hashTable, 'Sam')
    insert(hashTable, 'Lou')
    insert(hashTable, 'Noida')
    insert(hashTable, 'Ted')
    display_hash(hashTable)


if __name__ == '__main__':
    main()
# https://www.geeksforgeeks.org/double-hashing/
