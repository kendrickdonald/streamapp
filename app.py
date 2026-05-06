import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

st.set_page_config(layout= 'wide')
df=pd.read_csv('india.csv')
list_of_states= list(df['State'].unique())
list_of_states.insert(0,'Overall India')
st.sidebar.title('India Data Viz')


selected_state = st.sidebar.selectbox('select a state', list_of_states)
primary= st.sidebar.selectbox('select a primary parameter', sorted(df.columns[5:]))
secondary= st.sidebar.selectbox('select a secondary parameter', sorted(df.columns[5:]))
plot= st.sidebar.button('Plot Graph')



if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig= px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=4,size_max=35,mapbox_style='carto-positron', width=1200, height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

