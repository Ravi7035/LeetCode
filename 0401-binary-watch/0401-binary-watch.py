class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        #solving through binary bits(1) calculation
        #there are 0-11 hours and 0-59 minutes so atmost there are 12*60           
        #possibilities
        output=[]

        for hour in range(12):
            for minute in range(60):

                if bin(hour).count("1")+bin(minute).count("1")==turnedOn:
                    time="{}:{:02d}".format(hour,minute)
                    output.append(time) 
                    #{0:2d}..it is used to formatting  
                    #integers and mainly dates :) ..

        return output


        