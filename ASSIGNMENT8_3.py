BERRY_TYPES = ["blueberry", "lingonberry", "cloudberry", "cranberry", "raspberry", "strawberry"]
count = {}
totalll = []
price = {}
berry = []
money = []
amount = []
def printer(berry, amount, money):
    print()
    print('Berry type   Picked berries (kg)   Money earned (eur)')
    print('-----------------------------------------------------')
    total = "Total"
    for i in range (len(berry)):
        cash = (float(money[i]) * float(amount[i]))
        totalll.append(float(cash))
        print(f'{berry[i]:12} {"{:.0f}".format(amount[i]):>19} {"{:.2f}".format(cash):>20}', end = "\n")
    print('-----------------------------------------------------')
    print(f'{total:12} {"{:.0f}".format(sum(amount)):>19} {"{:.2f}".format(sum(totalll)):>20}', end = "")
    
    

def main():
    name = input('Enter the name of the file containing the berry data:\n')
    soorce = open(name, "r")
    for line in soorce:
        try:
            line = line.strip()
            nohow = line.split(",")
            if len(nohow) == 3:
                if nohow[1] in BERRY_TYPES:
                    if nohow[1] in count:
                        count[nohow[1]] += int(nohow[2])
                    else:
                        count[nohow[1]] = int(nohow[2])
        except OSError:
            print("Invalid file:{:s}".format(name))
        except ValueError:
            print("Invalid line:{:s}".format(line))
        except IndexError:
            print("Invalid line:{:s}".format(line))
    print('File read.')
    soorce.close()
    
    name1 = input('Enter the name of the file containing the prices of the berries:\n')
    prices = open(name1, "r")
    for line in prices:
        try:
            line = line.strip()
            protip = line.split(":")
            if len(protip) > 2:
                print("Invalid line:{:s}".format(line))
            if protip[0] in BERRY_TYPES:
                price[protip[0]] = protip[1]
        except OSError:
            print("Invalid file:{:s}".format(name1))
        except ValueError:
            print("Invalid line:{:s}".format(line))
        except IndexError:
            print("Invalid line:{:s}".format(line))
    print('File read.')
    prices.close()
    
    
    
    try:
        for key in count:
            if key in BERRY_TYPES:
                berry.append(key)
                amount.append(float(count[key]))
        for item in berry:
            for key in price:
                if item == key:
                    money.append(float(price[key]))
        if len(money) != len(amount):
            raise ArithmeticError
        printer(berry, amount, money)
    except ArithmeticError:
        print('Some of the berry prices are missing from the file {:s}.'.format(name1))
        
    

main()