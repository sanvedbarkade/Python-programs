def checkEven(A):
    if(A%2 == 0):
        return True
    else:
        return False

def main():
    Ret = checkEven(11)
    if(Ret == True):

        print("its even number")
    else:
        print("its odd number")

if __name__=="__main__":
    main()