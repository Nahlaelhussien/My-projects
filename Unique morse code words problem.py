import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = list(string.ascii_lowercase)
        dic={}
        for i in range(26):
            dic[alphabet[i]]=morse[i]
        trans=[]
        for word in words:
            r=""
            for letter in word:
                r=r+dic[letter]
            trans.append(r)
        return len(set(trans))

