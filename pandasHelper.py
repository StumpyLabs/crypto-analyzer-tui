import coingeckoHelper
import pandas as pd
import json
from IPython.core.display_functions import display


def grabGecko():
    data = coingeckoHelper.marketCapDec()
    data = json.loads(data)
    return data


# case "mc" market cap
def mc():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'market_cap', 'market_cap_rank'])
    df = df.sort_values(['market_cap'], ascending=False)

    # change format market_cap
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')
    df["market_cap"] = df["market_cap"].apply(lambda x: '${:,.2f}'.format(x))

    df.rename(columns={'id': 'Coin',
                       'market_cap_rank': 'Market Cap Rank',
                       'market_cap': 'Market Cap'}, inplace=True)

    display(df.to_string(index=False))


# case "p" price
def p():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'current_price'])
    df = df.sort_values(['current_price'], ascending=False)

    # change format current_price
    df["current_price"] = pd.to_numeric(df["current_price"], errors='coerce')
    df["current_price"] = df["current_price"].apply(lambda x: '${:,.2f}'.format(x))

    df.rename(columns={'id': 'Coin',
                       'current_price': 'Current Price'}, inplace=True)

    display(df.to_string(index=False))


# case "pc" price change 24h
def pc():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'price_change_percentage_24h', 'current_price'])
    df = df.sort_values(['price_change_percentage_24h'], ascending=False)

    # change format current_price
    df["current_price"] = pd.to_numeric(df["current_price"], errors='coerce')
    df["current_price"] = df["current_price"].apply(lambda x: '${:,.2f}'.format(x))

    # change format price_change_percentage_24h
    df["price_change_percentage_24h"] = pd.to_numeric(df["price_change_percentage_24h"], errors='coerce')
    df["price_change_percentage_24h"] = df["price_change_percentage_24h"].apply(lambda x: '%{:,.4f}'.format(x))

    df.rename(columns={'id': 'Coin',
                       'price_change_percentage_24h': 'Price Change 24hrs',
                       'current_price': 'Current Price'}, inplace=True)


    display(df.to_string(index=False))


# case "v" volume
def v():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'total_volume'])
    df = df.sort_values(['total_volume'], ascending=False)

    # change format volume
    df["total_volume"] = pd.to_numeric(df["total_volume"], errors='coerce')
    df["total_volume"] = df["total_volume"].apply(lambda x: '${:,.2f}'.format(x))

    # rename columns
    df.rename(columns={'id': 'Coin',
                       'total_volume': 'Total Volume'}, inplace=True)

    display(df.to_string(index=False))


# case "al" all-time low
def al():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'atl', 'atl_change_percentage', 'atl_date'])
    df = df.sort_values(['atl_change_percentage'], ascending=False)

    # change format atl
    df["atl"] = pd.to_numeric(df["atl"], errors='coerce')
    df["atl"] = df["atl"].apply(lambda x: '${:,.10f}'.format(x))

    # change format atl_change_percentage
    df["atl_change_percentage"] = pd.to_numeric(df["atl_change_percentage"], errors='coerce')
    df["atl_change_percentage"] = df["atl_change_percentage"].apply(lambda x: '%{:,.4f}'.format(x))

    # change format atl_date
    df["atl_date"] = pd.to_datetime(df["atl_date"])
    df["atl_date"] = df["atl_date"].dt.strftime('%b-%d-%Y')

    # rename columns
    df.rename(columns={'id': 'Coin', 'atl': 'ATL',
                       'atl_change_percentage': 'ATL % Change',
                       'atl_date': 'ATL Date'}, inplace=True)

    display(df.to_string(index=False))


# case "ah" all-time high
def ah():
    # grab data
    data = grabGecko()

    # build data frame and sort
    df = pd.DataFrame(data, columns=['id', 'ath', 'ath_change_percentage', 'ath_date'])
    df = df.sort_values(['ath_change_percentage'], ascending=False)

    # change format ath
    df["ath"] = pd.to_numeric(df["ath"], errors='coerce')
    df["ath"] = df["ath"].apply(lambda x: '${:,.6f}'.format(x))

    # change format ath_change_percentage
    df["ath_change_percentage"] = pd.to_numeric(df["ath_change_percentage"], errors='coerce')
    df["ath_change_percentage"] = df["ath_change_percentage"].apply(lambda x: '%{:,.4f}'.format(x))

    # change format ath_date
    df["ath_date"] = pd.to_datetime(df["ath_date"])
    df["ath_date"] = df["ath_date"].dt.strftime('%b-%d-%Y')

    # rename columns
    df.rename(columns={'id': 'Coin','ath': 'ATH',
                       'ath_change_percentage': 'ATH % Change',
                       'ath_date': 'ATH Date'}, inplace=True)

    display(df.to_string(index=False))
