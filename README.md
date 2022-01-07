# Documentation 
4 functions and one script are used to create the streamlit application : 

- url_creator.py
- eiopa_fun.py
- sql_create_tab.py
- sqlconnect.py
- IFRS17_curvreApp.py

## url_creator.py
This function needs 2 arguments : year and month. Based on these 2 arguments, this function will create the URL in order to download the EIOPA zip file for the corresponding year and month.

## eiopa_fun.py
Based on 2 arguments, url and country name, this function has 3 objectives :

- Import the excel file where eiopa rfr curve is stored
- Took the VA parameters (should be change based on the paper wrote by Eric and Damien)
- Calculate the IFRS17 curve again based on the paper (should be change as well, the current formula is for demo purpose)

## sql_create_tab.py
One of the requirements is to have SSMS (SQL Server Manageent Studio). At this stage, the tool use windows username and windows password to connect to the database.

Based on the server name (srv), db name (db), country, year and month, this function create a table in the desired database. Notice that, this function could be merge with the next function (sqlconnect.py) quite easily. But for the development purpose, we keep this separately.

## sqlconnect.py
Based on server name (srv), db name (db), country, year and month will upload
the dataframe created with eiopa_fun.py in the table create by sql_create_tab.py

## IFRS17_curveApp.py
Finally, by running this script using Anaconda terminal, the application will be on run locally. To run the app, please open the terminal using Anaconda. Open Anaconda > Environments > arrow next to base (root) > Open terminal. Enter in the terminal the path where the streamlit application is stored using cd command:

            cd <path to the folder>

Once the path is set, run the application as follow :

     <path to the folder>  streamlit run IFRS1_curveApp.py


The application will be on running local in your favorite browser. 