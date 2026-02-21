class Solution(object):
    def checkValidString(self, s):
        #using two stack for appending of open brackets and another for stars

        Openstack=[]
        Starstack=[]

        for i,char in enumerate(s):
            if char=="(":
                Openstack.append(i)
            elif char=="*":
                Starstack.append(i)
            else:
                if Openstack:
                    Openstack.pop()
                elif Starstack:
                    Starstack.pop()
                else:
                    return False

        while Openstack and Starstack:

            if Openstack[-1] < Starstack[-1]:

                Openstack.pop()
                Starstack.pop()

            else:
                return False

        return not Openstack

        #using greedy appraoch

        low=0
        high=0
        
        for char in s:

            if char=="(":
                low+=1
                high+=1

            elif char==")":
                low-=1
                high-=1

            else:
                low-=1
                high+=1

            if high < 0:

                return False
            elif low <0:
                low=0

        return low==0




        