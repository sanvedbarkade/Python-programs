import sys #sys = System

def main():

    print("Demonstration of command line Arguments")
    print("name of Application : ",sys.argv[0])
    print("datatype of argv id : ",type(sys.argv))
    print("Number of command line Arguments are : ",len(sys.argv))

if __name__ == "__main__":
    main()

