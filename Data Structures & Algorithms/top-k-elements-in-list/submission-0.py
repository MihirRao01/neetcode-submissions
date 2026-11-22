class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution = []
        my_dict = defaultdict(int)
        frequency_table = defaultdict(list)

        for num in nums:
            my_dict[num]+=1
        
        for key, value in my_dict.items():
            frequency_table[value].append(key)

        for freq in range(len(nums),-1,-1):
            if frequency_table[freq] != []:
                if len(solution) < k:
                    for sol in frequency_table[freq]:
                        solution.append(sol)
        
        return solution
                






            
        

        