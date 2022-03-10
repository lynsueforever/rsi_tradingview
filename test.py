from this import d
from numpy import setdiff1d
import pandas as pd
from stoch_rsi import stoch_rsi_tradingview
from rsi import rsi_tradingview2
from decimal import Decimal

if __name__ == '__main__':
    #14:00,rsi:28.88,close 39232.5, pre_close:39173.5
    #14:05,rsi:31.29,close 39269.5, pre_close;39232.5
    #14:10,rsi:30.38,close 39239.0,pre_close:39269.5
    r1 = Decimal('28.88')
    p1 = Decimal('39232.5')
    u1 = Decimal('59')
    d1 = Decimal('0')

    r2 = Decimal('31.29')
    p2 = Decimal('39269.5')
    u2 = Decimal('37')
    d2 = Decimal('0')
    算出俩啦 ！！！！https://www.wolframalpha.com/input?i=100+-+100+%2F+%281%2B27305889%2F1205000*8435000%2F438105027%29
e = 27305889/1205000 ; f = 438105027/8435000 ; g = 100 - 100 / (1+27305889/1205000*8435000/438105027); 
    100/(100-28.88)-1 = a/b;
    100/(100-31.29)-1 = c/d;
    c= 1/14 *37 + 13/14 * a;
    d= 1/14 *0 + 13/14 * b;
    e = 1/14 *0 + 13/14 * c;
    f = 1/14 *30.5 + 13/14 * d;
    g = 100 - 100 / (1+e/f); 
    100/(100-31.29)-1 = su2/sd2

    28.88/71.12 = su1/sd1

    31.29 / 68.71 = (37+13*su1) / (13 * sd1)

    su1 sd1 
    #r3 = ?

    exit(0)
    ohlc = pd.read_csv("bit.csv", index_col="date")

    aaa = rsi_tradingview2(ohlc,14)
    print("RSI: ")
    for i in aaa:
        print (i)
    exit(0)
    for i in range(len(rsi)):
        print(f"Date={ohlc.index[i]}\tRSI={rsi[i]}")
    exit(0)
    rsi, stochrsi_K, stochrsi_D = stoch_rsi_tradingview(ohlc)
    print("\n\nSTOCH_RSI: ")
    for i, v in rsi.items():
         print(f"Date={ohlc.index[i]}\tRSI={rsi[i]}\tK={stochrsi_K[i]}\tD={stochrsi_D[i]}")
