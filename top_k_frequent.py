# memory: O(n) time: O(n)
def k_frequent(nums, k):
    # can make hashmap, but bad time nlogn
    # store dict of count as key and list of vals in key
    # bucket sort
    count_dict = {}
    freq = [[] for i in range(len(nums)+1)]

    # store freq of each num in map
    for n in nums:
        count_dict[n] = 1 + count_dict.get(n, 0)
    # make array that has count as index and list of nums of that count as subarray
    for n, count in count_dict:
        freq[count].append(n)

    result = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result




