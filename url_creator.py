import calendar



def createurl(year, month):
    
    y = int(year)
    m = int(month)
    day = str(calendar.monthrange(y, m)[1])
    
    url = "https://www.eiopa.europa.eu/sites/default/files/risk_free_interest_rate/eiopa_rfr_" + year + month + day + ".zip"
    
    return url
    







