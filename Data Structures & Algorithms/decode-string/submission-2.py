class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def expand(i):
            curr = ""
            while i < n and s[i] != ']':
                # Letter
                if s[i].isalpha():
                    curr += s[i]
                    i += 1

                else:
                    mul = "" 
                    while i < n and s[i].isdigit():
                        mul += s[i]
                        i += 1
                    i += 1
                    new_curr, i = expand(i)
                    curr += new_curr * int(mul)
                    i += 1
            return curr, i

        ans, _ = expand(0)
        return ans
                    