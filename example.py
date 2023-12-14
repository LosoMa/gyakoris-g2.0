import random as rr


def isPerfect():
    pass

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
            

startMeassage = "Kezdőérték: "
endMassage = "Végérték: "
ammountMassage = "Értékek száma: "
#amount =input("Értékek száma: ")
start = makeNumber2(startMeassage)
end = makeNumber2(endMassage)
ammount = makeNumber2(ammountMassage)
