class Number:
    def __init__(self,n):
        self.number=n
    def reverse(self):
        num=self.number
        rev=0
        while num!=0:
            rev=(rev*10)+(num%10)
            num=num//10
        return rev
    def isPalindrome(self):
        return self.reverse()==self.number
    def isPrime(self):
        j=0
        for i in range(2,self.number):
            if self.number%i==0:
                j+=1
            else:
                pass
        return j!=1
x=Number(int(input("enter a number: ")))
print(f"reverse of the given number is {x.reverse()}")
print(f"given number is a Palindrome number: {x.isPalindrome()}")
print(f"given number is prime: {x.isPrime()}")