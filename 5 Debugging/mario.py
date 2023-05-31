def main():
    height = int(input("Heights: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i) #this line use the run and debug

if __name__ == "__main__":
    main()