class Solution(object):
    def longestValidParentheses(self, s):
        max_len = 0
        dp = [0] * len(s)
        
        for i in range(1, len(s)):
            if s[i] == ')':
                
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':

                    prev_len = dp[i - 1] 
                    before_match = dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0
                    
                    dp[i] = prev_len + 2 + before_match
            
            max_len = max(max_len, dp[i])
            
        return max_len