class solution:
    def power_with_module(self,a,b,c):
        a=a%c
        result=1
        for i in range(1,b+1):
            result=(a*result)%c
        return result
a1=solution()
a=int(input())
b=int(input())
c=int(input())
print(a1.power_with_module(a,b,c))

