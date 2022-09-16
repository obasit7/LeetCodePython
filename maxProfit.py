arr = [7, 2, 5, 1, 8, 4]

left_ptr = 0
right_ptr = 1
buy_at = arr[left_ptr]
max_profit = 0

# space = O(n), time=O(n)
while right_ptr <= len(arr)-1:
    if arr[left_ptr] < arr[right_ptr]:
        if arr[right_ptr] > max_profit:
            max_profit = arr[right_ptr] - arr[left_ptr]

    else:
        buy_at = arr[right_ptr]
        left_ptr = right_ptr

    right_ptr += 1

print(max_profit)

