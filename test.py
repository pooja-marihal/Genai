
# Import pandas library
import pandas as pd
import streamlit as st
from Logging import st_logging as log
 

log_obj = log.St_logging()
logger = log_obj.create_log()
# initialize list elements
data = [10,20,30,40,50,60]
 
# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data, columns=['Numbers'])
 
# print dataframe.
st.write(df)
logger.info('df created')
