import os, time

def showMenu():
   
    while True:
        global showingMenu
         #Menu Welcome message
        print("Here is our menu, what would you like to order?")
        #Looping through dictionary
        i = 1
        for key, value in menu.items():
            print(f"[{i}] {key}: {value}")
            i+=1
        print("[4] Done")
        print("[5] Quit")
    
        order = input("Input the menu number or name: ")
        #Makes it lower case to make it case insensitive
        order.lower()
        match order:
            case "ice cream":
                orders.append("Ice Cream")
                break 
            case "1":
                orders.append("Ice Cream")
                break 
            case "crepes":
                orders.append("Crepes")
                break  
            case "2":
                orders.append("Crepes")
                break 
            case "froyo":
                orders.append("Froyo")
                break
            case "3":
                orders.append("Froyo")
                break
            case"4":
                showingMenu = False
                if orders.len == 0:
                    os._exit(0)
                break
            case"5":
                os._exit(0)
                
            case _:
                print("\033[31mhmmm, i'm sorry but i don't think the item exist in our menu. Please input the menu number or name\033[0m")
                time.sleep(3)
                os.system("clear")
                continue

def more():
    global showingMenu
    while showingMenu:
        os.system("clear")
        showOrders()
        more = input("Do you want to order anything else? (y/n): ")
        more.lower()
        match more:
            case "y":
                showingMenu = True
                os.system("clear")
                break
            case "n":
                showingMenu = False
                os.system("clear")
                break
            case _:
                os.system("clear")
                print("\033[31mDo you want to order anything else or what??? >:(\033[0m")
                time.sleep(2)
                continue

def showOrders():
    if orders.count("Ice Cream") > 0:
        print(f"Ice Cream x {orders.count("Ice Cream")}: {menu["Ice Cream"] * orders.count("Ice Cream")}")
    if orders.count("Crepes") > 0:
        print(f"Crepes x {orders.count("Crepes")}: {menu["Crepes"] * orders.count("Crepes")}")
    if orders.count("Froyo") > 0:
        print(f"Froyo x {orders.count("Froyo")}: {menu["Froyo"] * orders.count("Froyo")}")
    iceCreamTotal = menu["Ice Cream"] * orders.count("Ice Cream")
    crepesTotal = menu["Crepes"] * orders.count("Crepes")
    froyoTotal = menu["Froyo"] * orders.count("Froyo")
    print(f"Total: {iceCreamTotal + crepesTotal + froyoTotal}")

menu = {
        "Ice Cream": 15000,
        "Crepes": 13000,
        "Froyo": 8000,
        }

orders = []

iceCreamCount = orders.count("Ice Cream")
CrepesCount = orders.count

#Main Code

print("Welcome to BlaBla Ice Cream Shop!!!")
time.sleep(2)

showingMenu = True

while showingMenu:
    #Showing the menu and ask for guest orders
    showMenu()
    #Asking if guest want to order anything else
    more()
print("Your Orders")
showOrders()
print("\nEnjoy your food :D")
time.sleep(8)
