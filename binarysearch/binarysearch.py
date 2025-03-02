class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1
        # when dealing 2 pointer make sure they converge
        while start < end:

            # start + mid is the new idea, and you need to update the 
            # code in the accordingly
            mid = start + (end - start ) // 2 

            if nums[mid] == target:
                return mid


            # update the start and end with + 1
            elif nums[mid] < target:
                start = mid + 1 
            
            elif nums[mid] > target:
                end = mid -1
        
        return -1
            
