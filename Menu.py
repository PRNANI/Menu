def menu():
    select = 0
    print("\n**************************")
    print("******** MENU ************")
    print("**************************")
    print("*[1]----   Hot_dog   ----*")
    print("*[2]----   Sandwich  ----*")
    print("*[3]----   Pizza     ----*")
    print("*[4]----   Hamburger ----*")
    print("*[5]----   Steak     ----*")
    print("**************************")
    print("**************************")
    print("--What you want to day?--")
    print("**************************")
    select = int(input(": "))
    return select

def main():
    name = ""
    exit = ""
    selectMenu = 0
    print("\nHello what is your name?: ")
    name = input() 

    while exit != 'y':
        selectMenu = menu()
        exit = ' '
        while exit != 'x' and exit != 'y':
            if selectMenu >= 1 and selectMenu <= 5:
                if selectMenu == 1:
                    print("\n|------------------------------|")
                    print("|---- [1]Hot_dog | 30THB   ----|")
                    print("|------------------------------|")
                elif selectMenu == 2:
                    print("\n|-------------------------------|")
                    print("|---- [2]Sandwich | 50THB   ----|")
                    print("|-------------------------------|")
                elif selectMenu == 3:
                    print("\n|------------------------------|")
                    print("|---- [3]Pizza | 200THB   -----|")
                    print("|------------------------------|") 
                elif selectMenu == 4:
                    print("\n|---------------------------------|")
                    print("|---- [4]Humburger | 120THB   ----|")
                    print("|---------------------------------|")
                elif selectMenu == 5:
                    print("\n|------------------------------|")
                    print("|---- [5]Steak | 150THB   -----|")
                    print("|------------------------------|")
                print("\n---Do you want this?---")
                print("\nYes[y] | No[x]: ")
                exit = input()
            else:
                exit = 'x'
    print("Exit Program!")

if __name__ == "__main__":
    main()
