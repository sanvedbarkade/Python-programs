def checkEvenX(A):
   return (A%2 == 0)

   checkEvenX = lambda A : (A%2 ==0)

def main():
    Ret = checkEvenX(11)
    if(Ret == True):

        print("its even number")
    else:
        print("its odd number")

if __name__=="__main__":
    main()

