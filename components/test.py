from turtle import position

from components.positions_get import positions_get
import MetaTrader5 as mt5
from orderSend import orderSend
from components.symbol import symbol

arg1 = 5029215
arg2 = "Mkimki5123"
arg3 = "FXGT-Demo"


# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)
    
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize(login=arg1,password=arg2,server=arg3):
    print("initialize() failed, error code =",mt5.last_error())
    quit()

symbol = "BTCUSD.."

positions_get(symbol)