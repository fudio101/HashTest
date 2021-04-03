hashTableSize = 11


def display_hash(hashTable):
    for i in range(len(hashTable)):
        if hashTable[i] != None:
            print(i, ' ', hashTable[i])
        else:
            print(i, ' None!!!')


def isFull(hashTable):  # 1 + n + 1 + O(n)
    currSize = 0
    for i in range(hashTableSize):
        if hashTable[i] != None:
            currSize += 1
    if currSize >= hashTableSize - 1:
        return True
    return False


def Hashing(keyvalue):  # 1 + 2*n + 1 = O(n)
    sum = 0
    for i in keyvalue:
        sum += ord(i)
    return sum % hashTableSize


def insert(hashTable, value):  # O(n) + O(n) + 1 + 4*n + 1 = O(n)
    if isFull(hashTable):
        return
    hash_key = Hashing(value)
    step = 0
    while hashTable[hash_key] != None:
        step += 1
        hash_key = (hash_key + step) % hashTableSize
    hashTable[hash_key] = value


def refresh(hashTable):
    hashTable = [None]*hashTableSize


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

# https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/F
# def search(hashTable, value):
#     hash_key = Hashing(value)
#     if hashTable[hash_key] == value:
#         print(value, " is found!")
#         return
#     print(value, " is'n found!")
    # search(hashTable, 'Mia')
    # search(hashTable, 'Mi')
