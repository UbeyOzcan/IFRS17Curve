import zipfile
import urllib.request
import pandas as pd
import openpyxl

url = "https://www.eiopa.europa.eu/sites/default/files/risk_free_interest_rate/eiopa_rfr_20211130.zip"

def Countries(url):
    
    
    filehandle, _ = urllib.request.urlretrieve(url)
    
    
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    term = zip_file_object.namelist()[2]
    
    file = zip_file_object.open(term)
    
    df = pd.read_excel(file, sheet_name= "RFR_spot_no_VA", header=1, engine="openpyxl")
        
    C = df.columns[2:]
        
    return C