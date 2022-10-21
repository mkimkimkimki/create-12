import MetaTrader5 as mt5

def positions_get(arg4):

  symb = arg4
  positions_dict = []
  
  positions=mt5.positions_get(symbol=symb)
  if positions==None:
    print("No positions on {}, error code={}".format(symb,mt5.last_error()))
  elif len(positions)>0:
    print()
    print("Total positions on {} = {}".format(symb,len(positions)))
    for position in positions:
      positions_dict.append(position)

  return positions_dict