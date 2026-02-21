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


        