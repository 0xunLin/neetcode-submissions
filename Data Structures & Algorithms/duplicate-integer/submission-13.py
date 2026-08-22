# This solution is the simplest one-line code, with O(N) time complexity and O(N) space complexity, where the set(nums) creates a pointer from the stack frame to the heap where an element is hashed to put into a hashed heap bucket according to its own hash, so duplicate elements whose values have already been put into the heap are skipped on check, if fresh new lement, then it passes the check and is put into the hashed bucket location, this is called open addressing or quadratic probing
# In this solution we use the len() function which is O(1) time complexity because it dirtectly checks the metadata field ob_size in the PyObject structural header in the heap and doesn't iterate over the array to count the number of elem; to find the size(length) of the original nums array, and its no duplicate hash set, we compare these two, if not equal -> False thus contains duplicates and, if equal -> True thus no duplicates
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))

#################################################################################################

# In this solution we sort the nums array in-place using the algorithm Timsort(a hybrid of merge sort and insertion sort) using the .sort() function, it doesn't make any copy of the list, but it does create a temporary stoarge timeline array which in the worst-case scales up to O(N/2) pointer slots on the heap
# In this solution the duplicates are sorted to be one-after-the-other in the array, and then the num[i] and num[i + 1] comparison, if equal -> contains duplicates, if not equal -> moves to the next index and makes the comprison again until the last index of the array and return False thus no duplicates
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
        
#################################################################################################

# IN this soultion we create an empty hash set and then as we iterate through the elements in the array, we slook at the heap bucket the hash of that element leads to, if it is filled -> contains duplicates, if empty -> add(insert) that elemet in the empty seen hash set heap bucket and iterate until the sequence compares all teh elements of the array, at the end if no True is returned -> return False thus no duplicates
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False