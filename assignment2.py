class Time():
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
        self.fix()     

    def sum(self,time2):
        self.result_h=self.h+time2.h
        self.result_m=self.m+time2.m
        self.result_s=self.s+time2.s 
        result=Time(self.result_h,self.result_m,self.result_s)
        return result
    
    def sub(self,time2):
        self.result_h=self.h-time2.h
        self.result_m=self.m-time2.m
        self.result_s=self.s-time2.s
        result=Time(self.result_h,self.result_m,self.result_s)
        return result
    
    @staticmethod
    def second_to_time(seconds):
        h= seconds//3600
        seconds=seconds-(h*3600)
        m=seconds//60
        seconds=seconds-(m*60)
        s=seconds

        time=Time(h,m,s)
        return time


    def gmt_to_tehran(self):      
        t=Time(3,30,0)     
        tehran_time=self.sum(t)         
        return tehran_time
    
    def show(self):
        print(f"{self.h}:{self.m}:{self.s}")

    def fix(self):          
        if self.s>60:     
            self.s-=60
            self.m+=1
        if self.m>60:
           self.m-=60
           self.h+=1
        if self.s<0:
           self.m-=1
           self.s+=60
        if self.m<0:
           self.h-=1
           self.m+=60
 

time1=Time(8,20,45)
time1.show()

time2=Time(7,35,20)
time2.show()

result_sum=time1.sum(time2)
result_sum.show()

time4=time2.gmt_to_tehran()
time4.show()

time5=Time.second_to_time(5000)
time5.show()
