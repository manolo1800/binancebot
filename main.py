from binanceUtils import BinanceRest


bn = BinanceRest()
coins_price = bn.get_ticker_price()

coins = list()

for coin_price in coins_price:
    
    if 'USDT' in coin_price['symbol'] and float(coin_price['price'])<20:
    
        coins.append(coin_price['symbol'])


#print(bn.get_ticker_price(symbol='FETUSDT'))

print(coins)