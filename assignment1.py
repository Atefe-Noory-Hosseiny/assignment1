class Franction():
    def __init__(self,s,m):
        self.s=s
        self.m=m

    def sum(self,f2):
        result_s=((self.s * f2.m)+(f2.s * self.m))
        result_m=(self.m * f2.m)
        result=Franction(result_s,result_m)
        return result
     
    def mul(self,f2):
        result_s=(self.s)*(f2.s)
        result_m=(self.m)*(f2.m)
        result=Franction(result_s,result_m)
        return result

    def sub(self,f2):
        result_s=((self.s * f2.m)-(f2.s * self.m))
        result_m=(self.m * f2.m)
        result=Franction(result_s,result_m)
        return result

    def div(self,f2):
        result_s=(self.s)*(f2.m)
        result_m=(self.m)*(f2.s)
        result=Franction(result_s,result_m)
        return result
    
    def show(self):
        print(self.s ,"/",self.m)



f1=Franction(2,3)
#f1.show()
f2=Franction(4,5)
#f2.show()

               
result_mul=f1.mul(f2)
result_mul.show()

result_sum=f1.sum(f2)
result_sum.show()

result_sub=f1.sub(f2)
result_sub.show()

result_div=f1.div(f2)
result_div.show()

