class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        solution = []
        my_dict = {}

        for index, num in enumerate(nums):
            temp = target - num
            if my_dict.get(temp,None) != None:
                solution_index = my_dict.get(temp)
                solution.append(solution_index)
                solution.append(index)
                break
            else:
                print(num)
                print(index)
                my_dict[num] = index

        return solution



        