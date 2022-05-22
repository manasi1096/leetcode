from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_list = []
        a = Counter(nums)
        
        return list(dict(sorted(a.items(), key=lambda item: item[1], reverse = True)).keys())[:k]

    
