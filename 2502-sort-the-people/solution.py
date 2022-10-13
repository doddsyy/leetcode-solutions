

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(heights)):
            dic[i] = heights[i]
        srted = sorted(dic,key = dic.get,reverse=True)
        li = []
        for num in srted:
            li.append(names[num])
        return li

