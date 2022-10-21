import MetaTrader5 as mt5



def sell_sltp(arg4,arg7,arg8,arg9,s):

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

    pip = arg9
    point = mt5.symbol_info(symbol).point
    price = s.price_open
    deviation = 0
    request = {
        "action": mt5.TRADE_ACTION_SLTP,
        "symbol": symbol,
        "type": mt5.ORDER_TYPE_SELL_LIMIT,
        "position": s.ticket,
        "price": price,
        "sl": price + (arg7*pip) * point,
        "tp": price - (arg8*pip) * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }
    # send a trading request
    result = mt5.order_send(request)
    # check the execution result
    print("1. order_send(): by {} at {} with deviation={} points".format(symbol,price,deviation))
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
        mt5.shutdown()
        quit()