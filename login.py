import MetaTrader5 as mt5
from orderSend import orderSend
from components.core_methods import factor
from components.symbol import symbol

def login(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10):

    # display data on the MetaTrader 5 package
    print("MetaTrader5 package author: ", mt5.__author__)
    print("MetaTrader5 package version: ", mt5.__version__)
        
    # establish connection to the MetaTrader 5 terminal
    if not mt5.initialize(login=arg1,password=arg2,server=arg3):
        print("initialize() failed, error code =",mt5.last_error())
        quit()


    arg5 = str(input("buy or sell or close or sort or get_positions : "))
    if arg5 == "cls":
        quit()
    arg4 = str(input("symbol : "))
    arg4 = symbol(arg4)
    if arg4 == "cls":
        quit()
    if arg5 == "close":
        arg6 = 0.00
        arg7 = 0
        arg8 = 0
        arg9 = 0
        arg10 = 0
    elif arg5 == "sort":
        arg6 = 0.00
        arg7 = int(input("sl : "))
        if arg7 == "cls":
            quit()
        arg8 = int(input("tp : "))
        if arg8 == "cls":
            quit()
        arg9 = int(input("pip = Xpoint : "))
        if arg9 == "cls":
            quit()
        arg10 = 0
    elif arg5 == "get_positions":
        arg6 = 0.00
        arg7 = 0
        arg8 = 0
        arg9 = 0
        arg10 = 0
    else:
        arg6 = float(input("lots : "))
        if arg6 == "cls":
            quit()
        arg7 = int(input("sl : "))
        if arg7 == "cls":
            quit()
        arg8 = int(input("tp : "))
        if arg8 == "cls":
            quit()
        arg9 = int(input("pip = Xpoint : "))
        if arg9 == "cls":
            quit()
        arg10 = int(input("count : "))
        if arg10 == "cls":
            quit()


    if not arg5 == "get_positions":
        factor(arg4,arg5,arg6,arg7,arg8,arg9,arg10)



    orderSend(
        arg4, #symbol
        arg5, #option_type
        arg6, #vol = xlots
        arg7, #sl = Xpips
        arg8, #tp = Xpips
        arg9, #1pip = Xpoint
        arg10, #count
    )

    mt5.shutdown()