from typing import Any
import schema
import models
from fastapi import FastAPI, Query, Request
from pydantic import ValidationError
from db import engine
from sqlalchemy.orm import sessionmaker
from fastapi_pagination import Page, paginate, add_pagination
from sqlalchemy import or_
from datetime import date
from functions import fetch_data
from sqlalchemy import desc


models.Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

steel_eye_task = FastAPI(debug=False,description="Steel Eye Data Engineer Task")
add_pagination(steel_eye_task)

columns_list = '''Available Sorting Options \n\n Please Copy/Paste as it is
          \n\n1.trade_id
          \n\n2.asset_class
           \n\n3.counterparty
           \n\n4.instrument_id
           \n\n5.instrument_name
           \n\n6.trade_date_time
           \n\n7.trade_details
           \n\n8.trader
           \n\n9.buySellIndicator
           \n\n10.price
           \n\n11.quantity'''

search_descripton = '''\n\nPlease note your inputs are searched against the following columns_list: \n\n1.counterparty\n\n2.instrumentId
\n\n3.instrumentName\n\n4.trader'''

filter_description = '''\n\nList of Available Filters: \n\n1.maxPrice\n\n2.minPrice
\n\n3.assetClass\n\n4.start\n\n5.end\n\n6.trade_type'''

extraSortValues = ["price",'quantity','buySellIndicator']

# API --> Listing trades
@steel_eye_task.get(path="/api/trade/all", response_model=Page[schema.Trade],
                    name="Get all Trade",
                    description=columns_list)
async def get_all(request:Request,sort_by: str = None,order:str = None):
    db = SessionLocal()
    query_params = dict(request.query_params)

    if query_params.get('sort_by') in extraSortValues:
        query = db.query(models.Trade).all()
        if query_params.get("order") == 'asc':
            return paginate(fetch_data(query, sort_by))
        else:
            return paginate(fetch_data(query, sort_by)[::-1])
    else:
        if query_params.get("order") == 'asc':
            query = db.query(models.Trade).order_by(sort_by).all()
        else:
            query = db.query(models.Trade).order_by(desc(sort_by)).all()
        return paginate(fetch_data(query))

# API --> Single trade
@steel_eye_task.get("/api/trade/{trade_id}", name="Get Single Trade by Id")
async def getSingleTrade(trade_id: int):
    db = SessionLocal()
    tradebyId = db.query(models.Trade).get(trade_id)
    if tradebyId:
        tempDict: dict[str, dict[str, Any] | Any] = {
            "assetClass": tradebyId.asset_class,
            "counterparty": tradebyId.counterparty,
            "instrumentId": tradebyId.instrument_id,
            "instrumentName": tradebyId.instrument_name,
            "tradeDateTime": tradebyId.trade_date_time,
            "tradeDetails": {
                "buySellIndicator": tradebyId.trade.buySellIndicator,
                "price": tradebyId.trade.price,
                "quantity": tradebyId.trade.quantity
            },
            "tradeId": tradebyId.trade_id,
            "trader": tradebyId.trader
        }
        return tempDict
    else:
        return {"message":"Requested Id does not exixts"}

@steel_eye_task.get("/api/search/", response_model=Page[schema.Trade], name="Search all Trades with Keywords",
                    description=columns_list + search_descripton)
async def searchTrade(request:Request,counter_party: str = None,
                      instrument_name: str = None, trader_name: str = None,
                      instrument_id: str = None, sort_by: str = None,
                      order:str = ['asc','desc']):
    db = SessionLocal()
    query_params = dict(request.query_params)
    counter_party = counter_party if counter_party else ""
    instrument_name = instrument_name if instrument_name else ""
    instrument_id = instrument_id if instrument_id else ""
    trader_name = trader_name if trader_name else ""
    search_api_query = db.query(models.Trade).filter(
        or_(
            models.Trade.counterparty.like(counter_party),
            models.Trade.instrument_name.like(instrument_name),
            models.Trade.instrument_id.like(instrument_id),
            models.Trade.trader.like(trader_name)
        )
    )
    if query_params.get('sort_by') in extraSortValues:
        query = search_api_query.all()
        if query_params.get("order") == 'asc':
            return paginate(fetch_data(query, sort_by))
        else:
            return paginate(fetch_data(query, sort_by)[::-1])
    else:
        if query_params.get("order") == 'asc':
            query = search_api_query.order_by(sort_by).all()
        else:
            query = search_api_query.order_by(desc(sort_by)).all()
        return paginate(fetch_data(query))

@steel_eye_task.get("/api/filter/", response_model=Page[schema.Trade], name="Get Filtered Trades", description=columns_list+filter_description)
async def filterTrades(request:Request,maxPrice: int = None, minPrice: int = None,
                       assetClass: str = None, end: date | None = None,
                       start: date | None = None, tradeType: str | None = ["SELL", "BUY"],
                       sort_by: str|None = None,order:str = ['asc','desc']):
    db = SessionLocal()
    query_params = dict(request.query_params)
    try:
        if query_params:
            optional_api_query = db.query(models.Trade).join(models.Trade.trade).filter(models.Trade.trade_id==models.TradeDetails.id)
            if "assetClass" in query_params:
                optional_api_query = optional_api_query.filter(models.Trade.asset_class == query_params["assetClass"])
            if "tradeType" in query_params:
                optional_api_query = optional_api_query.filter(models.TradeDetails.buySellIndicator == query_params["tradeType"].upper())
            if "minPrice" in query_params:
                optional_api_query = optional_api_query.filter(models.TradeDetails.price >= query_params["minPrice"])
            if "maxPrice" in query_params:
                optional_api_query = optional_api_query.filter(models.TradeDetails.price <= query_params["maxPrice"])
            if ("end" in query_params) and ("start" in query_params):
                optional_api_query = optional_api_query.filter(models.Trade.trade_date_time.between(query_params["start"],query_params['end']))
            if query_params.get('sort_by') in extraSortValues:
                query = optional_api_query.limit(10).all()
                if query_params.get("order") == 'asc':
                    return paginate(fetch_data(query, sort_by))
                else:
                    return paginate(fetch_data(query, sort_by)[::-1])
            else:
                if query_params.get("order") == 'asc':
                    query = optional_api_query.order_by(sort_by).all()
                else:
                    query = optional_api_query.order_by(desc(sort_by)).all()
                return paginate(fetch_data(query))


    except ValidationError as e:
        print("Exceptiom",e)
        return {"message":"No Records Found"}


