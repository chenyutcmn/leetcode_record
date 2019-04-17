#大佬的DP方法，作为菜鸡的我一辈子也想不到
class Solution:
# @return a boolean
def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
    return dp[-1]

#双指针解法也是可行的，是我太菜，写不出来
bool isMatch(const char *s, const char *p) {
    const char* star=NULL;
    const char* ss=s;
    while (*s){
        //advancing both pointers when (both characters match) or ('?' found in pattern)
        //note that *p will not advance beyond its length 
        if ((*p=='?')||(*p==*s)){s++;p++;continue;} 

        // * found in pattern, track index of *, only advancing pattern pointer 
        if (*p=='*'){star=p++; ss=s;continue;} 
        //current characters didn't match, last pattern pointer was *, current pattern pointer is not *
        //only advancing pattern pointer
        if (star){ p = star+1; s=++ss;continue;} 
        //current pattern pointer is not star, last patter pointer was not *
        //characters do not match
        return false;
        }

        //check for remaining characters in pattern
        while (*p=='*'){p++;}

        return !*p;  
    }