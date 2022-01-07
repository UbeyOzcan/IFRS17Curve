import streamlit as st
from eiopa_fun import download_eiopa
from sqlconnect import SQL_upload
from sql_create_tab import SQL_create_table
from url_creator import createurl
from Country_generator import Countries




def homepage():
    st.write("""
        # IFRS17 curve calculation Tool
        ### This application has been developped to compute the IFRS17 curve based on EIOPA free risk rate curve ###
        #""")
    st.write("To be completed with some theoretical aspect of the IFRS17 curve.")
        

def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage", 
            "Graph table and SQL"
        ]
    )
    
    
    

    if page == "Homepage":
        homepage()
    
    elif page == "Graph table and SQL":
        C = ('Euro', 'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus',
               'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
               'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia',
               'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
               'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Slovakia',
               'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom',
               'Australia', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia',
               'Hong Kong', 'India', 'Japan', 'Malaysia', 'Mexico', 'New Zealand',
               'Singapore', 'South Africa', 'South Korea', 'Taiwan', 'Thailand',
               'Turkey', 'United States')
        
        
        st.write("# Graphic, Table and SQL upload")
        st.write("In this page, a table compare EIOPA Risk free rate curve and IFRS17 curve. Next to that, a graphic is created to visualise them together.")
        st.write("Please enter the year, the month, the Country for which the IFRS17 curve has to be computed.")
        st.write("Next to that, please enter the server name and the Database name in which a table will be created and upload eiopa and IFRS17 curve.")
        # st.sidebar.text_input("EIOPA url", key  = "url")
        st.sidebar.text_input("Enter the year", key = "year")
        st.sidebar.text_input("Enter month", key = "month")
        country = st.sidebar.selectbox("Choose  Country", C)
        st.sidebar.text_input("Server Name", key  = "server")
        st.sidebar.text_input("Database Name", key  = "db_name")
        # st.sidebar.text_input("Table name", key = "tab_name")
        run = st.sidebar.button("Run !")
        
        
        if run:
            url = createurl(st.session_state.year, st.session_state.month)
            rates = download_eiopa(url, country)
            
            st.subheader("Table")
            st.write(rates)
            
            st.subheader("Graph")
            st.line_chart(rates)
            
            st.subheader("SQL Server")
            
            st.write("Creating table in SQL")
            SQL_create_table(st.session_state.server, st.session_state.db_name, country, st.session_state.year, st.session_state.month)
            st.success('The table ' + "curve_" + st.session_state.year + "_" + st.session_state.month + ' has been added to ' + st.session_state.db_name)
            
            
            st.write("Sending to the SQL Server")
            SQL_upload(st.session_state.server, st.session_state.db_name, country, rates.head(21),  st.session_state.year,  st.session_state.month)
            st.success('The EIOPA and IFRS17 curve have been update to the SQL server')
            
        
        

if __name__ == "__main__":
    main()

        


    
    

        
        
        
        
