import MetaTrader5 as mt5
from components.buy_sltp import buy_sltp

def buy_request(arg4,arg6,arg7,arg8,arg9,x):

    # prepare the buy request structure
    symbol = arg4 #arg4
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        mt5.shutdown()
        quit()
    
    # if the symbol is unavailable in MarketWatch, add it
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, exit",symbol)
            mt5.shutdown()
            quit()

    lot = arg6
    point = mt5.symbol_info(symbol).point
    pip = arg9 * point
    price = mt5.symbol_info_tick(symbol).ask
    deviation = 0
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "tp": price + (arg8 * pip),
        "sl:": price - (arg7 * pip),
        "price": price,
        "deviation": deviation,
        "magic": 23400,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }
    # send a trading request
    result = mt5.order_send(request)
    # check the execution result
    xx = x + 1
    print("{}. order_send(): by {} {} lots at {} with deviation={} points".format(xx,symbol,lot,price,deviation))
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        # request the result as a dictionary and display it element by element
        result_dict=result._asdict()
        for field in result_dict.keys():
            print("   {}={}".format(field,result_dict[field]))
            # if this is a trading request structure, display it element by element as well
            if field=="request":
                traderequest_dict=result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
        print("shutdown() and quit")