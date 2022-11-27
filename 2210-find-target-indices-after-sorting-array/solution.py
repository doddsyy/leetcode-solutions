class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        li = []
        srt = sorted(nums)
        for i in range(len(srt)):
            if srt[i] == target:
                li.append(i)

        return li
