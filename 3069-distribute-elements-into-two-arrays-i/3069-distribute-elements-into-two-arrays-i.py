class Solution(object):
    def resultArray(self, nums):
        arr1=[]
        arr2=[]

        for i in range(len(nums)):
            index=i+1

            if index > 2:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])

            elif index % 2==1:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
        


        




     