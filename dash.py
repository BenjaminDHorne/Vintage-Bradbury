import database
import streamlit as st
import pandas as pd
import numpy as np

st.title("Vintage Bradbury Collection App")


@st.cache
def load_data():
    list_of_tups = database.get_starter_data()
    # create DataFrame using data becuase streamlit uses pandas.
    df = pd.DataFrame(list_of_tups, columns=['Player', 'Team', 'Card Set', 'Purchase Price'])
    return df


# Main <-------
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)