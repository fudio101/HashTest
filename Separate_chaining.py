hashTableSize = 11


def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()


def Hashing(keyvalue):  # 1 + 2*n + 1 = O(n)
    sum = 0
    for i in keyvalue:
        sum += ord(i)
    return sum % hashTableSize


def insert(hashTable, value):  # O(n)
    hash_key = Hashing(value)
    hashTable[hash_key].append(value)


def refresh(hashTable):
    hashTable = [[] for _ in range(hashTableSize)]


def main():
    hashTable = [[] for _ in range(hashTableSize)]
    insert(hashTable, 'Allahabad')
    insert(hashTable, 'Mumbai')
    insert(hashTable, 'Mathura')
    insert(hashTable, 'Delhi')
    insert(hashTable, 'Punjab')
    insert(hashTable, 'Noida')
    insert(hashTable, 'Mia')
    insert(hashTable, 'Tim')
    insert(hashTable, 'Bea')
    insert(hashTable, 'Zoe')
    insert(hashTable, 'Jan')
    insert(hashTable, 'Ada')
    insert(hashTable, 'Leo')
    insert(hashTable, 'Sam')
    insert(hashTable, 'Lou')
    insert(hashTable, 'Max')
    insert(hashTable, 'Ted')
    display_hash(hashTable)


if __name__ == '__main__':
    main()
# def search(hashTable, value):
#     hash_key = Hashing(value)
#     for s in hashTable[hash_key]:
#         if s == value:
#             print(value, " is found!")
#             return
#     print(value, " is'n found!")
    # search(hashTable, 'Mia')
    # search(hashTable, 'Mi')
