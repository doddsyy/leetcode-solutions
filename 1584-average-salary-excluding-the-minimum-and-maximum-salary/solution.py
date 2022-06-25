class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(salary[salary.index(max(salary))])
        salary.remove(salary[salary.index(min(salary))])
        
        return sum(salary)/len(salary)
