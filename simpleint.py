def simple_intrest(principal,intrest,time):
    return (principal*intrest*time)/100

if __name__ == "__main__":
    p = int(input("entwe the principal amount "))
    i = int(input("intrest rate"))
    t = int(input("time in years"))
    print("Simple intrest is:",simple_intrest(p,i,t))