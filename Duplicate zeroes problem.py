class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        
        while i < size:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 1
            i+=1

        
