class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def isTrue(t):
            total=0
            for w in workerTimes:
                time=0
                k=1
                while True:
                    time+=k*w
                    if time > t:
                        break
                    total+=1
                    k+=1
                    if total >= mountainHeight:
                        return True
            return False

        left=0
        right=min(workerTimes) *mountainHeight*(mountainHeight+1)//2

        while left <= right:
            mid=(left+right)//2
            
            if isTrue(mid):
                right=mid-1
            else:
                left=mid+1
        return left
  
        

      