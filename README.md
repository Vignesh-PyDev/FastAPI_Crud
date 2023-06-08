![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

# Project Name

> Building a REST API with endpoints serving Trade data from a mocked database.

## Prerequisites

This project requires Python (version 3.6 or later),virtual environment,Postman for API Testing,Database for data Storage and Retreival.
To make sure you have them available on your machine,
try running the following command.

```sh
$ python -V
Python 3.10.6
```

## Table of contents

- [Project Name](#project-name)
  - [Prerequisites](#prerequisites)
  - [Table of contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Serving the app](#serving-the-app)
  - [API](#api)
    - [useBasicFetch](#usebasicfetch)
      - [Options](#options)
    - [fetchData](#fetchdata) 
 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installation

**BEFORE YOU INSTALL:** please read the [prerequisites](#prerequisites)

Create a virtual environment using the following command:
```
$ virtualenv <virtual_env_name>
$ source <virtual_env_name>/bin/activate```

Now cloning this repo on your local machine:

```sh
$ git clone https://github.com/Vignesh-PyDev/FastAPI_Crud.git
$ cd PROJECT
```

To install and set up the library, run:

```sh
$ pip install -r requirements.txt
```

Now,the we need to ingest some data for testing the API's for that,

```
$ python3 data_ingestion.py

```
It will ingest data to our local SQLlite Database.

## Usage

### Serving the app

```
$ uvicorn main:steel_eye_task --reload
```

### API #1 --> /api/trade/all

### Listing trades:

Lists all available trades,

### API #1.1 /api/trade/all?sort_by=price&page=1&size=records_per_page

I have given support to sort/paginate the response by adding the query parameters.

All those are optional,if no query_params are given the response will be generated with default values.


### API #2 --> /api/trade/{ID}

## Single trade:

Fetch Single Record associated with the given ID.

### API #3 --> /api/search/?query_params

### Example:/api/search/?counter_party=eHealth%20Solutions&trader_name=Jack%20Thompson&sort_by=price&page=1&size=50

## Query Params:

For Sorting:

1.trade_id

2.asset_class

3.counterparty

4.instrument_id

5.instrument_name

6.trade_date_time

7.trade_details

8.trader

9.buySellIndicator

10.price

11.quantity

Search Query Params:

1.counterparty

2.instrumentId

3.instrumentName

4.trader

## Searching trades:

API to search across the trades using the query_params as passed in the URL.

I have given support to sort/paginate the response by adding the query parameters.

### API #$ --> /api/filter/?query_params

### Example:/api/filter/?maxPrice=3000&minPrice=300&end=2023-01-31&start=2022-01-01&tradeType=BUy&page=1&size=50

## Query Params:

For Sorting:
1.trade_id

2.asset_class

3.counterparty

4.instrument_id

5.instrument_name

6.trade_date_time

7.trade_details

8.trader

9.buySellIndicator

10.price

11.quantity

List of Available Filters:

1.maxPrice

2.minPrice

3.assetClass

4.start

5.end

6.trade_type

## Filter trades:

API to filter trades. Filter the response using filters passed in the URL.

I have given support to sort/paginate the response by adding the query parameters.
