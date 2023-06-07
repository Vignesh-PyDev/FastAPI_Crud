from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from models import *
import uuid
fake = Faker()
engine = create_engine('sqlite:///testdb.db')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)
def ingest_dummy_data():
    session = SessionLocal()
    assetClassList = [  "Equities",
                        "Bonds",
                        'Derivatives',
                        "Currencies",
                        "Commodities",
                        "Cryptocurrencies",
                        "Exchange-Traded Funds (ETFs)",
                        "Real Estate Investment Trusts (REITs)",
                        "Mutual Funds",
                        "Options",
                        "Indices"
                      ]
    counterpartyList = ["Individuals",
                        "Banks and Financial Institutions","Corporations",
                        "Government Entities","MedTech Solutions",
                        "HealthTech Innovations",
                        "PharmaElectronics",
                        "MediConnect",
                        "BioTech Systems",
                        "eHealth Solutions",
                        "MediTech Corporation",
                        "HealthCare Electronics",
                        "MediGadget",
                        "MediCore Technologies",
                        "HealthTech Labs",
                        "ePharma Solutions","ABC Electronics",
                        "XYZ Tech",
                        "Gadget Solutions",
                        "Digital Innovations",
                        "E-Tech Corporation",
                        "Techtronics",
                        "ElectroTech",
                        "TechMasters",
                        "Cyber Systems",
                        "TechGurus",
                        "ElectroWorld",
                        "Innovative Electronics"
                        ]
    instrumentList = [
        "Smartphone",
        "Laptop",
        "Tablet",
        "Smart TV",
        "Smartwatch",
        "Headphones",
        "Bluetooth Speaker",
        "Digital Camera",
        "Gaming Console",
        "E-book Reader",
        "Fitness Tracker",
        "Virtual Reality Headset",
        "Drone",
        "Wireless Earbuds",
        "Portable Power Bank",
        "Electrocardiogram (ECG) Machine",
        "Ultrasound Machine",
        "MRI Scanner",
        "CT Scanner",
        "X-ray Machine",
        "Infusion Pump",
        "Blood Pressure Monitor",
        "Pulse Oximeter",
        "Ventilator",
        "Defibrillator",
        "Ophthalmoscope",
        "Otoscope",
        "Stethoscope",
        "Glucose Meter",
        "Thermometer",
        "Nebulizer",
        "Anesthesia Machine",
        "Endoscope",
        "Dental X-ray Machine",
        "Pacemaker"
    ]

    trader_names = [
        "Rajesh Gupta",
        "Priya Sharma",
        "Amit Patel",
        "Sneha Verma",
        "Vikram Singh",
        "Neha Desai",
        "Sanjay Shah",
        "Ananya Mehta",
        "Rahul Joshi",
        "Kavita Kapoor"
        "John Smith",
        "Emily Johnson",
        "Michael Davis",
        "Emma Brown",
        "Christopher Wilson",
        "Sarah Thompson",
        "David Anderson",
        "Olivia Martinez",
        "Daniel Clark",
        "Sophia White",
        "James Smith",
        "Emily Johnson",
        "Oliver Brown",
        "Sophie Wilson",
        "Jack Thompson",
        "Grace Anderson",
        "William Clark",
        "Amelia Green",
        "Daniel Wright",
        "Charlotte Mitchell"
    ]

    buySellIndicatorList = ["BUY","SELL"]

    for _ in range(999):
        random_buySellIndicator = buySellIndicatorList[fake.pybool()]
        random_quantity = fake.pyint(min_value = 1,max_value = 49)
        random_price = fake.pyfloat(right_digits=2, positive=True, min_value=299, max_value=9999)
        new_data = TradeDetails(buySellIndicator = random_buySellIndicator,
                                    price = random_price,
                                    quantity = random_quantity)
        session.add(new_data)
        session.commit()

        random_asset_class = fake.random_element(elements=assetClassList)
        random_counter_party = fake.random_element(elements=counterpartyList)
        ins_id = str(uuid.uuid4())
        ins_name = fake.random_element(elements=instrumentList)
        trd_time = fake.date_time_between(start_date = "-4y",end_date="now")
        trdrname = fake.random_element(elements=trader_names)
        trddetails = new_data.id
        trade_new_data = Trade(asset_class = random_asset_class,
                               counterparty = random_counter_party,
                               instrument_id = ins_id,
                               instrument_name = ins_name,
                               trade_date_time = trd_time,
                               trader = trdrname,
                               trade_details = trddetails)
        session.add(trade_new_data)
        session.commit()
ingest_dummy_data()
