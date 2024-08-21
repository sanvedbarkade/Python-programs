def Display(Cnt):
    i = 0
    if (Cnt <= 0):
        print("invalid input")
        return

    while(i < Cnt):
        print("jay Ganesh", end = " ")
        i = i + 1



def main():
    print("please enter the frequency : ")
    No = int(input())
    Display(No)

if __name__ == "__main__":
        main()