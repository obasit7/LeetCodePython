# given s and t, find min window in s which contains t
# if not return ""

# have a hashmap for t and s and store count of have(S) and need(T)
# update have hashmap and count whenever S char == T char
# when have == need, store result as starting and ending index and length
# repeat by removing left most char while have!=need. if char in have, subtract one
# if result < stored result, stored result = result
# Time: O(n), difficulty: Hard

def minWindow(s:str, t:str):
    if t == "":
        return ""

    countT, window = {}, {}
    result, resultLength = [-1,-1], float("infinity")
    l = 0

    for c in t:
        countT[c] = countT.get(c, 0) + 1
        # .get gets val of key if present otherwise returns 0

    have, need = 0, len(countT)

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        # checking if c is what we need and if count in window and T is same
        if c in countT and window[c] == countT[c]:
            have += 1 # increment have by 1
        # keep shrinking till condition True if have == need
        while have == need:
            #update result if new length < prev result length
            if (r - l + 1) < resultLength:
                result = [l, r]
                resultLength = (r - l + 1)

            # remove/pop left
            window[s[l]] -= 1
            # if char in window and removing makes count less than needed, decr have
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = result

    return s[l:r+1] if resultLength != float("infinity") else ""





