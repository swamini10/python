#for printing even and odd as per requirements

while True:
    
    choice = input("even or odd : ")

    num = int(input(f"Enter number till which you need {choice} numbers : "))
    if choice=='even':
        print(f"{choice} numbers till {num}")
        for i in range(1,num):
            if i%2==0:
                print(i)

    elif choice=='odd':
        print(f"{choice} numbers till {num}")
        for i in range(1,num):
            if i%2!=0:
                print(i)

    con = int(input("Enter 1 to continue or 0 to break : "))
    if con==1:
        pass

    else:
        break
