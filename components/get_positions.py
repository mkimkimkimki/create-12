from turtle import position
import MetaTrader5 as mt5

def get_positions(arg4):

    symb = arg4

    x=0
    s = 0

    positions=mt5.positions_get(symbol=symb)
    if positions==None:
        print("No positions on {}, error code={}".format(symb,mt5.last_error()))
    print()
    print("Total positions on {} = {}".format(symb,len(positions)))
    print()
    print()

    positions_dict = []

    while len(positions) > x:
        position_info = {
            "ticket": positions[x][0],
            "time": positions[x][1],
            "time_msc": positions[x][2],
            "time_update": positions[x][3],
            "time_update_msc": positions[x][4],
            "type": positions[x][5],
            "magic": positions[x][6],
            "identifier": positions[x][7],
            "reason": positions[x][8],
            "volume": positions[x][9],
            "price_open": positions[x][10],
            "sl": positions[x][11],
            "tp": positions[x][12],
            "price_current": positions[x][13],
            "swap": positions[x][14],
            "profit": positions[x][15],
            "symbol": positions[x][16],
            "comment": positions[x][17],
            "external_id": positions[x][18]
        }

        positions_dict.append(position_info)
        x += 1

    print(len(positions_dict))

        #眉毛を抜いた、遅いと