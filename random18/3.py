class Coputation:
    def __init__(self) -> None:
        pass
    def Factorial(self,n):
        count=1
        for i in range(1,n+1):
            count*=i
        return count
    def Sum(self,n):
        sum=0
        for i in range(1,n+1):
            sum+=i
        return sum
    def testPrim (self, n):
        j = 0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False
    def testprims (self, n, m):
        
        common = 0
        for i in range (1, n + 1):
            if (n% i == 0 and m% i == 0):
                common = common + 1
        if common == 1:
            print ("The numbers", n, "and", m, "are primes")
        else:
            print ("The numbers", n, "and", m, "are not primes")


    def tableMult (self, k):
        for i in range (1,10):
            print (i, "x", k, "=", i * k)

    def allTablesMult (self):
        for k in range (1,10):
            print ("\nthe multiplication table of:", k, "is:")
            for i in range (1,10):
                print (i, "x", k, "=", i * k)

    def listDiv (self, n):
        listdiv = []
        for i in range (1, n + 1):
            if (n% i == 0):
                listdiv.append (i)
        return listdiv

    def listDivPrim (self, n):
        listdiv = []
        for i in range (1, n + 1):
            if (n% i == 0 and self.testPrim (i)):
                listdiv.append (i)
        return listdiv
computation=Coputation()
print(computation.Factorial(5))
print(computation.Sum(6))
computation.testPrim(10)
computation.testprims(3,7)
print(computation.listDiv(16))
print(computation.listDivPrim(16))
computation.tableMult(3)
computation.allTablesMult()