import pandas as pd
import quandl
import requests

class QuandlSocket:

    def __init__(self):
        quandl.ApiConfig.api_key = 'mo86a9qvF7TU2nsF5zzN'

#Class for portfolio optimization, downloads relevant portfolio data
class PortfolioDataRequest:

    #stocks = [], start_date/end_date are strings
    def __init__(self, stocks, start_date, end_date):
        QuandlSocket()
        data = quandl.get_table(
            'WIKI/PRICES',
            ticker=stocks,
            qopts={'columns': ['date', 'ticker', 'adj_close']},
            date={'gte': start_date, 'lte': end_date},
            paginate=True
            )
        df = data.set_index('date')
        self.table = df.pivot(columns='ticker')
        # By specifying col[1] in below list comprehension
        # You can select the stock names under multi-level column
        self.table.columns = [col[1] for col in self.table.columns]

