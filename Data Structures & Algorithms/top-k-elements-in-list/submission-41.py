class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print(nums)
        my_dict = {key: 0 for key in nums}
        # print(my_dict)
        for i in nums:
            my_dict[i]=my_dict[i]+1
        # print(my_dict)
        filtered_dict = heapq.nlargest(k, my_dict, key=my_dict.get)
        # print(filtered_dict)
        return filtered_dict
        