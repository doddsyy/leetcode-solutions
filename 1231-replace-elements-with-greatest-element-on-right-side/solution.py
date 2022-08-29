class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if arr[i+1:]:
                li = arr[i+1:]
                arr[i] = max(li)
            else:
                arr[i] = -1
        return arr
