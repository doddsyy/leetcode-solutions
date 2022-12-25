class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        li = []
        for item in strs:
            if item.isdigit():
                li.append(int(item))
            else:
                li.append(len(item))
        return max(li)
