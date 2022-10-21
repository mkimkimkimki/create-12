


def factor(arg4,arg5,arg6,arg7,arg8,arg9,arg10):

    print()
    print()
    print()
    print()
    print("*****Drink Tabasco******")
    print()
    type_tabasco = str(input("Type tabasco × 2 (発声) : "))
    tabasco2 = "tabasco" * 2
    if not type_tabasco == tabasco2:
        quit()
    if type_tabasco == "cls":
        quit()
    drink_tabasco = str(input("Did you drink it??. yes?: "))
    if not drink_tabasco == "yes":
        quit()
    if drink_tabasco == "cls":
        quit()
    print()
    print()
    print()
    print()
    print("-----STATUS Check-----")
    print()
    print("Symbol: {}".format(arg4))
    print("Type: {}".format(arg5))
    if arg5 == "close" and "sort":
        print("Lots: {}".format("-"))
    else:
        print("Lots: {}".format(arg6))
    print("SL: {}".format(arg7))
    print("TP: {}".format(arg8))
    print("pip: {}".format(arg9))
    if arg5 == "close" and "sort":
        print("Count: {}".format("-"))
    else:
        print("Count: {}".format(arg10))
    print()
    lets_trade = str(input("Let's {} it!!!!!. {}? : ".format(arg5,arg5)))
    if not arg5 == lets_trade:
        quit()
    if lets_trade == "cls":
        quit()