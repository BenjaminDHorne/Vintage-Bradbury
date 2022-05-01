import database
import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def load_card_data():
    list_of_tups = database.get_starter_data()
    # create DataFrame using data becuase streamlit uses pandas.
    df = pd.DataFrame(list_of_tups, columns=['Player', 'Team', 'Card Set', 'Purchase Price'])
    return df


@st.cache
def load_mem_data():
    list_of_tups = database.get_starter_mem_data()
    # create DataFrame using data because streamlit uses pandas.
    df = pd.DataFrame(list_of_tups, columns=['Item Name', 'Estimated Value'])
    return df

#TODO: Build page layout. Use sidebar sliders and checkboxes to filter the data. Like this: https://github.com/andyuttley/pgaapp/blob/master/pga_app.py

# Main <-----------------------------
st.title("The Horne Collection")
st.sidebar.header('Choose the Sub Collection to View:')

with st.sidebar:
    pass

data_load_state = st.text('Loading data...')
data_card = load_card_data()
data_mem = load_mem_data()
data_load_state.text('Loading data...done!')

if st.checkbox('Show top 10 cards by price'):
    st.subheader('Top 10 cards')
    st.write(data_card)

if st.checkbox('Show top 10 memorabilia items by price'):
    st.subheader('Top 10 memorabilia items')
    st.write(data_mem)


