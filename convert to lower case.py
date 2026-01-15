class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = ""
        for i in s:
            if 'A' <= i <= 'Z':
                s1 += chr(ord(i) + 32)
            else:
                s1 += i
        return s1

       
