
def word_break(s: str, word_dict: dict):
    dp = [False] * (len(s)+1)
    dp[len(s)] = True

    # neetcode  --> {'neet', 'code', 'leet'}
    for i in range(len(s)-1, -1, -1):
        for w in word_dict:
            # check whether len(s[i:i+len(w)) == w
            if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i] == True:
                break

    return dp[0]
