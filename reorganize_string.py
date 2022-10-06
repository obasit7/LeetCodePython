# Time: O(nlogn) avg
# 2 solutions: HashMap or MaxHeap
import heapq
from collections import Counter
def reorganize(s: str):
    count = {}
    for c in s:
        count[c] = 1 + count.get(c, 0)

    # heapified based on first key
    max_heap = [[-count, char] for char, count in count.items()]
    heapq.heapify(max_heap) # O(n) avg

    prev = None
    result = ""
    while max_heap or prev:

        if prev and not max_heap:
            return ""

        count, char = heapq.heappop(max_heap)
        result += char
        count += 1  # since we store it as -ve for maxheap

        if prev:
            heapq.heappush(max_heap, prev)
            prev = None

        if count != 0:
            prev = [count, char]

    return result


print(reorganize("aaabcdd"))
