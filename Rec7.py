i = 1

def DisplayR(No):
    global i
    
    if(i <= No):
     
     print(i)
     i = i + 1
     DisplayR(No)

def main():
    print("enter the number : ")
    Value = int(input())

    DisplayR(Value)

if __name__=="__main__": #special variable, starter
    main()



