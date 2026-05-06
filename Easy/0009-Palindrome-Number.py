class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            reserved_num=0
            temp=x
            i=0
            while temp>0:
                i=temp%10
                reserved_num=reserved_num*10+i
                temp=temp//10
            if reserved_num==x:
                return True
            else:
                return False
        """
        :type x: int
        :rtype: bool
        """
        
