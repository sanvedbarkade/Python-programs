def Display(Cnt):
    i = 0
    if (Cnt <= 0):
        print("invalid input")
        return

    for i in range(Cnt):
        print("jay Ganesh")


def main():
    print("please enter the frequency : ")
    No = int(input())
    Display(No)

if __name__ == "__main__":
        main()