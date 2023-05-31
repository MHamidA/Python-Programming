#generator, yield

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i # rather than return it will be crashed, because running out of cpu

if __name__ == "__main__":
    main()