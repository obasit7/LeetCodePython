# time: O(logn)

def search_array(arr: list, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) //2
        if target == arr[mid]:
            return mid
        # left sorted portion [5,6,7,8,2,3,4]
        if arr[left] <= arr[mid]:
            # search right portion
            if target > arr[mid] or target < arr[left]:
                left = mid + 1
            # search left portion
            else:
                right = mid - 1
        # right sorted portion  [5,6,7,1,2,3,4]
        else:
            if target < arr[mid] or target > arr[right]:
                # search left portion
                right = mid -1
            else:
                left = mid + 1

    return -1

