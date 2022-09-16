#Time O(n)
# make left and right pointer

arr = [1,8,6,2,5,4,8,3,7]
l ,r = 0, len(arr) - 1
max_area = 0

while l < r:
    area = (r - l) * min(arr[l], arr[r])
    max_area = max (area, max_area)

    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1


print (max_area)