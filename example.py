import random as rr


def isPerfect(n):
    divnumbers = [1]
    for i in range(2, n, 1):
        if n %i == 0:
            divnumbers.append(i)
    
    return sum(divnumbers) == n
            

#def makeNumber(n) :
    #try:
     #   n = int(n)
    #except ValueError:
     #   n = None
    #return n

#def repeatInput():
   # start = None
    #while start == None:
     #   start = input(f"Kezdőérték: ")
      #  if makeNumber(start):
       #     print(start)
        
        
        #else:
         #   print("Helytelen érték")


def rrGenerator(s,e,a):
    numbers = []
    for i in range(a):
        numbers.append(rr.randint(s,e))
    return numbers




def makeNumber2(text):
    #isCorrect = False
    while True:#not isCorrect:
        n = input(text)
        try:
            n = int(n)
            
            return n
        except ValueError:
            print("Helytelen érték.")
            
perfectnumbers = []
perfectnumfrq = {}
startMeassage = "Kezdőérték: "
endMassage = "Végérték: "
ammountMassage = "Értékek száma: "
#amount =input("Értékek száma: ")
start = makeNumber2(startMeassage)
end = makeNumber2(endMassage)
ammount = makeNumber2(ammountMassage)

RN = rrGenerator(start, end, ammount)

for num in RN:
    if isPerfect(num):
        perfectnumbers.append(num)
        
for num in perfectnumbers:
    if num in perfectnumfrq.keys():
        perfectnumfrq[num] +=1
    else:
        perfectnumfrq[num] =1
        
for key in perfectnumfrq:
    print(f"{key}: {perfectnumfrq[key]} db")