class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for i in strs:
            # print(i)
            
            sorted_key = "".join(sorted(i))
            anagram_map[sorted_key].append(i)
            
        anagram_list=list(anagram_map.values())
        return anagram_list   
        