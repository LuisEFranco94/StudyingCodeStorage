import streamlit as st
import pandas as pd
import numpy as np
import time

teamsNFLAFC=["Baltimore Ravens","Buffalo Bills","Cincinnati Bengals","Cleveland Browns",
            "Denver Broncos","Houston Texans","Indianapolis Colts","Jacksonville Jaguars",
            "Kansas City Chiefs","Las Vegas Raiders","Los Angeles Chargers","Miami Dolphins",
            "New England Patriots","New York Jets","Pittsburgh Steelers","Tennessee Titans"]

teamsNFLNFC= ["Arizona Cardinals","Atlanta Falcons","Carolina Panthers","Chicago Bears",
            "Dallas Cowboys", "Detroit Lions", "Green Bay Packers", "Los Angeles Rams",
            "Minnesota Vikings", "New Orleans Saints","New York Giants", "Philadelphia Eagles",
            "San Francisco 49ers","Seattle Seahawks","Tampa Bay Buccaneers","Washington Commanders"]

teamsNFL = sorted(teamsNFLAFC + teamsNFLNFC)    
playoffs = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
            False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False] 

#df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
df = pd.DataFrame(list(zip(teamsNFL,playoffs)),columns=["Team Name","Playoffs"])
#with st.spinner(text='In progress'):
    #time.sleep(3)
    #st.success('Done')

st.data_editor(df,column_config={
        "Playoffs": st.column_config.CheckboxColumn(
            "PLAYOFFS?",
            help="Did this team **clinch** a playoff spot?",
            default=False,
        )
    },
    disabled=["Team Name"],
    hide_index=True)


#add_selectbox = st.sidebar.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone")
#)

#tab1, tab2 = st.sidebar.tabs(["Regular Season","Postseason"])


# Display code
#with st.echo():
#st.code(code, language='python')