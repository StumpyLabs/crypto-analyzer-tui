import curl
import requests
import json
import pandas as pd
import coingeckoCalls

import analyzer
import coingeckoHelper

dataTest = [{"id":"bitcoin","symbol":"btc","name":"Bitcoin"},{"id":"ethereum","symbol":"eth","name":"Ethereum"},{"id":"litecoin","symbol":"ltc","name":"Litecoin"}]


def main():
    #analyzer.run()

    data = coingeckoHelper.marketCapDec()

    listDicts = json.loads(data)

    df = pd.DataFrame(listDicts, columns=['id', 'market_cap', 'current_price'])

    print(df)


if __name__ == '__main__':
    main()
