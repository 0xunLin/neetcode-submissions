class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ws = len(s1)
        s1 = list(s1)
        s1 = sorted(s1)
        left = 0

        while left < len(s2):
            s3 = list(s2)
            s3 = s3[left:left+ws]
            s3 = sorted(s3)
            if s1 == s3:
                return True
            left += 1
        return False