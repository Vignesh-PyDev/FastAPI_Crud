""""""
def fetch_data(data,sort_key = None):
    response_dict = []
    print(sort_key,"in fn")
    for Iter in data:
        tempDict = {
            "assetClass": Iter.asset_class,
            "counterparty": Iter.counterparty,
            "instrumentId": Iter.instrument_id,
            "instrumentName": Iter.instrument_name,
            "tradeDateTime": Iter.trade_date_time,
            "tradeDetails": {
                "buySellIndicator": Iter.trade.buySellIndicator,
                "price": Iter.trade.price,
                "quantity": Iter.trade.quantity
            },
            "tradeId": Iter.trade_id,
            "trader": Iter.trader
        }
        response_dict.append(tempDict)
    if sort_key:
        return sorted(response_dict,key=lambda i: i['tradeDetails'][sort_key])
    else:
        return response_dict