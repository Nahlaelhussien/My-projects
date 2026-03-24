class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        target=skill[i]+skill[j]
        result=0
        while i<len(skill) and j>=i:
            if skill[i]+skill[j]!=target:
                return -1
            result += skill[i] * skill[j]
            i += 1
            j -= 1
        return result
