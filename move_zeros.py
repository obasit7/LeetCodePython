#given array of numbers, move all zeros to right side of array
#while maintaining order

# solution: quicksort/select
# move non zero values to left of array

def move_zeros(nums: list):
    left_ptr = 0
    for r in range(len(nums)):
        if nums[r]: #swap l and r
            nums[left_ptr], nums[r] = nums[r], nums[left_ptr]
            left_ptr += 1

    return nums

print(move_zeros([0,1,0,5,12,0]))
