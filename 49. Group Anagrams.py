class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}

        for i in strs:

            count = [0]*26

            for j in i:

                count[ord(j)-ord('a')] += 1

            if tuple(count) in mydict.keys():

                mydict[tuple(count)].append(i)

            else:
                mydict[tuple(count)] = [i]
        
        return mydict.values()
    
