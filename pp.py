class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        for i in range(len(prices)):
            if prices[i]==min(prices):
                return (max(prices[i:])) -prices[i]
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        seen=[]
        for i in range(len(prices)):
            for j in range(i,len(prices)-1):
                if prices[i] < prices[j+1]:
                    seen.append(prices[j+1]-prices[i])
        if seen:
           return max(seen)
        else:
            return 0

        
        
        
runn=Solution()
print(runn.maxProfit([7,2,4,6]))
print(runn.maxProfit([7,6,4,3,1]))
num=[2,3,4,5]
print(num[-1])