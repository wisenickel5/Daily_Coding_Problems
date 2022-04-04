# Solved by Dylan A. on 01/18/2021
# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, 
# and an encoded message, count the number of 
# ways it can be decoded. For example, the 
# message '111' would give 3, since it could be 
# decoded as 'aaa', 'ka', and 'ak'.

def NumOfSolutions(s: str) -> int:
    # Base Cases
    if s is None or s[0] == '0':
        return 0

    # Create an array the length of the string
    dp = [1] * len(s)

    for i in range(1, len(s)):
        # One Digit Check
        dp[i] = 0 if int(s[i]) == 0 else dp[i - 1]

        # Two Digit Check
        if 10 <= int(s[i-1 : i+1]) <= 26:
            dp[i] += dp[i - 2 if i > 1 else 0]
    
    # Return last element
    print(dp[-1])
    return dp[-1]

if __name__ == '__main__':
    code = '2212'
    NumOfSolutions(code)