class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            i=0
            j=len(s)-1
            count=1
            while i<=j:
                if s[i]== s[j]:
                    i+=1
                    j-=1
                elif count > 0:
                    skip_left = s[i+1:j+1]
                    skip_right = s[i:j]
                    if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                        return True
                    else:
                        return False
                else:
                    return False
