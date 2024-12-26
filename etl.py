import streamlit as st
import pandas as pd
data={
    'Task':['Extract','Transform','Load'],
    'Status':['Completed','Inprogress','pending']
}
df=pd.DataFrame(data)
st.write('ETL pipeline execution status',df)
