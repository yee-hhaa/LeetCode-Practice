class Solution(object):
    def isValid(self, s):
        """
        思路:運用堆疊
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:  
                    return False
                top = stack.pop()
                if char == ")" and top != "(": 
                    return False
                if char == "]" and top != "[": 
                    return False
                if char == "}" and top != "{": 
                    return False
        return not stack


