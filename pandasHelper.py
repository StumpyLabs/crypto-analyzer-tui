import coingeckoHelper
import pandas as pd

#def textToDF()


def geckoChoices(customerInput):
    match customerInput:
        case "mc":
            return coingeckoHelper.marketCapDec()
        case "p":
            return coingeckoHelper.marketCapDec()
        case "pc":
            return coingeckoHelper.marketCapDec()
        case "v":
            return coingeckoHelper.marketCapDec()
        case "vc":
            return coingeckoHelper.marketCapDec()