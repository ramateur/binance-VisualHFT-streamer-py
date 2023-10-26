from datetime import datetime

def UpdateSnapshot(asks, bids, market):
    Asks = []
    Bids = []
    for ask in asks:
        Asks.append({
                    'DecimalPlaces': 2, 
                    'EntryID': 0, 
                    'IsBid': 'False', 
                    'LayerName': '', 
                    'LocalTimeStamp': datetime.now().strftime("%Y.%m.%d-%H.%M.%S.%f"), 
                    'Price': ask[0], 
                    'ProviderID': 23, 
                    'ServerTimeStamp': datetime.now().strftime("%Y.%m.%d-%H.%M.%S.%f"), 
                    'Size': ask[1], 
                    'Symbol': market
                    })
        pass
    for bid in bids:
        Bids.append({
                    'DecimalPlaces': 2, 
                    'EntryID': 0, 
                    'IsBid': 'True', 
                    'LayerName': '', 
                    'LocalTimeStamp': datetime.now().strftime("%Y.%m.%d-%H.%M.%S.%f"), 
                    'Price': bid[0], 
                    'ProviderID': 23, 
                    'ServerTimeStamp': datetime.now().strftime("%Y.%m.%d-%H.%M.%S.%f"), 
                    'Size': bid[1], 
                    'Symbol': market
                    })
        pass
    data = {
            'Asks': Asks,
            'Bids': Bids,
            'DecimalPlaces': 2, 
            'ProviderId': 23, 
            'ProviderName': 'Binance', 
            'ProviderStatus': 2, 
            'Symbol': market, 
            'SymbolMultiplier': 1
            }
    return data

def UpdateTrade(data, market):
    Trade = {
            'ProviderId': 23, 
            'ProviderName': 'Binance',           
            'Price': float(data['p']),
            'Size': float(data['q']),
            'TimeStamp': datetime.now().strftime("%Y.%m.%d-%H.%M.%S.%f"), 
            'IsBuy': bool(data['m']),
            'Flags': '',
            'Symbol': market
            }
    return Trade