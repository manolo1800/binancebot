from binance.spot import Spot as client 
from dotenv import load_dotenv
import os

# esta clase tiene como finalidad servir todos los metodos de binance-connector sin la necesidad de loguearse en 
# cada archivo en se utilicen 
class BinanceRest:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        self.secret_key = os.getenv('SECRET_KEY')
        self.client = client(api_key=self.api_key,api_secret=self.secret_key)

    
    # -------- MARKET -----------------------------------------------

    def get_exchange_info(self,symbol: str, symbols: list = None):

        if symbol!=None:

            exchange_info = self.client.exchange_info(symbol=symbol)

        else:

            exchange_info = self.client.exchange_info(symbols=symbols)

        return exchange_info
    
    def get_depth(self,symbol: str):

        depth = self.client.depth(symbol=symbol)

        return depth
    
    def get_trades(self,symbol: str):

        trades = self.client.trades(symbol=symbol)

        return trades
    
    def get_historical_trades(self,symbol: str):

        historical_trades = self.client.historical_trades(symbol=symbol)

        return historical_trades
    
    def get_agg_trades(self,symbol: str):

        agg_trades = self.client.agg_trades(symbol=symbol)

        return agg_trades
    
    def get_klines(self,symbol: str, interval: str):

        klines = self.client.klines(symbol=symbol,interval=interval)

        return klines
    
    def get_ui_klines(self,symbol: str, interval: str):

        ui_klines = self.client.ui_klines(symbol=symbol,interval=interval)

        return ui_klines
    
    def get_ui_klines(self,symbol: str, interval: str):

        ui_klines = self.client.ui_klines(symbol=symbol,interval=interval)

        return ui_klines
    
    def get_avg_price(self,symbol: str):

        avg_price = self.client.avg_price(symbol=symbol)

        return avg_price
    
    def get_ticker_24hr(self,symbol: str, symbols: list = None):

        if symbol!=None:

            ticker_24hr = self.client.ticker_24hr(symbol=symbol)

        else:

            ticker_24hr = self.client.ticker_24hr(symbols=symbols)
        
        return ticker_24hr
    
    def get_trading_day_ticker(self,symbol: str, symbols: list = None):

        if symbol!=None:

            trading_day_ticker = self.client.trading_day_ticker(symbol=symbol)

        else:

            trading_day_ticker = self.client.trading_day_ticker(symbols=symbols)
        
        return trading_day_ticker
    
    def get_ticker_price(self,symbol: str = None , symbols: list = None):

        if symbol!=None:

            traer_price =  self.client.ticker_price(symbol=symbol)
            price = traer_price['price']

        else:

            price =  self.client.ticker_price(symbols=symbols)

        return price
    
    def get_book_ticker(self,symbol: str = None , symbols: list = None):

        if symbol!=None:

            book_ticker =  self.client.book_ticker(symbol=symbol)

        else:

            book_ticker =  self.client.book_ticker(symbols=symbols)

        return book_ticker

    def get_rolling_window_ticker(self,symbol: str = None , symbols: list = None):

        if symbol!=None:

            rolling_window_ticker =  self.client.rolling_window_ticker(symbol=symbol)
            
        else:

            rolling_window_ticker =  self.client.rolling_window_ticker(symbols=symbols)

        return rolling_window_ticker
    

    # ---------------- WALLET -----------------------------------------

    def get_coin_info(self):

        coin_info = self.client.coin_info()

        return coin_info
    
    def get_account_snapshot(self,type: str):

        account_snapshot = self.client.account_snapshot(type=type)

        return account_snapshot

    def get_balance(self):

        traer_balance = self.client.balance()
        balance_btc = traer_balance[0]['balance']
        valor_btc = self.get_ticker_price(symbol='BTCUSDT')

        balance_usdt = float(balance_btc)*float(valor_btc)
        
        return balance_usdt

    def get_deposit_address(self,coin: str ):

        deposit_address = self.client.deposit_address(coin=coin)

        return deposit_address








