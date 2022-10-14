class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ans=[]
        for i in range(len(prices)-1):
            flag=False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    ans.append(abs(prices[i]-prices[j]))
                    flag=True
                    break
            if flag==False:
                ans.append(prices[i])
    
                
        ans.append(prices[-1])
        return ans
        
        
        
        
        
        #li = []
        #for i in range(len(prices)):
         #   if prices.count(min(prices[i:])) == 1:
          #      if prices[i] == prices[i:]:
           #          li.append(prices[i])
            #else:
             #   for num in prices[i+1:]:
              #      if num <= prices[i]:
               #         li.append(prices[i] - num)
                #        break
        #return li
