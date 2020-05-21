'''
Given an array of integers, perform some number k of operations. Each operation consists of removing
any element from the array, dividing it by 2 and inserting the ceiling of that result back into the array.
Minimize the sum of the elements in the final array.
Example:
nums = [10, 20, 7]
k = 4
Pick    Pick/2 Ceiling Result
Initial array [10, 20, 7]
7         3.5      4          [ 10, 20, 4]
10         5       5           [5, 20, 4]
20         10      10          [5, 10, 4]
10         5        5          [5, 5, 4]
The sum of the final array is 5 + 5 + 4 = 14, and that sum is minimal.
'''



import math

def minimumSum(nums,k):
  max_index = len(nums) - 1
  for i in range(k):
    #find index of maximun number 
    max_index = nums.index(max(nums))
    nums[max_index] = math.ceil(max(nums)/2) # repalce max_value by its half. 
  return sum(nums)

nums = [10,20,7]
k= 4
print(minimumSum(nums,k))
