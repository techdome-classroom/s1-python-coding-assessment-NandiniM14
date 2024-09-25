def decode_message( s: str, p: str) -> bool:

# write your code here
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]

# Test cases
print(decode_message("aa", "a"))   # False
print(decode_message("aa", "*"))   
print(decode_message("cb", "?a"))  
print(decode_message("cb", "?b"))  