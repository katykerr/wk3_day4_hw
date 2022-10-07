# Given an array of sorted integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.
# You may assume that each input would have exactly one 
# solution, and you may not use the same element twice.
# You can return the answer in any order.
# ex.1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# ex. 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]


#bo below
def whichNums(nums, target):
    for n in nums:
        other_int = target - n
        if other_int == n:
            continue
        elif other_int in nums:
            return [nums.index(n),nums.index(other_int)]

print(whichNums([2,7,11,15],13))
print(whichNums([3,2,0,4],6))



  #chris below
    def whiteboard(list, target):
    counter = 0
    currentvalue = 0

    while counter < len(list):
        currentvalue = list[counter]
        for i in list:
            currentvalue += i
            if currentvalue == target and list.index(list[counter]) != list.index(i):
                print(f'{list.index(list[counter])}, {list.index(i)}')
            else:
                currentvalue = list[counter]
        counter += 1


whiteboard([2,7,11,15], 9)



#shoha w/ dict

def twoSum(nums, target):
    d = {} #value : index
    for i in range (len(nums)):
        pair = target - nums[i]
        if pair in d:
            return [d[pair], i]
        d[nums[i]] = i
    return