import pandas as pd 
import streamlit as st

from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(       
    fs_protocol='webdav',         
    fs_root_folder="BMLD_App_DB"  
    ) 
login_manager = LoginManager(data_manager) 
login_manager.login_register()             

if 'data_df' not in st.session_state:
    st.session_state['data_df'] = data_manager.load_user_data(
        'data.csv',                     
        initial_value=pd.DataFrame(),   
        parse_dates=['timestamp']       
    )

st.set_page_config(page_title="Data Analyzer", page_icon=":material/monitor_weight:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_anleitung = st.Page("views/Benutzeranleitung_1.py", title="Benutzeranleitung", icon=":material/live_help:")
pg_theorie  = st.Page("views/Theorie.py",  title="Theorie",  icon=":material/psychology_alt:")
pg_data_analyer = st.Page("views/passing_bablok2.py", title="Passing Bablok generator", icon=":material/calculate:")
pg_bland_altman = st.Page("views/bland_altman2.py", title="Bland-Altman generator", icon=":material/scatter_plot:")

pg = st.navigation([pg_home, pg_anleitung, pg_theorie, pg_data_analyer, pg_bland_altman])
pg.run()
