nums = [4, 9, 11, 14]

def two_sum(nums, target):
   list =[]
   for i, value in enumerate(nums):
      for j, value in enumerate(nums):
         if nums[i] + nums[j] == target:
            list.append(i)
            list.append(j)
            return list

print(two_sum(nums, 13))