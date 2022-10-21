import MetaTrader5 as mt5
from components.buy_request import buy_request
from components.sell_request import sell_request
from components.close_request import close_request
from components.positions_get import positions_get
from components.buy_sltp import buy_sltp
from components.sell_sltp import sell_sltp
from components.get_positions import get_positions


def orderSend(arg4,arg5,arg6,arg7,arg8,arg9,arg10):
        
    x = 0

    if arg5 == "buy":
        print("buy it ")
        while x < arg10:
            buy_request(arg4,arg6,arg7,arg8,arg9,x)
            x += 1
    elif arg5 == "sell":
        print("sell it ")
        while x < arg10:
            sell_request(arg4,arg6,arg7,arg8,arg9,x)
            x += 1
    elif arg5 == "close":
        print("close positios")
        close_request(arg4)
    elif arg5 == "sort":
        print("sort positions")
        s = positions_get(arg4)
        x = 0

        while x < len(s):

            if s[x].type == 0:
                buy_sltp(arg4,arg7,arg8,arg9,s[x])
            elif s[x].type == 1:
                sell_sltp(arg4,arg7,arg8,arg9,s[x])
            else:
                print("")

            x += 1

    elif arg5 == "get_positions":
        get_positions(arg4)
    else:
        print("error from ordersend")
        quit()