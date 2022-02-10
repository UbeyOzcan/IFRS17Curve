import zipfile
import urllib.request
import pandas as pd
import openpyxl
import numpy as np

def download_eiopa(url, country):
    
    filehandle, _ = urllib.request.urlretrieve(url)

    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    term = zip_file_object.namelist()[2]

    file = zip_file_object.open(term)

    df = pd.read_excel(file, sheet_name= "RFR_spot_no_VA", header=1, engine="openpyxl")

    rates = df[[country]].tail(-8).reset_index(drop = True)

    df_VA = pd.read_excel(file, sheet_name= "RFR_spot_with_VA", header=1, engine= "openpyxl")
    VA = df_VA[[country]].iloc[[7]].values


    dur_A = 0.005
    dur_P= 1

    arg_1 = (dur_A/dur_P)/0.65 * 0.5
    rates[["IFRS17curve"]] = rates[[country]]  + VA * arg_1

    
    output = pd.DataFrame(rates).astype(float).round(4)
    output.columns = ["eiopa", "IFRS17curve"]

    return output










