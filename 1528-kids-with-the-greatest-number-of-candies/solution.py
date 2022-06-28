class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li = []
        for i in range(0 , len(candies)):
            li.append((candies[i] + extraCandies) >= max(candies))
        return li
        
