from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date,Float,DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

fake = Faker()

engine = create_engine('sqlite:///testdb.db')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class TradeDetails(Base):
    __tablename__ = 'tradedetails'
    id = Column(Integer, primary_key=True, index=True)
    buySellIndicator = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    trade_relation = relationship("Trade",back_populates="trade")

class Trade(Base):
    __tablename__ = 'trade'

    trade_id = Column(Integer, primary_key=True)

    asset_class = Column(String)

    counterparty = Column(String)

    instrument_id = Column(String)

    instrument_name = Column(String)

    trade_date_time = Column(DateTime)

    trade_details = Column(Integer, ForeignKey("tradedetails.id"))

    trader = Column(String)

    trade = relationship("TradeDetails", back_populates="trade_relation")
