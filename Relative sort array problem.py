from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
     arr1.sort()
     result=[]
     count=Counter(arr1)
     for target in arr2:
        result.extend([target] * count[target])
        del count[target]
     for key in sorted(count):
        result.extend([key]*count[key])
     return result
