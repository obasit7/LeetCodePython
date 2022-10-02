arr = [1,2,3,1]

def contains_duplicate(arr: list):
    hashSet = set()
    for num in arr:
        if num in hashSet:
            return True
        hashSet.add(num)

    return False