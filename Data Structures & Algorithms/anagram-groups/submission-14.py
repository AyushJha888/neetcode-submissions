class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            # 1. Create a fixed-size list of 26 zeros (one for each letter a-z)
            count = [0] * 26
            
            # 2. Loop through each character and calculate its ord index
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
                
            # 3. Convert the list to a tuple so it can be used as a dictionary key
            # (Python lists are mutable and can't be dictionary keys, but tuples can!)
            key = tuple(count)
            
            # 4. Group them up
            anagram_map[key].append(s)
            
        return list(anagram_map.values())