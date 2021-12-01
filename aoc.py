from abc import abstractproperty


class aoc:
    def day1_1(self,data):
        """find increases in data"""
        assessment = []
        assessment.append((data[0],0))
        for i in range(1,len(data)):
            if data[i] > data[i-1]:
                assessment.append((data[i],1))
            elif data[i] < data[i-1]:
                assessment.append((data[i],-1))
            else:
                assessment.append((data[i],0))
        return assessment
                
    def day1_2(self,data):
        """find increases in data"""
        groups = []
        for i in range(0, len(data)-2):
            temp = data[i]+data[i+1]+data[i+2]
            groups.append(temp)
        
        print(groups)
        return groups