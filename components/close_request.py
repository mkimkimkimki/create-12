import MetaTrader5 as mt5
from components.positions_get import positions_get

def close_request(arg4):

    s = positions_get(arg4)
    x = 0
    while x < len(s):

        if s[x].type == 1:
            input_type = mt5.ORDER_TYPE_BUY
        elif s[x].type == 0:
            input_type = mt5.ORDER_TYPE_SELL

        deviation = 0
 
    # create a close request

        price=mt5.symbol_info_tick(s[x].symbol).ask
        deviation=0
        request={
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": s[x].symbol,
            "volume": s[x].volume,
            "type": input_type,
            "position": s[x].ticket,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }
        # send a trading request
        result=mt5.order_send(request)
        # check the execution result
        xx = x + 1
        print("{}. close position #{}: sell {} {} lots at {} with deviation={} points".format(xx,s[x].ticket,s[x].symbol,s[x].volume,price,deviation))
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("4. order_send failed, retcode={}".format(result.retcode))
            print("   result",result)
            # request the result as a dictionary and display it element by element
            
        x += 1