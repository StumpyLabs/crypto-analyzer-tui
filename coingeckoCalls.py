import pandasHelper


def runCoingecko(customerInput):
    
    match customerInput:
        case "mc":
            return pandasHelper.mc()
        case "p":
            return pandasHelper.p()
        case "pc":
            return pandasHelper.pc()
        case "v":
            return pandasHelper.v()
        case "al":
            return pandasHelper.al()
        case "ah":
            return pandasHelper.ah()
