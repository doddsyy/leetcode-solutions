class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        srtd = sorted(nums)
        arr = []
        for n in range(int((len(nums)/2))):
            arr.append(srtd[1])
            arr.append(srtd[0])
            
            srtd.remove(srtd[1])
            srtd.remove(srtd[0])
        return arr

        

        
